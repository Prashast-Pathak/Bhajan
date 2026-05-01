#!/usr/bin/env python3
"""
Injects GA4 + AdSense tags into all 66 newly generated hub pages.
Covers: planet/, nakshatra/, rashi/, remedy/, tithi/, muhurat/
"""
from pathlib import Path

ROOT = Path('/Users/prashastpathak/Bhajan')
DIRS = ['planet', 'nakshatra', 'rashi', 'remedy', 'tithi', 'muhurat']

GA4 = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-03ZRSSBHGJ"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-03ZRSSBHGJ');
</script>"""

ADSENSE = """
<!-- Google AdSense Auto Ads -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-8437539747039479"
     crossorigin="anonymous"></script>"""

injected = skipped = 0

for d in DIRS:
    for html_file in (ROOT / d).rglob('index.html'):
        content = html_file.read_text(encoding='utf-8')
        changed = False
        if 'G-03ZRSSBHGJ' not in content:
            content = content.replace('<head>', f'<head>\n{GA4}', 1)
            changed = True
        if 'ca-pub-8437539747039479' not in content:
            content = content.replace('<head>', f'<head>\n{ADSENSE}', 1)
            changed = True
        if changed:
            html_file.write_text(content, encoding='utf-8')
            injected += 1
            print(f"  ✓  {html_file.relative_to(ROOT)}")
        else:
            skipped += 1

print(f"\n✅ Done — GA4+AdSense injected into {injected} pages, {skipped} already had tags.")
