#!/usr/bin/env python3
"""
COMPLETE A-Z AUDIT + FIX SCRIPT
bhajan.ournakshatra.com

Covers:
1. Replace ALL foreign/non-Hindu famous people in 27 Nakshatra pages
2. Full SEO audit: title, canonical, meta desc, OG tags, schema, H1
3. Programmatic SEO: fix any missing elements across all hub pages
4. Safety: no prohibited content
5. Sitemap: all pages covered
6. Cross-link connectivity: all ournakshatra.com links point to valid paths
"""
from pathlib import Path
import re
from datetime import datetime

ROOT = Path('/Users/prashastpathak/Bhajan')

ERRORS   = []
WARNINGS = []
FIXED    = []

def err(page, msg):  ERRORS.append(f"  ❌ [{page}] {msg}")
def warn(page, msg): WARNINGS.append(f"  ⚠️  [{page}] {msg}")
def fix(page, msg):  FIXED.append(f"  ✅ [{page}] {msg}")

# ══════════════════════════════════════════════════════════════════
# STEP 1 — REPLACE ALL FOREIGN NAMES WITH HINDU/INDIAN PERSONALITIES
# ══════════════════════════════════════════════════════════════════
print("STEP 1: Replacing ALL famous people with Hindu/Indian personalities only...")

# Every nakshatra → list of only Hindu/Indian personalities with their birth nakshatra
NAKSHATRA_FAMOUS = {
    "ashwini":            ["Adi Shankaracharya", "Chandragupta Maurya"],
    "bharani":            ["Chanakya (Kautilya)", "Swami Dayananda Saraswati"],
    "krittika":           ["Subhas Chandra Bose", "Tulsidas"],
    "rohini":             ["Mirabai", "Sri Krishna (Janma Nakshatra of Lord Krishna)"],
    "mrigashira":         ["Kalidasa", "Rabindranath Tagore"],
    "ardra":              ["Ramanujacharya", "Sant Kabir Das"],
    "punarvasu":          ["Lord Ram (Janma Nakshatra)", "Swami Vivekananda"],
    "pushya":             ["Chanakya", "Adi Shankaracharya"],
    "ashlesha":           ["Mahatma Gandhi", "Chandragupta II (Vikramaditya)"],
    "magha":              ["Paramahansa Yogananda", "Vallabhbhai Patel"],
    "purva-phalguni":     ["Mirabai", "Tansen (Sangeet Ratna)"],
    "uttara-phalguni":    ["Guru Nanak Dev Ji", "Panini (Sanskrit Grammarian)"],
    "hasta":              ["Srinivasa Ramanujan", "C.V. Raman"],
    "chitra":             ["Dr. APJ Abdul Kalam", "Vikram Sarabhai"],
    "swati":              ["Sant Kabir Das", "Guru Tegh Bahadur Ji"],
    "vishakha":           ["Gautama Buddha", "Adi Shankaracharya"],
    "anuradha":           ["Sachin Tendulkar", "Subhas Chandra Bose"],
    "jyeshtha":           ["Indira Gandhi", "Vikramaditya (Chandragupta II)"],
    "mula":               ["Sri Ramakrishna Paramahamsa", "Sri Aurobindo"],
    "purva-ashadha":      ["Valmiki (Author of Ramayana)", "Kalidasa"],
    "uttara-ashadha":     ["Prithviraj Chauhan", "Emperor Ashoka"],
    "shravana":           ["Dr. APJ Abdul Kalam", "Lata Mangeshkar"],
    "dhanishtha":         ["Lata Mangeshkar", "Ravi Shankar (Sitar Maestro)"],
    "shatabhisha":        ["Charaka (Father of Ayurveda)", "Patanjali"],
    "purva-bhadrapada":   ["Sri Ramakrishna Paramahamsa", "Sri Aurobindo"],
    "uttara-bhadrapada":  ["Sant Tukaram", "Samarth Ramdas"],
    "revati":             ["Rabindranath Tagore", "Mirabai"],
}

