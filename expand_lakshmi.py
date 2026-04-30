import json

with open('data/bhajans.json', 'r') as f:
    data = json.load(f)

for b in data:
    if b['slug'] == 'om-jai-lakshmi-mata':
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
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 2",
                "label_english": "Verse 2",
                "lines": [
                    {
                        "hindi": "दुर्गा रूप निरंजनी, सुख सम्पत्ति दाता।",
                        "roman": "Durga Roop Niranjani, Sukh Sampatti Data.",
                        "hindi_meaning": "आप ही दुर्गा का निरंजन रूप हैं, और आप ही सुख तथा संपत्ति प्रदान करने वाली हैं।",
                        "english": "You are the pure form of Goddess Durga, the giver of happiness and wealth."
                    },
                    {
                        "hindi": "जो कोई तुमको ध्यावत, ऋद्धि-सिद्धि धन पाता॥",
                        "roman": "Jo Koi Tumko Dhyavat, Riddhi-Siddhi Dhan Pata.",
                        "hindi_meaning": "जो कोई भी आपका ध्यान करता है, वह ऋद्धि (समृद्धि), सिद्धि (सफलता) और धन प्राप्त करता है।",
                        "english": "Whoever meditates on You attains prosperity, success, and wealth."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 3",
                "label_english": "Verse 3",
                "lines": [
                    {
                        "hindi": "तुम पाताल निवासिनि, तुम ही शुभदाता।",
                        "roman": "Tum Patal Nivasini, Tum Hi Shubhdata.",
                        "hindi_meaning": "आप ही पाताल में निवास करने वाली हैं और आप ही शुभ फल देने वाली हैं।",
                        "english": "You reside in the netherworld, and You alone are the bestower of auspiciousness."
                    },
                    {
                        "hindi": "कर्म प्रभाव प्रकाशिनि, भवनिधि की त्राता॥",
                        "roman": "Karma Prabhav Prakashini, Bhavnidhi Ki Trata.",
                        "hindi_meaning": "आप कर्मों के प्रभाव को प्रकाशित करने वाली हैं और भवसागर (संसार) से तारने वाली हैं।",
                        "english": "You illuminate the effects of our actions and save us from the ocean of worldly existence."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 4",
                "label_english": "Verse 4",
                "lines": [
                    {
                        "hindi": "जिस घर में तुम रहतीं, सब सद्गुण आता।",
                        "roman": "Jis Ghar Mein Tum Rahti, Sab Sadgun Aata.",
                        "hindi_meaning": "जिस घर में आपका वास होता है, वहाँ सभी सद्गुण स्वतः आ जाते हैं।",
                        "english": "In the house where You reside, all good virtues naturally enter."
                    },
                    {
                        "hindi": "सब सम्भव हो जाता, मन नहीं घबराता॥",
                        "roman": "Sab Sambhav Ho Jata, Man Nahi Ghabrata.",
                        "hindi_meaning": "सब कुछ संभव हो जाता है और मन कभी भयभीत या चिंतित नहीं होता।",
                        "english": "Everything becomes possible, and the mind never worries."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 5",
                "label_english": "Verse 5",
                "lines": [
                    {
                        "hindi": "तुम बिन यज्ञ न होते, वस्त्र न कोई पाता।",
                        "roman": "Tum Bin Yagya Na Hote, Vastra Na Koi Pata.",
                        "hindi_meaning": "आपके बिना कोई यज्ञ (शुभ कार्य) संपन्न नहीं हो सकता, और किसी को वस्त्र आदि प्राप्त नहीं होते।",
                        "english": "Without You, no auspicious rituals can be completed, and none can acquire clothing or comforts."
                    },
                    {
                        "hindi": "खान-पान का वैभव, सब तुमसे आता॥",
                        "roman": "Khan-Pan Ka Vaibhav, Sab Tumse Aata.",
                        "hindi_meaning": "खान-पान और जीवन का सारा वैभव आप ही की कृपा से आता है।",
                        "english": "The luxury of food, drink, and a good life all come from Your grace."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 6",
                "label_english": "Verse 6",
                "lines": [
                    {
                        "hindi": "शुभ-गुण मंदिर सुन्दर, क्षीरोदधि-जाता।",
                        "roman": "Shubh-Gun Mandir Sundar, Kshirodadhi-Jata.",
                        "hindi_meaning": "आप शुभ गुणों का सुंदर मंदिर हैं, और क्षीर सागर (दूध के समुद्र) से प्रकट हुई हैं।",
                        "english": "You are the beautiful temple of auspicious virtues, born from the Ocean of Milk."
                    },
                    {
                        "hindi": "रत्न चतुर्दश तुम बिन, कोई नहीं पाता॥",
                        "roman": "Ratna Chaturdash Tum Bin, Koi Nahi Pata.",
                        "hindi_meaning": "समुद्र मंथन के चौदह रत्न आपके बिना कोई प्राप्त नहीं कर सकता था।",
                        "english": "Without You, no one could have attained the fourteen jewels from the ocean churning."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 7",
                "label_english": "Verse 7",
                "lines": [
                    {
                        "hindi": "महालक्ष्मीजी की आरती, जो कोई नर गाता।",
                        "roman": "Mahalakshmiji Ki Aarti, Jo Koi Nar Gata.",
                        "hindi_meaning": "महालक्ष्मी जी की इस आरती को जो कोई भी मनुष्य गाता है,",
                        "english": "Whoever sings this Aarti of Goddess Mahalakshmi,"
                    },
                    {
                        "hindi": "उर आनन्द समाता, पाप उतर जाता॥",
                        "roman": "Ur Anand Samata, Paap Utar Jata.",
                        "hindi_meaning": "उसके हृदय में अपार आनंद भर जाता है और उसके सारे पाप नष्ट हो जाते हैं।",
                        "english": "Their heart is filled with immense joy, and all their sins are washed away."
                    }
                ]
            }
        ]

with open('data/bhajans.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Expanded Lakshmi Aarti.")
