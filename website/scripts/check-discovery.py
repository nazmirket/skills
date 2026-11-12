"""Validate discovery and share previews in the deployable static export."""

import json
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
import struct
from urllib.parse import urlsplit
from xml.etree import ElementTree

OUT = Path(__file__).resolve().parents[1] / "out"
ORIGIN = "https://skills.mirket.dev"


class Document(HTMLParser):
    def __init__(self, file):
        super().__init__()
        self.in_head = False
        self.capture = None
        self.meta = defaultdict(list)
        self.canonical = []
        self.titles = []
        self.graphs = []
        self.ids = set()
        self.h1 = 0
        self.source = file.read_text()
        self.feed(self.source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "head":
            self.in_head = True
        if tag == "h1":
            self.h1 += 1
        if self.in_head and tag == "title":
            self.capture = self.titles
        if self.in_head and tag == "link" and attrs.get("rel") == "canonical":
            self.canonical.append(attrs.get("href"))
        if self.in_head and tag == "meta":
            key = attrs.get("property") or attrs.get("name")
            if key:
                self.meta[key].append(attrs.get("content"))
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self.capture = self.graphs

    def handle_endtag(self, tag):
        if tag == "head":
            self.in_head = False
        if tag in ("title", "script"):
            self.capture = None

    def handle_data(self, data):
        if self.capture is not None:
            self.capture.append(data)


def public_url(file):
    path = file.relative_to(OUT).as_posix().removesuffix("index.html")
    return f"{ORIGIN}/{path}"


def only(values):
    assert len(values) == 1 and values[0], values
    return values[0]


def check_page(file):
    page = Document(file)
    url = public_url(file)
    assert page.canonical == [url], page.canonical
    assert page.meta["og:url"] == [url]
    title = only(page.titles)
    description = only(page.meta["description"])
    for prefix in ("og", "twitter"):
        assert page.meta[f"{prefix}:title"] == [title]
        assert page.meta[f"{prefix}:description"] == [description]
        only(page.meta[f"{prefix}:image:alt"])
    assert page.meta["og:type"] == ["website"]
    assert page.meta["og:site_name"] == ["Mirket"]
    assert page.meta["twitter:card"] == ["summary_large_image"]
    assert page.meta["og:image:type"] == ["image/png"]
    assert not any("noindex" in value.lower() for value in page.meta["robots"])
    assert page.h1 == 1 and "main-content" in page.ids

    image = only(page.meta["og:image"])
    assert page.meta["twitter:image"] == [image]
    src = urlsplit(image)
    assert f"{src.scheme}://{src.netloc}" == ORIGIN and src.path.startswith("/social/")
    assert src.path.endswith(".png") and not (src.query or src.fragment)
    card = (OUT / src.path.lstrip("/")).read_bytes()
    assert card[:8] == b"\x89PNG\r\n\x1a\n" and card[12:16] == b"IHDR"
    assert struct.unpack(">II", card[16:24]) == (1200, 630)
    assert page.meta["og:image:width"] == ["1200"] and page.meta["og:image:height"] == ["630"]
    assert len(card) < 1_000_000, "Keep previews lightweight for social crawlers"

    graph = json.loads(only(page.graphs))
    assert graph["@context"] == "https://schema.org"
    nodes = graph["@graph"]
    web_page = next(node for node in nodes if node["@id"] == f"{url}#webpage")
    assert web_page["url"] == url and web_page["name"] == title
    assert web_page["mainEntity"]["@id"] in {node["@id"] for node in nodes}
    if url.startswith(f"{ORIGIN}/docs/skills/"):
        crumbs = next(node for node in nodes if node["@type"] == "BreadcrumbList")["itemListElement"]
        assert [item["position"] for item in crumbs] == list(range(1, len(crumbs) + 1))
        assert crumbs[-1]["item"] == url and len(crumbs) >= 2
    return title, description, image


def main():
    assert (OUT / "index.html").is_file(), "Run npm run build first."
    pages = [file for file in OUT.rglob("index.html") if file.relative_to(OUT).parts[0] not in {"404", "_not-found"}]
    urls = {public_url(file) for file in pages}
    sitemap = ElementTree.parse(OUT / "sitemap.xml").getroot()
    listed = [node.text for node in sitemap.findall(".//{*}loc")]
    assert len(listed) == len(urls) and set(listed) == urls, "Sitemap and export differ"

    cards = set()
    titles = set()
    descriptions = set()
    for file in pages:
        try:
            title, description, card = check_page(file)
            assert title not in titles and description not in descriptions and card not in cards
            titles.add(title)
            descriptions.add(description)
            cards.add(card)
        except (AssertionError, StopIteration, ValueError, OSError) as error:
            raise AssertionError(f"{file.relative_to(OUT)}: {error}") from error

    robots = (OUT / "robots.txt").read_text()
    assert "User-Agent: *" in robots and "Allow: /" in robots
    assert f"Sitemap: {ORIGIN}/sitemap.xml" in robots

    llms = (OUT / "llms.txt").read_text()
    assert llms.startswith("# Mirket\n") and all(f"({url})" in llms for url in urls)

    docs = Document(OUT / "docs/index.html")
    assert {"install-mirket", "install-in-codex", "install-in-claude-code", "common-questions"} <= docs.ids
    assert "codex plugin add mirket@mirket" in docs.source
    assert "claude plugin install mirket@mirket" in docs.source

    for fallback in ("404.html", "404/index.html", "_not-found/index.html"):
        file = OUT / fallback
        if fallback != "404.html" and not file.is_file():
            continue
        not_found = Document(file)
        assert not not_found.canonical and not not_found.meta["og:url"], fallback
        assert any("noindex" in value for value in not_found.meta["robots"]), fallback
    print(f"Verified {len(pages)} indexable HTML pages, {len(cards)} social PNGs, sitemap, robots.txt, llms.txt and 404.")


if __name__ == "__main__":
    main()
