// Get a channel's latest videos with their comments using the YouTube Scraper All-in-One on Apify.
// Actor: https://apify.com/t800solutions/youtube-scraper
//
// Usage (Node.js 18+):
//   npm install
//   export APIFY_TOKEN=<your Apify API token>
//   node channel-videos-with-comments.mjs https://www.youtube.com/@Google 10 20

import { writeFile } from 'node:fs/promises';
import { ApifyClient } from 'apify-client';

const [channel = 'https://www.youtube.com/@Google', maxVideos = '10', maxComments = '20'] = process.argv.slice(2);

if (!process.env.APIFY_TOKEN) {
    console.error('Set APIFY_TOKEN first: https://console.apify.com/settings/integrations');
    process.exit(1);
}

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('t800solutions/youtube-scraper').call(
    { start_urls: [channel], max_videos: Number(maxVideos), comments: true, max_comments: Number(maxComments) },
    { maxTotalChargeUsd: 1 }, // the run stops at $1.00
);

if (run.status !== 'SUCCEEDED') {
    console.error(`The run did not succeed (status: ${run.status}).`);
    process.exit(1);
}

const { items } = await client.dataset(run.defaultDatasetId).listItems();
await writeFile('videos-with-comments.json', JSON.stringify(items, null, 2));
console.log(`Saved ${items.length} videos to videos-with-comments.json`);
for (const video of items.slice(0, 5)) {
    console.log(`- ${video.title} | ${video.views} views | ${video.comments_delivered ?? 0} comments delivered`);
}
