import re
import json

with open('/Users/prashastpathak/Bhajan/scratch/allcontent', 'r', encoding='utf-8') as f:
    content = f.read()

content_fixed = re.sub(r'("meaning_english"\s*:\s*"[^"]*")\s*\]', r'\1}', content)

idx = content_fixed.find("chapter-3-verse-1")
start_idx = content_fixed.rfind("[", 0, idx)
decoder = json.JSONDecoder()
obj, end = decoder.raw_decode(content_fixed[start_idx:])
verses = [v['verse'] for v in obj]
print(verses)
