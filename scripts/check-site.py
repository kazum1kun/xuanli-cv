"""Check generated HTML links, original page URLs, metadata, and search coverage.

Run after `npm run build`: python scripts/check-site.py [output-directory]
Uses only the Python standard library and makes no network requests.
"""

from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urljoin, urlsplit


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else ROOT / "public"
ORIGIN = "https://xlin.io"
PUBLICATIONS = (
    "globecom-24-entanglement", "globecom-24-pricing", "icccn-22",
    "infocom-23", "iotdi-23", "jsac-22", "mass-23", "master-thesis",
    "milcom-24-mvat", "milcom-24-offloading", "modprod-21",
)
TALKS = (
    "iot-system-vulnerability-analysis-and-network-hardening-with-shortest-attack-trace-in-a-weighted-attack-graph",
    "most-vulnerable-attack-trace-in-a-probabilistic-attack-graph",
    "network-hardening-in-iot-networks-with-weighted-attack-graphs",
)
LEGACY_PAGES = [f"/publication/{slug}/" for slug in PUBLICATIONS]
LEGACY_PAGES += [f"/talk/{slug}/" for slug in TALKS]
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input",
             "link", "meta", "param", "source", "track", "wbr"}


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.links = []
        self.ids = set()
        self.canonical = None
        self.meta = {}
        self.schemas = []
        self.stack = []
        self.search_text = []
        self.json_buffer = None
        self.feed(text)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.ids.add(attrs["name"])
        for key in ("href", "src", "poster", "data-filename"):
            value = attrs.get(key)
            if value and not value.startswith(("data:", "javascript:")):
                self.links.append((key, value))
        if attrs.get("srcset") and not attrs["srcset"].startswith("data:"):
            for candidate in attrs["srcset"].split(","):
                self.links.append(("srcset", candidate.strip().split()[0]))
        if tag == "link" and "canonical" in attrs.get("rel", "").split():
            self.canonical = attrs.get("href")
        if tag == "meta":
            self.meta[attrs.get("name", attrs.get("property", ""))] = attrs.get("content", "")
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self.json_buffer = []
        if tag not in VOID_TAGS:
            indexed = "data-pagefind-body" in attrs or any(item[1] for item in self.stack)
            ignored = tag in {"script", "style"} or "data-pagefind-ignore" in attrs
            ignored = ignored or any(item[2] for item in self.stack)
            self.stack.append((tag, indexed, ignored))

    def handle_endtag(self, tag):
        if tag == "script" and self.json_buffer is not None:
            self.schemas.append(json.loads("".join(self.json_buffer)))
            self.json_buffer = None
        for position in range(len(self.stack) - 1, -1, -1):
            if self.stack[position][0] == tag:
                del self.stack[position:]
                break

    def handle_data(self, text):
        if self.json_buffer is not None:
            self.json_buffer.append(text)
        if self.stack and self.stack[-1][1] and not self.stack[-1][2]:
            self.search_text.append(text)


def route_for(path):
    relative = path.relative_to(OUTPUT).as_posix()
    return "/" + (relative[:-10] if relative.endswith("index.html") else relative)


def file_for(route):
    target = OUTPUT / unquote(route).lstrip("/")
    if target.is_dir() or route.endswith("/"):
        target /= "index.html"
    return target


