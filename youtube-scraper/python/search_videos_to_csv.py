"""Search YouTube and save the videos to a CSV file with the YouTube Scraper All-in-One on Apify.

Actor: https://apify.com/t800solutions/youtube-scraper

Usage:
    pip install -r requirements.txt
    export APIFY_TOKEN=<your Apify API token>
    python search_videos_to_csv.py "web scraping tutorial" --max 50 --out videos.csv

Add --list for the cheaper "list only" mode (title, views, duration, channel, without opening each video).
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
from decimal import Decimal

from apify_client import ApifyClient

ACTOR = "t800solutions/youtube-scraper"
COLUMNS = ["title", "url", "channel_name", "views", "likes", "comments_count", "published", "duration_seconds", "type",
           "category", "channel_subscribers", "channel_url", "id"]


def main() -> None:
    parser = argparse.ArgumentParser(description="YouTube search results to CSV with the YouTube Scraper All-in-One on Apify.")
    parser.add_argument("search_term", help='what to search for, e.g. "web scraping tutorial"')
    parser.add_argument("--max", type=int, default=50, help="maximum number of videos (default 50)")
    parser.add_argument("--list", action="store_true", help="list only: faster and cheaper, no likes or full description")
    parser.add_argument("--out", default="videos.csv", help="CSV file to write")
    parser.add_argument("--max-charge", type=Decimal, default=Decimal("1.00"),
                        help="maximum charge for the run in US$ (the run stops there)")
    args = parser.parse_args()

    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("Set APIFY_TOKEN first: https://console.apify.com/settings/integrations")

    client = ApifyClient(token)
    run = client.actor(ACTOR).call(
        run_input={"search_terms": [args.search_term], "max_videos": args.max, "details": "list" if args.list else "full"},
        max_total_charge_usd=args.max_charge,
        logger=None,  # no Actor log in the terminal; open the run in Apify Console to see it
    )
    if run is None or run.status != "SUCCEEDED":
        sys.exit(f"The run did not succeed (status: {run.status if run else 'not started'}).")

    videos = list(client.dataset(run.default_dataset_id).iterate_items())
    with open(args.out, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=COLUMNS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(videos)
    print(f"Saved {len(videos)} videos to {args.out}")


if __name__ == "__main__":
    main()
