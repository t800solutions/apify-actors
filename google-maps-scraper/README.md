# Google Maps Scraper examples (Python, JavaScript, cURL)

Examples for **[📍 Google Maps Scraper – Most Accurate Extractor](https://apify.com/t800solutions/google-maps-scraper)** on Apify: scrape Google Maps places for lead generation and local market research, with business names, phones, websites, addresses, ratings, reviews and coordinates. The Actor searches whole cities neighborhood by neighborhood, beyond the 60-result limit of Google's official Places API, and keeps only the places inside your area.

## Examples

| Example | What it does |
|---|---|
| [python/scrape_places_to_csv.py](python/scrape_places_to_csv.py) | Any search term and location to a CSV file you can open in Excel or Google Sheets |
| [python/businesses_without_website.py](python/businesses_without_website.py) | Local businesses that have no website: a lead list for web designers and marketing agencies |
| [javascript/scrape-places.mjs](javascript/scrape-places.mjs) | The same search from Node.js, saved to `places.json` |
| [curl/run-sync.sh](curl/run-sync.sh) | One HTTP call that runs the Actor and returns the places (runs of up to 5 minutes) |

## How to run

```bash
export APIFY_TOKEN=<your Apify API token>   # https://console.apify.com/settings/integrations

cd python
pip install -r requirements.txt
python scrape_places_to_csv.py "dentist" "Austin, TX, USA" --max 50
python businesses_without_website.py "personal trainer" "Florianópolis, SC, Brasil" --max 20 --language pt-BR
```

The location can be a city (`Austin, TX, USA`), a whole state (`Texas, USA`), several states (`Texas; Oklahoma, USA`) or a country (`Italy`). Every example caps the charge per run (default $1.00).

## Input

| Field | Example | Meaning |
|---|---|---|
| `search_terms` | `["dentist"]` | Up to 10 terms |
| `location` | `"Austin, TX, USA"` | City, state, several states or country |
| `max_places_per_search` | `50` | Maximum places per search term |
| `language` | `"en"` | Language of the results (30 languages) |
| `website_filter` | `"without_website"` | Add-on filter: `with_website` or `without_website` |

The full list of fields is on the [Actor page](https://apify.com/t800solutions/google-maps-scraper) (Input tab).

## Output (one row per place, shortened)

```json
{
  "name": "Example Dental Studio",
  "phone": "(512) 555-0100",
  "website": "https://www.example.com/",
  "address": "100 Example Ave Suite 200, Austin, TX 78701",
  "city": "Austin",
  "state": "Texas",
  "country_code": "US",
  "category": "Dentist",
  "rating": 4.8,
  "reviews_count": 312,
  "latitude": 30.2672,
  "longitude": -97.7431,
  "url": "https://www.google.com/maps/place/..."
}
```

## Pricing

Pay per event: $3.20 per 1,000 places on the Apify Free plan, less on paid plans. Places outside your area or not matching your filters are not charged. Details on the [Actor page](https://apify.com/t800solutions/google-maps-scraper) (Pricing tab).

## Ready-made examples on Apify (no code)

[Restaurants in New York City](https://apify.com/t800solutions/google-maps-scraper/examples/restaurants-in-new-york-city) · [Dentists in London](https://apify.com/t800solutions/google-maps-scraper/examples/dentists-in-london) · [Real estate agencies in Miami](https://apify.com/t800solutions/google-maps-scraper/examples/real-estate-agencies-in-miami) · [Plumbers in Los Angeles](https://apify.com/t800solutions/google-maps-scraper/examples/plumbers-in-los-angeles) · [Hotels in Paris](https://apify.com/t800solutions/google-maps-scraper/examples/hotels-in-paris) · [Coffee shops in São Paulo](https://apify.com/t800solutions/google-maps-scraper/examples/coffee-shops-in-sao-paulo) · [Businesses without a website](https://apify.com/t800solutions/google-maps-scraper/examples/businesses-without-website) · [Gyms in Texas](https://apify.com/t800solutions/google-maps-scraper/examples/gyms-in-texas)

<!-- outros-actors:inicio -->
## 🧩 More Actors by T800 Solutions

| Actor | What it does | Examples |
|---|---|---|
| [📄 PDF Extractor All-in-One: Text, Tables & OCR](https://apify.com/t800solutions/pdf-extractor) | PDF to text, Markdown, tables, OCR for scanned PDFs in 20 languages, RAG chunks and images | [pdf-extractor/](../pdf-extractor/) |
| [📹 YouTube Scraper All-in-One: Videos & Transcripts](https://apify.com/t800solutions/youtube-scraper) | Videos, Shorts, live streams, channels and playlists from YouTube, with comments and transcripts in one run | [youtube-scraper/](../youtube-scraper/) |

All our Actors: [apify.com/t800solutions](https://apify.com/t800solutions)
<!-- outros-actors:fim -->