def main():
    failures = []
    documents = {}
    for path in OUTPUT.rglob("*.html"):
        if "pagefind" in path.relative_to(OUTPUT).parts:
            continue
        try:
            documents[path] = Document(path.read_text(encoding="utf-8"))
        except (ValueError, OSError) as error:
            failures.append(f"{path.relative_to(OUTPUT)}: malformed HTML metadata: {error}")

    checked_links = 0
    for path, document in documents.items():
        route = route_for(path)
        for kind, value in document.links:
            target_url = urlsplit(urljoin(ORIGIN + route, value))
            if target_url.netloc != "xlin.io" or target_url.scheme not in {"http", "https"}:
                continue
            target = file_for(target_url.path)
            checked_links += 1
            if not target.is_file():
                failures.append(f"{route}: broken {kind} {value}")
            elif target_url.fragment and target in documents:
                fragment = unquote(target_url.fragment)
                if fragment not in documents[target].ids:
                    failures.append(f"{route}: missing fragment {value}")

    for route in LEGACY_PAGES:
        document = documents.get(file_for(route))
        if document is None:
            failures.append(f"Original route missing: {route}")
            continue
        if document.canonical != ORIGIN + route:
            failures.append(f"{route}: missing production canonical")
        if not document.meta.get("description"):
            failures.append(f"{route}: missing description")
        expected_type = "Event" if route.startswith("/talk/") else "Article"
        if not any(schema.get("@type") == expected_type for schema in document.schemas):
            failures.append(f"{route}: missing {expected_type} structured data")
        words = set(re.findall(r"\w+", " ".join(document.search_text).lower()))
        if len(words) < 40:
            failures.append(f"{route}: only {len(words)} searchable words; abstract may be excluded")

    # Check rendered attribution against every source record, including new papers.
    profiles = {}
    hidden_profiles = set()
    for path in (ROOT / "data" / "authors").glob("*.yaml"):
        source = path.read_text(encoding="utf-8")
        display = re.search(r"^  display: (.+)$", source, re.MULTILINE)
        if display:
            profiles[path.stem] = display.group(1).strip("\"'")
        if "is_owner: true" in source:
            continue
        route = f"/authors/{path.stem}/"
        document = documents.get(file_for(route))
        author_page = ROOT / "content" / "authors" / path.stem / "_index.md"
        if author_page.is_file() and re.search(r"^profile: false$", author_page.read_text(encoding="utf-8"), re.MULTILINE):
            hidden_profiles.add(path.stem)
            if document is not None:
                failures.append(f"Hidden author profile still rendered: {route}")
            continue
        if document is None:
            failures.append(f"Author profile missing: {route}")
            continue
        if not any(kind == "src" and f"/{path.stem}_" in value
                   for kind, value in document.links):
            failures.append(f"{route}: author portrait missing")
        if profiles.get(path.stem, "") not in " ".join(document.search_text):
            failures.append(f"{route}: author biography is not searchable")
        if not document.meta.get("description", "").startswith(profiles.get(path.stem, "")):
            failures.append(f"{route}: missing biography description")

    publication_count = 0
    for source_path in (ROOT / "content" / "publication").glob("*/index.md"):
        publication_count += 1
        source = source_path.read_text(encoding="utf-8")
        match = re.search(r"^authors:\n((?:- .+\n)+)", source, re.MULTILINE)
        raw_authors = [line[2:] for line in match.group(1).splitlines()] if match else []
        expected_names = [profiles.get(author, author) for author in raw_authors]
        route = f"/publication/{source_path.parent.name}/"
        document = documents.get(file_for(route))
        if document is None:
            failures.append(f"Publication missing: {route}")
            continue
        article = next((schema for schema in document.schemas
                        if schema.get("@type") == "Article"), {})
        authors = article.get("author", [])
        if isinstance(authors, dict):
            authors = [authors]
        if [author.get("name") for author in authors] != expected_names:
            failures.append(f"{route}: structured author names/order differ from source")
        hrefs = {urlsplit(value).path for kind, value in document.links if kind == "href"}
        for author in raw_authors:
            if author in profiles and author != "xuanli" and author not in hidden_profiles and f"/authors/{author}/" not in hrefs:
                failures.append(f"{route}: missing profile link for {author}")
            if author in hidden_profiles:
                person = next((person for person in authors if person.get("name") == profiles[author]), {})
                if person.get("url"):
                    failures.append(f"{route}: hidden author has a structured profile URL: {author}")
        if "abstract" not in document.ids:
            failures.append(f"{route}: full abstract missing")
        if "Abstract source:" in source or "Abstract source:" in " ".join(document.search_text):
            failures.append(f"{route}: abstract-source line remains")

    for path, document in documents.items():
        for author in hidden_profiles:
            for kind, value in document.links:
                if f"/authors/{author}/" in value or (kind in {"src", "srcset"} and f"/{author}_" in value):
                    failures.append(f"{route_for(path)}: hidden author profile or portrait still linked: {author}")

    if not (OUTPUT / "pagefind" / "pagefind.js").is_file():
        failures.append("Pagefind index missing; run npm run build before checking")
    if failures:
        print("Site checks failed:")
        for failure in sorted(set(failures)):
            print(f"- {failure}")
        return 1
    print(f"Checked {len(documents)} HTML pages and {checked_links} internal references; "
          f"all {len(LEGACY_PAGES)} original content routes, metadata, and abstract search coverage pass. "
          f"Verified attribution on {publication_count} publications, {len(profiles) - len(hidden_profiles) - 1} visible coauthor profiles, "
          f"and {len(hidden_profiles)} hidden profiles.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
