import os
import asyncio
from pathlib import Path
from dotenv import load_dotenv
from telegram import Bot

load_dotenv(Path(".env"))

async def main():
    bot = Bot(os.getenv("TELEGRAM_BOT_TOKEN"))
    async with bot:
        updates = await bot.get_updates()
        for update in updates:
            if update.message:
                print("Your Chat ID:", update.message.chat_id)

asyncio.run(main())
