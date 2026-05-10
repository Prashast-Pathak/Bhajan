import re
import json

with open('/Users/prashastpathak/Bhajan/scratch/allcontent_fixed', 'r', encoding='utf-8') as f:
    content_fixed = f.read()

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

from collections import defaultdict
ch_verses = defaultdict(list)
for v in all_verses:
    slug = v.get('slug', '')
    m = re.search(r'chapter-(\d+)', slug)
    if m:
        ch = int(m.group(1))
        ch_verses[ch].append(v)

for ch in list(ch_verses.keys()):
    uniq = {}
    for v in ch_verses[ch]:
        uniq[v['verse']] = v
    ch_verses[ch] = [uniq[k] for k in sorted(uniq.keys())]

print("Verses extracted per chapter:")
for ch in sorted(ch_verses.keys()):
    print(f"Chapter {ch}: {len(ch_verses[ch])} verses")
    
