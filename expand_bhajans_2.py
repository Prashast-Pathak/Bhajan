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
                    },
                    {
                        "hindi": "गगन सम अंग कांति काली, राधिका चमक रही आली।",
                        "roman": "Gagan Sam Ang Kanti Kaali, Radhika Chamak Rahi Aali.",
                        "hindi_meaning": "जिनके शरीर की चमक आकाश के समान श्याम रंग की है, और उनके साथ श्री राधिका जी चमक रही हैं।",
                        "english": "His complexion is dark and vast like the sky, and beside Him, Radhika shines brightly."
                    },
                    {
                        "hindi": "लतन में ठाढ़े बनमाली, भ्रमर सी अलक, कस्तूरी तिलक।",
                        "roman": "Latan Mein Thadhe Banmali, Bhramar Si Alak, Kasturi Tilak.",
                        "hindi_meaning": "लताओं के बीच वनमाली (कृष्ण) खड़े हैं, जिनकी लटें भंवरों जैसी हैं और माथे पर कस्तूरी का तिलक है।",
                        "english": "The Lord of the forest stands amidst the creepers, with locks like bees and a musk mark on His forehead."
                    },
                    {
                        "hindi": "चंद्र सी झलक, ललित छवि श्यामा प्यारी की॥",
                        "roman": "Chandra Si Jhalak, Lalit Chhavi Shyama Pyari Ki.",
                        "hindi_meaning": "उनकी झलक चंद्रमा के समान सुंदर है, यह प्यारी श्यामा (राधा) और श्याम की छवि अत्यंत मनमोहक है।",
                        "english": "His glimpse is as beautiful as the moon; such is the lovely image of the beloved dark Lord."
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
                        "roman": "Kanakmay Mor Mukut Bilsai, Devata Darsan Ko Tarsain.",
                        "hindi_meaning": "उनके सिर पर सोने से जड़ा हुआ मोर मुकुट सुशोभित है, जिनके दर्शनों के लिए देवता भी तरसते हैं।",
                        "english": "A golden peacock crown adorns His head, a sight that even the gods yearn to see."
                    },
                    {
                        "hindi": "गगन सों सुमन रासि बरसै, बजे मुरचंग, मधुर मिरदंग।",
                        "roman": "Gagan So Suman Raasi Barsai, Baje Murchang, Madhur Mirdang.",
                        "hindi_meaning": "आकाश से फूलों की वर्षा हो रही है, और मुरचंग तथा मधुर मृदंग बज रहे हैं।",
                        "english": "Showers of flowers fall from the sky, while musical instruments like the Murchang and sweet Mridang are playing."
                    },
                    {
                        "hindi": "ग्वालिन संग अतुल रति गोप कुमारी की॥",
                        "roman": "Gwalin Sang Atul Rati Gop Kumari Ki.",
                        "hindi_meaning": "ग्वालिनों और गोप-कुमारियों (गोपियों) के साथ उनका अतुलनीय प्रेम है।",
                        "english": "He shares an incomparable, divine love with the cowherd girls (Gopis)."
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
                        "roman": "Jahan Te Prakat Bhai Ganga, Kalush Kali Haarini Shri Ganga.",
                        "hindi_meaning": "जिनके चरणों से गंगा जी प्रकट हुईं, वे गंगा जो कलियुग के पापों को हरने वाली हैं।",
                        "english": "From whose feet emerged the river Ganga, the sacred Ganga that destroys the sins of the dark age (Kali Yuga)."
                    },
                    {
                        "hindi": "स्मरन ते होत मोह भंगा, बसी शिव सीस, जटा के बीच।",
                        "roman": "Smaran Te Hot Moh Bhanga, Basi Shiv Sees, Jata Ke Beech.",
                        "hindi_meaning": "जिनके स्मरण मात्र से मोह भंग हो जाता है, वही गंगा भगवान शिव के सिर की जटाओं के बीच निवास करती हैं।",
                        "english": "Merely remembering Him destroys worldly attachments; that same Ganga resides in the matted hair of Lord Shiva."
                    },
                    {
                        "hindi": "हरै अघ कीच, चरन छवि श्री बनवारी की॥",
                        "roman": "Harai Agh Keech, Charan Chhavi Shri Banwari Ki.",
                        "hindi_meaning": "श्री बनवारी (कृष्ण) के चरणों की वह सुंदर छवि पापों के कीचड़ को हरने वाली है।",
                        "english": "The beautiful image of Shri Banwari's (Krishna's) feet washes away the mud of our sins."
                    }
                ]
            }
        ]

    elif b['slug'] == 'raghupati-raghav-raja-ram':
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
                "label_hindi": "अंतरा 1",
                "label_english": "Verse 1",
                "lines": [
                    {
                        "hindi": "सुन्दर विग्रह मेघश्याम, गंगा तुलसी शालग्राम।",
                        "roman": "Sundar Vigrah Meghshyam, Ganga Tulsi Shalagram.",
                        "hindi_meaning": "जिनका स्वरूप बादलों के समान सुंदर श्याम वर्ण है, जिन्हें गंगा, तुलसी और शालिग्राम प्रिय हैं।",
                        "english": "Whose beautiful form is dark like a raincloud, to whom the Ganges, Tulsi, and Shalagram are dear."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 2",
                "label_english": "Verse 2",
                "lines": [
                    {
                        "hindi": "भद्रगिरीश्वर सीताराम, भगत-जनप्रिय सीताराम।",
                        "roman": "Bhadragirishwar Sita Ram, Bhagat-Janpriya Sita Ram.",
                        "hindi_meaning": "भद्रगिरि के ईश्वर श्री सीताराम, जो अपने भक्तों को अत्यंत प्रिय हैं।",
                        "english": "Sita and Ram, the Lords of Bhadragiri, who are deeply loved by their devotees."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 3",
                "label_english": "Verse 3",
                "lines": [
                    {
                        "hindi": "जानकीरमण सीताराम, जयजय राघव सीताराम।",
                        "roman": "Janakiraman Sita Ram, Jai Jai Raghav Sita Ram.",
                        "hindi_meaning": "जानकी (सीता) को आनंदित करने वाले सीताराम, श्री राघव और सीताराम की बारंबार जय हो।",
                        "english": "Sita and Ram, the delighters of Janaki. All glories to Raghav, Sita, and Ram."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 4",
                "label_english": "Verse 4",
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

with open('data/bhajans.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Expanded Kunj Bihari and Raghupati Raghav.")
