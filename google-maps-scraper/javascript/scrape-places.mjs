// Scrape Google Maps places with the Google Maps Scraper on Apify and save them to places.json.
// Actor: https://apify.com/t800solutions/google-maps-scraper
//
// Usage (Node.js 18+):
//   npm install
//   export APIFY_TOKEN=<your Apify API token>
//   node scrape-places.mjs "restaurant" "Miami, FL, USA" 50

import { writeFile } from 'node:fs/promises';
import { ApifyClient } from 'apify-client';

const [searchTerm = 'restaurant', location = 'Miami, FL, USA', max = '50'] = process.argv.slice(2);

if (!process.env.APIFY_TOKEN) {
    console.error('Set APIFY_TOKEN first: https://console.apify.com/settings/integrations');
    process.exit(1);
}

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('t800solutions/google-maps-scraper').call(
    { search_terms: [searchTerm], location, max_places_per_search: Number(max), language: 'en' },
    { maxTotalChargeUsd: 1 }, // the run stops at $1.00
);

if (run.status !== 'SUCCEEDED') {
    console.error(`The run did not succeed (status: ${run.status}).`);
    process.exit(1);
}

const { items } = await client.dataset(run.defaultDatasetId).listItems();
await writeFile('places.json', JSON.stringify(items, null, 2));
console.log(`Saved ${items.length} places to places.json`);
for (const place of items.slice(0, 5)) {
    console.log(`- ${place.name} | ${place.phone ?? 'no phone'} | ${place.website ?? 'no website'} | ${place.rating ?? '-'}★`);
}
