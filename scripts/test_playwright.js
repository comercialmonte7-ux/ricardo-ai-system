const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  page.on('console', msg => console.log('PAGE LOG:', msg.text()));
  page.on('pageerror', err => console.log('PAGE ERROR:', err.message));
  await page.goto('file:///Users/ricardomarimodinger/.gemini/antigravity/scratch/ricardo-ai-system/index.html', { waitUntil: 'networkidle' });
  await browser.close();
})();
