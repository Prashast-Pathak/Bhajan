import json

new_verses = [
    {
        "type": "antara",
        "label_hindi": "अंतरा ९",
        "label_english": "Verse 9",
        "lines": [
            {
                "hindi": "तुम ही जग की माता, तुम ही हो भरता।",
                "roman": "Tum hi jag ki mata, Tum hi ho bharta.",
                "hindi_meaning": "आप ही इस पूरे संसार की माता हैं और आप ही सबका भरण-पोषण करने वाली हैं।",
                "english": "You alone are the mother of the universe, and You alone are the sustainer."
            },
            {
                "hindi": "भक्तन की दुःख हरता, सुख-सम्पत्ति करता॥",
                "roman": "Bhaktan ki dukh harta, Sukh sampatti karta.",
                "hindi_meaning": "आप भक्तों के दुखों को हरने वाली और सुख-सम्पत्ति प्रदान करने वाली हैं।",
                "english": "You remove the sorrows of Your devotees and bestow happiness and wealth."
            }
        ]
    },
    {
        "type": "antara",
        "label_hindi": "अंतरा १०",
        "label_english": "Verse 10",
        "lines": [
            {
                "hindi": "भुजा चार अति शोभित, वरमुद्रा धारी।",
                "roman": "Bhuja char ati shobhit, Varmudra dhari.",
                "hindi_meaning": "आपकी चार भुजाएँ अत्यंत सुशोभित हैं और आप वरदान देने की मुद्रा (वरमुद्रा) धारण किए हुए हैं।",
                "english": "Your four arms look extremely beautiful, adorned in the boon-giving posture (Varmudra)."
            },
            {
                "hindi": "मनवांछित फल पावत, सेवत नर-नारी॥",
                "roman": "Manvanchhit phal pavat, Sevat nar-nari.",
                "hindi_meaning": "जो भी नर-नारी आपकी सेवा करते हैं, वे मनचाहा फल प्राप्त करते हैं।",
                "english": "Men and women who serve You obtain the fruits of their desired wishes."
            }
        ]
    },
    {
        "type": "antara",
        "label_hindi": "अंतरा ११",
        "label_english": "Verse 11",
        "lines": [
            {
                "hindi": "कंचन थाल विराजत, अगर कपूर बाती।",
                "roman": "Kanchan thaal birajat, Agar kapoor baati.",
                "hindi_meaning": "सोने की थाली में अगरबत्ती और कपूर की बाती सजी हुई है।",
                "english": "In a golden plate, incense and camphor wicks are elegantly arranged."
            },
            {
                "hindi": "श्रीमालकेतु में राजत, कोटि रतन ज्योति॥",
                "roman": "Shrimalketu mein rajat, Koti ratan jyoti.",
                "hindi_meaning": "आपके भाल पर करोड़ों रत्नों के समान प्रकाशमान ज्योति सुशोभित है।",
                "english": "On Your forehead shines a light radiant like millions of jewels."
            }
        ]
    }
]

with open('data/bhajans.json', 'r') as f:
    data = json.load(f)

for b in data:
    if b['slug'] == 'jai-ambe-gauri':
        # Currently 10 verses. We want to insert 3 new verses before the last one.
        if len(b['verses']) == 10:
            last_verse = b['verses'].pop()
            b['verses'].extend(new_verses)
            b['verses'].append(last_verse)
            
            # Update labels for all verses
            for i in range(1, len(b['verses'])):
                b['verses'][i]['label_hindi'] = f"अंतरा {i}"
                b['verses'][i]['label_english'] = f"Verse {i}"

with open('data/bhajans.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Added 3 missing verses to Jai Ambe Gauri!")
