import os
import re
import glob

def extract_from_bhajan():
    with open('bhajan.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract HTML blocks
    # Header
    header_match = re.search(r'<header class="main-header">.*?</header>', content, re.DOTALL)
    header_html = header_match.group(0) if header_match else ""

    # Mobile menu overlay and drawer
    menu_match = re.search(r'<!-- Mobile Menu Overlay -->\s*<div id="mobileMenuOverlay".*?</div>\s*<div id="mobileMenu".*?</div>', content, re.DOTALL)
    menu_html = menu_match.group(0) if menu_match else ""

    # Toggle mobile menu script
    toggle_script_match = re.search(r'<script>\s*function toggleMobileMenu\(\).*?</script>', content, re.DOTALL)
    toggle_script = toggle_script_match.group(0) if toggle_script_match else ""

    # UI toggles script
    ui_toggles_match = re.search(r'<script>\s*// ── UI TOGGLES \(consolidated\) ──.*?</script>', content, re.DOTALL)
    ui_toggles = ui_toggles_match.group(0) if ui_toggles_match else ""

    return header_html, menu_html, toggle_script, ui_toggles

def process_file(filepath, header_html, menu_html, toggle_script, ui_toggles):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Replace <header>...</header>
    content = re.sub(r'<header.*?</header>', header_html, content, flags=re.DOTALL)

    # Remove existing mobile menu blocks
    content = re.sub(r'<!-- Mobile Menu Overlay -->\s*<div id="mobileMenuOverlay".*?</div>\s*<div id="mobileMenu".*?</div>', '', content, flags=re.DOTALL)
    content = re.sub(r'<div id="mobileMenuOverlay".*?</div>\s*<div id="mobileMenu".*?</div>', '', content, flags=re.DOTALL)

    # Remove existing toggle scripts
    content = re.sub(r'<script>\s*function toggleMobileMenu\(\).*?</script>', '', content, flags=re.DOTALL)
    
    # Remove all UI TOGGLES or CHANTING MODE scripts
    content = re.sub(r'<script>\s*// ── UI TOGGLES.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<script>\s*// ── GLOBAL UI TOGGLES.*?</script>', '', content, flags=re.DOTALL)
    content = re.sub(r'<script>\s*// ── CHANTING MODE.*?</script>', '', content, flags=re.DOTALL)

    # Now we need to insert the menu and scripts right after the </header>
    # Find </header>
    if '</header>' in content:
        insert_text = f"\n\n{menu_html}\n\n{toggle_script}\n\n{ui_toggles}\n"
        content = content.replace('</header>', f'</header>{insert_text}', 1)

    # Clean up multiple blank lines
    content = re.sub(r'\n{3,}', '\n\n', content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {filepath}")
    else:
        print(f"No changes needed: {filepath}")

def main():
    header_html, menu_html, toggle_script, ui_toggles = extract_from_bhajan()
    
    if not all([header_html, menu_html, toggle_script, ui_toggles]):
        print("Error extracting from bhajan.html")
        return

    html_files = glob.glob("*.html")
    for file in html_files:
        if file == 'bhajan.html':
            continue
        process_file(file, header_html, menu_html, toggle_script, ui_toggles)

if __name__ == "__main__":
    main()