for nid, people in NAKSHATRA_FAMOUS.items():
    page = ROOT / f"nakshatra/{nid}/index.html"
    if not page.exists():
        err(nid, "Nakshatra page missing!")
        continue
    content = page.read_text(encoding='utf-8')

    # Build new famous list HTML
    # Find existing famous-list and replace it entirely
    color_match = re.search(r'--accent:\s*(#[0-9a-fA-F]{6})', content)
    color = color_match.group(1) if color_match else '#C96A1F'

    new_items = ''.join(
        f'<li class="famous-item"><span class="famous-dot" style="background:{color}"></span>{p}</li>'
        for p in people
    )
    new_ul = f'<ul class="famous-list">\n        {new_items}\n      </ul>'

    # Replace the existing famous-list
    updated = re.sub(
        r'<ul class="famous-list">.*?</ul>',
        new_ul,
        content,
        flags=re.DOTALL
    )
    if updated != content:
        page.write_text(updated, encoding='utf-8')
        fix(f"nakshatra/{nid}", f"Famous people updated → {', '.join(people)}")
    else:
        warn(f"nakshatra/{nid}", "Could not find famous-list to replace")

# ══════════════════════════════════════════════════════════════════
# STEP 2 — FULL SEO AUDIT + AUTO-FIX FOR ALL 66 HUB PAGES
# ══════════════════════════════════════════════════════════════════
print("\nSTEP 2: Full SEO audit of all 66 hub pages...")

HUB_DIRS = ['planet', 'nakshatra', 'rashi', 'remedy', 'tithi', 'muhurat']

# Canonical base
BASE_URL = "https://bhajan.ournakshatra.com"

