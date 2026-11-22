# Playwright Test

Read the project's runner command, configured browsers, base URL and server startup. Pin the build or dev server being tested. Exercise one journey through its real entry point.

Use roles, accessible names, labels or agreed test IDs. Scope repeated controls to the relevant row or region. After the action, use a retrying locator assertion for the observable result. For a popup or download, register the event wait before triggering it, then check the destination or file. Wait for the state the user needs instead of a fixed delay or global network idle.

For an account page that provides a named address dialog, this case checks dismissal and keyboard focus together. It uses the project's configured base URL.

```js
import { test, expect } from '@playwright/test';

test('dismissing the address editor returns focus', async ({ page }) => {
  await page.goto('/account');
  const edit = page.getByRole('button', { name: 'Edit address' });
  const dialog = page.getByRole('dialog', { name: 'Delivery address' });
  await edit.click();
  await expect(dialog).toBeVisible();
  await page.keyboard.press('Escape');
  await expect(dialog).toBeHidden();
  await expect(edit).toBeFocused();
});
```

- **Isolation.** Use the runner's fresh browser context. A shared read-only fixture can serve several tests. Isolate backend records when tests write or depend on mutable state. Reuse authenticated state only while its role and expiry fit. Use separate identities for conflicting writes and keep session files private. Use the real service for the integration under test. Stub an outside dependency for a deliberately controlled case and say what the stub covers.
- **Failures.** Run the matching case and project first, then the required browser matrix. Retain a trace on failure or collect one on the first retry. Inspect the failing action, DOM state, relevant console error and network response. Identify which attempt produced the evidence, report a recovered retry as flaky and sanitize artifacts before sharing.
- **Performance.** Time fixture setup separately from the journey. Check backend capacity and fixture isolation before adjusting worker count or sharding.

Report the build, browser project, case, data, real or stubbed services and observed result. For **every visual check**, follow [Design's full-resolution screenshot requirements](../../design/references/tools/Screenshot.md). Its [Playwright guide](../../design/references/tools/Playwright.md) covers browser capture.
