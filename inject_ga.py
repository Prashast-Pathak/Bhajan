import os
from pathlib import Path

ROOT = Path('/Users/prashastpathak/Bhajan')

ga_tag = """
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-03ZRSSBHGJ"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-03ZRSSBHGJ');
</script>
"""

for html_file in ROOT.glob('*.html'):
    content = html_file.read_text(encoding='utf-8')
    if 'G-03ZRSSBHGJ' not in content:
        # Inject right after <head> to prioritize analytics loading
        content = content.replace('<head>', f'<head>\n{ga_tag}')
        html_file.write_text(content, encoding='utf-8')
        print(f"Injected GA4 into {html_file.name}")
