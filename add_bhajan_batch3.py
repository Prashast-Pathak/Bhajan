import json

with open('data/bhajans.json', 'r') as f:
    data = json.load(f)

for b in data:
    if b['slug'] == 'vaishnav-jan':
        b['reference'] = "A 15th-century Gujarati bhajan composed by poet Narsinh Mehta."
        b['verses'] = [
            {
                "type": "mukhda",
                "label_hindi": "मुखड़ा",
                "label_english": "Refrain",
                "lines": [
                    {
                        "hindi": "वैष्णव जन तो तेने कहिये जे पीड परायी जाणे रे।",
                        "roman": "Vaishnav Jan To Tene Kahiye Je Peed Parayi Jaane Re.",
                        "hindi_meaning": "सच्चा वैष्णव (भगवान का भक्त) उसी को कहना चाहिए, जो दूसरों की पीड़ा को जानता और समझता है।",
                        "english": "Call those true Vaishnavas (devotees of God) who understand the pain of others."
                    },
                    {
                        "hindi": "पर दुःखे उपकार करे तोये मन अभिमान न आणे रे॥",
                        "roman": "Par Dukhe Upkar Kare Toye Man Abhiman Na Aane Re.",
                        "hindi_meaning": "जो दूसरों के दुखों को दूर करने के लिए उपकार करता है, फिर भी मन में कोई अभिमान नहीं लाता।",
                        "english": "Who help others in their sorrow, yet let no arrogance enter their mind."
                    }
                ]
            }
        ]

    elif b['slug'] == 'shri-ramachandra-kripalu':
        b['reference'] = "Composed by Goswami Tulsidas in Vinay Patrika."
        b['verses'] = [
            {
                "type": "mukhda",
                "label_hindi": "मुखड़ा",
                "label_english": "Refrain",
                "lines": [
                    {
                        "hindi": "श्री रामचन्द्र कृपालु भजु मन हरण भवभय दारुणं।",
                        "roman": "Shri Ramachandra Kripalu Bhaju Man Haran Bhavbhay Darunam.",
                        "hindi_meaning": "हे मन! कृपालु श्री रामचन्द्र जी का भजन कर, जो जन्म-मरण के दारुण (भयानक) भय को हरने वाले हैं।",
                        "english": "O mind! Chant the name of the compassionate Shri Ramachandra, who removes the terrifying fear of the cycle of birth and death."
                    },
                    {
                        "hindi": "नवकंज लोचन कंज मुख कर कंज पद कंजारुणं॥",
                        "roman": "Navkanj Lochan Kanj Mukh Kar Kanj Pad Kanjarunam.",
                        "hindi_meaning": "जिनके नेत्र नए खिले हुए कमल के समान हैं, जिनका मुख और हाथ कमल के समान हैं, और जिनके चरण लाल कमल के समान हैं।",
                        "english": "Whose eyes are like newly blossomed lotuses, whose face and hands are like lotuses, and whose feet are like red lotuses."
                    }
                ]
            }
        ]

    elif b['slug'] == 'madhurashtakam':
        b['reference'] = "Composed by Sri Vallabhacharya, describing the sweetness of Lord Krishna."
        b['verses'] = [
            {
                "type": "stanza",
                "label_hindi": "श्लोक 1",
                "label_english": "Stanza 1",
                "lines": [
                    {
                        "hindi": "अधरं मधुरं वदनं मधुरं,",
                        "roman": "Adharam Madhuram Vadanam Madhuram,",
                        "hindi_meaning": "उनके होंठ मधुर हैं, उनका मुख मधुर है,",
                        "english": "His lips are sweet, His face is sweet,"
                    },
                    {
                        "hindi": "नयनं मधुरं हसितं मधुरम्।",
                        "roman": "Nayanam Madhuram Hasitam Madhuram.",
                        "hindi_meaning": "उनके नेत्र मधुर हैं, उनकी मुस्कान मधुर है।",
                        "english": "His eyes are sweet, His smile is sweet."
                    },
                    {
                        "hindi": "हृदयं मधुरं गमनं मधुरं,",
                        "roman": "Hridayam Madhuram Gamanam Madhuram,",
                        "hindi_meaning": "उनका हृदय मधुर है, उनकी चाल मधुर है,",
                        "english": "His heart is sweet, His walk is sweet,"
                    },
                    {
                        "hindi": "मधुराधिपतेरखिलं मधुरम्॥",
                        "roman": "Madhuradhipater Akhilam Madhuram.",
                        "hindi_meaning": "मधुरता के अधिपति (श्री कृष्ण) का सब कुछ मधुर ही मधुर है।",
                        "english": "Everything about the Lord of Sweetness is absolutely sweet."
                    }
                ]
            }
        ]

with open('data/bhajans.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Batch 3 complete.")
