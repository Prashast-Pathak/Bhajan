import re
import glob

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all occurrences of <div class="mobile-menu-drawer" id="mobileMenu">
    matches = list(re.finditer(r'<div class="mobile-menu-drawer" id="mobileMenu">', content))
    if len(matches) != 2:
        return

    # We want to remove the second block.
    # The block ends at the second </div> after the opening div.
    # But it's easier to find the start of the second block and the start of the next block
    # or just use regex to match the whole block.
    start = matches[1].start()
    
    # Let's find the closing </div></div> of the mobileMenu block
    # The mobileMenu block structure is:
    # <div class="mobile-menu-drawer" id="mobileMenu">
    #   <div class="mobile-menu-header">...</div>
    #   <div class="mobile-menu-links">...</div>
    # </div>
    
    # We can search for <div class="hero"> or <div class="hero-tag"> which comes immediately after.
    # Let's use regex to find the end of the second mobile menu.
    end_match = re.search(r'</div>\s*</div>\s*<div class="hero(?:-tag)?', content[start:])
    if not end_match:
        end_match = re.search(r'</div>\s*</div>\s*<div class="hero"', content[start:])
    
    if end_match:
        end = start + end_match.start() + 13 # index after </div></div>
        new_content = content[:start] + content[end:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {filepath}")
    else:
        print(f"Could not find end of second mobile menu in {filepath}")

for path in glob.glob('remedy/**/*.html', recursive=True):
    fix_file(path)
for path in glob.glob('remedy/*.html', recursive=True):
    fix_file(path)
