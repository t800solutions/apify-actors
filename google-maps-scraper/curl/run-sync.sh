#!/usr/bin/env bash
# Run the Google Maps Scraper on Apify and print the places as JSON (runs of up to 5 minutes).
# Actor: https://apify.com/t800solutions/google-maps-scraper
#
# Usage:
#   export APIFY_TOKEN=<your Apify API token>
#   ./run-sync.sh
set -euo pipefail
: "${APIFY_TOKEN:?Set APIFY_TOKEN first: https://console.apify.com/settings/integrations}"

curl -sS -X POST "https://api.apify.com/v2/acts/t800solutions~google-maps-scraper/run-sync-get-dataset-items?maxTotalChargeUsd=1" \
  -H "Authorization: Bearer ${APIFY_TOKEN}" \
  -H "Content-Type: application/json" \
  -d '{"search_terms": ["restaurant"], "location": "Miami, FL, USA", "max_places_per_search": 20, "language": "en"}'
