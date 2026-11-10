import type { Metadata } from "next";
import "@fontsource/space-grotesk/400.css";
import "@fontsource/space-grotesk/600.css";
import "@fontsource/space-grotesk/700.css";
import "@fontsource/ibm-plex-mono/400.css";
import "@fontsource/ibm-plex-mono/500.css";
import "@fontsource/press-start-2p/400.css";
import "./globals.css";
import {SiteHeader, SiteFooter} from "../components/SiteChrome";

export const metadata: Metadata = {
  title: "Mirket — good work, on repeat",
  icons: { icon: "/mirket-logo.png" },
  description: "A practical collection of agent skills for thoughtful work with Codex and Claude Code.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body><a className="skip-link" href="#main-content">Skip to content</a><SiteHeader/>{children}<SiteFooter/></body></html>;
}
