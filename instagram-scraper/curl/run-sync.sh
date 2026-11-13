#!/usr/bin/env bash
# Run the Instagram Scraper All-in-One on Apify and print the rows as JSON (runs of up to 5 minutes).
# Actor: https://apify.com/t800solutions/instagram-scraper
#
# Usage:
#   export APIFY_TOKEN=<your Apify API token>
#   ./run-sync.sh nasa
set -euo pipefail
: "${APIFY_TOKEN:?Set APIFY_TOKEN first: https://console.apify.com/settings/integrations}"
PROFILE="${1:-nasa}"

curl -sS -X POST "https://api.apify.com/v2/acts/t800solutions~instagram-scraper/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer ${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d "{\"start_urls\": [\"${PROFILE}\"], \"max_posts_per_profile\": 12}"
