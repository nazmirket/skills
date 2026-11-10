import type {Metadata, Viewport} from "next";
import "@fontsource/space-grotesk/400.css";
import "@fontsource/space-grotesk/600.css";
import "@fontsource/space-grotesk/700.css";
import "@fontsource/ibm-plex-mono/400.css";
import "@fontsource/ibm-plex-mono/500.css";
import "@fontsource/press-start-2p/400.css";
import "./globals.css";
import {SiteHeader, SiteFooter} from "../components/SiteChrome";
import {origin, siteName} from "../lib/discovery";

export const metadata: Metadata = {
  metadataBase: new URL(origin),
  title: siteName,
  applicationName: siteName,
  icons: {
    icon: {url: "/mirket-logo.png", type: "image/png"},
    apple: {url: "/apple-touch-icon.png", sizes: "180x180", type: "image/png"},
  },
};

export const viewport: Viewport = {themeColor: "#100c10", colorScheme: "dark"};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body><a className="skip-link" href="#main-content">Skip to content</a><SiteHeader/>{children}<SiteFooter/></body></html>;
}
