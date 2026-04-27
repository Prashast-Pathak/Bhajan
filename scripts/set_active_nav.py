import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

for file in ROOT.glob("*.html"):
    content = file.read_text(encoding="utf-8")
    fname = file.name
    
    # Remove any existing active classes from the nav items
    content = re.sub(r'class="(nav-item-[a-z]+) active"', r'class="\1"', content)
    
    # Define mapping from filename to nav class
    mapping = {
        "index.html": "nav-item-home",
        "bhajans.html": "nav-item-bhajans",
        "bhagavad-gita.html": "nav-item-gita",
        "shlokas.html": "nav-item-shlokas",
        "prayers.html": "nav-item-prayers",
        "wisdom.html": "nav-item-wisdom"
    }
    
    if fname in mapping:
        cls = mapping[fname]
        content = content.replace(f'class="{cls}"', f'class="{cls} active"')
        
    file.write_text(content, encoding="utf-8")
    print(f"Set active for {fname}")

