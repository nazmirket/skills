import Link from "next/link";

export default function NotFound() {
  return <main className="wrap section prose" id="main-content" tabIndex={-1}>
    <p className="eyebrow">ERROR / 404</p>
    <h1>Page not found</h1>
    <p>Go to the <Link href="/">Mirket homepage</Link> or browse the <Link href="/docs/">documentation</Link>.</p>
  </main>;
}
