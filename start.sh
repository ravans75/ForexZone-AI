#!/bin/bash
export DATABASE_URL=postgresql://trader:trader@localhost:5432/trading_bot
export TWELVE_API_KEY=3685c5293bfe40ce82f366f613091ef8
export NEWS_API_KEY=6066ad61000e4832a3096856089c23b1
export TELEGRAM_BOT_TOKEN=8723782051:AAGQhYYW1Yy5u7mS3kLegKI_zTwKAHvuFOo
export TELEGRAM_CHAT_ID=8518628617
export HOST=0.0.0.0
export PORT=8000

cd /root/trading_bot
exec /root/trading_bot/venv/bin/python main.py
