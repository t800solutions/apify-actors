# PDF Extractor examples: PDF to Markdown, tables to CSV, RAG chunks (Python, JavaScript, cURL)

Examples for **[📄 PDF Extractor All-in-One: Text, Tables & OCR](https://apify.com/t800solutions/pdf-extractor)** on Apify: turn any PDF into clean, structured data with text in reading order (even 2, 3 or 4-column layouts), LLM-ready Markdown, tables as rows and columns, OCR for scanned PDFs in 20 languages, RAG chunks with page numbers, and the images inside the PDF. Failed PDFs are not charged.

## Examples

| Example | What it does |
|---|---|
| [python/pdf_to_markdown.py](python/pdf_to_markdown.py) | PDFs to `.md` files for ChatGPT, Claude or any LLM; `--ocr` reads scanned pages |
| [python/extract_tables_to_csv.py](python/extract_tables_to_csv.py) | Every table of every PDF to its own CSV file (tables are free) |
| [python/rag_chunks_to_jsonl.py](python/rag_chunks_to_jsonl.py) | Overlapping chunks with page numbers, as JSONL for embeddings and vector databases |
| [javascript/pdf-to-markdown.mjs](javascript/pdf-to-markdown.mjs) | PDF to Markdown from Node.js |
| [curl/run-sync.sh](curl/run-sync.sh) | One HTTP call that runs the Actor and returns the result (runs of up to 5 minutes) |

## How to run

```bash
export APIFY_TOKEN=<your Apify API token>   # https://console.apify.com/settings/integrations

cd python
pip install -r requirements.txt
python pdf_to_markdown.py https://www.irs.gov/pub/irs-pdf/fw9.pdf
python extract_tables_to_csv.py https://www.w3.org/WAI/WCAG21/working-examples/pdf-table/table.pdf
python rag_chunks_to_jsonl.py https://www.irs.gov/pub/irs-pdf/fw9.pdf --chunk-size 1000 --overlap 150
```

Every example caps the charge per run (default $1.00). Up to 1,000 PDF links per run; uploads and base64 also work through the API.

## Input

| Field | Example | Meaning |
|---|---|---|
| `urls` | `["https://example.com/report.pdf"]` | Links to PDFs or images |
| `output_format` | `"document"` | `document` (one row per PDF), `pages` (one row per page) or `chunks` (RAG chunks) |
| `include_markdown` | `true` | LLM-ready Markdown with headings, lists and tables |
| `extract_tables` | `true` | Tables as rows and columns (free) |
| `ocr_scanned_pages` | `true` | Add-on: OCR for pages without a text layer |
| `ocr_languages` | `["eng", "por"]` | OCR languages (20 available) |
| `page_range` | `"1-5, 8, 12-"` | Only some pages |
| `pdf_password` | `"secret"` | Password-protected PDFs |

The full list of fields is on the [Actor page](https://apify.com/t800solutions/pdf-extractor) (Input tab).

## Output (one row per PDF, shortened)

```json
{
  "source": "https://example.com/annual-report.pdf",
  "status": "success",
  "page_count": 3,
  "extracted_page_count": 3,
  "ocr_page_count": 0,
  "text": "Annual Report 2026 ...",
  "markdown": "# Annual Report 2026\n\n## Summary\n\n...",
  "tables": [{"page": 2, "rows": [["Product", "Price"], ["Coffee", "2.50"]]}],
  "processed_at": "2026-11-09T10:00:00Z"
}
```

## Pricing

Pay per event, on the Apify Free plan: $1.00 per 1,000 pages, $5.00 per 1,000 PDFs, $6.00 per 1,000 OCR pages (only pages without text). Tables are free and failed PDFs are not charged. A 100-page digital PDF costs about $0.11. Details on the [Actor page](https://apify.com/t800solutions/pdf-extractor) (Pricing tab).

## Ready-made examples on Apify (no code)

[PDF to Markdown for LLMs](https://apify.com/t800solutions/pdf-extractor/examples/pdf-to-markdown-for-llm) · [Tables to Excel and CSV](https://apify.com/t800solutions/pdf-extractor/examples/extract-tables-from-pdf-to-excel) · [Scanned PDF to text (OCR)](https://apify.com/t800solutions/pdf-extractor/examples/scanned-pdf-to-text-ocr) · [Extract images](https://apify.com/t800solutions/pdf-extractor/examples/extract-images-from-pdf) · [PDF pages to PNG](https://apify.com/t800solutions/pdf-extractor/examples/convert-pdf-pages-to-png-images) · [RAG chunks](https://apify.com/t800solutions/pdf-extractor/examples/pdf-to-rag-chunks) · [Multi-column PDFs](https://apify.com/t800solutions/pdf-extractor/examples/multi-column-pdf-to-text)

<!-- outros-actors:inicio -->
## 🧩 More Actors by T800 Solutions

| Actor | What it does | Examples |
|---|---|---|
| [📍 Google Maps Scraper – Most Accurate Extractor](https://apify.com/t800solutions/google-maps-scraper) | Business names, phones, websites, addresses, ratings and reviews from Google Maps, across whole cities and only inside your area | [google-maps-scraper/](../google-maps-scraper/) |
| [📹 YouTube Scraper All-in-One: Videos & Transcripts](https://apify.com/t800solutions/youtube-scraper) | Videos, Shorts, live streams, channels and playlists from YouTube, with comments and transcripts in one run | [youtube-scraper/](../youtube-scraper/) |

All our Actors: [apify.com/t800solutions](https://apify.com/t800solutions)
<!-- outros-actors:fim -->
