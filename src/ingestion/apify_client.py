import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv(override=True)

token = os.getenv("APIFY_API_TOKEN", "").strip()

if not token:
    print("Token missing")
    raise SystemExit(1)

try:
    client = ApifyClient(token)

    actors = client.actors().list(limit=1)

    print("APIFY ACTOR API ACCESS SUCCESSFUL")
    print("Actors found:", len(actors.items))

except Exception as error:
    print("ACTOR API ERROR:", error)
