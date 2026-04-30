import json

with open('data/bhajans.json', 'r') as f:
    data = json.load(f)

for b in data:
    if b['slug'] == 'achyutam-keshavam':
        b['reference'] = "Traditional Krishna Bhajan popularized by Sri Adi Shankaracharya's Achyutashtakam."
        b['verses'] = [
            {
                "type": "mukhda",
                "label_hindi": "मुखड़ा",
                "label_english": "Refrain",
                "lines": [
                    {
                        "hindi": "अच्युतं केशवं कृष्ण दामोदरं,",
                        "roman": "Achyutam Keshavam Krishna Damodaram,",
                        "hindi_meaning": "हे अच्युत (जो कभी नष्ट नहीं होते), हे केशव (जिनके सुंदर बाल हैं), हे कृष्ण, हे दामोदर,",
                        "english": "O Infallible One, O Keshav, O Krishna, O Damodara,"
                    },
                    {
                        "hindi": "राम नारायणं जानकी वल्लभम्॥",
                        "roman": "Rama Narayanam Janaki Vallabham.",
                        "hindi_meaning": "हे राम, हे नारायण, हे जानकी (सीता) के प्रिय।",
                        "english": "O Rama, O Narayana, O Beloved of Janaki (Sita)."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 1",
                "label_english": "Verse 1",
                "lines": [
                    {
                        "hindi": "कौन कहते है भगवान आते नहीं,",
                        "roman": "Kaun Kehte Hai Bhagwan Aate Nahi,",
                        "hindi_meaning": "कौन कहता है कि भगवान नहीं आते?",
                        "english": "Who says that God does not come?"
                    },
                    {
                        "hindi": "तुम मीरा के जैसे बुलाते नहीं॥",
                        "roman": "Tum Meera Ke Jaise Bulate Nahi.",
                        "hindi_meaning": "तुम उन्हें मीरा की तरह पुकारते नहीं हो।",
                        "english": "You just do not call Him with the devotion of Meera."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 2",
                "label_english": "Verse 2",
                "lines": [
                    {
                        "hindi": "कौन कहते है भगवान खाते नहीं,",
                        "roman": "Kaun Kehte Hai Bhagwan Khate Nahi,",
                        "hindi_meaning": "कौन कहता है कि भगवान कुछ खाते नहीं?",
                        "english": "Who says that God does not eat?"
                    },
                    {
                        "hindi": "बेर शबरी के जैसे खिलाते नहीं॥",
                        "roman": "Ber Shabari Ke Jaise Khilate Nahi.",
                        "hindi_meaning": "तुम उन्हें शबरी की तरह प्रेम से बेर खिलाते नहीं हो।",
                        "english": "You just do not feed Him berries with the love of Shabari."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 3",
                "label_english": "Verse 3",
                "lines": [
                    {
                        "hindi": "कौन कहते है भगवान सोते नहीं,",
                        "roman": "Kaun Kehte Hai Bhagwan Sote Nahi,",
                        "hindi_meaning": "कौन कहता है कि भगवान सोते नहीं?",
                        "english": "Who says that God does not sleep?"
                    },
                    {
                        "hindi": "माँ यशोदा के जैसे सुलाते नहीं॥",
                        "roman": "Maa Yashoda Ke Jaise Sulate Nahi.",
                        "hindi_meaning": "तुम उन्हें माता यशोदा की तरह लोरी गाकर सुलाते नहीं हो।",
                        "english": "You just do not put Him to sleep with the affection of Mother Yashoda."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 4",
                "label_english": "Verse 4",
                "lines": [
                    {
                        "hindi": "कौन कहते है भगवान नाचते नहीं,",
                        "roman": "Kaun Kehte Hai Bhagwan Nachte Nahi,",
                        "hindi_meaning": "कौन कहता है कि भगवान नाचते नहीं?",
                        "english": "Who says that God does not dance?"
                    },
                    {
                        "hindi": "गोपियों की तरह तुम नचाते नहीं॥",
                        "roman": "Gopiyo Ki Tarah Tum Nachate Nahi.",
                        "hindi_meaning": "तुम उन्हें गोपियों की तरह प्रेम के वशीभूत होकर नचाते नहीं हो।",
                        "english": "You just do not make Him dance with the pure love of the Gopis."
                    }
                ]
            }
        ]

with open('data/bhajans.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Added Achyutam Keshavam")