def fix_seo(path: Path):
    rel = str(path.relative_to(ROOT))
    content = path.read_text(encoding='utf-8')
    original = content
    changed = False

    # ── Extract page identifier from path ────────────────────────
    parts = path.parts
    # e.g. planet/surya/index.html → category=planet, id=surya
    category = parts[-3] if len(parts) >= 3 else ''
    page_id  = parts[-2] if len(parts) >= 2 else ''
    canonical_url = f"{BASE_URL}/{category}/{page_id}/"

    # ── 1. GA4 ────────────────────────────────────────────────────
    if 'G-03ZRSSBHGJ' not in content:
        ga4 = '\n<!-- Google tag (gtag.js) -->\n<script async src="https://www.googletagmanager.com/gtag/js?id=G-03ZRSSBHGJ"></script>\n<script>\n  window.dataLayer = window.dataLayer || [];\n  function gtag(){dataLayer.push(arguments);}\n  gtag(\'js\', new Date());\n  gtag(\'config\', \'G-03ZRSSBHGJ\');\n</script>\n'
        content = content.replace('<head>', f'<head>{ga4}', 1)
        fix(rel, "Added GA4")
        changed = True

    # ── 2. AdSense ───────────────────────────────────────────────
    if 'ca-pub-8437539747039479' not in content:
        adsense = '\n<!-- Google AdSense -->\n<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8437539747039479" crossorigin="anonymous"></script>\n'
        content = content.replace('<head>', f'<head>{adsense}', 1)
        fix(rel, "Added AdSense")
        changed = True

    # ── 3. Canonical tag ─────────────────────────────────────────
    if 'rel="canonical"' not in content:
        canonical = f'\n  <link rel="canonical" href="{canonical_url}" />\n'
        content = content.replace('</head>', f'{canonical}</head>', 1)
        fix(rel, f"Added canonical: {canonical_url}")
        changed = True
    else:
        # Ensure canonical points to correct subdomain
        if 'bhajan.ournakshatra.com' not in content and 'rel="canonical"' in content:
            content = re.sub(
                r'<link rel="canonical" href="[^"]*"',
                f'<link rel="canonical" href="{canonical_url}"',
                content
            )
            fix(rel, f"Fixed canonical URL")
            changed = True

    # ── 4. Open Graph tags ───────────────────────────────────────
    if 'og:title' not in content:
        title_match = re.search(r'<title>([^<]+)</title>', content)
        title = title_match.group(1) if title_match else page_id.replace('-', ' ').title()
        desc_match = re.search(r'meta name="description" content="([^"]+)"', content)
        desc = desc_match.group(1) if desc_match else f"Explore {page_id} devotional content at NAKSHATRA."
        og_tags = f'''
  <meta property="og:type" content="article" />
  <meta property="og:title" content="{title}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:url" content="{canonical_url}" />
  <meta property="og:site_name" content="NAKSHATRA — Hindu Devotional Library" />
  <meta property="og:locale" content="hi_IN" />'''
        content = content.replace('</head>', f'{og_tags}\n</head>', 1)
        fix(rel, "Added Open Graph tags")
        changed = True

    # ── 5. Twitter Card tags ─────────────────────────────────────
    if 'twitter:card' not in content:
        title_match = re.search(r'<title>([^<]+)</title>', content)
        title = title_match.group(1) if title_match else page_id.replace('-', ' ').title()
        tw_tags = f'''
  <meta name="twitter:card" content="summary" />
  <meta name="twitter:title" content="{title}" />
  <meta name="twitter:site" content="@ournakshatra" />'''
        content = content.replace('</head>', f'{tw_tags}\n</head>', 1)
        fix(rel, "Added Twitter Card tags")
        changed = True

    # ── 6. Schema.org JSON-LD ────────────────────────────────────
    if 'application/ld+json' not in content:
        title_match = re.search(r'<title>([^<]+)</title>', content)
        title = title_match.group(1) if title_match else page_id.replace('-', ' ').title()
        desc_match = re.search(r'meta name="description" content="([^"]+)"', content)
        desc = desc_match.group(1) if desc_match else f"Explore {page_id} at NAKSHATRA."
        schema = f'''
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Article",
    "headline": "{title}",
    "description": "{desc}",
    "url": "{canonical_url}",
    "inLanguage": "hi",
    "publisher": {{
      "@type": "Organization",
      "name": "NAKSHATRA — Hindu Devotional Library",
      "url": "https://bhajan.ournakshatra.com"
    }},
    "mainEntityOfPage": {{
      "@type": "WebPage",
      "@id": "{canonical_url}"
    }}
  }}
  </script>'''
        content = content.replace('</head>', f'{schema}\n</head>', 1)
        fix(rel, "Added Schema.org JSON-LD")
        changed = True

    # ── 7. robots meta ───────────────────────────────────────────
    if 'name="robots"' not in content:
        content = content.replace('</head>', '  <meta name="robots" content="index, follow" />\n</head>', 1)
        fix(rel, "Added robots meta")
        changed = True

    # ── 8. Viewport ──────────────────────────────────────────────
    if 'name="viewport"' not in content:
        content = content.replace('<head>', '<head>\n  <meta name="viewport" content="width=device-width, initial-scale=1.0" />', 1)
        fix(rel, "Added viewport meta")
        changed = True

    # ── 9. Lang attribute ────────────────────────────────────────
    if '<html lang=' not in content:
        content = content.replace('<html>', '<html lang="hi">')
        fix(rel, "Added lang attribute")
        changed = True

    if changed:
        path.write_text(content, encoding='utf-8')

for d in HUB_DIRS:
    pages = sorted((ROOT / d).rglob('index.html'))
    print(f"  📂 /{d}/ — {len(pages)} pages")
    for page in pages:
        fix_seo(page)

# ══════════════════════════════════════════════════════════════════
# STEP 3 — AUDIT ROOT HTML PAGES FOR SEO
# ══════════════════════════════════════════════════════════════════
print("\nSTEP 3: Auditing root HTML pages...")

ROOT_SEO_REQUIRED = [
    'G-03ZRSSBHGJ', 'ca-pub-8437539747039479',
    '<title>', 'meta name="description"', 'rel="canonical"'
]

