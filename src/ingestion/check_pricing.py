from apify_client import ApifyClient
from dotenv import load_dotenv
import os

load_dotenv(override=True)

client = ApifyClient(os.getenv("APIFY_API_TOKEN").strip())
actor = client.actor("tri_angle/telegram-scraper").get()

print("\n--- PRICING INFORMATION ---")
print(actor.pricing_infos)

print("\n--- DEFAULT RUN OPTIONS ---")
print(actor.default_run_options)

print("\n--- EXAMPLE INPUT ---")
print(actor.example_run_input)

