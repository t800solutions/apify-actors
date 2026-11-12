"""Scrape Google Maps places with the Google Maps Scraper on Apify and save them to a CSV file.

Actor: https://apify.com/t800solutions/google-maps-scraper

Usage:
    pip install -r requirements.txt
    export APIFY_TOKEN=<your Apify API token>
    python scrape_places_to_csv.py "dentist" "Austin, TX, USA" --max 100 --out dentists.csv

The location can be a city ("Austin, TX, USA"), a whole state ("Texas, USA") or a country ("Italy").
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
from decimal import Decimal

from apify_client import ApifyClient

ACTOR = "t800solutions/google-maps-scraper"
COLUMNS = ["name", "phone", "website", "address", "city", "state", "country_code", "category", "rating",
           "reviews_count", "latitude", "longitude", "url"]


def main() -> None:
    parser = argparse.ArgumentParser(description="Google Maps places to CSV with the Google Maps Scraper on Apify.")
    parser.add_argument("search_term", help='what to look for, e.g. "dentist"')
    parser.add_argument("location", help='city, state or country, e.g. "Austin, TX, USA"')
    parser.add_argument("--max", type=int, default=50, help="maximum number of places (default 50)")
    parser.add_argument("--language", default="en", help="language of the results, e.g. en, pt-BR, fr")
    parser.add_argument("--out", default="places.csv", help="CSV file to write")
    parser.add_argument("--max-charge", type=Decimal, default=Decimal("1.00"),
                        help="maximum charge for the run in US$ (the run stops there)")
    args = parser.parse_args()

    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("Set APIFY_TOKEN first: https://console.apify.com/settings/integrations")

    client = ApifyClient(token)
    run = client.actor(ACTOR).call(
        run_input={"search_terms": [args.search_term], "location": args.location,
                   "max_places_per_search": args.max, "language": args.language},
        max_total_charge_usd=args.max_charge,
        logger=None,  # no Actor log in the terminal; open the run in Apify Console to see it
    )
    if run is None or run.status != "SUCCEEDED":
        sys.exit(f"The run did not succeed (status: {run.status if run else 'not started'}).")

    places = list(client.dataset(run.default_dataset_id).iterate_items())
    with open(args.out, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=COLUMNS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(places)
    print(f"Saved {len(places)} places to {args.out}")


if __name__ == "__main__":
    main()
