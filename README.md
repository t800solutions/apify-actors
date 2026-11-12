# T800 Solutions Actors on Apify: examples and guides

[![Apify Store](https://img.shields.io/badge/Apify%20Store-t800solutions-97d700)](https://apify.com/t800solutions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Ready-to-run examples for the **T800 Solutions** Actors on the [Apify Store](https://apify.com/t800solutions): a **Google Maps scraper** for lead lists and local market data, and an all-in-one **PDF extractor** for text, Markdown, tables, OCR and RAG chunks. Each example calls the Actor through the official Apify API client, waits for the run and saves the results to a file you can open right away.

| Actor | What it does | Examples |
|---|---|---|
| [📍 Google Maps Scraper – Most Accurate Extractor](https://apify.com/t800solutions/google-maps-scraper) | Business names, phones, websites, addresses, ratings and reviews from Google Maps, across whole cities and only inside your area | [google-maps-scraper/](google-maps-scraper/) |
| [📄 PDF Extractor All-in-One: Text, Tables & OCR](https://apify.com/t800solutions/pdf-extractor) | PDF to text, Markdown, tables, OCR for scanned PDFs in 20 languages, RAG chunks and images | [pdf-extractor/](pdf-extractor/) |

## 🚀 Quick start

1. Create a free Apify account at [apify.com](https://apify.com) (the Free plan includes $5 of usage every month, no credit card).
2. Copy your API token from [Console → Settings → API & Integrations](https://console.apify.com/settings/integrations).
3. Pick an example folder, install the client and run it:

```bash
export APIFY_TOKEN=<your Apify API token>

# Python
pip install -r google-maps-scraper/python/requirements.txt
python google-maps-scraper/python/scrape_places_to_csv.py "dentist" "Austin, TX, USA" --max 50

# JavaScript (Node.js 18+)
cd pdf-extractor/javascript && npm install && node pdf-to-markdown.mjs https://www.irs.gov/pub/irs-pdf/fw9.pdf
```

Every example sets a **maximum charge per run** (`--max-charge`, default $1.00), so a run never costs more than you expect. Both Actors are pay per event: you pay only for what is delivered, and failed items are not charged.

## 🧭 What is inside

```
google-maps-scraper/
  python/       scrape_places_to_csv.py, businesses_without_website.py
  javascript/   scrape-places.mjs
  curl/         run-sync.sh
pdf-extractor/
  python/       pdf_to_markdown.py, extract_tables_to_csv.py, rag_chunks_to_jsonl.py
  javascript/   pdf-to-markdown.mjs
  curl/         run-sync.sh
```

## 🔌 Other ways to use the Actors

- **No code:** open the Actor page on the Apify Store, fill in the form and click Start. Results export to Excel, CSV or JSON.
- **Ready-made examples on Apify:** each Actor has example tasks you can copy and run, such as [scanned PDF to text with OCR](https://apify.com/t800solutions/pdf-extractor/examples/scanned-pdf-to-text-ocr) or [restaurants in New York City](https://apify.com/t800solutions/google-maps-scraper/examples/restaurants-in-new-york-city).
- **Automation tools:** the official Apify integrations for [n8n](https://docs.apify.com/platform/integrations/n8n), [Make](https://docs.apify.com/platform/integrations/make) and [Zapier](https://docs.apify.com/platform/integrations/zapier).
- **AI agents:** Claude, Cursor and other MCP clients can find and run the Actors through the [Apify MCP server](https://docs.apify.com/platform/integrations/mcp).

## ❓ FAQ

**Do I need a paid Apify plan?** No. The Free plan's monthly $5 covers about 1,500 Google Maps places or about 4,700 pages of digital PDFs.

**Where do I find my API token?** In [Console → Settings → API & Integrations](https://console.apify.com/settings/integrations). Keep it secret: use an environment variable, never paste it into code you share.

**A run failed. What now?** The scripts print the run status. Open the run in [Apify Console → Runs](https://console.apify.com/actors/runs) to see the log, or open an issue on the Actor page.

## 🤝 Contributing

Found a bug in an example or want another one? Open an issue or a pull request in this repository.

## 📄 License

The examples are released under the [MIT License](LICENSE). The Actors themselves run on Apify and are billed by Apify.
