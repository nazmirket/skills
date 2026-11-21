# Playwright

Use the project's installed runner, browser configuration and fixtures when repeatable interaction, comparison or diagnostics will change a design decision. A capable [direct browser](Browser.md) can perform the same one-off check. The [screenshot standard](Screenshot.md) applies to both.

## Prepare the page

- Use the existing preview or start the project's own server on a free local address. Wait for its actual route to be ready, record the build, and stop only processes you started. A connected socket proves less than the expected application state.
- Create an isolated context per case. Set viewport, device scale, locale, timezone, color scheme, motion and input mode to what the case requires. Use the same fixture, route, clock and settings for before/after. Reuse approved session state where needed and keep it out of shared evidence.
- Find the task through visible roles, accessible names and labels. Scope an ambiguous locator to a named region, row or dialog. Use a deliberate test id for a surface without a stable semantic locator. Let actionability and retrying assertions wait for observable state. Use a labeled completion message, expected count, decoded image or disappearing skeleton rather than a fixed delay or an idle-network heuristic.
- Drive important transitions through real inputs. For a dialog, press the key that opens it, verify initial focus, exercise Tab and Escape, and verify focus return. For a form, submit invalid data, correct one field and inspect the remaining errors and values. When waiting on a response, popup or download, arm the wait before the triggering action and then verify the user-visible outcome.

## Capture a review state

The [capture helper](../../scripts/full-page.mjs) takes an already prepared Playwright Page. It preserves the state, requests a lossless full-document capture at device scale, checks geometry on both sides of capture and rejects a low-density or cropped result. It imports only Node built-ins. Resolve the helper from the Design folder and use the runner already installed in the project.

```js
import { chromium } from 'playwright';
import { join } from 'node:path';
import { pathToFileURL } from 'node:url';

const helper = join(process.env.DESIGN_DIR, 'scripts', 'full-page.mjs');
const { captureFullPage } = await import(pathToFileURL(helper).href);
const browser = await chromium.launch();
try {
  const context = await browser.newContext({
    viewport: { width: 1280, height: 800 }, deviceScaleFactor: 2,
  });
  context.setDefaultTimeout(15_000);
  const page = await context.newPage();
  await page.goto(process.env.PREVIEW_URL, { waitUntil: 'domcontentloaded' });
  // This report has a deferred chart, lazy images and a final totals row.
  const chart = page.getByRole('region', { name: 'Monthly activity' });
  await chart.scrollIntoViewIfNeeded();
  await chart.getByRole('table', { name: 'Recorded totals' }).waitFor();
  for (const img of await page.locator('main img[loading="lazy"]').all()) {
    if (await img.isVisible()) {
      await img.scrollIntoViewIfNeeded();
      await img.evaluate(element => element.decode(), undefined, { timeout: 10_000 });
    }
  }
  const end = page.getByRole('contentinfo');
  await end.scrollIntoViewIfNeeded();
  await end.getByText('End of report', { exact: true }).waitFor();
  await page.evaluate(() => window.scrollTo({ top: 0, behavior: 'instant' }));
  console.log(await captureFullPage(page, 'desktop-full.png'));
} finally {
  await browser.close();
}
```

Replace the example's chart and footer with this fixture's deferred sections and final meaningful content. Visit each one at the intended viewport and verify its loaded state. A footer can render while a chart halfway down still shows a skeleton. For the narrow version use a new context at the real narrow CSS width with native high density. Reopen both PNGs and inspect them using the [full-surface checks](Screenshot.md#verify-the-file). Overlays, nested scrollers, dynamic feeds and asset placeholders still require visual inspection.

## Diagnose an unexpected result

Record the first failed action or assertion, expected and observed state, and the fixture and environment needed to replay it. Inspect the locator's accessible name, focus, bounding box, computed style or intercepting element as relevant. A console error, HTTP error response and failed network request are different observations. In the affected run, correlate page errors, response statuses or request failures with the action before assigning cause. Keep authorized traces and screenshots from that run, with secrets and session data out of handoffs. A retry can reveal instability. Preserve the first failure. Report exactly which browser engines, breakpoints, input modes and states you exercised.