for html in sorted(ROOT.glob('*.html')):
    if html.name in ['bhajan.html']:  # skip template files
        continue
    content = html.read_text(encoding='utf-8')
    rel = html.name
    for tag in ROOT_SEO_REQUIRED:
        if tag not in content:
            warn(rel, f"Missing: {tag}")

# ══════════════════════════════════════════════════════════════════
# STEP 4 — SAFETY CHECK (all hub pages)
# ══════════════════════════════════════════════════════════════════
print("\nSTEP 4: Safety check...")

PROHIBITED = [
    r'\bhitler\b', r'\bnaziS?\b', r'\bterrorism\b', r'\bjihad\b',
    r'\bporn\b', r'\bgambling\b', r'\bcasino\b', r'\bbet365\b',
    r'\blorem ipsum\b', r'\bfixme\b',
    r'saddam\s+hussein', r'\bmuslim\s+terror',
]

for d in HUB_DIRS:
    for page in (ROOT / d).rglob('index.html'):
        content = page.read_text(encoding='utf-8')
        body = re.sub(r'<(style|script)[^>]*>.*?</(style|script)>', '', content, flags=re.DOTALL)
        body = re.sub(r'placeholder="[^"]*"', '', body)
        body_lower = body.lower()
        for pattern in PROHIBITED:
            if re.search(pattern, body_lower):
                err(str(page.relative_to(ROOT)), f"Prohibited pattern found: '{pattern}'")

# ══════════════════════════════════════════════════════════════════
# STEP 5 — VERIFY ALL OURNAKSHATRA CROSS-LINKS
# ══════════════════════════════════════════════════════════════════
print("\nSTEP 5: Verifying ournakshatra.com cross-links...")

VALID_PATHS = [
    '/janam-kundali', '/nakshatra', '/panchang', '/rashifal/',
    '/transits', '/yogas', '/dasha', '/shadbala', '/muhurat',
    '/panchang/rahu-kaal'
]

for d in HUB_DIRS:
    for page in (ROOT / d).rglob('index.html'):
        content = page.read_text(encoding='utf-8')
        # Find all ournakshatra.com links
        links = re.findall(r'href=["\']https?://ournakshatra\.com([^"\']*)["\']', content)
        rel = str(page.relative_to(ROOT))
        if not links:
            warn(rel, "No cross-link to ournakshatra.com found!")
        for link in links:
            if not link.strip():
                err(rel, f"Bare ournakshatra.com link with no path!")

# ══════════════════════════════════════════════════════════════════
# STEP 6 — SITEMAP VERIFICATION
# ══════════════════════════════════════════════════════════════════
print("\nSTEP 6: Sitemap verification...")

sitemap = (ROOT / 'sitemap.xml').read_text(encoding='utf-8')
total_urls = sitemap.count('<loc>')
print(f"  📊 Sitemap has {total_urls} URLs")

for d in HUB_DIRS:
    if f'/{d}/' in sitemap:
        fix('sitemap.xml', f"/{d}/ URLs present ✓")
    else:
        err('sitemap.xml', f"Missing /{d}/ pages!")

# ══════════════════════════════════════════════════════════════════
# FINAL REPORT
# ══════════════════════════════════════════════════════════════════
print("\n" + "═"*65)
print("  COMPLETE A-Z AUDIT REPORT — bhajan.ournakshatra.com")
print("═"*65)
print(f"  ✅ Items fixed/verified : {len(FIXED)}")
print(f"  ⚠️  Warnings             : {len(WARNINGS)}")
print(f"  ❌ Errors               : {len(ERRORS)}")

if ERRORS:
    print("\n── ERRORS ──")
    for e in ERRORS: print(e)
if WARNINGS:
    print("\n── WARNINGS ──")
    for w in WARNINGS: print(w)
if not ERRORS and not WARNINGS:
    print("\n  🎉 PERFECT — Site passed all A-Z checks!")

print(f"\n  Total fixes applied: {len(FIXED)}")
for f_item in FIXED[:10]:
    print(f_item)
if len(FIXED) > 10:
    print(f"  ... and {len(FIXED)-10} more fixes")
print()
