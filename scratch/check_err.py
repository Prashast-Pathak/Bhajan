import re
import json

with open('/Users/prashastpathak/Bhajan/scratch/allcontent', 'r', encoding='utf-8') as f:
    content = f.read()

content_fixed = re.sub(r'("meaning_english"\s*:\s*"[^"]*")\s*\]', r'\1}', content)

start_idx = 464771
decoder = json.JSONDecoder()
try:
    obj, end = decoder.raw_decode(content_fixed[start_idx:])
except json.JSONDecodeError as e:
    err_idx = start_idx + e.pos
    print(repr(content_fixed[err_idx-50:err_idx+50]))

