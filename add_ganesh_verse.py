import json

new_verse = {
  "type": "antara",
  "label_hindi": "अंतरा ५",
  "label_english": "Verse 5",
  "lines": [
    {
      "hindi": "दीनन की लाज राखो शम्भु सुत वारी।",
      "roman": "Deenan ki laaj rakho, Shambhu sut vari,",
      "hindi_meaning": "हे शिव पुत्र (शम्भू सुत), दीनों और असहायों की लाज रखिए,",
      "english": "Protect the honor of the poor and helpless, O Son of Shiva,"
    },
    {
      "hindi": "कामना को पूर्ण करो जग बलिहारी॥",
      "roman": "Kaamna ko purna karo jag balihari.",
      "hindi_meaning": "संसार की सभी इच्छाओं को पूर्ण करें, सारा जग आप पर बलिहारी है।",
      "english": "Fulfill the desires of everyone, the whole world is devoted to You."
    }
  ]
}

with open('data/bhajans.json', 'r') as f:
    data = json.load(f)

for b in data:
    if b['slug'] == 'jai-ganesh-deva':
        # Check if it already has verse 5
        if len(b['verses']) < 6:
            # Insert before the last verse if the last verse is the 'Sur shyam' concluding verse?
            # Usually 'Sur shyam sharan aaye' is the concluding line, so 'Deenan ki laaj rakho' goes before it.
            # Let's insert it at index 4 (before the last one).
            b['verses'].insert(4, new_verse)
            # update labels
            for i in range(1, len(b['verses'])):
                b['verses'][i]['label_hindi'] = f"अंतरा {i}"
                b['verses'][i]['label_english'] = f"Verse {i}"

with open('data/bhajans.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Added 'Deenan ki laaj rakho' to Jai Ganesh Deva!")
