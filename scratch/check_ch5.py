import re
import json

with open('/Users/prashastpathak/Bhajan/scratch/allcontent', 'r', encoding='utf-8') as f:
    content = f.read()

# Specifically find chapter-5-verse-21
idx = content.find("chapter-5-verse-21")
if idx != -1:
    print("Found chapter-5-verse-21 in content")
    # Let's print the block around it
    print(content[idx-200:idx+300])

