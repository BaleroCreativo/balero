// Uso: node flyers/render.mjs mega-europa [ancho] [alto]  -> flyers/<nombre>.png
// Ej.: node flyers/render.mjs mega-europa-1x1 1080 1080
import { chromium } from 'playwright';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const name = process.argv[2] ?? 'mega-europa';
const width = Number(process.argv[3] ?? 1080);
const height = Number(process.argv[4] ?? 1350);
const dir = path.dirname(fileURLToPath(import.meta.url));
const browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium' });
const page = await browser.newPage({ viewport: { width, height } });
await page.goto('file://' + path.join(dir, `${name}.html`));
await page.waitForLoadState('networkidle');
await page.screenshot({ path: path.join(dir, `${name}.png`) });
await browser.close();
console.log('ok', name, width, height);
