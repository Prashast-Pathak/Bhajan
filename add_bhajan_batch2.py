import json

with open('data/bhajans.json', 'r') as f:
    data = json.load(f)

for b in data:
    if b['slug'] == 'aarti-kunj-bihari-ki':
        b['reference'] = "Traditional Aarti dedicated to Lord Krishna."
        b['verses'] = [
            {
                "type": "mukhda",
                "label_hindi": "मुखड़ा",
                "label_english": "Refrain",
                "lines": [
                    {
                        "hindi": "आरती कुंजबिहारी की, श्री गिरिधर कृष्णमुरारी की।",
                        "roman": "Aarti Kunj Bihari Ki, Shri Giridhar Krishna Murari Ki.",
                        "hindi_meaning": "कुंजों (बगीचों) में विहार करने वाले श्री कृष्ण की आरती उतारते हैं, जो गोवर्धन पर्वत को धारण करने वाले और मुरारी (मुर नामक राक्षस को मारने वाले) हैं।",
                        "english": "We perform the Aarti of the one who roams the groves (Kunj Bihari), Shri Krishna, the holder of the Govardhan mountain and the enemy of the demon Mura."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 1",
                "label_english": "Verse 1",
                "lines": [
                    {
                        "hindi": "गले में बैजंती माला, बजावै मुरली मधुर बाला।",
                        "roman": "Gale Mein Baijanti Mala, Bajave Murli Madhur Bala.",
                        "hindi_meaning": "जिनके गले में वैजयंती फूलों की माला है, और जो मधुर बांसुरी बजाते हैं।",
                        "english": "Wearing a garland of Vaijayanti flowers around His neck, the beautiful boy plays a sweet flute."
                    },
                    {
                        "hindi": "श्रवण में कुण्डल झलकाला, नंद के आनंद नंदलाला।",
                        "roman": "Shravan Mein Kundal Jhalkala, Nand Ke Anand Nandlala.",
                        "hindi_meaning": "जिनके कानों में कुंडल झिलमिला रहे हैं, वे नंद बाबा को आनंद देने वाले नंदलाल हैं।",
                        "english": "Earrings sparkle in His ears, He is the beloved son of Nanda who brings him joy."
                    }
                ]
            }
        ]

    elif b['slug'] == 'om-jai-lakshmi-mata':
        b['reference'] = "Traditional Aarti for Goddess Lakshmi, sung on Diwali and Fridays."
        b['verses'] = [
            {
                "type": "mukhda",
                "label_hindi": "मुखड़ा",
                "label_english": "Refrain",
                "lines": [
                    {
                        "hindi": "ॐ जय लक्ष्मी माता, मैया जय लक्ष्मी माता।",
                        "roman": "Om Jai Lakshmi Mata, Maiya Jai Lakshmi Mata.",
                        "hindi_meaning": "हे माता लक्ष्मी, आपकी जय हो!",
                        "english": "Om, Victory to Mother Lakshmi, Victory to You!"
                    },
                    {
                        "hindi": "तुमको निशिदिन सेवत, हरि विष्णु विधाता॥",
                        "roman": "Tumko Nishidin Sevat, Hari Vishnu Vidhata.",
                        "hindi_meaning": "भगवान विष्णु और विधाता (ब्रह्मा) रात-दिन आपकी सेवा (ध्यान) करते हैं।",
                        "english": "Lord Vishnu and Brahma meditate upon You day and night."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 1",
                "label_english": "Verse 1",
                "lines": [
                    {
                        "hindi": "उमा रमा ब्रह्माणी, तुम ही जग माता।",
                        "roman": "Uma Rama Brahmani, Tum Hi Jag Mata.",
                        "hindi_meaning": "आप ही उमा (पार्वती), रमा (लक्ष्मी), और ब्रह्माणी (सरस्वती) हैं। आप ही पूरे जगत की माता हैं।",
                        "english": "You are Uma, Rama, and Brahmani. You alone are the Mother of the Universe."
                    },
                    {
                        "hindi": "सूर्य चन्द्रमा ध्यावत, नारद ऋषि गाता॥",
                        "roman": "Surya Chandrama Dhyavat, Narad Rishi Gata.",
                        "hindi_meaning": "सूर्य और चंद्रमा आपका ध्यान करते हैं, और नारद मुनि आपका गुणगान करते हैं।",
                        "english": "The Sun and Moon meditate on You, and Sage Narada sings Your praises."
                    }
                ]
            }
        ]

    elif b['slug'] == 'raghupati-raghav-raja-ram':
        b['reference'] = "Traditional Ram Dhun popularized by Mahatma Gandhi."
        b['verses'] = [
            {
                "type": "mukhda",
                "label_hindi": "मुखड़ा",
                "label_english": "Refrain",
                "lines": [
                    {
                        "hindi": "रघुपति राघव राजाराम, पतित पावन सीताराम।",
                        "roman": "Raghupati Raghav Raja Ram, Patit Pavan Sita Ram.",
                        "hindi_meaning": "रघुवंश के राजा श्री राम की जय हो, जो माता सीता के साथ मिलकर पापियों को भी पवित्र कर देते हैं।",
                        "english": "Glory to King Rama of the Raghu dynasty, the uplifter of the fallen, along with Mother Sita."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा",
                "label_english": "Verse",
                "lines": [
                    {
                        "hindi": "ईश्वर अल्लाह तेरो नाम, सबको सन्मति दे भगवान।",
                        "roman": "Ishwar Allah Tero Naam, Sabko Sanmati De Bhagwan.",
                        "hindi_meaning": "ईश्वर और अल्लाह दोनों आपके ही नाम हैं। हे भगवान, सब को सद्बुद्धि प्रदान करें।",
                        "english": "Ishwar and Allah are both Your names. O Lord, grant pure wisdom to everyone."
                    }
                ]
            }
        ]

    elif b['slug'] == 'mere-ghar-ram-aayo':
        b['reference'] = "Popular modern devotional song celebrating the arrival of Lord Rama."
        b['verses'] = [
            {
                "type": "mukhda",
                "label_hindi": "मुखड़ा",
                "label_english": "Refrain",
                "lines": [
                    {
                        "hindi": "मेरी चौखट पे चल के आज चारो धाम आए हैं,",
                        "roman": "Meri Chaukhat Pe Chal Ke Aaj Charo Dham Aaye Hain,",
                        "hindi_meaning": "आज मेरे दरवाज़े पर चलकर मानो चारों धाम (तीर्थ) आ गए हैं,",
                        "english": "Today, it feels as if the four holy pilgrimage sites have walked to my doorstep,"
                    },
                    {
                        "hindi": "बजाओ ढोल स्वागत में मेरे घर राम आए हैं।",
                        "roman": "Bajao Dhol Swagat Mein Mere Ghar Ram Aaye Hain.",
                        "hindi_meaning": "उनके स्वागत में ढोल बजाओ, क्योंकि मेरे घर श्री राम आए हैं।",
                        "english": "Play the drums in welcome, for Lord Rama has come to my home."
                    }
                ]
            }
        ]

with open('data/bhajans.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Batch 2 complete.")
