#!/usr/bin/env python3
"""
Remove legacy inline dark-mode / font-size scripts from <head>.
Our consolidated UI TOGGLES block already handles all of this.
"""
import re, glob

# Patterns we want to strip out of <head> scripts
HEAD_SCRIPT_PATTERNS = [
    # Pattern 1: old self-contained dark+font script block (upanishads, shlokas, prayers)
    r'<script>\s*let fontSize = parseInt\(localStorage\.getItem\([\'"]sgs_fontsize[\'"]\).*?</script>',
    # Pattern 2: dark mode only block (bhagavad-gita, wisdom)
    r'<script>\s*document\.addEventListener\([\'"]DOMContentLoaded[\'"].*?sgs_dark.*?</script>',
    # Pattern 3: combined old dark+toggle block
    r'<script>\s*if\s*\(localStorage\.getItem\([\'"]sgs_dark[\'"]\)\s*===\s*[\'"]true[\'"]\)\s*document\.body\.classList\.add\([\'"]dark-mode[\'"]\).*?</script>',
]

files = glob.glob("*.html")
total = 0

for file in files:
    if file == 'bhajan.html':
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    for pattern in HEAD_SCRIPT_PATTERNS:
        new_content = re.sub(pattern, '', content, flags=re.DOTALL)
        if new_content != content:
            content = new_content

    # Clean up extra blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)

    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        total += 1
        print(f"  Cleaned: {file}")

print(f"\nDone — {total} files updated.")
