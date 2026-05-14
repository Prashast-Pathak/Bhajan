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
  <link rel=\"manifest\" href=\"/manifest.json\">
  <script>
    if ('serviceWorker' in navigator) {{
      window.addEventListener('load', () => {{
        navigator.serviceWorker.register('/sw.js').then(reg => {{
          console.log('[SW] Registered: ', reg.scope);
        }}).catch(err => {{
          console.log('[SW] Registration failed: ', err);
        }});
      }});
    }}
  </script>
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


def get_gita_cta(chapter):
    ctas = {
        1: {'title': 'Overcome Anxiety & Confusion', 'text': 'Arjuna faced paralyzing doubt. Are difficult planetary transits clouding your path? Check if you are undergoing Sade Sati or Kaal Sarp Dosha.', 'btn': 'Check Doshas & Transits', 'url': 'https://ournakshatra.com/'},
        2: {'title': 'Find Your True Purpose', 'text': 'Lord Krishna reveals the eternal soul. What is your soul meant to achieve in this life? Discover your life purpose in your free Vedic Birth Chart.', 'btn': 'Get Free Birth Chart', 'url': 'https://ournakshatra.com/janam_landing.html'},
        3: {'title': 'Karma & Career Paths', 'text': 'Action (Karma) is unavoidable. What kind of work brings you fulfillment and prosperity? See your Dasha timeline and Career Yogas.', 'btn': 'Check Career Yogas', 'url': 'https://ournakshatra.com/janam_landing.html'},
        4: {'title': 'Wisdom & Inner Light', 'text': 'Transcendental knowledge dispels ignorance. Which planet brings you wisdom and spiritual growth? Find your Ishta Devata in your Kundali.', 'btn': 'Find Ishta Devata', 'url': 'https://ournakshatra.com/janam_landing.html'},
        5: {'title': 'Renunciation & Balance', 'text': 'True renunciation is performing duty without attachment. Seek balance in your life by analyzing your planetary alignments.', 'btn': 'View Free Kundali', 'url': 'https://ournakshatra.com/janam_landing.html'},
        6: {'title': 'Meditation & Focus', 'text': 'Control the restless mind through practice. Discover which planetary mantras can bring you deepest meditation and peace.', 'btn': 'Discover Remedies', 'url': 'https://bhajan.ournakshatra.com/remedy/'},
        7: {'title': 'Knowledge of the Absolute', 'text': 'The divine energy permeates everything. Connect with the cosmos by understanding your Nakshatra and Rashi.', 'btn': 'Find Your Nakshatra', 'url': 'https://ournakshatra.com/janam_landing.html'},
        8: {'title': 'The Eternal Journey', 'text': "The soul's journey spans lifetimes. What karmic debts (Doshas) have you carried over into this life?", 'btn': 'Check Birth Doshas', 'url': 'https://ournakshatra.com/janam_landing.html'},
        9: {'title': 'The Sovereign Science', 'text': 'Bhakti (Devotion) is the highest path. Deepen your devotion by worshipping the deity corresponding to your Atmakaraka.', 'btn': 'Find Ruling Deity', 'url': 'https://ournakshatra.com/janam_landing.html'},
        10: {'title': 'Divine Opulence', 'text': 'God is the source of all majesty. Is there a Dhana Yoga (Wealth Yoga) hidden in your birth chart?', 'btn': 'Check Wealth Yogas', 'url': 'https://ournakshatra.com/janam_landing.html'},
        11: {'title': 'The Universal Form', 'text': 'The cosmic vision reveals the terrifying and magnificent power of time. See how time (Dasha) will unfold in your life.', 'btn': 'Check Dasha Timeline', 'url': 'https://ournakshatra.com/janam_landing.html'},
        12: {'title': 'The Path of Devotion', 'text': 'Unwavering devotion leads to the divine. Strengthen your Bhakti by aligning with your cosmic planetary guides.', 'btn': 'Find Your Planets', 'url': 'https://ournakshatra.com/janam_landing.html'},
        13: {'title': 'Nature, the Enjoyer & Consciousness', 'text': 'Understand the field (body) and the knower (soul). How do the planets interact with your physical and mental well-being?', 'btn': 'Check Health Indicators', 'url': 'https://ournakshatra.com/janam_landing.html'},
        14: {'title': 'The Three Modes of Material Nature', 'text': 'Are you driven by Sattva, Rajas, or Tamas? Discover your inherent nature and Nakshatra traits.', 'btn': 'Read Nakshatra Traits', 'url': 'https://ournakshatra.com/janam_landing.html'},
        15: {'title': 'The Supreme Divine Personality', 'text': 'Cut the banyan tree of attachment with detachment. Find the spiritual remedies meant specifically for your chart.', 'btn': 'View Free Kundali', 'url': 'https://ournakshatra.com/janam_landing.html'},
        16: {'title': 'Divine & Demoniac Natures', 'text': 'Cultivate divine qualities to escape suffering. Are afflicted planets causing inner turmoil? Check for remedies.', 'btn': 'Find Planetary Remedies', 'url': 'https://bhajan.ournakshatra.com/remedy/'},
        17: {'title': 'The Divisions of Faith', 'text': 'Faith determines our destination. Align your faith with the cosmic rhythms by following your auspicious times (Muhurat).', 'btn': 'Check Auspicious Muhurats', 'url': 'https://ournakshatra.com/'},
        18: {'title': 'Liberation Through Renunciation', 'text': 'Surrender all duties to the Supreme. Begin your journey of self-discovery and karmic understanding today.', 'btn': 'Get Full Birth Chart', 'url': 'https://ournakshatra.com/janam_landing.html'}
    }
    c = ctas.get(int(chapter), {
        'title': 'Discover Your Cosmic Path',
        'text': 'The Bhagavad Gita reveals the eternal truth. Now, decode your own karmic journey.',
        'btn': 'Get Your Free Birth Chart',
        'url': 'https://ournakshatra.com/'
    })
    
    return f"""
    <div style="margin-top: 30px; padding: 20px; background: #fffcf8; border: 1px solid #e2d1b3; border-radius: 8px; text-align: center;">
      <h3 style="color: #a85816; margin-top: 0;">✨ {safe(c['title'])}</h3>
      <p style="color: #5c3d20; font-size: 0.95rem;">{safe(c['text'])}</p>
      <a href="{safe(c['url'])}" target="_blank" style="display: inline-block; margin-top: 10px; padding: 10px 20px; background: #c96a1f; color: #fff; text-decoration: none; border-radius: 5px; font-weight: bold;">{safe(c['btn'])} →</a>
    </div>
    """

def create_gita():
    chapters = load(DATA / "gita.json").get("chapters", [])
    for chapter in chapters:
        c = chapter.get("chapter")
        for verse in chapter.get("verses", []):
            v = verse.get("verse")
            slug = str(verse.get("slug") or f"gita-{c}-{v}")
            title = f"Bhagavad Gita {c}.{v}"
            cta_html = get_gita_cta(c)
            body = (
                f"<p><strong>Sanskrit:</strong> {safe(verse.get('sanskrit') or '')}</p>"
                f"<p><strong>Meaning:</strong> {safe(verse.get('english_translation') or verse.get('hindi_translation') or '')}</p>"
                f"<p><a href=\"/bhagavad-gita.html?chapter={safe(c)}&verse={safe(v)}\">Open full Gita verse page</a></p>"
                f"{cta_html}"
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
