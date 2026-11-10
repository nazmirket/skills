import Image from "next/image";
import Link from "next/link";
import {repo} from "../lib/content";

function Brand({small = false}: {small?: boolean}) {
  const size = small ? 24 : 32;
  return <Link href="/" className="brand" aria-label="Mirket home">
    <Image src="/mirket-logo.png" alt="" width={size} height={size}/>
    <span>MIRKET<span className="accent">.</span>{!small && <small>AGENT SKILLS</small>}</span>
  </Link>;
}

export function SiteHeader() {
  return <header className="site-header">
    <div className="header wrap">
      <Brand/>
      <nav aria-label="Main navigation">
        <Link href="/docs/">Docs</Link><Link href="/#skills">Skills</Link><Link href="/#install">Install</Link>
      </nav>
      <a className="header-link" href={repo}>GitHub <span aria-hidden="true">↗</span></a>
    </div>
  </header>;
}

export function SiteFooter() {
  return <footer className="footer wrap">
    <Brand small/>
    <div className="footer-links">
      <a href={repo}>GitHub ↗</a><Link href="/docs/">Documentation</Link><a href={`${repo}/blob/main/LICENSE`}>MIT License ↗</a>
      <a href="https://x.com/nazmirket" aria-label="X — Nazmi Yılmaz">X<span aria-hidden="true">&nbsp;↗</span></a>
      <a href="https://www.linkedin.com/in/nazmirket/" aria-label="LinkedIn — Nazmi Yılmaz">LinkedIn<span aria-hidden="true">&nbsp;↗</span></a>
    </div>
  </footer>;
}
