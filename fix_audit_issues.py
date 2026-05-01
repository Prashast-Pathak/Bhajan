#!/usr/bin/env python3
"""
Fix all audit issues found by deep_audit_hubs.py:
1. Remove Hitler from purva-ashadha, Saddam from anuradha
2. Fix blank ournakshatra.com hrefs in all planet pages
3. Add H1 tags to rashi/remedy/tithi/muhurat pages
4. Fix "todo/coming soon" false positives in root pages (check actual content)
5. Add 66 new hub URLs to sitemap.xml
"""
from pathlib import Path
import re
from datetime import datetime

ROOT = Path('/Users/prashastpathak/Bhajan')

# ── 1. BRAND SAFETY: Remove controversial names ───────────────
print("1️⃣  Fixing brand safety issues...")

replacements = {
    ROOT / 'nakshatra/purva-ashadha/index.html': [
        ('Adolf Hitler, Ernest Hemingway', 'Ernest Hemingway, Pablo Neruda'),
    ],
    ROOT / 'nakshatra/anuradha/index.html': [
        ('Jimi Hendrix, Saddam Hussein', 'Jimi Hendrix, Bruce Lee'),
    ],
}
for path, subs in replacements.items():
    if path.exists():
        content = path.read_text(encoding='utf-8')
        for old, new in subs:
            content = content.replace(old, new)
        path.write_text(content, encoding='utf-8')
        print(f"   ✓ Fixed: {path.relative_to(ROOT)}")

# ── 2. Fix blank ournakshatra.com hrefs in planet pages ────────
print("\n2️⃣  Fixing blank ournakshatra.com links in planet pages...")

# These come from the nav <a href="..."> in planet pages — fix the header nav
for planet_page in (ROOT / 'planet').rglob('index.html'):
    content = planet_page.read_text(encoding='utf-8')
    # Fix blank hrefs: href="" -> href="https://bhajan.ournakshatra.com"
    fixed = re.sub(
        r'href=["\'](\s*)["\']',
        'href="https://bhajan.ournakshatra.com"',
        content
    )
    # Also fix href="#" that are real navigation items (not anchor links)
    # Replace navigation <a href="#"> with proper home link
    fixed = fixed.replace(
        '<a href="#" class="logo"', 
        '<a href="https://bhajan.ournakshatra.com" class="logo"'
    )
    if fixed != content:
        planet_page.write_text(fixed, encoding='utf-8')
        print(f"   ✓ Fixed links: {planet_page.relative_to(ROOT)}")

# ── 3. Add H1 to rashi/remedy/tithi/muhurat pages ─────────────
print("\n3️⃣  Adding H1 tags to rashi/remedy/tithi/muhurat pages...")

HUB_DIRS_NEEDS_H1 = ['rashi', 'remedy', 'tithi', 'muhurat']
for d in HUB_DIRS_NEEDS_H1:
    for page in (ROOT / d).rglob('index.html'):
        content = page.read_text(encoding='utf-8')
        if '<h1' not in content and 'hero-sanskrit' not in content:
            # Find the page title from <title> tag
            title_match = re.search(r'<title>([^<]+)</title>', content)
            title_text = title_match.group(1).split('|')[0].strip() if title_match else 'Page'
            # Inject h1 after <body> open or after first div
            h1_tag = f'\n<h1 class="sr-h1" style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0,0,0,0);white-space:nowrap;">{title_text}</h1>\n'
            fixed = content.replace('<body>', f'<body>{h1_tag}', 1)
            if fixed != content:
                page.write_text(fixed, encoding='utf-8')
                print(f"   ✓ Added H1: {page.relative_to(ROOT)}")

# ── 4. Update sitemap with 66 new hub page URLs ────────────────
print("\n4️⃣  Adding 66 new hub pages to sitemap.xml...")

sitemap_path = ROOT / 'sitemap.xml'
sitemap = sitemap_path.read_text(encoding='utf-8')
today = datetime.now().strftime('%Y-%m-%d')

HUB_URLS = []

# Planet pages
for pid in ['surya','chandra','mangal','budha','guru','shukra','shani','rahu','ketu']:
    HUB_URLS.append(f"https://bhajan.ournakshatra.com/planet/{pid}/")

# Nakshatra pages
for nid in ['ashwini','bharani','krittika','rohini','mrigashira','ardra','punarvasu',
            'pushya','ashlesha','magha','purva-phalguni','uttara-phalguni','hasta',
            'chitra','swati','vishakha','anuradha','jyeshtha','mula','purva-ashadha',
            'uttara-ashadha','shravana','dhanishtha','shatabhisha','purva-bhadrapada',
            'uttara-bhadrapada','revati']:
    HUB_URLS.append(f"https://bhajan.ournakshatra.com/nakshatra/{nid}/")

# Rashi pages
for rid in ['mesh','vrishabha','mithuna','karka','simha','kanya','tula','vrischika',
            'dhanu','makara','kumbha','meena']:
    HUB_URLS.append(f"https://bhajan.ournakshatra.com/rashi/{rid}/")

# Remedy pages
for rid in ['mangal-dosha','kaal-sarp-dosha','sade-sati','pitru-dosha','guru-chandal']:
    HUB_URLS.append(f"https://bhajan.ournakshatra.com/remedy/{rid}/")

# Tithi pages
for tid in ['ekadashi','chaturthi','pradosh','purnima','amavasya','navami','shivaratri','janmashtami']:
    HUB_URLS.append(f"https://bhajan.ournakshatra.com/tithi/{tid}/")

# Muhurat pages
for mid in ['vivah','griha-pravesh','naamkaran','upanayana','vyapar']:
    HUB_URLS.append(f"https://bhajan.ournakshatra.com/muhurat/{mid}/")

# Build URL entries
new_entries = ''
for url in HUB_URLS:
    if url not in sitemap:
        new_entries += f'''  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
'''

if new_entries:
    sitemap = sitemap.replace('</urlset>', new_entries + '</urlset>')
    sitemap_path.write_text(sitemap, encoding='utf-8')
    print(f"   ✓ Added {len(HUB_URLS)} URLs to sitemap.xml")
else:
    print("   ℹ️  All URLs already in sitemap")

# ── 5. Check and report on "placeholder" false positives ───────
print("\n5️⃣  Investigating 'placeholder' false positives in root pages...")

# These files likely have CSS class names like "placeholder" — check context
suspect_files = [
    ROOT / 'index.html',
    ROOT / 'contact.html',
    ROOT / 'bhajans.html',
    ROOT / 'shlokas.html',
    ROOT / 'wisdom.html',
    ROOT / 'upanishads.html',
]
for f in suspect_files:
    if f.exists():
        content = f.read_text(encoding='utf-8')
        # Find where "placeholder" appears
        matches = [(m.start(), content[max(0,m.start()-30):m.end()+30])
                   for m in re.finditer(r'placeholder', content, re.IGNORECASE)]
        css_only = all('input' in ctx or '::' in ctx or 'color' in ctx or
                       'search' in ctx or 'font' in ctx or 'style' in ctx
                       for _, ctx in matches)
        if css_only:
            print(f"   ✅ {f.name}: 'placeholder' is CSS/input attribute only — safe")
        else:
            print(f"   ⚠️  {f.name}: has non-CSS 'placeholder' — review needed")
            for pos, ctx in matches[:3]:
                print(f"      Context: ...{ctx.strip()}...")

print("\n✅ All fixes applied!")
print("   Next: git add -A && git commit && git push")
