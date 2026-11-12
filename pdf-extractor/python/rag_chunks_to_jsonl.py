"""Split PDFs into RAG chunks with page numbers and save them as JSONL, ready for embeddings and a vector database.

Uses the PDF Extractor All-in-One on Apify with Output format = RAG chunks.
Actor: https://apify.com/t800solutions/pdf-extractor

Usage:
    pip install -r requirements.txt
    export APIFY_TOKEN=<your Apify API token>
    python rag_chunks_to_jsonl.py https://www.irs.gov/pub/irs-pdf/fw9.pdf --chunk-size 1000 --overlap 150

Each line of the JSONL has the chunk text and metadata (source, first and last page, position), so answers can cite
the page. Load it into Pinecone, Weaviate, Chroma, Qdrant, LangChain or LlamaIndex.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from decimal import Decimal

from apify_client import ApifyClient

ACTOR = "t800solutions/pdf-extractor"


def main() -> None:
    parser = argparse.ArgumentParser(description="PDF to RAG chunks (JSONL) with the PDF Extractor All-in-One on Apify.")
    parser.add_argument("urls", nargs="+", help="links to PDFs")
    parser.add_argument("--chunk-size", type=int, default=1000, help="characters per chunk (default 1000)")
    parser.add_argument("--overlap", type=int, default=150, help="characters shared by neighbor chunks (default 150)")
    parser.add_argument("--out", default="chunks.jsonl")
    parser.add_argument("--max-charge", type=Decimal, default=Decimal("1.00"),
                        help="maximum charge for the run in US$ (the run stops there)")
    args = parser.parse_args()

    token = os.environ.get("APIFY_TOKEN")
    if not token:
        sys.exit("Set APIFY_TOKEN first: https://console.apify.com/settings/integrations")

    client = ApifyClient(token)
    run = client.actor(ACTOR).call(
        run_input={"urls": args.urls, "output_format": "chunks", "chunk_size": args.chunk_size,
                   "chunk_overlap": args.overlap},
        max_total_charge_usd=args.max_charge,
        logger=None,  # no Actor log in the terminal; open the run in Apify Console to see it
    )
    if run is None or run.status != "SUCCEEDED":
        sys.exit(f"The run did not succeed (status: {run.status if run else 'not started'}).")

    count = 0
    with open(args.out, "w", encoding="utf-8") as file:
        for row in client.dataset(run.default_dataset_id).iterate_items():
            if row.get("status") == "failed" or not row.get("text"):
                continue
            record = {"text": row["text"], "metadata": {"source": row["source"], "page_start": row.get("page_start"),
                                                        "page_end": row.get("page_end"), "chunk": row.get("chunk_index")}}
            file.write(json.dumps(record, ensure_ascii=False) + "\n")
            count += 1
    print(f"Saved {count} chunks to {args.out}")


if __name__ == "__main__":
    main()
