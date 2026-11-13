# Instagram Scraper examples: profiles, posts and comments (Python, JavaScript, cURL)

Examples for **[📸 Instagram Scraper All-in-One: Posts & Comments](https://apify.com/t800solutions/instagram-scraper)** on Apify: paste profile links or usernames, post or reel links and hashtags, and get public profiles (followers, bio, links, latest posts), posts and reels with full details (likes, comment count, date, location, music, media URLs) and the comments of each post, all in one run and without login. No Instagram account, no API key, no cookies.

## Examples

| Example | What it does |
|---|---|
| [python/profiles_to_csv.py](python/profiles_to_csv.py) | A list of profiles to a CSV file (followers, following, bio, links, verified) you can open in Excel or Google Sheets |
| [python/post_comments.py](python/post_comments.py) | The comments of one or more posts, one JSON file each |
| [javascript/profile-posts-with-details.mjs](javascript/profile-posts-with-details.mjs) | A profile's latest posts with full details (likes, date, location, music), from Node.js |
| [curl/run-sync.sh](curl/run-sync.sh) | One HTTP call that runs the Actor and returns the rows (runs of up to 5 minutes) |

## How to run

```bash
export APIFY_TOKEN=<your Apify API token>   # https://console.apify.com/settings/integrations

cd python
pip install -r requirements.txt
python profiles_to_csv.py nasa natgeo nike --out profiles.csv
python post_comments.py https://www.instagram.com/reel/Dfc1mYxFevS/
```

Every example caps the charge per run (default $1.00).

## Input

| Field | Example | Meaning |
|---|---|---|
| `start_urls` | `["https://www.instagram.com/nasa/", "#travel"]` | Profiles (link or username), post or reel links, hashtags (up to 1,000) |
| `max_posts_per_profile` | `12` | Latest posts delivered with each profile (12 always, up to 24 when Instagram allows; 0 = details only) |
| `max_posts_per_hashtag` | `12` | Recent posts of each hashtag (up to 12 without login) |
| `post_details` | `true` | Open each post for likes, comment count, date, location, music, tagged users and media URLs |
| `comments`, `max_comments_per_post` | `true`, `50` | Add-on: the comments Instagram shows on the public post page (about 11 per post) |
| `only_newer_than` | `"2026-01-01"` | Only posts from that date on (included) |
| `proxy_country` | `"US"` | Two-letter country of the proxy |

The full list of fields is on the [Actor page](https://apify.com/t800solutions/instagram-scraper) (Input tab).

## Output (one row per profile, post or hashtag, shortened)

```json
{
  "kind": "profile",
  "username": "nasa",
  "full_name": "NASA",
  "followers_count": 104337717,
  "following_count": 91,
  "verified": true,
  "biography": "Making the seemingly impossible, possible.",
  "external_urls": ["https://www.nasa.gov/"],
  "posts_delivered": 12,
  "posts": [{"shortcode": "Dfc1mYxFevS", "type": "reel", "caption": "Apply to become an astronaut! ...", "display_url": "https://..."}]
}
```

## Pricing

Pay per event, on the Apify Free plan: $2.35 per 1,000 profiles (with the 12 posts of the profile page), $2.40 per 1,000 posts with full details, $1.50 per 1,000 list-only posts (hashtags and extra profile posts), $2.35 per 1,000 comments. Date filter and proxy country are included; private profiles, removed posts and failed links are not charged. Details on the [Actor page](https://apify.com/t800solutions/instagram-scraper) (Pricing tab).

<!-- outros-actors:inicio -->
## 🧩 More Actors by T800 Solutions

| Actor | What it does | Examples |
|---|---|---|
| [📍 Google Maps Scraper – Most Accurate Extractor](https://apify.com/t800solutions/google-maps-scraper) | Business names, phones, websites, addresses, ratings and reviews from Google Maps, across whole cities and only inside your area | [google-maps-scraper/](../google-maps-scraper/) |
| [📄 PDF Extractor All-in-One: Text, Tables & OCR](https://apify.com/t800solutions/pdf-extractor) | PDF to text, Markdown, tables, OCR for scanned PDFs in 20 languages, RAG chunks and images | [pdf-extractor/](../pdf-extractor/) |
| [📹 YouTube Scraper All-in-One: Videos & Transcripts](https://apify.com/t800solutions/youtube-scraper) | Videos, Shorts, live streams, channels and playlists from YouTube, with comments and transcripts in one run | [youtube-scraper/](../youtube-scraper/) |

All our Actors: [apify.com/t800solutions](https://apify.com/t800solutions)
<!-- outros-actors:fim -->
