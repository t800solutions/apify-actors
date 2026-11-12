# YouTube Scraper examples: videos, comments and transcripts (Python, JavaScript, cURL)

Examples for **[📹 YouTube Scraper All-in-One: Videos & Transcripts](https://apify.com/t800solutions/youtube-scraper)** on Apify: search YouTube with every filter or paste channel, playlist and video links, and get videos, Shorts and live streams with full details (views, likes, publish date, description, keywords, category and the channel's numbers), plus the comments and the transcript of each video, all in one run. No YouTube API key, no quota.

## Examples

| Example | What it does |
|---|---|
| [python/search_videos_to_csv.py](python/search_videos_to_csv.py) | A YouTube search to a CSV file you can open in Excel or Google Sheets (`--list` for the cheaper mode) |
| [python/channel_transcripts.py](python/channel_transcripts.py) | The transcripts of a channel's latest videos, one file each (text, timestamped, SRT, VTT or JSON) |
| [javascript/channel-videos-with-comments.mjs](javascript/channel-videos-with-comments.mjs) | A channel's latest videos with their comments, from Node.js |
| [curl/run-sync.sh](curl/run-sync.sh) | One HTTP call that runs the Actor and returns the videos (runs of up to 5 minutes) |

## How to run

```bash
export APIFY_TOKEN=<your Apify API token>   # https://console.apify.com/settings/integrations

cd python
pip install -r requirements.txt
python search_videos_to_csv.py "web scraping tutorial" --max 50
python channel_transcripts.py https://www.youtube.com/@Google --max 20 --languages en pt
```

Every example caps the charge per run (default $1.00).

## Input

| Field | Example | Meaning |
|---|---|---|
| `search_terms` | `["web scraping tutorial"]` | Up to 20 search terms |
| `start_urls` | `["https://www.youtube.com/@Google"]` | Videos, channels, playlists, Shorts or search pages (up to 1,000) |
| `max_videos`, `max_shorts`, `max_live_streams` | `50`, `10`, `0` | Limits per search or link |
| `details` | `"full"` | `full` (likes, description, exact date, channel numbers) or `list` (cheaper) |
| `only_newer_than` | `"30 days"` | Only videos after a date, for channels and playlists (included) |
| `comments`, `max_comments`, `comment_replies` | `true`, `50`, `true` | Add-on: comments per video, with replies |
| `transcript`, `transcript_languages`, `transcript_format` | `true`, `["en", "pt"]`, `"srt"` | Add-on: YouTube captions in your language order and format |

The full list of fields is on the [Actor page](https://apify.com/t800solutions/youtube-scraper) (Input tab).

## Output (one row per video, shortened)

```json
{
  "id": "hHQlcnubuFI",
  "title": "Learn Web Scraping in 5 Minutes",
  "url": "https://www.youtube.com/watch?v=hHQlcnubuFI",
  "views": 188988,
  "likes": 5321,
  "comments_count": 210,
  "published": "2026-03-17",
  "duration_seconds": 293,
  "category": "Education",
  "channel_name": "CodeHead",
  "channel_subscribers": 120000,
  "comments_delivered": 50,
  "comments": [{"text": "Great tutorial!", "author": "@someone", "likes": 12, "reply_to": null}],
  "transcript": "[00:00:00] Hi, in this video ...",
  "transcript_minutes": 4.9
}
```

## Pricing

Pay per event, on the Apify Free plan: $3.20 per 1,000 videos with full details, $1.00 per 1,000 list-only videos, $1.20 per 1,000 comments, $1.20 per 1,000 started hours of transcribed video (a video up to 60 minutes counts 1). Date filter, search filters and channel data are included; unavailable videos and videos without captions are not charged. Details on the [Actor page](https://apify.com/t800solutions/youtube-scraper) (Pricing tab).

<!-- outros-actors:inicio -->
## 🧩 More Actors by T800 Solutions

| Actor | What it does | Examples |
|---|---|---|
| [📍 Google Maps Scraper – Most Accurate Extractor](https://apify.com/t800solutions/google-maps-scraper) | Business names, phones, websites, addresses, ratings and reviews from Google Maps, across whole cities and only inside your area | [google-maps-scraper/](../google-maps-scraper/) |
| [📄 PDF Extractor All-in-One: Text, Tables & OCR](https://apify.com/t800solutions/pdf-extractor) | PDF to text, Markdown, tables, OCR for scanned PDFs in 20 languages, RAG chunks and images | [pdf-extractor/](../pdf-extractor/) |

All our Actors: [apify.com/t800solutions](https://apify.com/t800solutions)
<!-- outros-actors:fim -->
