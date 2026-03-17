# Trading Bot — Project Notes

## Overview
AI-powered trading signal system for XAUUSD, EURUSD, BTCUSD, ETHUSD.
Generates BUY/SELL signals with Entry, TP, SL, Confidence score.
Sends Telegram alerts with chart images. Python Dash dashboard.

---

## Server Info
- Local IP: 172.20.92.61
- SSH: `ssh root@172.20.92.61` (password: `kali`)
- Dashboard: http://172.20.92.61:8050
- API: http://172.20.92.61:8000

---

## Services
```bash
systemctl status trading-bot     # signal engine + FastAPI
systemctl status trading-dash     # Dash dashboard

systemctl restart trading-bot
systemctl restart trading-dash

journalctl -u trading-bot -f      # live logs
journalctl -u trading-dash -f
```

---

## API Keys
| Key | Value |
|-----|-------|
| TwelveData | 3685c5293bfe40ce82f366f613091ef8 |
| NewsAPI | 6066ad61000e4832a3096856089c23b1 |
| Telegram Bot Token | 8723782051:AAGQhYYW1Yy5u7mS3kLegKI_zTwKAHvuFOo |
| Telegram Chat ID | 8518628617 |

---

## Database
- Engine: PostgreSQL (Docker container: `trading_postgres`)
- URL: `postgresql://trader:trader@localhost:5432/trading_bot`
- Tables: `ohlcv`, `signals`, `news`, `alert_logs`

```bash
docker exec trading_postgres psql -U trading_user -d trading_bot -c "\dt"
```

---

## Project Structure
```
/root/trading_bot/
├── main.py                    # orchestrator
├── start.sh                   # manual start script
├── requirements.txt
├── .env                       # API keys
├── core/
│   ├── market_data.py         # yfinance (free, no rate limit)
│   ├── historical_loader.py   # store OHLCV to PostgreSQL
│   ├── realtime_stream.py     # Binance WebSocket (crypto)
│   └── news_engine.py         # NewsAPI + TextBlob sentiment
├── strategy/
│   ├── smc_engine.py          # BOS, CHoCH, OB, FVG, Liquidity
│   ├── price_action.py        # Trend, S/R, Patterns
│   ├── volume_engine.py       # VWAP, Volume spike/divergence
│   ├── liquidity_engine.py    # Stop hunt detection
│   └── multi_timeframe.py     # M5/M15/H1/H4 bias
├── ai/
│   ├── feature_engineering.py # 14-dim feature vectors
│   ├── lstm_predictor.py      # LSTM model inference
│   └── training_pipeline.py   # train per-symbol models
├── signals/
│   ├── signal_engine.py       # combine all → BUY/SELL
│   └── risk_management.py     # RR 1:3 min, 0.02% risk, 1% DD
├── alerts/
│   └── telegram_bot.py        # send chart + message
├── dashboard/
│   ├── api.py                 # FastAPI backend (port 8000)
│   ├── dash_app.py            # Python Dash UI (port 8050)
│   └── chart_engine.py        # Plotly chart image generator
└── database/
    ├── models.py              # SQLAlchemy models
    └── db_manager.py          # DB session management
```

---

## Data Sources
| Symbol | Source | Ticker |
|--------|--------|--------|
| XAUUSD | yfinance | GC=F (Gold Futures) |
| EURUSD | yfinance | EURUSD=X |
| BTCUSD | yfinance + Binance WS | BTC-USD |
| ETHUSD | yfinance + Binance WS | ETH-USD |

---

## Signal Logic
Signals fire when confidence >= 0.25 AND RR >= 1:3

Scoring (0–1 each, averaged):
- MTF bias (M5/M15/H1/H4 alignment)
- Volume score (VWAP, spike, divergence)
- SMC score (BOS, CHoCH, OB, FVG, liquidity grab)
- AI probability (LSTM model, defaults 0.5 if no model)

### Risk Rules
- Min RR: 1:3
- Max RR: 1:100
- Max risk per trade: 0.02% of capital
- Max daily drawdown: 1%
- Default capital: $100,000

---

## Dashboard Tabs (http://172.20.92.61:8050)
1. **XAUUSD Chart** — 1m candlestick + Entry/TP/SL lines + signal badges
2. **MTF Signals** — M5/M15/H1/H4 charts + AI gauge + BUY/SELL/WAIT conclusion
3. **Other Assets** — EURUSD/BTCUSD/ETHUSD signal cards with TP/SL/RR
4. **News Feed** — live news with sentiment scores per symbol
5. **History & Alerts** — trade history + Telegram alert log

---

## Telegram Alert Format
```
⚡ TRADE SIGNAL
Pair: XAUUSD
Signal: BUY
Entry: 5008.89
TP: 5015.31
SL: 5006.76
Confidence: 54%
MTF Bias: BUY ✅
+ chart image attached
```

---

## Train LSTM Models (optional)
```python
from core.historical_loader import get_ohlcv_df
from ai.training_pipeline import train

for symbol in ["XAUUSD", "EURUSD", "BTCUSD", "ETHUSD"]:
    df = get_ohlcv_df(symbol, "1h", limit=2000)
    train(symbol, df)
```
Models saved to: `/root/trading_bot/ai/models/`

---

## Common Commands
```bash
# View live signals
curl http://localhost:8000/api/signals | python3 -m json.tool

# View XAUUSD candles
curl "http://localhost:8000/api/ohlcv/XAUUSD?timeframe=1m&limit=5"

# View MTF bias
curl http://localhost:8000/api/mtf/XAUUSD

# Check bot log
tail -f /root/trading_bot/bot.log

# Restart everything
systemctl restart trading-bot trading-dash
```

---

## Notes
- TwelveData replaced with **yfinance** (free, no API key needed)
- Binance WebSocket used for real-time crypto price streaming
- XAUUSD uses Gold Futures (GC=F) as proxy — prices ~$5000/oz
- HTML dashboard removed, replaced with Python Dash
- Bot auto-restarts via systemd on crash
