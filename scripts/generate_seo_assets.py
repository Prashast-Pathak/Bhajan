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
    static_paths = [
        "/",
        "/index.html",
        "/bhajans.html",
        "/bhagavad-gita.html",
        "/shlokas.html",
        "/prayers.html",
        "/upanishads.html",
        "/wisdom.html",
        "/about.html",
        "/privacy-policy.html",
        "/contact.html",
        "/terms.html",
        "/disclaimer.html",
    ]
    urls = [to_url(base, p) for p in static_paths] + gita_chapter_urls(base) + bhajan_urls(base) + remedy_urls(base)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for url in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{url}</loc>")
        lines.append(f"    <lastmod>{now}</lastmod>")
        lines.append("    <changefreq>weekly</changefreq>")
        lines.append("    <priority>0.8</priority>")
        lines.append("  </url>")
    lines.append("</urlset>")
    (ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_robots(base: str):
    content = f"""User-agent: *
Allow: /

# Standard crawl controls
Disallow: /templates/

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
