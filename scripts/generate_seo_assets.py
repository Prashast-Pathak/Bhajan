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


def dynamic_urls(base: str):
    urls = []

    bhajans = load_json(DATA / "bhajans.json")
    for row in bhajans:
        slug = str(row.get("slug", "")).strip()
        if slug:
            urls.append(f"/bhajan.html?slug={slug}")

    shlokas = load_json(DATA / "shlokas.json")
    for row in shlokas:
        slug = str(row.get("slug", "")).strip()
        if slug:
            urls.append(f"/shlokas.html?slug={slug}")

    prayers = load_json(DATA / "prayers.json").get("prayers", [])
    for row in prayers:
        slug = str(row.get("slug", "")).strip()
        if slug:
            urls.append(f"/prayers.html?slug={slug}")

    upanishads = load_json(DATA / "upanishads.json")
    for row in upanishads:
        slug = str(row.get("slug", "")).strip()
        if slug:
            urls.append(f"/upanishads.html?slug={slug}")

    wisdom_topics = load_json(DATA / "wisdom.json").get("topics", [])
    for row in wisdom_topics:
        slug = str(row.get("slug", "")).strip()
        if slug:
            urls.append(f"/wisdom.html?topic={slug}")

    gita_chapters = load_json(DATA / "gita.json").get("chapters", [])
    for chapter in gita_chapters:
        c = chapter.get("chapter")
        for verse in chapter.get("verses", []):
            v = verse.get("verse")
            if c is not None and v is not None:
                urls.append(f"/bhagavad-gita.html?chapter={c}&verse={v}")

    # Dedupe while preserving order
    seen = set()
    ordered = []
    for u in urls:
        if u not in seen:
            seen.add(u)
            ordered.append(u)
    return [to_url(base, u) for u in ordered]

def programmatic_urls(base: str):
    prog_root = ROOT / "programmatic"
    if not prog_root.exists():
        return []
    urls = []
    for file in prog_root.rglob("*.html"):
        rel = "/" + str(file.relative_to(ROOT)).replace("\\", "/")
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
    urls = [to_url(base, p) for p in static_paths] + dynamic_urls(base)
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
