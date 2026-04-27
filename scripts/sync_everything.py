import re
import glob

with open('bhajan.html', 'r', encoding='utf-8') as f:
    bhajan = f.read()

# 1. Extract CSS
css_match = re.search(r'<style id="premium-header-styles">(.*?)</style>', bhajan, re.DOTALL)
if not css_match:
    print("Could not find CSS in bhajan.html")
    exit(1)
css_to_inject = css_match.group(1)

# 2. Extract Header
header_match = re.search(r'<header class="main-header">.*?</header>', bhajan, re.DOTALL)
header_html = header_match.group(0)

# 3. Extract Mobile Menu
menu_match = re.search(r'<!-- Mobile Menu Overlay -->.*?</div>\n</div>(?=\n\n<script>\nfunction toggleMobileMenu)', bhajan, re.DOTALL)
if not menu_match:
    print("Could not extract mobile menu")
    exit(1)
menu_html = menu_match.group(0)

# 4. Extract Scripts
toggle_script_match = re.search(r'<script>\nfunction toggleMobileMenu\(\).*?</script>', bhajan, re.DOTALL)
toggle_script = toggle_script_match.group(0)

ui_toggles_match = re.search(r'<script>\n// ── UI TOGGLES.*?\}\)\(\);\n</script>', bhajan, re.DOTALL)
if not ui_toggles_match:
    # Try generic
    ui_toggles_match = re.search(r'<script>\n// ── GLOBAL UI TOGGLES.*?\}\)\(\);\n</script>', bhajan, re.DOTALL)
ui_toggles = ui_toggles_match.group(0) if ui_toggles_match else ""

print("Extracted all components successfully!")

files = glob.glob("*.html")
for file in files:
    if file == 'bhajan.html':
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    original = content

    # CSS
    if '<style id="premium-header-styles">' in content:
        content = re.sub(r'<style id="premium-header-styles">.*?</style>', f'<style id="premium-header-styles">{css_to_inject}</style>', content, flags=re.DOTALL)
    else:
        # Remove old CSS
        content = re.sub(r'\s*/\* HEADER \*/.*?(?=\s*/\* [A-Z ]+ \*/)', '\n', content, flags=re.DOTALL)
        content = re.sub(r'\s*/\* MOBILE MENU DRAWER \*/.*?(?=\s*/\* [A-Z ]+ \*/)', '\n', content, flags=re.DOTALL)
        content = content.replace('</head>', f'  <style id="premium-header-styles">{css_to_inject}</style>\n</head>')

    # Mobile Menu removal (must be done before header, as regex might match weirdly)
    content = re.sub(r'<!-- Mobile Menu Overlay -->.*?(?=<script>\nfunction toggleMobileMenu)', '', content, flags=re.DOTALL)
    content = re.sub(r'<div id="mobileMenuOverlay".*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div id="mobileMenu".*?</div>\n</div>', '', content, flags=re.DOTALL)

    # HTML Header replacement
    content = re.sub(r'<header.*?</header>', header_html, content, flags=re.DOTALL)

    # Scripts removal
    content = re.sub(r'<script>\s*function toggleMobileMenu.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<script>\s*// ── UI TOGGLES.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<script>\s*// ── GLOBAL UI TOGGLES.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<script>\s*// ── CHANTING MODE.*?</script>', '', content, flags=re.DOTALL)

    # Inject Mobile Menu and Scripts
    if '</header>' in content:
        insert = f"\n\n{menu_html}\n\n{toggle_script}\n\n{ui_toggles}\n"
        content = content.replace('</header>', f'</header>{insert}', 1)

    # Clean up blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)

    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
