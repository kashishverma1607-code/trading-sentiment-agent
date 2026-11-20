from apify_client import ApifyClient
from dotenv import load_dotenv
import os

load_dotenv(override=True)

token = os.getenv("APIFY_API_TOKEN", "").strip()

if not token:
    raise ValueError("Apify token missing")

client = ApifyClient(token)

INPUT = {
    "collectMessages": True,
    "profiles": ["https://t.me/StockIntelligence"]
}

print("Actor: Telegram Scraper")
print("Channel:", INPUT["profiles"][0])
print("Token loaded:", bool(token))
print("Configuration ready!")
print("No scraping started.")
