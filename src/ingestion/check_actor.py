from apify_client import ApifyClient
from dotenv import load_dotenv
import os

load_dotenv(override=True)

token = os.getenv("APIFY_API_TOKEN", "").strip()

client = ApifyClient(token)

try:
    actor_info = client.actor("tri_angle/telegram-scraper").get()

    print("=" * 45)
    print("ACTOR INFORMATION")
    print("=" * 45)

    print("Actor ID:", actor_info.id)
    print("Actor name:", actor_info.name)
    print("Actor username:", actor_info.username)
    print("Actor title:", actor_info.title)

except Exception as error:
    print("Error:", error)
