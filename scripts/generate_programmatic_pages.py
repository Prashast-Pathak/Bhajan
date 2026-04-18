#!/usr/bin/env python3
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT / "programmatic"


def load(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def safe(v):
    return html.escape(str(v or ""))


def write_page(path: Path, title: str, desc: str, heading: str, body_html: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    page = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>{safe(title)}</title>
  <meta name=\"description\" content=\"{safe(desc)}\" />
  <meta name=\"robots\" content=\"index,follow\" />
  <style>
    body {{ font-family: Georgia, serif; max-width: 860px; margin: 40px auto; line-height: 1.7; padding: 0 16px; color: #1f1b2d; }}
    a {{ color: #3d2d88; }}
    h1 {{ font-size: 2rem; margin-bottom: 12px; }}
    .meta {{ color: #5b5672; font-size: .95rem; margin-bottom: 18px; }}
    .card {{ border: 1px solid #e6e3f1; border-radius: 12px; padding: 16px; background: #faf9ff; }}
  </style>
</head>
<body>
  <h1>{safe(heading)}</h1>
  <div class=\"meta\">Programmatic spiritual reference page</div>
  <div class=\"card\">{body_html}</div>
  <p><a href=\"/index.html\">Back to Home</a></p>
</body>
</html>
"""
    path.write_text(page, encoding="utf-8")


def create_bhajans():
    rows = load(DATA / "bhajans.json")
    for row in rows:
        slug = str(row.get("slug", "")).strip()
        if not slug:
            continue
        title = row.get("title_hindi") or row.get("title_english") or slug
        deity = row.get("deity", "")
        desc = f"{title} lyrics, meaning, story and devotional context."
        body = (
            f"<p><strong>Deity:</strong> {safe(deity)}</p>"
            f"<p><strong>Significance:</strong> {safe(row.get('significance') or row.get('significance_hindi') or '')}</p>"
            f"<p><a href=\"/bhajan.html?slug={safe(slug)}\">Open full bhajan page</a></p>"
        )
        write_page(OUT / "bhajans" / f"{slug}.html", f"{title} | Bhajan", desc, str(title), body)


def create_shlokas():
    rows = load(DATA / "shlokas.json")
    for row in rows:
        slug = str(row.get("slug", "")).strip()
        if not slug:
            continue
        title = row.get("title_hindi") or row.get("title_english") or slug
        body = (
            f"<p><strong>Source:</strong> {safe(row.get('source_ref') or row.get('source') or '')}</p>"
            f"<p><strong>Sanskrit:</strong> {safe(row.get('sanskrit') or '')}</p>"
            f"<p><a href=\"/shlokas.html?slug={safe(slug)}\">Open full shloka page</a></p>"
        )
        write_page(OUT / "shlokas" / f"{slug}.html", f"{title} | Shloka", f"{title} shloka meaning and source", str(title), body)


def create_prayers():
    rows = load(DATA / "prayers.json").get("prayers", [])
    for row in rows:
        slug = str(row.get("slug", "")).strip()
        if not slug:
            continue
        title = row.get("title_hindi") or row.get("title_english") or slug
        body = (
            f"<p><strong>Occasion:</strong> {safe(row.get('occasion') or '')}</p>"
            f"<p><strong>Duration:</strong> {safe(row.get('duration_minutes') or '')} minutes</p>"
            f"<p><a href=\"/prayers.html?slug={safe(slug)}\">Open full prayer sequence</a></p>"
        )
        write_page(OUT / "prayers" / f"{slug}.html", f"{title} | Prayer", f"{title} prayer steps and benefits", str(title), body)


def create_upanishads():
    rows = load(DATA / "upanishads.json")
    for row in rows:
        slug = str(row.get("slug", "")).strip()
        if not slug:
            continue
        title = row.get("name_hindi") or row.get("name_english") or slug
        body = (
            f"<p><strong>Veda:</strong> {safe(row.get('veda') or '')}</p>"
            f"<p><strong>Theme:</strong> {safe(row.get('theme_english') or row.get('theme_hindi') or '')}</p>"
            f"<p><a href=\"/upanishads.html?slug={safe(slug)}\">Open full upanishad page</a></p>"
        )
        write_page(OUT / "upanishads" / f"{slug}.html", f"{title} | Upanishad", f"{title} teachings and verse insights", str(title), body)


def create_wisdom():
    rows = load(DATA / "wisdom.json").get("topics", [])
    for row in rows:
        slug = str(row.get("slug", "")).strip()
        if not slug:
            continue
        title = row.get("title_hindi") or row.get("title_english") or slug
        body = (
            f"<p><strong>Topic Intro:</strong> {safe(row.get('intro_english') or row.get('intro_hindi') or '')}</p>"
            f"<p><a href=\"/wisdom.html?topic={safe(slug)}\">Open full wisdom topic</a></p>"
        )
        write_page(OUT / "wisdom" / f"{slug}.html", f"{title} | Wisdom", f"{title} spiritual guidance and practical application", str(title), body)


def create_gita():
    chapters = load(DATA / "gita.json").get("chapters", [])
    for chapter in chapters:
        c = chapter.get("chapter")
        for verse in chapter.get("verses", []):
            v = verse.get("verse")
            slug = str(verse.get("slug") or f"gita-{c}-{v}")
            title = f"Bhagavad Gita {c}.{v}"
            body = (
                f"<p><strong>Sanskrit:</strong> {safe(verse.get('sanskrit') or '')}</p>"
                f"<p><strong>Meaning:</strong> {safe(verse.get('english_translation') or verse.get('hindi_translation') or '')}</p>"
                f"<p><a href=\"/bhagavad-gita.html?chapter={safe(c)}&verse={safe(v)}\">Open full Gita verse page</a></p>"
            )
            write_page(OUT / "gita" / f"{slug}.html", f"{title} meaning", f"{title} meaning and commentary", title, body)


def main():
    if OUT.exists():
        # remove stale html files but keep directory
        for p in OUT.rglob("*.html"):
            p.unlink()
    create_bhajans()
    create_shlokas()
    create_prayers()
    create_upanishads()
    create_wisdom()
    create_gita()
    count = len(list(OUT.rglob("*.html")))
    print(f"Generated {count} programmatic pages in {OUT}")


if __name__ == "__main__":
    main()
