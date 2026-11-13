// Get a profile's latest posts with full details using the Instagram Scraper All-in-One on Apify.
// Actor: https://apify.com/t800solutions/instagram-scraper
//
// Usage (Node.js 18+):
//   npm install
//   export APIFY_TOKEN=<your Apify API token>
//   node profile-posts-with-details.mjs nasa 12

import { writeFile } from 'node:fs/promises';
import { ApifyClient } from 'apify-client';

const [profile = 'nasa', maxPosts = '12'] = process.argv.slice(2);

if (!process.env.APIFY_TOKEN) {
    console.error('Set APIFY_TOKEN first: https://console.apify.com/settings/integrations');
    process.exit(1);
}

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('t800solutions/instagram-scraper').call(
    { start_urls: [profile], max_posts_per_profile: Number(maxPosts), post_details: true },
    { maxTotalChargeUsd: 1 }, // the run stops at $1.00
);

if (run.status !== 'SUCCEEDED') {
    console.error(`The run did not succeed (status: ${run.status}).`);
    process.exit(1);
}

const { items } = await client.dataset(run.defaultDatasetId).listItems();
const posts = items.filter((row) => row.kind === 'post');
await writeFile('posts-with-details.json', JSON.stringify(posts, null, 2));
console.log(`Saved ${posts.length} posts to posts-with-details.json`);
for (const post of posts.slice(0, 5)) {
    console.log(`- ${post.url} | ${post.likes_count ?? 'hidden'} likes | ${post.comments_count ?? 0} comments | ${post.timestamp}`);
}
