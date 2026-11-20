from apify_client import ApifyClient
from dotenv import load_dotenv
import os
import json

load_dotenv(override=True)

client = ApifyClient(os.getenv("APIFY_API_TOKEN").strip())

try:
    actor = client.actor("GEHKCq804or1PjLFf")

    versions = actor.versions().list()

    print("\nACTOR VERSIONS")
    print(json.dumps(versions.items, indent=2, default=str))

    if versions.items:
        version = versions.items[0].get("versionNumber")
        print("\nLATEST VERSION:", version)

        schema = actor.version(version).get()
        print("\nACTOR INPUT SCHEMA")
        print(json.dumps(schema, indent=2, default=str))

except Exception as error:
    print("ERROR:", type(error).__name__, str(error))
