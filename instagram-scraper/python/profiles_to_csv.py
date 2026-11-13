"""Get Instagram profiles (followers, following, bio, links) into a CSV file with the Instagram Scraper All-in-One on Apify.

Actor: https://apify.com/t800solutions/instagram-scraper

Usage:
    pip install -r requirements.txt
    export APIFY_TOKEN=<your Apify API token>
    python profiles_to_csv.py nasa natgeo nike --out profiles.csv
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
from decimal import Decimal

from apify_client import ApifyClient

ACTOR = "t800solutions/instagram-scraper"
COLUMNS = ["username", "full_name", "followers_count", "following_count", "posts_count", "verified", "private",
           "category", "biography", "external_urls", "url", "posts_delivered"]


def main() -> None:
    parser = argparse.ArgumentParser(description="Instagram profiles to CSV with the Instagram Scraper All-in-One on Apify.")
    parser.add_argument("profiles", nargs="+", help="usernames or profile links, e.g. nasa https://www.instagram.com/natgeo/")
    parser.add_argument("--posts", type=int, default=0, help="latest posts to include per profile (default 0 = details only)")
    parser.add_argument("--out", default="profiles.csv", help="CSV file to write")
    parser.add_argument("--max-charge", type=Decimal, default=Decimal("1.00"),
                        help="maximum charge for the run in US$ (the run stops there)")
    args = parser.parse_args()

    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("Set APIFY_TOKEN first: https://console.apify.com/settings/integrations")

    client = ApifyClient(token)
    run = client.actor(ACTOR).call(
        run_input={"start_urls": args.profiles, "max_posts_per_profile": args.posts},
        max_total_charge_usd=args.max_charge,
        logger=None,  # no Actor log in the terminal; open the run in Apify Console to see it
    )
    if run is None or run.status != "SUCCEEDED":
        sys.exit(f"The run did not succeed (status: {run.status if run else 'not started'}).")

    rows = [r for r in client.dataset(run.default_dataset_id).iterate_items() if r.get("kind") == "profile"]
    with open(args.out, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=COLUMNS, extrasaction="ignore")
        writer.writeheader()
        for r in rows:
            r["external_urls"] = " ".join(r.get("external_urls") or [])
            writer.writerow(r)
    print(f"Saved {len(rows)} profiles to {args.out}")


if __name__ == "__main__":
    main()
