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
SKILLS = REPO / "skills"
EXPECTED_SKILLS = {
    "adapt", "architect", "audit", "author", "brief", "clean", "code",
    "debug", "deploy", "design", "equip", "execute",
    "market", "migrate", "plan", "preflight",
    "refactor", "search", "ship", "test",
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
    for directory in (SKILLS, REPO / "references", REPO / "docs", REPO / "instructions", REPO / "tests"):
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
        self.assertFalse((REPO / "plugin.json").exists())
        codex = read_json(REPO / ".codex-plugin/plugin.json")
        self.assertEqual(codex["skills"], "./skills/")
        self.assertTrue(exact_path_exists(REPO / codex["skills"]))
        self.assertEqual((REPO / codex["skills"]).resolve(), SKILLS)
        self.assertEqual(codex["hooks"], "./hooks/hooks.json")
        self.assertNotIn("extensions", codex)
        self.assertTrue(codex["interface"]["displayName"].strip())
        self.assertTrue(codex["interface"]["shortDescription"].strip())
        self.assertLessEqual(len(codex["interface"]["shortDescription"]), 30)

    def test_both_marketplaces_use_the_root_catalog_and_hooks(self):
        codex = read_json(REPO / ".codex-plugin/plugin.json")
        claude = read_json(REPO / ".claude-plugin/plugin.json")
        # Claude Code discovers the default skills/ and hooks/hooks.json at its plugin root.
        self.assertNotIn("skills", claude)
        self.assertNotIn("hooks", claude)
        self.assertFalse(SKILLS.is_symlink())
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
                self.assertEqual(source, "./")
                self.assertEqual((REPO / source).resolve(), REPO)

        codex_hooks = REPO / codex["hooks"]
        self.assertTrue(exact_path_exists(codex_hooks))
        self.assertEqual(codex_hooks.resolve(), REPO / "hooks/hooks.json")
        for groups in read_json(codex_hooks)["hooks"].values():
            for group in groups:
                for hook in group["hooks"]:
                    script = shlex.split(hook["command"])[-1]
                    prefix = "${CLAUDE_PLUGIN_ROOT}/"
                    with self.subTest(script=script):
                        self.assertTrue(script.startswith(prefix))
                        self.assertTrue(exact_path_exists(REPO / script[len(prefix):]))
        for key in ("logo", "composerIcon"):
            self.assertTrue(exact_path_exists(REPO / codex["interface"][key]))

    def test_global_guidance_agrees(self):
        self.assertEqual((REPO / "instructions/AGENTS.md").read_bytes(), (REPO / "instructions/CLAUDE.md").read_bytes())

    def test_global_plugin_reference_paths_resolve(self):
        references = set()
        for path in (REPO / "instructions/AGENTS.md", REPO / "instructions/CLAUDE.md"):
            references.update(re.findall(r"`((?:skills/[a-z][a-z0-9-]*/)?references/[^`]+\.md)`", path.read_text(encoding="utf-8")))
        self.assertTrue(references, "No plugin reference paths found in global guidance")
        for reference in references:
            with self.subTest(reference=reference):
                self.assertTrue(exact_path_exists(REPO / reference))

    def test_catalog_matches_skill_metadata_routing_and_documentation(self):
        catalog = {p.name for p in SKILLS.iterdir() if p.is_dir() and not p.name.startswith(".")}
        self.assertEqual(catalog, EXPECTED_SKILLS)
        routing = SKILLS / "execute/references/Routing.md"
        # A cross-reference to a supporting skill does not give it an owner row.
        owner_links = re.findall(
            r"^\| [^|\n]+ \| \[[^\]]+\]\(([^\s)#]+/SKILL\.md)(?:#[^)]*)?\)",
            routing.read_text(encoding="utf-8"), re.MULTILINE,
        )
        owners = {(routing.parent / link).resolve() for link in owner_links}
        self.assertEqual(owners, {SKILLS / name / "SKILL.md" for name in catalog})
        guide = (REPO / "docs/README.md").read_text(encoding="utf-8")
        self.assertEqual(set(re.findall(r"\.\./skills/([^/]+)/SKILL\.md", guide)), catalog)
        display_names = set()
        for name in sorted(catalog):
            with self.subTest(skill=name):
                skill = SKILLS / name
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

    def test_skill_references_stay_inside_the_portable_catalog(self):
        for path in SKILLS.rglob("*.md"):
            prose = "\n".join(prose_lines(path.read_text(encoding="utf-8")))
            boundary = SKILLS / "design" if path.relative_to(SKILLS).parts[0] == "design" else SKILLS
            with self.subTest(source=path.relative_to(SKILLS)):
                self.assertNotRegex(prose, r"(?i)https?://")
            for url in re.findall(r"\]\(([^\s)]+)\)", prose):
                target = urlsplit(url)
                with self.subTest(source=path.relative_to(SKILLS), target=url):
                    self.assertFalse(target.scheme or target.netloc, "Skill references must be local")
                    if target.path:
                        destination = (path.parent / unquote(target.path)).resolve()
                        self.assertIn(boundary, destination.parents)


if __name__ == "__main__":
    unittest.main()
