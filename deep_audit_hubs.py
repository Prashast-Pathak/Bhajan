#!/usr/bin/env python3
"""
Deep Audit Script — bhajan.ournakshatra.com
Checks: Safety, Completeness, Connectivity, Content Quality
"""
from pathlib import Path
import re, json

ROOT = Path('/Users/prashastpathak/Bhajan')
HUB_DIRS = ['planet', 'nakshatra', 'rashi', 'remedy', 'tithi', 'muhurat']
ISSUES = []
WARNINGS = []
PASS = []

def flag(severity, page, issue):
    if severity == 'ERROR':
        ISSUES.append(f"  ❌ [{page}] {issue}")
    elif severity == 'WARN':
        WARNINGS.append(f"  ⚠️  [{page}] {issue}")
    else:
        PASS.append(f"  ✅ [{page}] {issue}")

# ── PROHIBITED CONTENT PATTERNS ────────────────────────────────
PROHIBITED = [
    (r'lorem ipsum', 'Lorem ipsum placeholder text'),
    (r'\btodo\b|\bfixme\b|\bcoming soon\b', 'Incomplete placeholder content'),
    (r'xxx|porn|gambling|casino|bet365|1xbet', 'Prohibited adult/gambling content'),
    (r'click here to win|free money|cryptocurrency invest', 'Spam/scam language'),
    (r'hitler|nazis|terrorism|jihad', 'Potentially harmful/sensitive political content'),
]

# ── REQUIRED ELEMENTS ──────────────────────────────────────────
REQUIRED_TAGS = [
    ('G-03ZRSSBHGJ',          'GA4 Analytics tag'),
    ('ca-pub-8437539747039479','AdSense tag'),
    ('ournakshatra.com',       'Cross-link to ournakshatra.com'),
]

# ── AUDIT FUNCTION ─────────────────────────────────────────────
def audit_file(path: Path):
    rel = str(path.relative_to(ROOT))
    try:
        content = path.read_text(encoding='utf-8')
    except Exception as e:
        flag('ERROR', rel, f"Cannot read file: {e}")
        return

    # 1. Content length check
    word_count = len(content.split())
    if word_count < 200:
        flag('ERROR', rel, f"Too thin — only {word_count} words (min 200)")
    elif word_count < 400:
        flag('WARN', rel, f"Sparse content — {word_count} words (recommended 400+)")

    # 2. Required tags
    for pattern, label in REQUIRED_TAGS:
        if pattern not in content:
            flag('ERROR', rel, f"Missing: {label}")

    # 3. Prohibited content (check body text only, skip CSS/script/input attrs)
    body_text = re.sub(r'<(style|script)[^>]*>.*?</(style|script)>', '', content, flags=re.DOTALL)
    body_text = re.sub(r'placeholder=["\'][^"\']*["\']', '', body_text)  # remove input placeholders
    body_lower = body_text.lower()
    for pattern, label in PROHIBITED:
        if re.search(pattern, body_lower):
            flag('ERROR', rel, f"Prohibited content found: {label}")

    # 4. Broken/empty links (skip style/script blocks to avoid CSS false positives)
    content_no_style = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
    content_no_style = re.sub(r'<script[^>]*>.*?</script>', '', content_no_style, flags=re.DOTALL)
    empty_hrefs = re.findall(r"href=[\"']\s*[\"']", content_no_style)
    if empty_hrefs:
        flag('WARN', rel, f"{len(empty_hrefs)} empty href(s) found")

    # 5. HTML structure checks
    if '<title>' not in content:
        flag('ERROR', rel, "Missing <title> tag")
    if 'meta name="description"' not in content:
        flag('WARN', rel, "Missing meta description")
    if '<h1' not in content and 'hero-sanskrit' not in content and 'hero-banner' not in content:
        flag('WARN', rel, "No H1 or hero heading found")

    # 6. Check ournakshatra.com links are valid (not empty)
    nakshatra_links = re.findall(r'href=["\']https?://ournakshatra\.com([^"\']*)["\']', content)
    for link in nakshatra_links:
        if len(link.strip()) == 0:
            flag('WARN', rel, "Blank ournakshatra.com link found")

    # 7. Hindi/Sanskrit content present (for hub pages)
    devanagari_pattern = re.compile(r'[\u0900-\u097F]')
    if not devanagari_pattern.search(content):
        flag('WARN', rel, "No Devanagari/Sanskrit text found — content may lack depth")


