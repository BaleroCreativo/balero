// Uso: node flyers/render.mjs mega-europa  -> flyers/mega-europa.png
import { chromium } from 'playwright';
import { fileURLToPath } from 'node:url';
import path from 'node:path';

const name = process.argv[2] ?? 'mega-europa';
const dir = path.dirname(fileURLToPath(import.meta.url));
const browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium' });
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
await page.goto('file://' + path.join(dir, `${name}.html`));
await page.waitForLoadState('networkidle');
await page.screenshot({ path: path.join(dir, `${name}.png`) });
await browser.close();
console.log('ok', name);
