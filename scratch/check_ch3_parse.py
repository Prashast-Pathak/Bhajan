import re
import json

with open('/Users/prashastpathak/Bhajan/scratch/allcontent', 'r', encoding='utf-8') as f:
    content = f.read()

content_fixed = re.sub(r'("meaning_english"\s*:\s*"[^"]*")\s*\]', r'\1}', content)

idx = content_fixed.find("chapter-3-verse-21")
if idx != -1:
    start_idx = content_fixed.rfind("[", 0, idx)
    decoder = json.JSONDecoder()
    try:
        obj, end = decoder.raw_decode(content_fixed[start_idx:])
        print("Success!")
    except json.JSONDecodeError as e:
        print(f"Error at {start_idx}: {e}")
        err_idx = start_idx + e.pos
        print(repr(content_fixed[err_idx-50:err_idx+50]))

