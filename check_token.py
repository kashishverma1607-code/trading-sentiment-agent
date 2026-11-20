from dotenv import load_dotenv
import os

load_dotenv(".env")
token = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()

print("Token found:", bool(token))
print("Contains colon:", ":" in token)
print("Starts with numeric ID:", token.split(":")[0].isdigit() if ":" in token else False)
print("Token length:", len(token))
