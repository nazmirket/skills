const assert = require('node:assert/strict');
const { mkdtemp, readFile, rm } = require('node:fs/promises');
const { tmpdir } = require('node:os');
const { join } = require('node:path');
const test = require('node:test');
const { chromium } = require('playwright');

test('capture covers the document at native density', async t => {
  const { captureFullPage, verifyFullPagePng } = await import('../skills/design/scripts/full-page.mjs');
  const folder = await mkdtemp(join(tmpdir(), 'mirket-design-'));
  t.after(() => rm(folder, { recursive: true, force: true }));
  const browser = await chromium.launch();
  t.after(() => browser.close());
  const viewport = { width: 391, height: 713 };
  const page = await browser.newPage({ viewport, deviceScaleFactor: 2 });
  const report = '<!doctype html><style>body{margin:0;width:500px}main{height:1800px}footer{height:30px}</style><main>Report</main><footer>End</footer>';
  await page.setContent(report);
  const full = await captureFullPage(page, join(folder, 'report.png'));
  assert.deepEqual(full.surface, { width: 500, height: 1830, dpr: 2 });
  assert.deepEqual(full.pixels, { width: 1000, height: 3660 });
  assert.deepEqual(verifyFullPagePng(await readFile(full.destination), full.surface), full.pixels);
  const viewportOnly = await page.screenshot({ scale: 'device' });
  assert.throws(() => verifyFullPagePng(viewportOnly, full.surface), /Expected full surface/);

  // In quirks mode the body's client dimensions supply the viewport extent.
  await page.setContent('<style>html,body{margin:0;width:38px;height:38px;overflow:hidden}</style>End');
  assert.equal(await page.evaluate(() => document.compatMode), 'BackCompat');
  const compact = await captureFullPage(page, join(folder, 'compact.png'));
  assert.deepEqual(compact.pixels, { width: 782, height: 1426 });

  const low = await browser.newPage({ viewport, deviceScaleFactor: 1 });
  await low.setContent(report);
  const rejected = join(folder, 'rejected.png');
  await assert.rejects(captureFullPage(low, rejected), /at least 2/);
  await assert.rejects(readFile(rejected), { code: 'ENOENT' });
});