def audit_hub_pages():
    print("\n" + "═"*60)
    print("  AUDITING 66 HUB PAGES")
    print("═"*60)
    total = 0
    for d in HUB_DIRS:
        pages = list((ROOT / d).rglob('index.html'))
        print(f"\n  📂 /{d}/ — {len(pages)} pages")
        for p in sorted(pages):
            audit_file(p)
            total += 1
    return total

def audit_existing_pages():
    print("\n" + "═"*60)
    print("  SPOT-CHECK: EXISTING BHAJAN/GITA/PRAYER PAGES (sample 20)")
    print("═"*60)
    all_pages = []
    for d in ['bhajan', 'gita', 'prayer', 'shloka', 'upanishad', 'wisdom']:
        all_pages.extend(list((ROOT / d).rglob('index.html')))
    # Sample every Nth file to get ~20
    step = max(1, len(all_pages) // 20)
    sampled = all_pages[::step][:20]
    for p in sampled:
        audit_file(p)
    return len(sampled)

def audit_root_pages():
    print("\n" + "═"*60)
    print("  AUDITING ROOT HTML PAGES")
    print("═"*60)
    root_pages = list(ROOT.glob('*.html'))
    for p in root_pages:
        audit_file(p)
    return len(root_pages)

def check_sitemap_coverage():
    print("\n" + "═"*60)
    print("  CHECKING SITEMAP COVERAGE")
    print("═"*60)
    sitemap_path = ROOT / 'sitemap.xml'
    if not sitemap_path.exists():
        flag('ERROR', 'sitemap.xml', "Sitemap does not exist!")
        return
    sitemap = sitemap_path.read_text(encoding='utf-8')
    url_count = sitemap.count('<loc>')
    print(f"  📊 Sitemap contains {url_count} URLs")

    # Check if hub pages are in sitemap
    for d in HUB_DIRS:
        if f'/{d}/' not in sitemap:
            flag('WARN', 'sitemap.xml', f"No /{d}/ URLs in sitemap — new hub pages not indexed!")
        else:
            flag('OK', 'sitemap.xml', f"/{d}/ pages found in sitemap")

def check_ads_txt():
    ads = ROOT / 'ads.txt'
    if not ads.exists():
        flag('ERROR', 'ads.txt', "ads.txt missing!")
    else:
        content = ads.read_text()
        if 'pub-8437539747039479' in content:
            flag('OK', 'ads.txt', "Correct publisher ID present")
        else:
            flag('ERROR', 'ads.txt', "Publisher ID mismatch!")

def check_famous_people_accuracy():
    """Flag historically dubious 'famous people' data."""
    print("\n" + "═"*60)
    print("  CHECKING FAMOUS PEOPLE DATA ACCURACY")
    print("═"*60)
    QUESTIONABLE = ['Hitler', 'Saddam Hussein', 'Adolf']
    for d in ['nakshatra']:
        for p in (ROOT / d).rglob('index.html'):
            content = p.read_text(encoding='utf-8')
            for name in QUESTIONABLE:
                if name in content:
                    flag('WARN', str(p.relative_to(ROOT)),
                         f"'{name}' listed as famous person — consider removing for brand safety")

# ── MAIN ──────────────────────────────────────────────────────
if __name__ == '__main__':
    print("\n🔍 NAKSHATRA BHAJAN — DEEP AUDIT REPORT")
    print("  bhajan.ournakshatra.com")
    print("  Run date: 2026-05-01")

    check_ads_txt()
    h = audit_hub_pages()
    r = audit_root_pages()
    s = audit_existing_pages()
    check_sitemap_coverage()
    check_famous_people_accuracy()

    print("\n" + "═"*60)
    print("  AUDIT SUMMARY")
    print("═"*60)
    print(f"  Total pages checked : {h + r + s}")
    print(f"  ✅ Passed checks    : {len(PASS)}")
    print(f"  ⚠️  Warnings         : {len(WARNINGS)}")
    print(f"  ❌ Errors           : {len(ISSUES)}")

    if ISSUES:
        print("\n── ERRORS (must fix) ──")
        for i in ISSUES: print(i)
    if WARNINGS:
        print("\n── WARNINGS (review) ──")
        for w in WARNINGS: print(w)
    if not ISSUES and not WARNINGS:
        print("\n  🎉 All checks passed — site is clean and complete!")
    print()
