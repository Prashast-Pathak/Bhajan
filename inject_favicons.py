import os
from pathlib import Path

ROOT = Path('/Users/prashastpathak/Bhajan')

favicon_tags = """
  <link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
  <link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
  <link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
"""

for html_file in ROOT.glob('*.html'):
    content = html_file.read_text(encoding='utf-8')
    if 'rel="apple-touch-icon"' not in content:
        # inject right before </head>
        content = content.replace('</head>', f'{favicon_tags}</head>')
        html_file.write_text(content, encoding='utf-8')
        print(f"Injected into {html_file.name}")
