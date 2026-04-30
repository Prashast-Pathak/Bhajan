import json

with open('data/bhajans.json', 'r') as f:
    data = json.load(f)

for b in data:
    if b['slug'] == 'ram-siya-ram':
        b['reference'] = "Traditional Ram Dhun based on Ramcharitmanas verses."
        b['verses'] = [
            {
                "type": "mukhda",
                "label_hindi": "मुखड़ा",
                "label_english": "Refrain",
                "lines": [
                    {
                        "hindi": "राम सिया राम सिया राम जय जय राम।",
                        "roman": "Ram Siya Ram Siya Ram Jai Jai Ram.",
                        "hindi_meaning": "श्री राम और माता सीता की जय हो।",
                        "english": "Victory to Lord Rama and Mother Sita."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "चौपाई 1",
                "label_english": "Choupai 1",
                "lines": [
                    {
                        "hindi": "होइहै वही जो राम रचि राखा।",
                        "roman": "Hoi Hai Wahi Jo Ram Rachi Rakha.",
                        "hindi_meaning": "वही होगा जो श्री राम ने रच कर रखा है (जो भगवान की इच्छा है)।",
                        "english": "Only that will happen which Lord Rama has ordained."
                    },
                    {
                        "hindi": "को करे तरफ़ बढ़ाए साखा॥",
                        "roman": "Ko Kare Taraf Badhaye Sakha.",
                        "hindi_meaning": "कौन व्यर्थ में तर्क करके बात को बढ़ाए?",
                        "english": "Who can argue or change His divine will?"
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "चौपाई 2",
                "label_english": "Choupai 2",
                "lines": [
                    {
                        "hindi": "धीरज धरम मित्र अरु नारी।",
                        "roman": "Dhiraj Dharam Mitra Aru Nari.",
                        "hindi_meaning": "धैर्य, धर्म, मित्र और पत्नी —",
                        "english": "Patience, righteousness, a friend, and a wife —"
                    },
                    {
                        "hindi": "आपद काल परिखिअहिं चारी॥",
                        "roman": "Aapad Kaal Parikhiahin Chari.",
                        "hindi_meaning": "इन चारों की परीक्षा विपत्ति के समय ही होती है।",
                        "english": "These four are tested only during times of adversity."
                    }
                ]
            }
        ]

    elif b['slug'] == 'deva-shree-ganesha':
        b['reference'] = "Popular Marathi/Hindi devotional chant for Lord Ganesha."
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
            }
        ]

    elif b['slug'] == 'jai-ambe-gauri':
        b['reference'] = "Traditional Aarti dedicated to Goddess Durga (Ambe Maa)."
        b['verses'] = [
            {
                "type": "mukhda",
                "label_hindi": "मुखड़ा",
                "label_english": "Refrain",
                "lines": [
                    {
                        "hindi": "जय अम्बे गौरी, मैया जय श्यामा गौरी।",
                        "roman": "Jai Ambe Gauri, Maiya Jai Shyama Gauri.",
                        "hindi_meaning": "हे माता अम्बे (गौरी), आपकी जय हो! हे श्यामा गौरी, आपकी जय हो!",
                        "english": "Victory to Mother Ambe (Gauri), Victory to Mother Shyama Gauri!"
                    },
                    {
                        "hindi": "तुम को निशि दिन ध्यावत, हरि ब्रह्मा शिवजी॥",
                        "roman": "Tum Ko Nishi Din Dhyavat, Hari Brahma Shivji.",
                        "hindi_meaning": "भगवान विष्णु, ब्रह्मा और शिव रात-दिन आपका ही ध्यान करते हैं।",
                        "english": "Lord Vishnu, Brahma, and Shiva meditate upon You day and night."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 1",
                "label_english": "Verse 1",
                "lines": [
                    {
                        "hindi": "मांग सिंदूर बिराजत, टीको मृग मद को।",
                        "roman": "Maang Sindoor Birajat, Teeko Mrig Mad Ko.",
                        "hindi_meaning": "आपकी माँग में सिंदूर सुशोभित है, और माथे पर कस्तूरी का तिलक है।",
                        "english": "Vermilion adorns Your hair parting, and a musk tilak shines on Your forehead."
                    },
                    {
                        "hindi": "उज्ज्वल से दो नैना, चंद्रबदन नीको॥",
                        "roman": "Ujjwal Se Do Naina, Chandrabadan Neeko.",
                        "hindi_meaning": "आपके दोनों नेत्र उज्ज्वल हैं, और आपका मुख चंद्रमा के समान सुंदर है।",
                        "english": "Your two eyes are bright, and Your face is as beautiful as the moon."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 2",
                "label_english": "Verse 2",
                "lines": [
                    {
                        "hindi": "कनक समान कलेवर, रक्ताम्बर राजै।",
                        "roman": "Kanak Saman Kalevar, Raktambar Rajai.",
                        "hindi_meaning": "आपका शरीर सोने के समान दमकता है, और आप लाल वस्त्रों में सुशोभित हैं।",
                        "english": "Your body shines like gold, and You look majestic in red garments."
                    },
                    {
                        "hindi": "रक्त पुष्प गल माला, कंठन पर साजै॥",
                        "roman": "Rakt Pushp Gal Mala, Kanthan Par Sajai.",
                        "hindi_meaning": "आपके गले में लाल फूलों की माला अत्यंत सुंदर लग रही है।",
                        "english": "A garland of red flowers beautifully adorns Your neck."
                    }
                ]
            }
        ]

with open('data/bhajans.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Batch 1 complete.")
