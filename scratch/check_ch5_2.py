import re
import json

with open('/Users/prashastpathak/Bhajan/scratch/allcontent', 'r', encoding='utf-8') as f:
    content = f.read()

content_fixed = re.sub(r'("meaning_english"\s*:\s*"[^"]*")\s*\]', r'\1}', content)

idx = content_fixed.find("chapter-5-verse-21")
if idx != -1:
    # find the opening bracket before this
    start_idx = content_fixed.rfind("[", 0, idx)
    # try to decode from start_idx
    decoder = json.JSONDecoder()
    try:
        obj, end = decoder.raw_decode(content_fixed[start_idx:])
        print("Success")
    except json.JSONDecodeError as e:
        print(f"Error parsing at {start_idx}: {e}")
        # Let's print the specific location
        err_idx = start_idx + e.pos
        print("Context around error:")
        print(content_fixed[max(0, err_idx-100):min(len(content_fixed), err_idx+100)])

