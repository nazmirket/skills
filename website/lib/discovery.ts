import type {Metadata} from "next";
import {getSkills, readSource, repo} from "./content";

export const origin = "https://skills.mirket.dev";
export const siteName = "Mirket";
export const cardSize = {width: 1200, height: 630};
export const canonicalUrl = (path: string) => new URL(path, origin).href;
const cardVersion = "v1";
const cardFile = (name: string) => `${name}-${cardVersion}.png`;

type PageInfo = {
  path: string;
  title: string;
  description: string;
  image: string;
  cardTitle: string;
  cardLabel: string;
  cardSummary: string;
};

export const homePage: PageInfo = {
  path: "/",
  title: "Mirket: Agent Skills for Codex & Claude Code",
  description: "Mirket is a free, open-source skills plugin for Codex and Claude Code. Install it and browse workflows for planning, debugging, design, and code review.",
  image: cardFile("mirket"),
  cardTitle: "Mirket",
  cardLabel: "OPEN-SOURCE PLUGIN",
  cardSummary: "Agent skills for Codex & Claude Code",
};

export const docsPage: PageInfo = {
  path: "/docs/",
  title: "Mirket Documentation: Install and Use Agent Skills",
  description: "Install Mirket in Codex or Claude Code, learn how the plugin works, and find the right skill for planning, debugging, design, or review.",
  image: cardFile("documentation"),
  cardTitle: "Documentation",
  cardLabel: "FIELD GUIDE",
  cardSummary: "Install Mirket and pick a skill",
};

export const memoryPage: PageInfo = {
  path: "/docs/memory/",
  title: "Local Hindsight Setup for Codex & Claude Code | Mirket",
  description: "Set up optional local Hindsight memory for Mirket in Codex or Claude Code. Learn how to choose a provider, scope capture, and verify recall.",
  image: cardFile("local-hindsight"),
  cardTitle: "Local Hindsight",
  cardLabel: "OPTIONAL MEMORY",
  cardSummary: "Set up local memory for your agent",
};

type Skill = ReturnType<typeof getSkills>[number];

export function skillPageInfo(skill: Skill): PageInfo {
  const summary = skill.summary.replace(/[.;]$/, "");
  return {
    path: `/docs/skills/${skill.slug}/`,
    title: `${skill.name} Skill for Codex & Claude Code | Mirket`,
    description: skill.description.length <= 155
      ? skill.description
      : `${summary} with Mirket ${skill.name}, an open-source skill for Codex and Claude Code.`,
    image: cardFile(`skill-${skill.slug}`),
    cardTitle: skill.name,
    cardLabel: "SKILL REFERENCE",
    cardSummary: summary,
  };
}

export function discoverablePages() {
  return [homePage, docsPage, memoryPage, ...getSkills().map(skillPageInfo)];
}

export function pageMetadata(page: PageInfo): Metadata {
  const url = canonicalUrl(page.path);
  const image = {
    url: canonicalUrl(`/social/${page.image}`),
    type: "image/png",
    ...cardSize,
    alt: `${page.cardTitle} — ${page.cardSummary}. Mirket pixel-art meerkat on a dark crimson background.`,
  };
  return {
    title: page.title,
    description: page.description,
    alternates: {canonical: url},
    robots: {index: true, follow: true, "max-image-preview": "large"},
    openGraph: {
      type: "website",
      locale: "en_US",
      siteName,
      url,
      title: page.title,
      description: page.description,
      images: [{...image, secureUrl: image.url}],
    },
    twitter: {
      card: "summary_large_image",
      title: page.title,
      description: page.description,
      images: [{url: image.url, alt: image.alt}],
    },
  };
}

type Breadcrumb = readonly [name: string, path: string];
export const docsBreadcrumb: Breadcrumb = ["Documentation", docsPage.path];

const siteId = canonicalUrl("/#website");
const projectId = canonicalUrl("/#mirket");
const pageId = (path: string) => canonicalUrl(`${path}#webpage`);
const ref = (id: string) => ({"@id": id});

export function pageGraph(page: PageInfo, breadcrumbs?: readonly Breadcrumb[]) {
  const url = canonicalUrl(page.path);
  const isHome = page === homePage;
  const isDocs = page === docsPage;
  const breadcrumbId = `${url}#breadcrumb`;
  const mainId = isHome ? projectId : isDocs ? `${url}#skill-catalog` : `${url}#guide`;
  const webPage = {
    "@type": isDocs ? "CollectionPage" : "WebPage",
    "@id": pageId(page.path),
    url,
    name: page.title,
    description: page.description,
    inLanguage: "en",
    isPartOf: ref(siteId),
    about: ref(projectId),
    mainEntity: ref(mainId),
    ...(breadcrumbs && {breadcrumb: ref(breadcrumbId)}),
  };

  const mainEntities = isHome ? [
    {
      "@type": "WebSite",
      "@id": siteId,
      name: siteName,
      url,
      inLanguage: "en",
    },
    {
      "@type": "SoftwareSourceCode",
      "@id": projectId,
      name: siteName,
      url,
      description: homePage.description,
      codeRepository: repo,
      license: `${repo}/blob/main/LICENSE`,
      version: JSON.parse(readSource("plugins/mirket/plugin.json")).version,
      runtimePlatform: ["Codex", "Claude Code"],
      isAccessibleForFree: true,
    },
  ] : isDocs ? [
    {
      "@type": "ItemList",
      "@id": mainId,
      name: "Mirket skill catalog",
      itemListElement: getSkills().map((skill, index) => ({
        "@type": "ListItem",
        position: index + 1,
        name: skill.name,
        url: canonicalUrl(skillPageInfo(skill).path),
      })),
    },
  ] : [
    {
      "@type": "TechArticle",
      "@id": mainId,
      headline: page.title,
      description: page.description,
      about: ref(projectId),
      inLanguage: "en",
      mainEntityOfPage: ref(pageId(page.path)),
    },
  ];

  const trail = breadcrumbs ? [{
    "@type": "BreadcrumbList",
    "@id": breadcrumbId,
    itemListElement: breadcrumbs.map(([name, path], index) => ({
      "@type": "ListItem",
      position: index + 1,
      name,
      item: canonicalUrl(path),
    })),
  }] : [];

  return {"@context": "https://schema.org", "@graph": [webPage, ...mainEntities, ...trail]};
}
