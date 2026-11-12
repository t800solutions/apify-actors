#!/usr/bin/env bash
# Run the YouTube Scraper All-in-One on Apify and print the videos as JSON (runs of up to 5 minutes).
# Actor: https://apify.com/t800solutions/youtube-scraper
#
# Usage:
#   export APIFY_TOKEN=<your Apify API token>
#   ./run-sync.sh "web scraping tutorial"
set -euo pipefail
: "${APIFY_TOKEN:?Set APIFY_TOKEN first: https://console.apify.com/settings/integrations}"
TERM_="${1:-web scraping tutorial}"

curl -sS -X POST "https://api.apify.com/v2/acts/t800solutions~youtube-scraper/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer ${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d "{\"search_terms\": [\"${TERM_}\"], \"max_videos\": 10, \"details\": \"full\"}"
