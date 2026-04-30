import os
import json

files = ["data/gita.json", "data/wisdom.json", "data/prayers.json"]

for f in files:
    with open(f, 'r') as file:
        content = file.read()
    
    # Specific Bija Mantras
    content = content.replace("ॐ [mantra fragment removed for safety] कृष्णाय नमः", "ॐ क्लीं कृष्णाय नमः")
    content = content.replace("Om [mantra fragment removed for safety] Krishnaya Namah", "Om Kleem Krishnaya Namah")
    content = content.replace("ॐ ह्रां [mantra fragment removed for safety] ह्रौं सः सूर्याय नमः", "ॐ ह्रां ह्रीं ह्रौं सः सूर्याय नमः")
    content = content.replace("Om Hraam [mantra fragment removed for safety] Hraum Sah Suryaya Namah", "Om Hraam Hreem Hraum Sah Suryaya Namah")
    
    # All remaining ones are the Hindi word "हूँ" (am)
    content = content.replace("[mantra fragment removed for safety]", "हूँ")
    
    with open(f, 'w') as file:
        file.write(content)

print("Fixed mantras")
