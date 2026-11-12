"""Find local businesses without a website on Google Maps: a lead list for web designers and marketing agencies.

Uses the Google Maps Scraper on Apify with the "Places with or without a website" filter (Add-on: Filters).
Actor: https://apify.com/t800solutions/google-maps-scraper

Usage:
    pip install -r requirements.txt
    export APIFY_TOKEN=<your Apify API token>
    python businesses_without_website.py "personal trainer" "Florianópolis, SC, Brasil" --max 20 --language pt-BR

Tip: categories where many businesses have no website (small local services) fill the list faster. Places that have a
website are skipped and not charged, so very common categories may need a longer run.
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
from decimal import Decimal

from apify_client import ApifyClient

ACTOR = "t800solutions/google-maps-scraper"
COLUMNS = ["name", "phone", "address", "city", "category", "rating", "reviews_count", "url"]


def main() -> None:
    parser = argparse.ArgumentParser(description="Businesses without a website on Google Maps, to CSV.")
    parser.add_argument("search_term")
    parser.add_argument("location")
    parser.add_argument("--max", type=int, default=20, help="maximum number of places (default 20)")
    parser.add_argument("--language", default="en")
    parser.add_argument("--out", default="no_website_leads.csv")
    parser.add_argument("--max-charge", type=Decimal, default=Decimal("1.00"),
                        help="maximum charge for the run in US$ (the run stops there)")
    args = parser.parse_args()

    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("Set APIFY_TOKEN first: https://console.apify.com/settings/integrations")

    client = ApifyClient(token)
    run = client.actor(ACTOR).call(
        run_input={"search_terms": [args.search_term], "location": args.location,
                   "max_places_per_search": args.max, "language": args.language,
                   "website_filter": "without_website"},
        max_total_charge_usd=args.max_charge,
        logger=None,  # no Actor log in the terminal; open the run in Apify Console to see it
    )
    if run is None or run.status != "SUCCEEDED":
        sys.exit(f"The run did not succeed (status: {run.status if run else 'not started'}).")

    leads = list(client.dataset(run.default_dataset_id).iterate_items())
    with open(args.out, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=COLUMNS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(leads)
    print(f"Saved {len(leads)} businesses without a website to {args.out}")


if __name__ == "__main__":
    main()
