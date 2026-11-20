from pathlib import Path
from dotenv import load_dotenv
import os

env_path = Path(".env").resolve()
load_dotenv(env_path, override=True)

print("ENV file exists:", env_path.exists())
print("Bot token loaded:", bool(os.getenv("TELEGRAM_BOT_TOKEN")))
print("Chat ID loaded:", bool(os.getenv("TELEGRAM_CHAT_ID")))
