// Convert PDFs to LLM-ready Markdown with the PDF Extractor All-in-One on Apify (one .md file per PDF).
// Actor: https://apify.com/t800solutions/pdf-extractor
//
// Usage (Node.js 18+):
//   npm install
//   export APIFY_TOKEN=<your Apify API token>
//   node pdf-to-markdown.mjs https://www.irs.gov/pub/irs-pdf/fw9.pdf

import { mkdir, writeFile } from 'node:fs/promises';
import { ApifyClient } from 'apify-client';

const urls = process.argv.slice(2);
if (urls.length === 0) urls.push('https://www.irs.gov/pub/irs-pdf/fw9.pdf');

if (!process.env.APIFY_TOKEN) {
    console.error('Set APIFY_TOKEN first: https://console.apify.com/settings/integrations');
    process.exit(1);
}

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('t800solutions/pdf-extractor').call(
    { urls, output_format: 'document', include_markdown: true },
    { maxTotalChargeUsd: 1 }, // the run stops at $1.00
);

if (run.status !== 'SUCCEEDED') {
    console.error(`The run did not succeed (status: ${run.status}).`);
    process.exit(1);
}

await mkdir('markdown', { recursive: true });
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const [index, row] of items.entries()) {
    if (row.status === 'failed') {
        console.log(`- ${row.source}: failed (${row.error_code}), not charged`);
        continue;
    }
    const name = (row.source.split('/').pop() || 'document').replace(/\.pdf$/i, '').replace(/[^A-Za-z0-9_-]+/g, '-');
    const path = `markdown/${String(index + 1).padStart(2, '0')}-${name}.md`;
    await writeFile(path, row.markdown ?? row.text ?? '');
    console.log(`- ${row.source}: ${row.extracted_page_count} pages -> ${path}`);
}
