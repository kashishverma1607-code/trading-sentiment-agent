import os
from pathlib import Path
from dotenv import load_dotenv
from telegram import Bot

BASE_DIR = Path(__file__).resolve().parents[2]
load_dotenv(BASE_DIR / ".env")

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError("Telegram token missing in .env file")

async def send_message(chat_id, message):
    bot = Bot(token=TOKEN)
    async with bot:
        await bot.send_message(
            chat_id=chat_id,
            text=message
        )

print("Telegram notification module loaded successfully!")
