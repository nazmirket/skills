import type {MetadataRoute} from "next";
import {canonicalUrl, discoverablePages} from "../lib/discovery";

export const dynamic = "force-static";

export default function sitemap(): MetadataRoute.Sitemap {
  return discoverablePages().map(({path}) => ({url: canonicalUrl(path)}));
}
