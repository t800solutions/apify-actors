"""Extract every table from PDFs to CSV files with the PDF Extractor All-in-One on Apify (tables are free).

Actor: https://apify.com/t800solutions/pdf-extractor

Usage:
    pip install -r requirements.txt
    export APIFY_TOKEN=<your Apify API token>
    python extract_tables_to_csv.py https://www.w3.org/WAI/WCAG21/working-examples/pdf-table/table.pdf --out tables

One CSV per table, named after the PDF and the page the table is on. Tables with or without borders and multi-row
headers are supported; tables are included in the page price.
"""

from __future__ import annotations

import argparse
import csv
import os
import re
import sys
from decimal import Decimal
from pathlib import Path

from apify_client import ApifyClient

ACTOR = "t800solutions/pdf-extractor"


def main() -> None:
    parser = argparse.ArgumentParser(description="PDF tables to CSV with the PDF Extractor All-in-One on Apify.")
    parser.add_argument("urls", nargs="+", help="links to PDFs")
    parser.add_argument("--out", default="tables", help="folder for the CSV files")
    parser.add_argument("--max-charge", type=Decimal, default=Decimal("1.00"),
                        help="maximum charge for the run in US$ (the run stops there)")
    args = parser.parse_args()

    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("Set APIFY_TOKEN first: https://console.apify.com/settings/integrations")

    client = ApifyClient(token)
    run = client.actor(ACTOR).call(
        run_input={"urls": args.urls, "output_format": "document", "extract_tables": True, "include_markdown": False},
        max_total_charge_usd=args.max_charge,
        logger=None,  # no Actor log in the terminal; open the run in Apify Console to see it
    )
    if run is None or run.status != "SUCCEEDED":
        sys.exit(f"The run did not succeed (status: {run.status if run else 'not started'}).")

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    total = 0
    for row in client.dataset(run.default_dataset_id).iterate_items():
        stem = re.sub(r"[^A-Za-z0-9_-]+", "-", row["source"].rsplit("/", 1)[-1].removesuffix(".pdf")).strip("-") or "document"
        for number, table in enumerate(row.get("tables") or [], start=1):
            path = out / f"{stem}-page{table['page']}-table{number}.csv"
            with open(path, "w", newline="", encoding="utf-8") as file:
                csv.writer(file).writerows(table["rows"])
            total += 1
            print(f"- {path} ({len(table['rows'])} rows)")
    print(f"Saved {total} tables to {out}/")


if __name__ == "__main__":
    main()
