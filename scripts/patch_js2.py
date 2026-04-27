import re

with open('bhajan.html', 'r', encoding='utf-8') as f:
    bhajan_html = f.read()

# Extract Mobile Menu JS
js_match = re.search(r'(function toggleMobileMenu.*?\}\n)', bhajan_html, re.DOTALL)
if not js_match:
    print("Could not extract JS from bhajan.html")
    exit(1)
mobile_js = js_match.group(1)

with open('bhagavad-gita.html', 'r', encoding='utf-8') as f:
    gita_html = f.read()

if 'function toggleMobileMenu' not in gita_html:
    # Find the last closing script tag or body
    injection = f"\n<script>\n{mobile_js}</script>\n</body>"
    gita_html = gita_html.replace('</body>', injection)
    with open('bhagavad-gita.html', 'w', encoding='utf-8') as f:
        f.write(gita_html)
    print("Injected function into bhagavad-gita.html")
else:
    print("Function already exists")
