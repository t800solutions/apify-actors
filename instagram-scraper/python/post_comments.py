"""Get the comments of Instagram posts or reels with the Instagram Scraper All-in-One on Apify (one JSON file per post).

Actor: https://apify.com/t800solutions/instagram-scraper

Usage:
    pip install -r requirements.txt
    export APIFY_TOKEN=<your Apify API token>
    python post_comments.py https://www.instagram.com/reel/Dfc1mYxFevS/ https://www.instagram.com/p/XXXX/
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from decimal import Decimal
from pathlib import Path

from apify_client import ApifyClient

ACTOR = "t800solutions/instagram-scraper"


def main() -> None:
    parser = argparse.ArgumentParser(description="Instagram post comments with the Instagram Scraper All-in-One on Apify.")
    parser.add_argument("posts", nargs="+", help="post or reel links")
    parser.add_argument("--max-comments", type=int, default=50, help="comments per post (Instagram shows about 11 without login)")
    parser.add_argument("--out-dir", default="comments", help="folder for the JSON files")
    parser.add_argument("--max-charge", type=Decimal, default=Decimal("1.00"), help="maximum charge for the run in US$")
    args = parser.parse_args()

    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("Set APIFY_TOKEN first: https://console.apify.com/settings/integrations")

    client = ApifyClient(token)
    run = client.actor(ACTOR).call(
        run_input={"start_urls": args.posts, "comments": True, "max_comments_per_post": args.max_comments},
        max_total_charge_usd=args.max_charge, logger=None,
    )
    if run is None or run.status != "SUCCEEDED":
        sys.exit(f"The run did not succeed (status: {run.status if run else 'not started'}).")

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    for row in client.dataset(run.default_dataset_id).iterate_items():
        if row.get("kind") != "post":
            continue
        path = out / f"{row['shortcode']}.json"
        path.write_text(json.dumps({"url": row["url"], "caption": row.get("caption"), "likes_count": row.get("likes_count"),
                                    "comments_count": row.get("comments_count"), "comments": row.get("comments") or []},
                                   indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"{row['url']}: {row.get('comments_delivered', 0)} comments -> {path}")


if __name__ == "__main__":
    main()
