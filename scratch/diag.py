import os
import json
import xml.etree.ElementTree as ET
import glob

base_dir = '/Users/prashastpathak/Bhajan'
gita_dir = os.path.join(base_dir, 'gita')
json_path = os.path.join(base_dir, 'data', 'gita.json')
sitemap_path = os.path.join(base_dir, 'sitemap.xml')

# 1. List chapter-level directories and index.html presence
print("1. Chapter-level directories under /gita/:")
chapter_dirs = []
if os.path.exists(gita_dir):
    for entry in sorted(os.listdir(gita_dir)):
        full_path = os.path.join(gita_dir, entry)
        if os.path.isdir(full_path):
            has_index = os.path.exists(os.path.join(full_path, 'index.html'))
            print(f"   - /gita/{entry}/ (index.html: {'Yes' if has_index else 'No'})")
            if entry.isdigit():
                chapter_dirs.append(entry)

print("\n2 & 3. Cross-check JSON vs Disk:")
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

json_chapters = {str(c['chapter']): len(c.get('verses', [])) for c in data.get('chapters', [])}

for ch_num in range(1, 8):
    ch_str = str(ch_num)
    json_count = json_chapters.get(ch_str, 0)
    
    # Count disk verse directories
    disk_count = 0
    ch_dir = os.path.join(gita_dir, ch_str)
    if os.path.exists(ch_dir):
        for entry in os.listdir(ch_dir):
            if os.path.isdir(os.path.join(ch_dir, entry)) and entry.isdigit():
                disk_count += 1
                
    gap = json_count - disk_count
    print(f"Chapter {ch_str}: JSON={json_count} | Disk={disk_count} | Gap={gap}")

print("\n4. Sitemap URLs containing /gita/:")
try:
    tree = ET.parse(sitemap_path)
    root = tree.getroot()
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    urls = [url.find('ns:loc', namespace).text for url in root.findall('ns:url', namespace)]
    
    gita_urls = [u for u in urls if '/gita/' in u]
    
    hub_count = 0
    verse_count = 0
    
    for u in gita_urls:
        parts = u.rstrip('/').split('/gita/')
        if len(parts) > 1:
            path = parts[1]
            segments = path.split('/')
            if len(segments) == 1:
                hub_count += 1
            elif len(segments) == 2 and segments[1].isdigit():
                verse_count += 1
            else:
                pass # Other variants
                
    print(f"Total /gita/ URLs: {len(gita_urls)}")
    print(f"  - Hub pages (e.g. /gita/{{n}}): {hub_count}")
    print(f"  - Verse pages (e.g. /gita/{{n}}/{{v}}): {verse_count}")
except Exception as e:
    print(f"Error parsing sitemap: {e}")
