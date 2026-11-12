"""Convert PDFs to LLM-ready Markdown with the PDF Extractor All-in-One on Apify (one .md file per PDF).

Actor: https://apify.com/t800solutions/pdf-extractor

Usage:
    pip install -r requirements.txt
    export APIFY_TOKEN=<your Apify API token>
    python pdf_to_markdown.py https://www.irs.gov/pub/irs-pdf/fw9.pdf --out markdown
    python pdf_to_markdown.py https://example.com/scanned.pdf --ocr --ocr-languages eng por

Markdown keeps headings, lists and tables, ready for ChatGPT, Claude or any LLM. With --ocr, scanned pages (no text
layer) are read by OCR; pages that already have text are not sent to OCR.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from decimal import Decimal
from pathlib import Path

from apify_client import ApifyClient

ACTOR = "t800solutions/pdf-extractor"


def file_name(source: str, index: int) -> str:
    stem = re.sub(r"[^A-Za-z0-9_-]+", "-", source.rsplit("/", 1)[-1].removesuffix(".pdf")).strip("-") or "document"
    return f"{index:02d}-{stem}.md"


def main() -> None:
    parser = argparse.ArgumentParser(description="PDF to Markdown with the PDF Extractor All-in-One on Apify.")
    parser.add_argument("urls", nargs="+", help="links to PDFs (or images, with --ocr)")
    parser.add_argument("--out", default="markdown", help="folder for the .md files")
    parser.add_argument("--ocr", action="store_true", help="read scanned pages with OCR (Add-on, extra cost per page)")
    parser.add_argument("--ocr-languages", nargs="+", default=["eng"], help="OCR languages, e.g. eng por spa")
    parser.add_argument("--max-charge", type=Decimal, default=Decimal("1.00"),
                        help="maximum charge for the run in US$ (the run stops there)")
    args = parser.parse_args()

    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("Set APIFY_TOKEN first: https://console.apify.com/settings/integrations")

    client = ApifyClient(token)
    run = client.actor(ACTOR).call(
        run_input={"urls": args.urls, "output_format": "document", "include_markdown": True,
                   "ocr_scanned_pages": args.ocr, "ocr_languages": args.ocr_languages},
        max_total_charge_usd=args.max_charge,
        logger=None,  # no Actor log in the terminal; open the run in Apify Console to see it
    )
    if run is None or run.status != "SUCCEEDED":
        sys.exit(f"The run did not succeed (status: {run.status if run else 'not started'}).")

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    for index, row in enumerate(client.dataset(run.default_dataset_id).iterate_items(), start=1):
        if row.get("status") == "failed":
            print(f"- {row['source']}: failed ({row.get('error_code')}), not charged")
            continue
        path = out / file_name(row["source"], index)
        path.write_text(row.get("markdown") or row.get("text") or "", encoding="utf-8")
        print(f"- {row['source']}: {row.get('extracted_page_count')} pages -> {path}")


if __name__ == "__main__":
    main()
