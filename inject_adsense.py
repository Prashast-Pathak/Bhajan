import os
from pathlib import Path

ROOT = Path('/Users/prashastpathak/Bhajan')
PUBLISHER_ID = "ca-pub-8437539747039479"

adsense_tag = f"""
<!-- Google AdSense Auto Ads -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={PUBLISHER_ID}"
     crossorigin="anonymous"></script>
"""

injected = []
skipped = []

for html_file in ROOT.glob('*.html'):
    content = html_file.read_text(encoding='utf-8')
    if PUBLISHER_ID in content:
        skipped.append(html_file.name)
        continue
    # Inject right after GA4 script block (or after <head> if no GA4)
    if '</script>\n</head>' in content:
        content = content.replace('</script>\n</head>', f'</script>\n{adsense_tag}\n</head>', 1)
    elif '<head>' in content:
        content = content.replace('<head>', f'<head>\n{adsense_tag}', 1)
    else:
        skipped.append(html_file.name + " (no <head> found)")
        continue
    html_file.write_text(content, encoding='utf-8')
    injected.append(html_file.name)

print(f"\n✅ AdSense injected into {len(injected)} root templates:")
for f in injected:
    print(f"   → {f}")
if skipped:
    print(f"\n⏭️  Skipped {len(skipped)} files (already have AdSense or no <head>):")
    for f in skipped:
        print(f"   → {f}")
