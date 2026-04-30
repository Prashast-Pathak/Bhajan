import json

with open('data/bhajans.json', 'r') as f:
    data = json.load(f)

for b in data:
    if b['slug'] == 'ram-siya-ram':
        b['verses'] = [
            {
                "type": "antara",
                "label_hindi": "चौपाई 1",
                "label_english": "Choupai 1",
                "lines": [
                    {
                        "hindi": "मंगल भवन अमंगल हारी।",
                        "roman": "Mangal Bhavan Amangal Haari.",
                        "hindi_meaning": "जो मंगलों के धाम हैं और अमंगलों (विपत्तियों) को हरने वाले हैं।",
                        "english": "The abode of all auspiciousness and the destroyer of all that is inauspicious."
                    },
                    {
                        "hindi": "द्रवहु सुदसरथ अचर बिहारी॥",
                        "roman": "Dravahu Sudasarath Achar Bihari.",
                        "hindi_meaning": "वे राजा दशरथ के आंगन में खेलने वाले श्री राम मुझ पर कृपा करें।",
                        "english": "May that Lord Rama, who played in Dasharatha's courtyard, shower His grace upon me."
                    }
                ]
            },
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
                "label_hindi": "चौपाई 2",
                "label_english": "Choupai 2",
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
                "label_hindi": "चौपाई 3",
                "label_english": "Choupai 3",
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
            },
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
                "label_hindi": "चौपाई 4",
                "label_english": "Choupai 4",
                "lines": [
                    {
                        "hindi": "जेहि के जेहि पर सत्य सनेहू।",
                        "roman": "Jehi Ke Jehi Par Satya Sanehu.",
                        "hindi_meaning": "जिसका जिस पर सच्चा स्नेह (प्रेम) होता है,",
                        "english": "Whoever has true affection and love for another,"
                    },
                    {
                        "hindi": "सो तेहि मिलय न कछु संदेहू॥",
                        "roman": "So Tehi Milay Na Kachhu Sandehu.",
                        "hindi_meaning": "वह उसे अवश्य मिलता है, इसमें कोई संदेह नहीं है।",
                        "english": "They will surely attain them, there is no doubt about it."
                    }
                ]
            },
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
                "label_hindi": "चौपाई 5",
                "label_english": "Choupai 5",
                "lines": [
                    {
                        "hindi": "जाकी रही भावना जैसी।",
                        "roman": "Jaaki Rahi Bhavana Jaisi.",
                        "hindi_meaning": "जिसके मन में जैसी भावना होती है,",
                        "english": "According to one's pure feelings and devotion,"
                    },
                    {
                        "hindi": "प्रभु मूरत देखी तिन तैसी॥",
                        "roman": "Prabhu Moorat Dekhi Tin Taisi.",
                        "hindi_meaning": "उसे भगवान का रूप वैसा ही दिखाई देता है।",
                        "english": "They behold the form of the Lord in exactly that way."
                    }
                ]
            },
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
            }
        ]
        
    elif b['slug'] == 'jai-ambe-gauri':
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
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 3",
                "label_english": "Verse 3",
                "lines": [
                    {
                        "hindi": "केहरि वाहन राजत, खड्ग खप्पर धारी।",
                        "roman": "Kehari Vahan Rajat, Khadga Khappar Dhari.",
                        "hindi_meaning": "सिंह आपकी सवारी है, और आप हाथों में तलवार तथा खप्पर धारण करती हैं।",
                        "english": "You ride a majestic lion, holding a sword and a skull-bowl."
                    },
                    {
                        "hindi": "सुर नर मुनि जन सेवत, तिनके दुख हारी॥",
                        "roman": "Sur Nar Muni Jan Sevat, Tinke Dukh Haari.",
                        "hindi_meaning": "देवता, मनुष्य और मुनि आपकी सेवा करते हैं, और आप उनके सभी दुखों को हरने वाली हैं।",
                        "english": "Gods, mortals, and sages serve You, and You destroy their sorrows."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 4",
                "label_english": "Verse 4",
                "lines": [
                    {
                        "hindi": "कानन कुण्डल शोभित, नासाग्रे मोती।",
                        "roman": "Kanan Kundal Shobhit, Nasagre Moti.",
                        "hindi_meaning": "आपके कानों में कुंडल सुशोभित हैं, और नासिका (नाक) में मोती चमक रहा है।",
                        "english": "Earrings adorn Your ears, and a pearl shines on the tip of Your nose."
                    },
                    {
                        "hindi": "कोटिक चन्द्र दिवाकर, सम राजत ज्योती॥",
                        "roman": "Kotik Chandra Divakar, Sam Rajat Jyoti.",
                        "hindi_meaning": "आपकी ज्योति करोड़ों सूर्य और चंद्रमाओं के समान उज्ज्वल है।",
                        "english": "Your divine light shines as brightly as millions of suns and moons."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 5",
                "label_english": "Verse 5",
                "lines": [
                    {
                        "hindi": "शुम्भ निशुम्भ बिदारे, महिषासुर घाती।",
                        "roman": "Shumbh Nishumbh Bidare, Mahishasur Ghati.",
                        "hindi_meaning": "आपने शुम्भ और निशुम्भ राक्षसों का वध किया, और महिषासुर का संहार किया।",
                        "english": "You destroyed the demons Shumbha and Nishumbha, and You are the slayer of Mahishasura."
                    },
                    {
                        "hindi": "धूम्र विलोचन नैना, निशदिन मदमाती॥",
                        "roman": "Dhumr Vilochan Naina, Nishdin Madmati.",
                        "hindi_meaning": "आपने धूम्रविलोचन नामक राक्षस का नाश किया। आपकी आंखें हर समय दिव्य आनंद से भरी रहती हैं।",
                        "english": "You defeated the demon Dhumralochan. Your eyes are always filled with divine bliss."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 6",
                "label_english": "Verse 6",
                "lines": [
                    {
                        "hindi": "चण्ड मुण्ड संहारे, शोणित बीज हरे।",
                        "roman": "Chand Mund Sanhare, Shonit Beej Hare.",
                        "hindi_meaning": "आपने चण्ड और मुण्ड नामक राक्षसों का संहार किया, और रक्तबीज का वध किया।",
                        "english": "You destroyed the demons Chanda and Munda, and defeated Raktabeeja."
                    },
                    {
                        "hindi": "मधु कैटभ दोउ मारे, सुर भयहीन करे॥",
                        "roman": "Madhu Kaitabh Dou Mare, Sur Bhayheen Kare.",
                        "hindi_meaning": "आपने मधु और कैटभ को भी मारा, जिससे देवताओं को भयमुक्त कर दिया।",
                        "english": "You killed both Madhu and Kaitabha, making the gods completely fearless."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 7",
                "label_english": "Verse 7",
                "lines": [
                    {
                        "hindi": "ब्रह्माणी रुद्राणी, तुम कमला रानी।",
                        "roman": "Brahmani Rudrani, Tum Kamala Rani.",
                        "hindi_meaning": "आप ही ब्रह्माणी, रुद्राणी और कमला (लक्ष्मी) रानी हैं।",
                        "english": "You are Brahmani, Rudrani, and Queen Kamala (Lakshmi)."
                    },
                    {
                        "hindi": "आगम निगम बखानी, तुम शिव पटरानी॥",
                        "roman": "Aagam Nigam Bakhani, Tum Shiv Patrani.",
                        "hindi_meaning": "आगम और निगम (वेद-शास्त्र) आपका गुणगान करते हैं। आप भगवान शिव की पटरानी हैं।",
                        "english": "The sacred scriptures and Vedas sing Your glory. You are the supreme consort of Lord Shiva."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 8",
                "label_english": "Verse 8",
                "lines": [
                    {
                        "hindi": "चौंसठ योगिनी गावत, नृत्य करत भैरों।",
                        "roman": "Chaunsath Yogini Gavat, Nritya Karat Bhairon.",
                        "hindi_meaning": "चौंसठ योगिनियाँ आपका गुणगान करती हैं, और भैरव आपके सामने नृत्य करते हैं।",
                        "english": "The sixty-four Yoginis sing Your praises, while Lord Bhairava dances before You."
                    },
                    {
                        "hindi": "बाजत ताल मृदंगा, अरु बाजत डमरू॥",
                        "roman": "Bajat Taal Mridanga, Aru Bajat Damaru.",
                        "hindi_meaning": "ताल, मृदंग और भगवान शिव का डमरू आपके सम्मान में बजता है।",
                        "english": "Cymbals, Mridang, and the Damaru sound in Your honor."
                    }
                ]
            },
            {
                "type": "antara",
                "label_hindi": "अंतरा 9",
                "label_english": "Verse 9",
                "lines": [
                    {
                        "hindi": "अम्बे जी की आरती जो कोई नर गावे।",
                        "roman": "Ambe Ji Ki Aarti Jo Koi Nar Gaave.",
                        "hindi_meaning": "जो कोई भी मनुष्य माता अम्बे की यह आरती गाता है,",
                        "english": "Whoever sings this Aarti of Mother Ambe,"
                    },
                    {
                        "hindi": "कहत शिवानन्द स्वामी, सुख सम्पत्ति पावे॥",
                        "roman": "Kahat Shivanand Swami, Sukh Sampatti Pave.",
                        "hindi_meaning": "शिवानंद स्वामी कहते हैं, वह व्यक्ति अपार सुख और संपत्ति प्राप्त करता है।",
                        "english": "Swami Shivananda says, that person attains immense happiness and prosperity."
                    }
                ]
            }
        ]

with open('data/bhajans.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Expanded Ram Siya Ram and Jai Ambe Gauri fully.")
