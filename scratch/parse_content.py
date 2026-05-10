import re
import json

with open('/Users/prashastpathak/Bhajan/scratch/allcontent', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the specific JSON syntax error: "meaning_english": "..." ] -> }
content_fixed = re.sub(r'("meaning_english":\s*"[^"]*")\s*\]', r'\1}', content)

blocks = []
decoder = json.JSONDecoder()
pos = 0
while pos < len(content_fixed):
    match = re.search(r'\[\s*\{', content_fixed[pos:])
    if not match:
        break
    start = pos + match.start()
    try:
        obj, end = decoder.raw_decode(content_fixed[start:])
        blocks.append(obj)
        pos = start + end
    except json.JSONDecodeError as e:
        print(f"Error at {start}: {e}")
        # Move forward a bit to avoid infinite loop
        pos = start + 1

print(f"Found {len(blocks)} JSON arrays.")
all_verses = []
for i, block in enumerate(blocks):
    if isinstance(block, list) and len(block) > 0 and 'verse' in block[0]:
        all_verses.extend(block)
        ch_set = set(v.get('chapter') for v in block if 'chapter' in v)
        print(f"Block {i}: Extracted {len(block)} verses. Chapters: {ch_set}")

print(f"Total verses extracted: {len(all_verses)}")

# Group verses by chapter to see if we have 3,4,5,6,7 completely
from collections import defaultdict
ch_verses = defaultdict(list)
for v in all_verses:
    if 'chapter' in v:
        ch_verses[v['chapter']].append(v)

for ch, v_list in sorted(ch_verses.items()):
    print(f"Chapter {ch}: {len(v_list)} verses")
