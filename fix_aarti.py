import json

with open('data/bhajans.json', 'r') as f:
    data = json.load(f)

for b in data:
    if b['slug'] == 'aarti-kunj-bihari-ki':
        b['verses'].append({
            "type": "antara",
            "label_hindi": "अंतरा 4",
            "label_english": "Verse 4",
            "lines": [
                {
                    "hindi": "चमकती उज्ज्वल तट रेनु, बज रही वृंदावन बेनु।",
                    "roman": "Chamkati ujjwal tat renu, baj rahi Vrindavan benu",
                    "hindi_meaning": "यमुना के तट की रेत उज्ज्वल चमक रही है, और वृंदावन में बांसुरी बज रही है।",
                    "english": "The sand on the banks shines brightly, and the flute is playing in Vrindavan."
                },
                {
                    "hindi": "चहुं दिसि गोपि ग्वाल धेनु, हंसत मृदु मंद चांदनी चंद।",
                    "roman": "Chahun disi gopi gwaal dhenu, hansat mridu mand chandani chand",
                    "hindi_meaning": "चारों दिशाओं में गोपियाँ, ग्वाले और गाएं हैं, और चाँद अपनी मंद-मंद चांदनी बिखेरता हुआ मुस्कुरा रहा है।",
                    "english": "In all directions are Gopis, cowherds, and cows, while the moon smiles with its soft, gentle moonlight."
                }
            ]
        })

with open('data/bhajans.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
