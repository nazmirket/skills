"""Validate distribution contracts without claiming live host behavior."""

import html
import json
import os
from pathlib import Path
import re
import shlex
import tempfile
import unicodedata
import unittest
from urllib.parse import unquote, urlsplit

REPO = Path(__file__).resolve().parents[1]
PLUGIN = REPO / "plugins/mirket"
EXPECTED_SKILLS = {
    "adapt", "architect", "audit", "author", "brief", "clean", "critique",
    "curate", "debug", "deploy", "design", "distill", "equip", "focus",
    "imagine", "migrate", "operate", "orchestrate", "plan", "preflight",
    "refactor", "release", "secure", "sleep", "test",
}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def exact_path_exists(path):
    """Check spelling on case-insensitive filesystems too; do not resolve it away."""
    path = Path(os.path.abspath(path))
    current = Path(path.anchor)
    for part in path.parts[1:]:
        if not current.is_dir() or part not in {entry.name for entry in current.iterdir()}:
            return False
        current /= part
    return current.exists()


def prose_lines(markdown):
    """Exclude fenced examples from Markdown headings and links."""
    fence = None
    for line in markdown.splitlines():
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", line)
        if marker:
            run, suffix = marker.groups()
            if fence is None:
                fence = run
                continue
            if run[0] == fence[0] and len(run) >= len(fence) and not suffix.strip():
                fence = None
                continue
        if fence is None:
            yield line


