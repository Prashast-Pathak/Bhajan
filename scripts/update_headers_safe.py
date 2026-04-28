#!/usr/bin/env python3
import re, glob

def update_headers():
    print("Extracting master header from bhajan.html...")
    with open('bhajan.html', 'r', encoding='utf-8') as f:
        master = f.read()
    
    css_match = re.search(r'<style id="premium-header-styles">.*?</style>', master, re.DOTALL)
    header_match = re.search(r'<header class="main-header">.*?</header>', master, re.DOTALL)
    
    if not css_match or not header_match:
        print("Error: Could not find master header components in bhajan.html")
        return
        
    master_css = css_match.group(0)
    master_header = header_match.group(0)
    
    files = glob.glob('*.html')
    updated = 0
    for file in files:
        if file == 'bhajan.html':
            continue
            
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original = content
        
        # Replace CSS
        if '<style id="premium-header-styles">' in content:
            content = re.sub(r'<style id="premium-header-styles">.*?</style>', master_css, content, flags=re.DOTALL)
        else:
            content = content.replace('</head>', f'{master_css}\n</head>')
            
        # Replace Header
        if '<header ' in content:
            # We assume header starts with <header and ends with </header>
            content = re.sub(r'<header.*?</header>', master_header, content, flags=re.DOTALL)
            
        if content != original:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {file}")
            updated += 1
            
    print(f"Successfully updated {updated} files with the new back button header.")

if __name__ == '__main__':
    update_headers()
