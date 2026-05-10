import os
import json
import re

base_dir = '/Users/prashastpathak/Bhajan'
gita_dir = os.path.join(base_dir, 'gita')
json_path = os.path.join(base_dir, 'data', 'gita.json')
sitemap_path = os.path.join(base_dir, 'sitemap.xml')

# 1. List chapter-level directories and index.html presence
print("1. Chapter-level directories under /gita/:")
if os.path.exists(gita_dir):
    for entry in sorted(os.listdir(gita_dir)):
        full_path = os.path.join(gita_dir, entry)
        if os.path.isdir(full_path):
            has_index = os.path.exists(os.path.join(full_path, 'index.html'))
            print(f"   - /gita/{entry}/ (index.html: {'Yes' if has_index else 'No'})")

print("\n2 & 3. Cross-check: JSON vs Disk Gap:")
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

json_chapters = {str(c['chapter']): len(c.get('verses', [])) for c in data.get('chapters', [])}

for ch_num in range(1, 8):
    ch_str = str(ch_num)
    json_count = json_chapters.get(ch_str, 0)
    
    disk_count = 0
    ch_dir = os.path.join(gita_dir, ch_str)
    if os.path.exists(ch_dir):
        for entry in os.listdir(ch_dir):
            if os.path.isdir(os.path.join(ch_dir, entry)) and entry.isdigit():
                disk_count += 1
                
    gap = json_count - disk_count
    print(f"Chapter {ch_str}: JSON={json_count} | Disk={disk_count} | Gap={gap}")

print("\n4. Sitemap URLs containing /gita/:")
with open(sitemap_path, 'r', encoding='utf-8') as f:
    sitemap_content = f.read()

# Extract all text inside <loc> or <ns0:loc>
loc_matches = re.findall(r'<[^>]*loc[^>]*>(.*?)</[^>]*loc[^>]*>', sitemap_content)
gita_urls = [u for u in loc_matches if '/gita/' in u]

hub_count = 0
verse_count = 0

for u in gita_urls:
    # https://bhajan.ournakshatra.com/gita/3/1
    # parts: ['', '3', '1']
    path_part = u.split('/gita/')[-1].strip('/')
    if not path_part:
        # Just /gita/
        continue
    segments = path_part.split('/')
    if len(segments) == 1:
        # e.g. chapter-1, 3
        hub_count += 1
    elif len(segments) == 2 and segments[1].isdigit():
        # e.g. 3/1, chapter-1/1
        verse_count += 1

print(f"Total /gita/ URLs in sitemap: {len(gita_urls)}")
print(f"  - Hub pages (e.g. /gita/{{chapter}}): {hub_count}")
print(f"  - Verse pages (e.g. /gita/{{chapter}}/{{verse}}): {verse_count}")