def heading_anchors(markdown):
    """GitHub-style anchors for this repository's ATX/setext Markdown headings."""
    anchors = set()
    previous = ""
    for line in prose_lines(markdown):
        anchors.update(re.findall(r'<(?:a|h[1-6])\b[^>]*\b(?:id|name)=["\']([^"\']+)["\']', line))
        match = re.match(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            title = match.group(1)
        elif previous.strip() and re.fullmatch(r" {0,3}(?:=+|-+)\s*", line):
            title = previous.strip()
        else:
            previous = line
            continue
        title = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", title)
        title = html.unescape(re.sub(r"<[^>]*>", "", title)).lower()
        slug = "".join(c for c in title if c in "_- " or unicodedata.category(c)[0] in "LNM").replace(" ", "-")
        anchor, suffix = slug, 0
        while anchor in anchors:
            suffix += 1
            anchor = f"{slug}-{suffix}"
        anchors.add(anchor)
        previous = ""
    return anchors


def markdown_sources():
    paths = set(REPO.glob("*.md"))
    for directory in (PLUGIN, REPO / "docs", REPO / "instructions", REPO / "tests"):
        paths.update(directory.rglob("*.md"))
    paths.update(REPO / name for name in ("website/README.md", "website/AGENTS.md"))
    return sorted(paths)


class MarkdownValidationTest(unittest.TestCase):
    def test_exact_case_is_checked_even_on_case_insensitive_filesystems(self):
        with tempfile.TemporaryDirectory() as root:
            path = Path(root) / "Routing.md"
            path.write_text("# Routes\n", encoding="utf-8")
            self.assertTrue(exact_path_exists(path))
            self.assertFalse(exact_path_exists(path.with_name("routing.md")))
            self.assertFalse(exact_path_exists(path.with_name("Missing.md")))

    def test_anchors_cover_formatting_duplicates_and_ignore_fenced_examples(self):
        text = """# A **useful** `heading`!
## A useful heading
## A useful heading-1
## [Linked title](Target.md)
Setext title
------------
```md
# Not a heading
```
<a id="explicit-anchor"></a>
"""
        self.assertEqual(heading_anchors(text), {
            "a-useful-heading", "a-useful-heading-1", "a-useful-heading-1-1",
            "linked-title", "setext-title", "explicit-anchor",
        })


class PackageWiringTest(unittest.TestCase):
    def test_compatibility_manifest_is_not_shadowed_by_a_portable_manifest(self):
        # Codex 0.167.0 discovers skills but drops hooks when root plugin.json wins.
        # Reconsider this contract only with actual host discovery/execution evidence.
        self.assertFalse((PLUGIN / "plugin.json").exists())
        codex = read_json(PLUGIN / ".codex-plugin/plugin.json")
        self.assertEqual(codex["skills"], "./skills/")
        self.assertTrue(exact_path_exists(PLUGIN / codex["skills"]))
        self.assertEqual((PLUGIN / codex["skills"]).resolve(), PLUGIN / "skills")
        self.assertEqual(codex["hooks"], "./hooks/hooks.json")
        self.assertNotIn("extensions", codex)
        self.assertTrue(codex["interface"]["displayName"].strip())
        self.assertTrue(codex["interface"]["shortDescription"].strip())
        self.assertLessEqual(len(codex["interface"]["shortDescription"]), 30)

    def test_both_marketplaces_resolve_to_the_package_and_its_hooks(self):
        codex = read_json(PLUGIN / ".codex-plugin/plugin.json")
        claude = read_json(PLUGIN / ".claude-plugin/plugin.json")
        for key in ("name", "version", "license", "description"):
            self.assertEqual(codex[key], claude[key], key)
        self.assertRegex(codex["version"], r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$")
        for path in (".agents/plugins/marketplace.json", ".claude-plugin/marketplace.json"):
            with self.subTest(path=path):
                entries = [p for p in read_json(REPO / path)["plugins"] if p["name"] == codex["name"]]
                self.assertEqual(len(entries), 1)
                source = entries[0]["source"]
                if isinstance(source, dict):
                    source = source["path"]
                self.assertTrue(exact_path_exists(REPO / source))
                self.assertEqual((REPO / source).resolve(), PLUGIN)

        codex_hooks = PLUGIN / codex["hooks"]
        self.assertTrue(exact_path_exists(codex_hooks))
        self.assertEqual(codex_hooks.resolve(), (PLUGIN / "hooks/hooks.json").resolve())
        for groups in read_json(codex_hooks)["hooks"].values():
            for group in groups:
                for hook in group["hooks"]:
                    script = shlex.split(hook["command"])[-1]
                    prefix = "${CLAUDE_PLUGIN_ROOT}/"
                    with self.subTest(script=script):
                        self.assertTrue(script.startswith(prefix))
                        self.assertTrue(exact_path_exists(PLUGIN / script[len(prefix):]))
        for key in ("logo", "composerIcon"):
            self.assertTrue(exact_path_exists(PLUGIN / codex["interface"][key]))

    def test_global_guidance_and_license_copies_agree(self):
        self.assertEqual((REPO / "instructions/AGENTS.md").read_bytes(), (REPO / "instructions/CLAUDE.md").read_bytes())
        self.assertEqual((REPO / "LICENSE").read_bytes(), (PLUGIN / "LICENSE").read_bytes())

    def test_global_plugin_reference_paths_resolve(self):
        references = set()
        for path in (REPO / "instructions/AGENTS.md", REPO / "instructions/CLAUDE.md"):
            references.update(re.findall(r"`(references/[^`]+\.md)`", path.read_text(encoding="utf-8")))
        for reference in references:
            with self.subTest(reference=reference):
                self.assertTrue(exact_path_exists(PLUGIN / reference))

    def test_catalog_matches_skill_metadata_routing_and_documentation(self):
        catalog = {p.name for p in (PLUGIN / "skills").iterdir() if p.is_dir() and not p.name.startswith(".")}
        self.assertEqual(catalog, EXPECTED_SKILLS)
        routing = (PLUGIN / "references/Routing.md").read_text(encoding="utf-8")
        self.assertEqual(set(re.findall(r"\.\./skills/([^/]+)/SKILL\.md", routing)), catalog)
        guide = (REPO / "docs/README.md").read_text(encoding="utf-8")
        self.assertEqual(set(re.findall(r"\.\./plugins/mirket/skills/([^/]+)/SKILL\.md", guide)), catalog)
        display_names = set()
        for name in sorted(catalog):
            with self.subTest(skill=name):
                skill = PLUGIN / "skills" / name
                frontmatter = skill.joinpath("SKILL.md").read_text(encoding="utf-8").split("---", 2)[1]
                self.assertRegex(frontmatter, rf"(?m)^name: {re.escape(name)}$")
                self.assertRegex(frontmatter, r'(?m)^description: "[^"\n]+"$')
                metadata = skill.joinpath("agents/openai.yaml").read_text(encoding="utf-8")
                # Metadata uses the project's small, quoted interface mapping.
                self.assertRegex(metadata, r"(?m)^interface:$")
                for key in ("display_name", "short_description"):
                    match = re.search(rf'^  {key}: ("[^"\n]+")$', metadata, re.MULTILINE)
                    self.assertIsNotNone(match, f"Missing quoted {key}")
                    value = json.loads(match.group(1))
                    self.assertTrue(value.strip())
                    if key == "display_name":
                        self.assertNotIn(value, display_names)
                        display_names.add(value)

    def test_local_markdown_links_have_exact_paths_and_valid_anchors(self):
        for path in markdown_sources():
            markdown = "\n".join(prose_lines(path.read_text(encoding="utf-8")))
            for url in re.findall(r"\]\(([^\s)]+)\)", markdown):
                target = urlsplit(url)
                if target.scheme or target.netloc:
                    continue
                destination = path.parent / unquote(target.path) if target.path else path
                with self.subTest(source=path.relative_to(REPO), target=url):
                    self.assertTrue(exact_path_exists(destination), f"Missing or incorrectly cased path: {destination}")
                    if target.fragment and destination.suffix.lower() == ".md":
                        self.assertIn(unquote(target.fragment), heading_anchors(destination.read_text(encoding="utf-8")))


if __name__ == "__main__":
    unittest.main()
