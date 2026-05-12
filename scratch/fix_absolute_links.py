import glob

html_files = glob.glob('/Users/prashastpathak/Bhajan/*.html')
updated = 0

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False
    
    # We want to replace relative Jyotish Hub links with absolute links.
    replacements = {
        'href="/planet/': 'href="https://ournakshatra.com/planet/',
        'href="/nakshatra/': 'href="https://ournakshatra.com/nakshatra/',
        'href="/rashi/': 'href="https://ournakshatra.com/rashi/',
        'href="/remedy/': 'href="https://ournakshatra.com/remedy/',
        'href="/tithi/': 'href="https://ournakshatra.com/tithi/',
        'href="/muhurat/': 'href="https://ournakshatra.com/muhurat/',
    }

    for old, new in replacements.items():
        if old in content:
            content = content.replace(old, new)
            changed = True

    if changed:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        updated += 1

print(f"Fixed relative links to absolute in {updated} HTML files.")
