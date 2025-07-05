from apify_client import ApifyClient
import os

APIFY_TOKEN = os.getenv("APIFY_TOKEN")  # Set this in your environment

def scrape_linkedin_profile(profile_url: str) -> dict:
    client = ApifyClient(APIFY_TOKEN)
    run_input = {"startUrls": [{"url": profile_url}]}

    try:
        run = client.actor("apify/linkedin-profile-scraper").call(run_input=run_input)
        items = client.dataset(run["defaultDatasetId"]).list_items().get("items", [])
        return items[0] if items else {}
    except Exception as e:
        print(f"[ERROR] LinkedIn scrape failed: {e}")
        return {}
