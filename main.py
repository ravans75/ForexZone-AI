import asyncio
import logging
import json
import os
import time
from datetime import datetime
from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

from database.db_manager import init_db, SessionLocal
from database.models import Signal, NewsItem
from core.market_data import fetch_ohlcv, get_multi_tf
from core.historical_loader import load_all
from core.realtime_stream import RealtimeStream
from core.twelvedata_stream import run as td_stream_run, register_callback as td_register
from core.news_engine import fetch_news
from signals.signal_engine import generate_signal
from signals.risk_management import validate_signal
from alerts.telegram_bot import send_signal_with_chart
import uvicorn

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger(__name__)

SYMBOLS = ["XAUUSD", "BTCUSD"]
POLL_INTERVAL = 60

stream = RealtimeStream()


async def process_symbol(symbol: str):
    t0 = time.time()
    try:
        # Sequential fetches — concurrent yfinance calls corrupt each other
        df = await fetch_ohlcv(symbol, "1m", 200)
        mtf_dfs = await get_multi_tf(symbol)

        if df is None or df.empty:
            logger.warning(f"No data for {symbol}")
            return

        # Final price sanity check
        from core.market_data import PRICE_RANGE
        lo, hi = PRICE_RANGE.get(symbol, (0, 1e9))
        entry_price = float(df["close"].iloc[-1])
        if not (lo <= entry_price <= hi):
            logger.error(f"Skipping {symbol}: price {entry_price} out of range {lo}–{hi}")
            return

        signal = await generate_signal(symbol, df, mtf_dfs)
        if not signal or not validate_signal(signal, capital=100000.0):
            return

        elapsed = time.time() - t0
        logger.info(f"Signal [{elapsed:.2f}s]: {signal}")

        # Save to DB
        session = SessionLocal()
        try:
            session.add(Signal(
                symbol=signal["symbol"], signal=signal["signal"],
                entry=float(signal["entry"]), tp=float(signal["tp"]), sl=float(signal["sl"]),
                confidence=float(signal["confidence"]),
                reasons=json.dumps(signal.get("reasons", [])),
            ))
            session.commit()
        except Exception as e:
            session.rollback()
            logger.error(f"DB save error: {e}")
        finally:
            session.close()

        # Generate chart and send Telegram alert with image
        image_path = ""
        try:
            from dashboard.chart_engine import generate_chart
            image_path = generate_chart(df, signal)
        except Exception as e:
            logger.error(f"Chart error: {e}")

        await send_signal_with_chart(signal, image_path)

        # Broadcast to dashboard
        try:
            from dashboard.api import broadcast_signal, broadcast_ai
            await broadcast_signal(signal)
            # broadcast AI probs if available
            from ai.feature_engineering import build_sequence
            from ai.lstm_predictor import predict
            seqs = build_sequence(df)
            if len(seqs):
                bear, bull = predict(symbol, seqs)
                await broadcast_ai(symbol, bear, bull)
        except Exception:
            pass

    except Exception as e:
        logger.error(f"process_symbol error {symbol}: {e}")


async def polling_loop():
    while True:
        # Sequential — prevents yfinance concurrent fetch corruption
        for s in SYMBOLS:
            await process_symbol(s)
        await asyncio.sleep(POLL_INTERVAL)


async def news_loop():
    while True:
        session = SessionLocal()
        try:
            for symbol in SYMBOLS:
                articles = await fetch_news(symbol, page_size=5)
                for a in articles:
                    session.add(NewsItem(
                        symbol=symbol,
                        title=a["title"],
                        source=a["source"],
                        sentiment=a["sentiment"],
                        published_at=datetime.fromisoformat(
                            a["published_at"].replace("Z", "+00:00"))
                        if a.get("published_at") else datetime.utcnow(),
                    ))
            session.commit()
        except Exception as e:
            session.rollback()
            logger.error(f"News loop error: {e}")
        finally:
            session.close()
        await asyncio.sleep(600)


async def stream_callback(symbol: str, candle: dict):
    try:
        from dashboard.api import broadcast_price
        await broadcast_price(symbol, candle["close"])
    except Exception:
        pass


async def td_price_callback(symbol: str, price: float):
    """Broadcast live TD tick to dashboard WebSocket."""
    try:
        from dashboard.api import broadcast_price
        await broadcast_price(symbol, price)
    except Exception:
        pass


async def main():
    init_db()
    logger.info("DB initialized")

    await load_all()
    logger.info("Historical data loaded")

    # Register TwelveData live price → dashboard broadcast
    td_register(td_price_callback)

    for sym in ["BTCUSD"]:
        stream.subscribe(sym, stream_callback)

    await asyncio.gather(
        polling_loop(),
        news_loop(),
        stream.start(),
        td_stream_run(),       # TwelveData WS for XAUUSD + BTCUSD live ticks
    )


if __name__ == "__main__":
    import threading

    def run_api():
        from dashboard.api import app
        host = os.getenv("HOST", "0.0.0.0")
        port = int(os.getenv("PORT", 8000))
        uvicorn.run(app, host=host, port=port, log_level="warning")

    api_thread = threading.Thread(target=run_api, daemon=True)
    api_thread.start()
    logger.info(f"Dashboard: http://{os.getenv('HOST','0.0.0.0')}:{os.getenv('PORT',8000)}")

    asyncio.run(main())
