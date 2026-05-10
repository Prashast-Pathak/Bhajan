import json
import re

log_path = "/Users/prashastpathak/.gemini/antigravity/brain/865d08c2-3df2-4595-946b-c0b53a5e37c5/.system_generated/logs/overview.txt"
contents = []
with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            entry = json.loads(line)
            if entry.get("source") == "MODEL" and "content" in entry:
                contents.append(entry["content"])
        except Exception as e:
            pass

full_text = "\n".join(contents)
matches = re.findall(r'```json\n(.*?)\n```', full_text, re.DOTALL)
print(f"Match 1 snippet:\n{matches[1][:500]}")

