"""Get the transcripts of a channel's latest videos with the YouTube Scraper All-in-One on Apify (one .txt per video).

Actor: https://apify.com/t800solutions/youtube-scraper

Usage:
    pip install -r requirements.txt
    export APIFY_TOKEN=<your Apify API token>
    python channel_transcripts.py https://www.youtube.com/@Google --max 20 --languages en pt --out transcripts

Transcripts come from YouTube's own captions (manual or auto-generated). Videos without captions are listed with the
reason and not charged for the transcript. Use --format srt, vtt, timestamped or json for other formats.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from decimal import Decimal
from pathlib import Path

from apify_client import ApifyClient

ACTOR = "t800solutions/youtube-scraper"
EXTENSIONS = {"text": "txt", "timestamped": "txt", "srt": "srt", "vtt": "vtt", "json": "json"}


def main() -> None:
    parser = argparse.ArgumentParser(description="Channel transcripts with the YouTube Scraper All-in-One on Apify.")
    parser.add_argument("channel", help="channel link, e.g. https://www.youtube.com/@Google")
    parser.add_argument("--max", type=int, default=20, help="how many of the latest videos (default 20)")
    parser.add_argument("--languages", nargs="+", default=["en"], help="language codes in order of preference")
    parser.add_argument("--format", default="text", choices=list(EXTENSIONS))
    parser.add_argument("--out", default="transcripts", help="folder for the transcript files")
    parser.add_argument("--max-charge", type=Decimal, default=Decimal("1.00"),
                        help="maximum charge for the run in US$ (the run stops there)")
    args = parser.parse_args()

    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("Set APIFY_TOKEN first: https://console.apify.com/settings/integrations")

    client = ApifyClient(token)
    run = client.actor(ACTOR).call(
        run_input={"start_urls": [args.channel], "max_videos": args.max, "transcript": True,
                   "transcript_languages": args.languages, "transcript_format": args.format},
        max_total_charge_usd=args.max_charge,
        logger=None,  # no Actor log in the terminal; open the run in Apify Console to see it
    )
    if run is None or run.status != "SUCCEEDED":
        sys.exit(f"The run did not succeed (status: {run.status if run else 'not started'}).")

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    saved = 0
    for video in client.dataset(run.default_dataset_id).iterate_items():
        if video.get("transcript_error") or not video.get("transcript"):
            print(f"- {video.get('title')}: no transcript ({video.get('transcript_error') or 'empty'}), not charged")
            continue
        stem = re.sub(r"[^A-Za-z0-9_-]+", "-", video.get("title") or video["id"]).strip("-")[:80] or video["id"]
        path = out / f"{video['id']}-{stem}.{EXTENSIONS[args.format]}"
        content = video["transcript"]
        path.write_text(content if isinstance(content, str) else __import__("json").dumps(content, ensure_ascii=False), encoding="utf-8")
        saved += 1
        print(f"- {video.get('title')}: {video.get('transcript_minutes')} min ({video.get('transcript_language')}) -> {path}")
    print(f"Saved {saved} transcripts to {out}/")


if __name__ == "__main__":
    main()
