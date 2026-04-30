import json

with open('data/bhajans.json', 'r') as f:
    data = json.load(f)

for b in data:
    if b['slug'] == 'mere-ghar-ram-aayo':
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
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 1",
                "label_english": "Verse 1",
                "lines": [
                    {
                        "hindi": "कथा शबरी की जैसे जुड़ गयी मेरी कहानी से,",
                        "roman": "Katha Shabari Ki Jaise Jud Gayi Meri Kahani Se,",
                        "hindi_meaning": "ऐसा लगता है जैसे माता शबरी की कथा मेरी अपनी कहानी से जुड़ गई है,",
                        "english": "It feels as though the story of Shabari has intertwined with my own story,"
                    },
                    {
                        "hindi": "न रोको आज धोने दो चरण आँखों के पानी से।",
                        "roman": "Na Roko Aaj Dhone Do Charan Aankhon Ke Paani Se.",
                        "hindi_meaning": "मुझे मत रोको, आज मुझे अपने आंसुओं के जल से उनके चरण धोने दो।",
                        "english": "Do not stop me today, let me wash His feet with the tears from my eyes."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 2",
                "label_english": "Verse 2",
                "lines": [
                    {
                        "hindi": "बहुत खुश है मेरे आँसू की प्रभु के काम आए हैं,",
                        "roman": "Bahut Khush Hai Mere Aansu Ki Prabhu Ke Kaam Aaye Hain,",
                        "hindi_meaning": "मेरे आंसू बहुत खुश हैं कि वे भगवान के किसी काम आ सके,",
                        "english": "My tears are overjoyed that they could be of service to the Lord,"
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

    elif b['slug'] == 'vaishnav-jan':
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
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 1",
                "label_english": "Verse 1",
                "lines": [
                    {
                        "hindi": "सकळ लोकमां सहुने वंदे, निंदा न करे केनी रे।",
                        "roman": "Sakal Lokma Sahune Vande, Ninda Na Kare Keni Re.",
                        "hindi_meaning": "वह पूरी दुनिया में सभी का सम्मान करता है और किसी की भी निंदा (बुराई) नहीं करता।",
                        "english": "He respects everyone in the entire world and does not speak ill of anyone."
                    },
                    {
                        "hindi": "वाच काछ मन निश्चळ राखे धन धन जननी तेनी रे॥",
                        "roman": "Vaach Kaachh Man Nishchal Rakhe, Dhan Dhan Janani Teni Re.",
                        "hindi_meaning": "जो अपने वचन, कर्म और मन को स्थिर और पवित्र रखता है, उस भक्त को जन्म देने वाली माता धन्य है।",
                        "english": "One who keeps his speech, actions, and mind pure and steady—blessed is the mother who bore him."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 2",
                "label_english": "Verse 2",
                "lines": [
                    {
                        "hindi": "समदृष्टि ने तृष्णा त्यागी परस्त्री जेने मात रे।",
                        "roman": "Samadrishti Ne Trishna Tyagi, Parastree Jene Maat Re.",
                        "hindi_meaning": "वह सभी को समान दृष्टि से देखता है, जिसने लालच का त्याग कर दिया है और जो पराई स्त्री को माता के समान मानता है।",
                        "english": "He looks upon all with equality, has renounced greed, and considers every other woman as a mother."
                    },
                    {
                        "hindi": "जिह्वा थकी असत्य न बोले परधन नव झाले हाथ रे॥",
                        "roman": "Jihva Thaki Asatya Na Bole, Pardhan Nav Jhale Haath Re.",
                        "hindi_meaning": "उसकी जीभ कभी झूठ नहीं बोलती और वह पराए धन को कभी हाथ नहीं लगाता।",
                        "english": "His tongue never speaks an untruth, and his hands never touch the wealth of others."
                    }
                ]
            }
        ]

    elif b['slug'] == 'shri-ramachandra-kripalu':
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
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 1",
                "label_english": "Verse 1",
                "lines": [
                    {
                        "hindi": "कंदर्प अगणित अमित छबि नवनील नीरद सुन्दरं।",
                        "roman": "Kandarp Aganit Amit Chhabi Navneel Neerad Sundaram.",
                        "hindi_meaning": "जिनकी सुंदरता अनगिनत कामदेवों से भी बढ़कर है, और जिनका शरीर नए, नीले जल से भरे बादलों के समान सुंदर है।",
                        "english": "Whose infinite beauty surpasses that of countless Kamadevas (gods of love), and whose form is as beautiful as newly formed blue rain clouds."
                    },
                    {
                        "hindi": "पट पीत मानहु तड़ित रुचि शुचि नौमि जनक सुतावरं॥",
                        "roman": "Pat Peet Manahu Tadit Ruchi Shuchi Noumi Janak Sutavaram.",
                        "hindi_meaning": "जिनके पीले वस्त्र बिजली की तरह चमक रहे हैं। ऐसे पवित्र, जनक नंदिनी (सीता) के पति श्री राम को मैं नमस्कार करता हूँ।",
                        "english": "Whose yellow garments flash like lightning. I bow to the pure Lord, the beloved husband of Janaka's daughter (Sita)."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 2",
                "label_english": "Verse 2",
                "lines": [
                    {
                        "hindi": "भजु दीनबंधु दिनेश दानव दैत्य वंश निकंदनं।",
                        "roman": "Bhaju Deenbandhu Dinesh Danav Daitya Vansh Nikandanam.",
                        "hindi_meaning": "उन दीनों के बंधु, सूर्य के समान तेजस्वी, और दानवों तथा दैत्यों के वंश का नाश करने वाले श्री राम का भजन करो।",
                        "english": "Worship the friend of the poor, radiant as the sun, the destroyer of the lineage of demons and giants."
                    },
                    {
                        "hindi": "रघुनंद आनंद कंद कोशल चंद दशरथ नंदनं॥",
                        "roman": "Raghunand Aanand Kand Koshal Chand Dasharath Nandanam.",
                        "hindi_meaning": "जो रघुकुल को आनंद देने वाले हैं, कोशल देश के लिए चंद्रमा के समान हैं, और दशरथ जी के प्रिय पुत्र हैं।",
                        "english": "The joy of the Raghu clan, the root of bliss, the moon of the Kosala kingdom, and the beloved son of Dasharatha."
                    }
                ]
            }
        ]

    elif b['slug'] == 'madhurashtakam':
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
            },
            {
                "type": "stanza",
                "label_hindi": "श्लोक 2",
                "label_english": "Stanza 2",
                "lines": [
                    {
                        "hindi": "वचनं मधुरं चरितं मधुरं,",
                        "roman": "Vachanam Madhuram Charitam Madhuram,",
                        "hindi_meaning": "उनके शब्द मधुर हैं, उनका चरित्र मधुर है,",
                        "english": "His words are sweet, His character is sweet,"
                    },
                    {
                        "hindi": "वसनं मधुरं वलितं मधुरम्।",
                        "roman": "Vasanam Madhuram Valitam Madhuram.",
                        "hindi_meaning": "उनके वस्त्र मधुर हैं, उनकी मुद्राएँ (मुड़ना) मधुर हैं।",
                        "english": "His garments are sweet, His postures are sweet."
                    },
                    {
                        "hindi": "चलितं मधुरं भ्रमितं मधुरं,",
                        "roman": "Chalitam Madhuram Bhramitam Madhuram,",
                        "hindi_meaning": "उनका चलना मधुर है, उनका घूमना मधुर है,",
                        "english": "His movements are sweet, His wandering is sweet,"
                    },
                    {
                        "hindi": "मधुराधिपतेरखिलं मधुरम्॥",
                        "roman": "Madhuradhipater Akhilam Madhuram.",
                        "hindi_meaning": "मधुरता के अधिपति (श्री कृष्ण) का सब कुछ मधुर ही मधुर है।",
                        "english": "Everything about the Lord of Sweetness is absolutely sweet."
                    }
                ]
            },
            {
                "type": "stanza",
                "label_hindi": "श्लोक 3",
                "label_english": "Stanza 3",
                "lines": [
                    {
                        "hindi": "वेणुर्मधुरो रेणुर्मधुरः,",
                        "roman": "Venur Madhuro Renur Madhurah,",
                        "hindi_meaning": "उनकी बांसुरी मधुर है, उनके चरणों की धूल मधुर है,",
                        "english": "His flute is sweet, the dust of His feet is sweet,"
                    },
                    {
                        "hindi": "पाणिर्मधुरः पादौ मधुरौ।",
                        "roman": "Panir Madhurah Padau Madhurau.",
                        "hindi_meaning": "उनके हाथ मधुर हैं, उनके पैर मधुर हैं।",
                        "english": "His hands are sweet, His feet are sweet."
                    },
                    {
                        "hindi": "नृत्यं मधुरं सख्यं मधुरं,",
                        "roman": "Nrityam Madhuram Sakhyam Madhuram,",
                        "hindi_meaning": "उनका नृत्य मधुर है, उनकी मित्रता मधुर है,",
                        "english": "His dancing is sweet, His friendship is sweet,"
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

print("Expanded last 4 bhajans.")
