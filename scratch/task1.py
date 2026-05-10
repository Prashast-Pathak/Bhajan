import re
import json

with open('/Users/prashastpathak/Bhajan/scratch/allcontent', 'r', encoding='utf-8') as f:
    content = f.read()

content_fixed = re.sub(r'("meaning_english"\s*:\s*"[^"]*")\s*\]', r'\1}', content)

all_verses = []
decoder = json.JSONDecoder()
pos = 0
while pos < len(content_fixed):
    match = re.search(r'\[\s*\{', content_fixed[pos:])
    if not match:
        break
    start = pos + match.start()
    try:
        obj, end = decoder.raw_decode(content_fixed[start:])
        if isinstance(obj, list) and len(obj) > 0 and 'verse' in obj[0]:
            all_verses.extend(obj)
        pos = start + end
    except json.JSONDecodeError as e:
        pos = start + 1

print(f"Total verses extracted: {len(all_verses)}")
if len(all_verses) > 0:
    print(f"First verse keys: {all_verses[0].keys()}")
    print(f"First verse slug: {all_verses[0].get('slug')}")
    print(f"Last verse slug: {all_verses[-1].get('slug')}")
