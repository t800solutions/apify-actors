#!/usr/bin/env bash
# Run the PDF Extractor All-in-One on Apify and print the result as JSON (runs of up to 5 minutes).
# Actor: https://apify.com/t800solutions/pdf-extractor
#
# Usage:
#   export APIFY_TOKEN=<your Apify API token>
#   ./run-sync.sh https://www.w3.org/WAI/WCAG21/working-examples/pdf-table/table.pdf
set -euo pipefail
: "${APIFY_TOKEN:?Set APIFY_TOKEN first: https://console.apify.com/settings/integrations}"
PDF_URL="${1:-https://www.w3.org/WAI/WCAG21/working-examples/pdf-table/table.pdf}"

curl -sS -X POST "https://api.apify.com/v2/acts/t800solutions~pdf-extractor/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer ${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d "{\"urls\": [\"${PDF_URL}\"], \"output_format\": \"document\", \"include_markdown\": true}"
