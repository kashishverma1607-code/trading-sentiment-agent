from apify_client import ApifyClient
from dotenv import load_dotenv
import os

load_dotenv(override=True)

token = os.getenv("APIFY_API_TOKEN", "").strip()

if not token:
    raise ValueError("Apify token missing in .env")

client = ApifyClient(token)

INPUT = {
    "collectMessages": True,
    "profiles": [
        "StockIntelligence"
    ]
}

print("Telegram channel configured successfully!")
print("Actor ID: GEHKCq804or1PjLFf")
print("Messages enabled:", INPUT["collectMessages"])
print("Channel:", INPUT["profiles"][0])
print("Ready for scraping.")
