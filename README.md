# Trading Bot — Setup Guide

## Quick Start

### 1. Clone & configure
```bash
cd /root/trading_bot
cp .env.example .env
# Edit .env with your API keys
```

### 2. Get API Keys (free tiers available)
| Service | URL | Used for |
|---|---|---|
| TwelveData | https://twelvedata.com | Forex/Gold OHLCV |
| NewsAPI | https://newsapi.org | News sentiment |
| Telegram BotFather | https://t.me/BotFather | Alerts |
| Binance | Public (no key needed) | Crypto OHLCV |

### 3. Docker (recommended)
```bash
docker-compose up -d
```
Dashboard: http://localhost:8000

### 4. Manual setup
```bash
# Install deps
pip install -r requirements.txt
python -m textblob.download_corpora

# Start PostgreSQL (or use Docker just for DB)
docker run -d --name pg -e POSTGRES_USER=trader -e POSTGRES_PASSWORD=trader \
  -e POSTGRES_DB=trading_bot -p 5432:5432 postgres:16-alpine

# Run
python main.py
```

### 5. Train LSTM models (optional, improves signals)
```python
from core.historical_loader import get_ohlcv_df
from ai.training_pipeline import train

for symbol in ["XAUUSD", "EURUSD", "BTCUSD", "ETHUSD"]:
    df = get_ohlcv_df(symbol, "1h", limit=2000)
    train(symbol, df)
```

## Architecture
```
main.py              — orchestrator (polling + streams + news)
core/
  market_data.py     — fetch OHLCV from Binance / TwelveData
  historical_loader  — store/retrieve from PostgreSQL
  realtime_stream    — Binance WebSocket (crypto)
  news_engine        — NewsAPI + TextBlob sentiment
strategy/
  smc_engine         — BOS, CHoCH, Order Blocks, FVG, Liquidity
  price_action       — Trend, S/R, Patterns
  volume_engine      — Spike, Divergence, VWAP, A/D
  liquidity_engine   — Pools, Stop Hunts
ai/
  feature_engineering — 14-dim feature vectors
  lstm_predictor      — load & run LSTM model
  training_pipeline   — train LSTM per symbol
signals/
  signal_engine       — combine all signals → BUY/SELL
  risk_management     — validate RR, position sizing
alerts/
  telegram_bot        — send formatted Telegram alerts
dashboard/
  api.py              — FastAPI + WebSocket server
  templates/index.html — live chart + signal panel
database/
  models.py           — OHLCV, Signal, NewsItem tables
  db_manager.py       — SQLAlchemy engine + session
```

## Signal Logic
Signals fire when score ≥ 6/15 points:
- BOS/CHoCH: +2/+1
- Liquidity Grab (Stop Hunt): +2
- Order Block: +2
- FVG: +1
- Volume Spike: +1
- VWAP position: +1
- Trend alignment: +1
- AI prediction >65%: +2
- News sentiment: +1
- Active session (London/NY): +1
- Chart pattern: +1
