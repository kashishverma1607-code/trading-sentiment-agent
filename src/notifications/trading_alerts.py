import os
import asyncio
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv
from telegram import Bot

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

if not TOKEN or not CHAT_ID:
    raise ValueError("Telegram credentials missing in .env")

FILE = BASE_DIR / "reports/ai_recommendations.csv"

if not FILE.exists():
    raise FileNotFoundError("AI recommendations file missing")

df = pd.read_csv(FILE)

message = "🚀 TRADING SENTIMENT AGENT\n\n"

for _, row in df.iterrows():
    message += (
        f"📊 {row['Stock']}\n"
        f"RSI: {row.get('RSI', 'N/A')}\n"
        f"Sentiment: {row.get('Average_Sentiment', 'N/A')}\n"
        f"Recommendation: {row.get('AI_Recommendation', 'HOLD')}\n\n"
    )

message += "For research purposes only. Not financial advice."

async def main():
    bot = Bot(TOKEN)
    async with bot:
        await bot.send_message(
            chat_id=CHAT_ID,
            text=message
        )

    print("Trading alerts sent successfully!")

asyncio.run(main())
