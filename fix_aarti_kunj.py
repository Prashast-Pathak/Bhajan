import json

with open('data/bhajans.json', 'r') as f:
    data = json.load(f)

for b in data:
    if b['slug'] == 'aarti-kunj-bihari-ki':
        b['verses'] = [
            {
                "type": "mukhda",
                "label_hindi": "मुखड़ा",
                "label_english": "Refrain",
                "lines": [
                    {
                        "hindi": "आरती कुंजबिहारी की, श्री गिरिधर कृष्णमुरारी की।",
                        "roman": "Aarti Kunj Bihari ki, Shri Giridhar Krishnamuari ki",
                        "hindi_meaning": "कुंज में विहार करने वाले श्री कृष्ण की आरती, जो पर्वत धारण करने वाले और मुरारी नाम से प्रसिद्ध हैं।",
                        "english": "Aarti of the Lord who roams the groves, Sri Krishna who lifted the mountain and is known as Murari."
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
                        "roman": "Gale mein baijanti mala, bajave murli madhur bala",
                        "hindi_meaning": "उनके गले में वैजयंती की माला है, और वे बालक-स्वरूप में मधुर बांसुरी बजा रहे हैं।",
                        "english": "Adorned with a Vaijayanti garland, the divine child plays the sweet flute."
                    },
                    {
                        "hindi": "श्रवण में कुण्डल झलकाला, नंद के आनंद नंदलाला।",
                        "roman": "Shravan mein kundal jhalkala, nand ke anand nandlala",
                        "hindi_meaning": "उनके कानों में कुंडल चमक रहे हैं — वे नंद बाबा के आनंद-पुत्र श्री नंदलाल हैं।",
                        "english": "Earrings glitter in His ears — He is Nandlala, the bliss of Nanda."
                    },
                    {
                        "hindi": "गगन सम अंग कांति काली, राधिका चमक रही आली।",
                        "roman": "Gagan sam ang kanti kali, Radhika chamak rahi aali",
                        "hindi_meaning": "उनके अंगों की कांति आकाश के समान श्यामल है, और उनके पास राधिका जी अपनी सखियों के साथ चमक रही हैं।",
                        "english": "His body glows dark as the sky, and Radhika shines brightly beside Him with her companions."
                    },
                    {
                        "hindi": "लतन में ठाढ़े बनमाली, भ्रमर सी अलक, कस्तूरी तिलक।",
                        "roman": "Latan mein thaadhe banmaali, bhramar si alak, kasturi tilak",
                        "hindi_meaning": "वे वन की लताओं में खड़े हैं, उनकी अलकें भौंरे के समान काली हैं और माथे पर कस्तूरी का तिलक शोभित है।",
                        "english": "Standing among the vines of the forest, His curls are dark as bees, with a musk tilak on His forehead."
                    },
                    {
                        "hindi": "चंद्र सी झलक, ललित छवि श्यामा प्यारी की॥",
                        "roman": "Chandra si jhalak, lalit chhavi shyama pyari ki",
                        "hindi_meaning": "उनकी छवि चंद्रमा-सी झलकती है — यह सुंदर छवि प्रियतमा श्यामा (राधा) जी की भी है।",
                        "english": "A moonlike radiance shines — this beautiful form belongs to His beloved Shyama (Radha)."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 2",
                "label_english": "Verse 2",
                "lines": [
                    {
                        "hindi": "कनकमय मोर मुकुट बिलसै, देवता दरसन को तरसैं।",
                        "roman": "Kanakamay mor mukut bilase, devata darasan ko tarasein",
                        "hindi_meaning": "उनके सिर पर सोने से जड़ा मोर-पंख का मुकुट शोभित है, देवता उनके दर्शन के लिए तरसते हैं।",
                        "english": "A golden peacock-feather crown adorns His head; the gods long for His divine vision."
                    },
                    {
                        "hindi": "गगन सों सुमन रासि बरसै, बजे मुरचंग, मधुर मिरदंग।",
                        "roman": "Gagan son suman raasi barase, baje murachang, madhur mridang",
                        "hindi_meaning": "आकाश से फूलों की वर्षा होती है, मुरचंग और मृदंग मधुर ध्वनि में बज रहे हैं।",
                        "english": "Flowers shower from the heavens, the morchang and mridang resound with sweet melody."
                    },
                    {
                        "hindi": "ग्वालिन संग अतुल रति गोप कुमारी की॥",
                        "roman": "Gwalin sang atul rati gop kumari ki",
                        "hindi_meaning": "गोप-कुमारियाँ (गोपियाँ) साथ में अतुलनीय आनंद से उनकी आरती करती हैं।",
                        "english": "The Gopi maidens rejoice alongside Him in incomparable devotion and love."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 3",
                "label_english": "Verse 3",
                "lines": [
                    {
                        "hindi": "जहां ते प्रकट भई गंगा, कलुष कलि हारिणि श्री गंगा।",
                        "roman": "Jahan te prakat bhai Ganga, kalush kali haarini shri Ganga",
                        "hindi_meaning": "जहाँ से पवित्र गंगा प्रकट हुईं, कलियुग के पापों का नाश करने वाली गंगा माता।",
                        "english": "From where the holy Ganga emerged — the Ganga who destroys all sins of the age of Kali."
                    },
                    {
                        "hindi": "स्मरन ते होत मोह भंगा, बसी शिव सीस, जटा के बीच।",
                        "roman": "Smaran te hot moh bhanga, basi shiv sees, jata ke beech",
                        "hindi_meaning": "उनके स्मरण मात्र से मोह-माया का नाश होता है, वे शिव जी की जटाओं के बीच निवास करती हैं।",
                        "english": "Remembering Her destroys all worldly illusion; She dwells within the matted locks of Lord Shiva."
                    },
                    {
                        "hindi": "हरै अघ कीच, चरन छवि श्री बनवारी की॥",
                        "roman": "Harai agh keech, charan chhavi shri Banwari ki",
                        "hindi_meaning": "वे सभी पापरूपी कीचड़ को हर लेती हैं — यह सौभाग्य है श्री बनवारी (कृष्ण) के चरणों की छवि से।",
                        "english": "She washes away the mire of all sins — by the glory of Sri Banwari's (Krishna's) lotus feet."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 4",
                "label_english": "Verse 4",
                "lines": [
                    {
                        "hindi": "चमकती उज्ज्वल तट रेनु, बज रही वृंदावन बेनु।",
                        "roman": "Chamkati ujjwal tat renu, baj rahi Vrindavan benu",
                        "hindi_meaning": "यमुना के तट की रेत उज्ज्वल चमक रही है, और वृंदावन में बांसुरी बज रही है।",
                        "english": "The sand on the riverbank shines brilliantly, and the flute melody fills Vrindavan."
                    },
                    {
                        "hindi": "चहुं दिसि गोपि ग्वाल धेनु, हंसत मृदु मंद चांदनी चंद।",
                        "roman": "Chahun disi gopi gwaal dhenu, hansat mridu mand chandni chand",
                        "hindi_meaning": "चारों दिशाओं में गोपियाँ, ग्वाले और गाएं हैं, चाँद मंद-मंद मुस्कुराते हुए चाँदनी बिखेर रहा है।",
                        "english": "Gopis, cowherds, and cows fill all four directions, as the moon smiles softly in the moonlit night."
                    },
                    {
                        "hindi": "करत आनंद, प्रमोद कंद श्री गिरिधारी की॥",
                        "roman": "Karat aanand, pramod kand shri Giridharis ki",
                        "hindi_meaning": "वे आनंद और प्रमोद के केंद्र हैं — श्री गिरिधारी (कृष्ण) जो पर्वत धारण करने वाले हैं।",
                        "english": "Creating joy and delight — Sri Giridhari, the lifter of the mountain, is the source of all bliss."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 5",
                "label_english": "Verse 5",
                "lines": [
                    {
                        "hindi": "यमुना तट धेनु चराई, गोप ग्वाल संग लेकर आई।",
                        "roman": "Yamuna tat dhenu charai, gop gwaal sang lekar aai",
                        "hindi_meaning": "यमुना के तट पर गायों को चराते हुए, गोप-ग्वालों के साथ वे वापस आए।",
                        "english": "Grazing the cows on the banks of Yamuna, He returned with the cowherd friends."
                    },
                    {
                        "hindi": "माखन मिश्री खाय रिझाई, नंद के लाल, बृजबाल।",
                        "roman": "Makhan mishri khaay rijhaai, nand ke laal, brijbaal",
                        "hindi_meaning": "माखन और मिश्री खाकर सबको रिझाने वाले, नंद के लाल और ब्रज के बालक।",
                        "english": "Delighting all with butter and sugar, the beloved son of Nanda, the darling of Braj."
                    },
                    {
                        "hindi": "लाड़ लड़ाई मैया यशोदा प्यारी की॥",
                        "roman": "Laad ladhai maiya Yashoda pyaari ki",
                        "hindi_meaning": "माँ यशोदा उन पर प्यार लुटाती हैं — यह है प्रिय यशोदा माँ का दुलार।",
                        "english": "Mother Yashoda lovingly indulges Him — the cherished pampering of beloved Mother Yashoda."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 6",
                "label_english": "Verse 6",
                "lines": [
                    {
                        "hindi": "भक्तन के काज सवारे, दुष्ट असुरन को संहारे।",
                        "roman": "Bhaktan ke kaaj savare, dusht asuran ko sanhare",
                        "hindi_meaning": "वे अपने भक्तों के कार्य सँवारते हैं और दुष्ट असुरों का संहार करते हैं।",
                        "english": "He fulfils the wishes of His devotees and destroys the wicked demons."
                    },
                    {
                        "hindi": "वृंदावन के बंशीधारे, प्रेम सागर, मन रंजन।",
                        "roman": "Vrindavan ke banshidhaare, prem saagar, man ranjan",
                        "hindi_meaning": "वृंदावन में बांसुरी धारण करने वाले प्रेम के सागर, मन को आनंदित करने वाले।",
                        "english": "The flute-bearer of Vrindavan, ocean of love, the one who delights all minds."
                    },
                    {
                        "hindi": "लीला रंजन सुंदर, छवि मनोहारी की॥",
                        "roman": "Leela ranjan sundar, chhavi manohaari ki",
                        "hindi_meaning": "उनकी लीलाएँ मन को प्रसन्न करती हैं और उनकी छवि मन को मोह लेती है।",
                        "english": "His divine pastimes delight the heart, and His form is utterly captivating."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 7",
                "label_english": "Verse 7 (Phalashruti)",
                "lines": [
                    {
                        "hindi": "आरती कुंजबिहारी की जो कोई नर गावे।",
                        "roman": "Aarti Kunj Bihari ki jo koi nar gaave",
                        "hindi_meaning": "जो भी व्यक्ति कुंजबिहारी की यह आरती गाता है।",
                        "english": "Whoever sings this aarti of Kunj Bihari with devotion."
                    },
                    {
                        "hindi": "कृष्ण कृपा ते भव-सागर सहजहि उतर जाए।",
                        "roman": "Krishna kripa te bhava-saagar sahajahi utar jaaye",
                        "hindi_meaning": "कृष्ण की कृपा से वह संसार-सागर से आसानी से पार हो जाता है।",
                        "english": "By Krishna's grace, he easily crosses the ocean of worldly existence."
                    },
                    {
                        "hindi": "श्री गिरिधर कृष्णमुरारी की, आरती कुंजबिहारी की।",
                        "roman": "Shri Giridhar Krishnamuari ki, aarti Kunj Bihari ki",
                        "hindi_meaning": "श्री गिरिधर कृष्णमुरारी की — कुंजबिहारी की आरती।",
                        "english": "Of Sri Giridhar Krishnamurari — the Aarti of Kunj Bihari."
                    }
                ]
            }
        ]
        print(f"Updated: {len(b['verses'])} verses now")

with open('data/bhajans.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print("Saved successfully.")
