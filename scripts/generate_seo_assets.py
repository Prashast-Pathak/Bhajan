#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
CONFIG = ROOT / "config" / "site.config.json"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def norm_base(url: str) -> str:
    return url.rstrip("/")


def to_url(base: str, path: str) -> str:
    if path.startswith("http://") or path.startswith("https://"):
        return path
    return f"{base}{path if path.startswith('/') else '/' + path}"


def gita_chapter_urls(base: str):
    """Generate clean /gita/N/ URLs for all 18 chapters."""
    return [to_url(base, f"/gita/{c}/") for c in range(1, 19)]


def bhajan_urls(base: str):
    """Generate clean /bhajan/slug/ URLs from bhajans.json."""
    urls = []
    bhajans_file = DATA / "bhajans.json"
    if not bhajans_file.exists():
        return []
    bhajans = load_json(bhajans_file)
    for row in bhajans:
        slug = str(row.get("slug", "")).strip()
        if slug:
            urls.append(to_url(base, f"/bhajan/{slug}/"))
    return urls

def remedy_urls(base: str):
    remedy_root = ROOT / "remedy"
    if not remedy_root.exists():
        return []
    urls = []
    for file in remedy_root.rglob("*.html"):
        # For folders like remedy/sasa-yoga/index.html, output /remedy/sasa-yoga/
        rel = "/" + str(file.relative_to(ROOT)).replace("\\", "/")
        if rel.endswith("/index.html"):
            rel = rel[:-10]
        urls.append(to_url(base, rel))
    return sorted(set(urls))


def write_sitemap(base: str):
    dist = ROOT / "dist"
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    seen = set()
    urls = []

    def add(path: str, priority: str = "0.7", freq: str = "monthly"):
        # Normalize: strip trailing slash for dedup key, keep slash in URL
        key = path.rstrip("/") or "/"
        if key not in seen:
            seen.add(key)
            urls.append((to_url(base, path), priority, freq))

    def classify(rel: str):
        """Return (priority, freq) based on the URL path."""
        if rel in ("/", ""):
            return "1.0", "daily"
        if any(rel.startswith(p) for p in ("/gita/", "/bhajan/", "/nakshatra/")):
            return "0.9", "weekly"
        return "0.7", "monthly"

    def scan_dir(root_dir: Path, base_dir: Path):
        """Walk root_dir and add every page as a clean URL."""
        if not root_dir.exists():
            return
        for html in sorted(root_dir.rglob("*.html")):
            rel = "/" + str(html.relative_to(base_dir)).replace("\\", "/")
            # /foo/bar/index.html → /foo/bar/
            if rel.endswith("/index.html"):
                rel = rel[: -len("index.html")]
            # skip raw .html files in dist root (handled separately)
            pri, freq = classify(rel)
            add(rel, pri, freq)

    # Junk folders to skip inside dist/
    SKIP_DIRS = {
        "node_modules", "templates", "backend", "scratch",
        "ai-index", "programmatic", "data", ".venv", "favicon_io", "docs",
    }

    def scan_dist(root_dir: Path):
        if not root_dir.exists():
            return
        for html in sorted(root_dir.rglob("*.html")):
            # Skip any path that contains a junk directory
            parts = set(html.relative_to(root_dir).parts)
            if parts & SKIP_DIRS:
                continue
            rel = "/" + str(html.relative_to(root_dir)).replace("\\", "/")
            if rel.endswith("/index.html"):
                rel = rel[: -len("index.html")]
            pri, freq = classify(rel)
            add(rel, pri, freq)

    # ── 1. Scan dist/ — the built SSR pages (skip junk) ──────────────────────
    scan_dist(dist)

    # ── 2. Scan root-level content folders (nakshatra, planet, rashi, etc.) ───
    #    These exist as separate directories at the project root on the server
    root_content_dirs = [
        "nakshatra", "planet", "rashi", "remedy", "muhurat",
        "bhajan", "gita", "prayer", "shloka", "upanishad",
        "wisdom", "tithi",
    ]
    for dirname in root_content_dirs:
        folder = ROOT / dirname
        scan_dir(folder, ROOT)

    # ── 3. Static .html files at root ─────────────────────────────────────────
    static_roots = [
        "/bhajans.html", "/bhagavad-gita.html", "/shlokas.html",
        "/prayers.html", "/upanishads.html", "/wisdom.html",
        "/about.html", "/privacy-policy.html", "/contact.html",
        "/terms.html", "/disclaimer.html", "/methodology.html",
        "/favorites.html", "/bhajan.html",
    ]
    for p in static_roots:
        add(p, "0.6", "monthly")

    # ── 4. Write XML ───────────────────────────────────────────────────────────
    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url, priority, freq in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{url}</loc>")
        lines.append(f"    <lastmod>{now}</lastmod>")
        lines.append(f"    <changefreq>{freq}</changefreq>")
        lines.append(f"    <priority>{priority}</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    out = ROOT / "sitemap.xml"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"  ✓ sitemap.xml — {len(urls)} URLs")


def write_robots(base: str):
    content = f"""User-agent: *
Allow: /

# Block dev artifacts and junk
Disallow: /templates/
Disallow: /node_modules/
Disallow: /backend/
Disallow: /scratch/
Disallow: /ai-index/
Disallow: /programmatic/
Disallow: /data/
Disallow: /.venv/

Sitemap: {base}/sitemap.xml
"""
    (ROOT / "robots.txt").write_text(content, encoding="utf-8")


def write_llms(base: str):
    content = f"""# llms.txt
Site: Sanatan Gyan Sagar
Base URL: {base}
Primary language: Hindi, Sanskrit, English
Purpose: Spiritual and educational reference content only.

Key sections:
- {base}/bhajans.html
- {base}/bhagavad-gita.html
- {base}/shlokas.html
- {base}/prayers.html
- {base}/upanishads.html
- {base}/wisdom.html

Policy notes:
- No medical, legal, or financial guarantees.
- Content is devotional and educational.
- Refer to {base}/disclaimer.html and {base}/privacy-policy.html
"""
    (ROOT / "llms.txt").write_text(content, encoding="utf-8")


def write_ai_txt(base: str):
    content = f"""# ai.txt
site={base}
allow_crawl=true
allow_train=true
content_license=all-rights-reserved
attribution_required=true
contact={load_json(CONFIG).get('legal_email','support@example.com')}
policy={base}/disclaimer.html
privacy={base}/privacy-policy.html
"""
    (ROOT / "ai.txt").write_text(content, encoding="utf-8")


def main():
    cfg = load_json(CONFIG)
    base = norm_base(cfg["base_url"])
    write_sitemap(base)
    write_robots(base)
    write_llms(base)
    write_ai_txt(base)
    print("Generated sitemap.xml, robots.txt, llms.txt, ai.txt")


if __name__ == "__main__":
    main()
