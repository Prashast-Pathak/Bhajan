import json
import os

gita_path = '/Users/prashastpathak/Bhajan/data/gita.json'
ch1_part1_path = '/Users/prashastpathak/Bhajan/scratch/ch1.json'
ch1_part2_path = '/Users/prashastpathak/Bhajan/scratch/ch1_part2.json'

with open(gita_path, 'r', encoding='utf-8') as f:
    gita_data = json.load(f)

with open(ch1_part1_path, 'r', encoding='utf-8') as f:
    ch1_data = json.load(f)

with open(ch1_part2_path, 'r', encoding='utf-8') as f:
    ch1_verses_part2 = json.load(f)

ch1_data['verses'].extend(ch1_verses_part2)

# Verify we have 47 verses
assert len(ch1_data['verses']) == 47, f"Expected 47 verses, got {len(ch1_data['verses'])}"

# Replace or insert into gita.json
chapters = gita_data.get('chapters', [])
found = False
for i, chap in enumerate(chapters):
    if chap.get('chapter') == 1:
        chapters[i] = ch1_data
        found = True
        break

if not found:
    # Find chapter 2 index to insert before it
    insert_idx = 0
    for i, chap in enumerate(chapters):
        if chap.get('chapter') == 2:
            insert_idx = i
            break
    chapters.insert(insert_idx, ch1_data)

gita_data['chapters'] = chapters

with open(gita_path, 'w', encoding='utf-8') as f:
    json.dump(gita_data, f, ensure_ascii=False, indent=2)

print(f"Total chapters in gita.json: {len(gita_data['chapters'])}")
print(f"Chapter 1 verse count: {len(ch1_data['verses'])}")
