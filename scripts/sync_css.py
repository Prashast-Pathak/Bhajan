import re
import glob

# 1. Extract CSS from bhajan.html
with open('bhajan.html', 'r', encoding='utf-8') as f:
    content = f.read()

css_match = re.search(r'<style id="premium-header-styles">(.*?)</style>', content, re.DOTALL)
if not css_match:
    print("Could not find CSS in bhajan.html")
    exit(1)

css_to_inject = css_match.group(1)

# 2. Inject into all other files
files = glob.glob("*.html")
for file in files:
    if file == 'bhajan.html':
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        file_content = f.read()

    original = file_content
    
    # Strategy 1: Replace premium-header-styles block
    if '<style id="premium-header-styles">' in file_content:
        file_content = re.sub(
            r'<style id="premium-header-styles">.*?</style>', 
            f'<style id="premium-header-styles">{css_to_inject}</style>', 
            file_content, 
            flags=re.DOTALL
        )
    else:
        # Strategy 2: Remove old header CSS blocks and append new <style> before </head>
        # Let's remove typical old header css
        file_content = re.sub(r'\s*/\* HEADER \*/.*?(?=\s*/\* [A-Z ]+ \*/)', '', file_content, flags=re.DOTALL)
        file_content = re.sub(r'\s*/\* MOBILE MENU DRAWER \*/.*?(?=\s*/\* [A-Z ]+ \*/)', '', file_content, flags=re.DOTALL)
        
        # Inject our new style block right before </head>
        new_style_block = f'<style id="premium-header-styles">{css_to_inject}</style>'
        file_content = file_content.replace('</head>', f'{new_style_block}\n</head>')

    if original != file_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(file_content)
        print(f"Updated CSS in {file}")
    else:
        print(f"Could not update CSS in {file}")

