#!/usr/bin/env python3
import os
import glob

# The new footer block to inject
NEW_FOOTER = """    <div class="footer-links" style="margin-bottom: 8px;">
      <a href="https://ournakshatra.com/janam_landing.html">Free Birth Chart</a>
      <a href="https://ournakshatra.com/kundli_matching_landing.html">Matchmaking</a>
      <a href="https://ournakshatra.com/panchang_landing.html">Daily Panchang</a>
      <a href="https://ournakshatra.com/tools.html">Yoga Directory</a>
    </div>
    <div class="footer-links">"""

NEW_NAV_LINK = '<a href="https://ournakshatra.com/janam_landing.html" style="color:var(--saffron); font-weight: 700;">✨ Free Kundli</a>'

html_files = glob.glob('*.html')
count = 0

for file in html_files:
    if file == 'index.html':
        continue # Already done manually
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    original = content
    
    # 1. Inject footer
    if 'Free Birth Chart' not in content and '<div class="footer-links">' in content:
        content = content.replace('<div class="footer-links">', NEW_FOOTER, 1)
        
    # 2. Inject nav
    if '✨ Free Kundli' not in content:
        # Look for the wisdom link and the jyotish dropdown
        target = '      <a href="wisdom.html">Wisdom</a>\n          <div class="nav-dropdown">'
        if target in content:
            content = content.replace(
                target,
                f'      <a href="wisdom.html">Wisdom</a>\n      {NEW_NAV_LINK}\n          <div class="nav-dropdown">'
            )
            
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        count += 1
        print(f"Updated {file}")

print(f"Phase 1 complete! Updated {count} root HTML files.")
