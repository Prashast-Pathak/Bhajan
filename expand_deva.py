import json

with open('data/bhajans.json', 'r') as f:
    data = json.load(f)

for b in data:
    if b['slug'] == 'deva-shree-ganesha':
        b['verses'] = [
            {
                "type": "mukhda",
                "label_hindi": "मुखड़ा",
                "label_english": "Refrain",
                "lines": [
                    {
                        "hindi": "देवा श्री गणेशा, देवा श्री गणेशा।",
                        "roman": "Deva Shree Ganesha, Deva Shree Ganesha.",
                        "hindi_meaning": "हे देवों के देव, श्री गणेश!",
                        "english": "O Lord Shree Ganesha!"
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 1",
                "label_english": "Verse 1",
                "lines": [
                    {
                        "hindi": "ज्वाला सी जलती है आँखों में जिसके भी दिल में तेरा नाम है।",
                        "roman": "Jwala si jalti hai aankhon mein jiske bhi dil mein tera naam hai.",
                        "hindi_meaning": "जिसके दिल में आपका नाम होता है, उसकी आँखों में एक दिव्य ज्वाला चमकती है।",
                        "english": "A divine flame burns in the eyes of the one who holds Your name in their heart."
                    },
                    {
                        "hindi": "परवाह ही क्या उसका आरंभ कैसा है और कैसा परिणाम है।",
                        "roman": "Parwah hi kya uska aarambh kaisa hai aur kaisa parinaam hai.",
                        "hindi_meaning": "उसे इस बात की कोई चिंता नहीं होती कि शुरुआत कैसी है और अंत क्या होगा।",
                        "english": "They care not about how things begin or what the outcome will be."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 2",
                "label_english": "Verse 2",
                "lines": [
                    {
                        "hindi": "धरती अंबर सितारे, उसकी नज़रे उतारें।",
                        "roman": "Dharti ambar sitare, uski nazare utaare.",
                        "hindi_meaning": "धरती, आकाश और सितारे भी उसकी नज़र उतारते हैं (उसकी रक्षा करते हैं)।",
                        "english": "The earth, the sky, and the stars protect and adore them."
                    },
                    {
                        "hindi": "डर भी उससे डरा रे, जिसकी रखवाली रे, करता साया तेरा।",
                        "roman": "Darr bhi usse dara re, jiski rakhwali re, karta saaya tera.",
                        "hindi_meaning": "डर भी उससे डरता है, जिसकी रक्षा आपकी छत्रछाया करती है।",
                        "english": "Even fear is afraid of the one who is protected by Your shadow."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 3",
                "label_english": "Verse 3",
                "lines": [
                    {
                        "hindi": "तेरी भक्ति तो वरदान है, जो कमाए वो धनवान है।",
                        "roman": "Teri bhakti to vardaan hai, jo kamaaye wo dhanwaan hai.",
                        "hindi_meaning": "आपकी भक्ति एक वरदान है, जो इसे कमा लेता है वह सच्चा धनवान है।",
                        "english": "Your devotion is a boon; whoever earns it is truly wealthy."
                    },
                    {
                        "hindi": "बिन किनारे की कश्ती है वो, देवा तुझसे जो अंजान है।",
                        "roman": "Bin kinaare ki kashti hai wo, Deva tujhse jo anjaan hai.",
                        "hindi_meaning": "जो इंसान आपसे अनजान है, उसका जीवन उस नाव की तरह है जिसका कोई किनारा नहीं।",
                        "english": "One who is unaware of You, O Lord, is like a boat without a shore."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 4",
                "label_english": "Verse 4",
                "lines": [
                    {
                        "hindi": "वीर को क्या डराए, मौत भी क्या मिटाए।",
                        "roman": "Veer ko kya daraaye, maut bhi kya mitaaye.",
                        "hindi_meaning": "सच्चे वीर को कौन डरा सकता है? मौत भी उसे कैसे मिटा सकती है?",
                        "english": "What can frighten a true warrior? Even death cannot erase them."
                    },
                    {
                        "hindi": "जो तेरे काम आए, उसकी तो शान है।",
                        "roman": "Jo tere kaam aaye, uski to shaan hai.",
                        "hindi_meaning": "जो आपके काम आता है (आपकी भक्ति करता है), उसकी तो अलग ही शान होती है।",
                        "english": "The one who serves You has a unique and supreme glory."
                    }
                ]
            }
        ]

with open('data/bhajans.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Expanded Deva Shree Ganesha fully.")
