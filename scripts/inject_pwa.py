import re
import glob
from pathlib import Path

ROOT = Path('/Users/prashastpathak/Bhajan')

PWA_TAGS = """
  <link rel="manifest" href="/manifest.json">
  <script>
    if ('serviceWorker' in navigator) {
      window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js').then(reg => {
          console.log('[SW] Registered: ', reg.scope);
        }).catch(err => {
          console.log('[SW] Registration failed: ', err);
        });
      });
    }
  </script>
"""

def inject_pwa(filepath):
    try:
        content = filepath.read_text(encoding='utf-8')
        if 'rel="manifest"' not in content or 'serviceWorker.register' not in content:
            # Inject right before </head>
            content = content.replace('</head>', f'{PWA_TAGS}</head>')
            filepath.write_text(content, encoding='utf-8')
            print(f"Injected PWA tags into {filepath.name}")
    except Exception as e:
        print(f"Error processing {filepath}: {e}")

# Apply to all top-level HTML files
for html_file in ROOT.glob('*.html'):
    inject_pwa(html_file)

# Apply to all remedy HTML files
for html_file in ROOT.glob('remedy/**/*.html'):
    inject_pwa(html_file)

# Apply to all programmatic HTML files
for html_file in ROOT.glob('programmatic/**/*.html'):
    inject_pwa(html_file)
