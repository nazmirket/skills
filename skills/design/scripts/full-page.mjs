import { readFile, realpath, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';

function requireNativeDensity(dpr) {
  if (!Number.isFinite(dpr) || dpr < 2) {
    throw new Error('Use a measured native capture density of at least 2.');
  }
}

// Checks geometry. The reviewer still inspects the image for missing content.
export function verifyFullPagePng(png, { width, height, dpr }) {
  requireNativeDensity(dpr);
  if (![width, height].every(Number.isSafeInteger) || width <= 0 || height <= 0) {
    throw new Error('Supply the measured full width and height in CSS pixels.');
  }
  if (png.length < 45 || png.subarray(0, 8).toString('hex') !== '89504e470d0a1a0a'
      || png.toString('ascii', 12, 16) !== 'IHDR' || png.subarray(-8, -4).toString('ascii') !== 'IEND') {
    throw new Error('Expected an original PNG with its header and end marker.');
  }
  const pixels = { width: png.readUInt32BE(16), height: png.readUInt32BE(20) };
  const expectedWidth = width * dpr;
  const expectedHeight = height * dpr;
  if (pixels.width < Math.floor(expectedWidth) || pixels.width > Math.ceil(expectedWidth)
      || pixels.height < Math.floor(expectedHeight) || pixels.height > Math.ceil(expectedHeight)) {
    throw new Error(`Expected full surface ${expectedWidth}×${expectedHeight} px, received ${pixels.width}×${pixels.height} px.`);
  }
  return pixels;
}

function measurePage(page) {
  return page.evaluate(() => {
    const root = document.documentElement;
    const body = document.body;
    return {
      width: Math.max(root.clientWidth, root.scrollWidth, root.offsetWidth, body?.clientWidth ?? 0, body?.scrollWidth ?? 0, body?.offsetWidth ?? 0),
      height: Math.max(root.clientHeight, root.scrollHeight, root.offsetHeight, body?.clientHeight ?? 0, body?.scrollHeight ?? 0, body?.offsetHeight ?? 0),
      dpr: window.devicePixelRatio,
      viewport: { width: window.innerWidth, height: window.innerHeight },
    };
  });
}

// Use the caller's prepared Playwright Page, including its route and UI state.
export async function captureFullPage(page, destination) {
  await page.waitForFunction(() => document.fonts.status === 'loaded', undefined, { timeout: 30_000 });
  const { viewport, ...surface } = await measurePage(page);
  requireNativeDensity(surface.dpr);
  const png = await page.screenshot({ type: 'png', fullPage: true, scale: 'device', caret: 'initial' });
  const after = await measurePage(page);
  if (surface.width !== after.width || surface.height !== after.height || surface.dpr !== after.dpr
      || viewport.width !== after.viewport.width || viewport.height !== after.viewport.height) {
    throw new Error('The document geometry changed during capture. Settle the intended state and retry.');
  }
  const pixels = verifyFullPagePng(png, surface);
  await writeFile(destination, png);
  return { destination, viewport, surface, pixels };
}

// Individual-skill installs can symlink the whole Design folder.
const isEntryPoint = import.meta.main ?? (process.argv[1]
  && await realpath(process.argv[1]).catch(() => undefined) === fileURLToPath(import.meta.url));
if (isEntryPoint) {
  const [file, width, height, dpr] = process.argv.slice(2);
  try {
    if (process.argv.length !== 6) throw new Error('Usage: node full-page.mjs image.png cssWidth cssHeight devicePixelRatio');
    const pixels = verifyFullPagePng(await readFile(file), { width: Number(width), height: Number(height), dpr: Number(dpr) });
    console.log(`Verified full-surface geometry: ${pixels.width}×${pixels.height} px.`);
  } catch (error) {
    console.error(error.message);
    process.exitCode = 1;
  }
}
