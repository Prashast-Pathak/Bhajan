import json

with open('data/bhajans.json', 'r') as f:
    data = json.load(f)

for b in data:
    if b['slug'] == 'madhurashtakam':
        b['verses'] = [
            {
                "type": "verse",
                "label_hindi": "श्लोक 1",
                "label_english": "Verse 1",
                "lines": [
                    {
                        "hindi": "अधरं मधुरं वदनं मधुरं नयनं मधुरं हसितं मधुरम् ।",
                        "roman": "Adharam madhuram vadanam madhuram nayanam madhuram hasitam madhuram",
                        "hindi_meaning": "उनके होंठ मधुर हैं, मुख मधुर है, आँखें मधुर हैं, उनकी मुस्कान मधुर है।",
                        "english": "His lips are sweet, His face is sweet, His eyes are sweet, His smile is sweet."
                    },
                    {
                        "hindi": "हृदयं मधुरं गमनं मधुरं मधुराधिपतेरखिलं मधुरम् ॥१॥",
                        "roman": "Hridayam madhuram gamanam madhuram madhuradhipaterakhilam madhuram",
                        "hindi_meaning": "उनका हृदय मधुर है, उनकी चाल मधुर है; मधुरता के ईश्वर (श्री कृष्ण) का सब कुछ मधुर है।",
                        "english": "His heart is sweet, His walk is sweet; everything about the Lord of Sweetness is sweet."
                    }
                ]
            },
            {
                "type": "verse",
                "label_hindi": "श्लोक 2",
                "label_english": "Verse 2",
                "lines": [
                    {
                        "hindi": "वचनं मधुरं चरितं मधुरं वसनं मधुरं वलितं मधुरम् ।",
                        "roman": "Vachanam madhuram charitam madhuram vasanam madhuram valitam madhuram",
                        "hindi_meaning": "उनके वचन मधुर हैं, उनका चरित्र मधुर है, उनके वस्त्र मधुर हैं, उनकी मुद्रा मधुर है।",
                        "english": "His words are sweet, His character is sweet, His garments are sweet, His posture is sweet."
                    },
                    {
                        "hindi": "चलितं मधुरं भ्रमितं मधुरं मधुराधिपतेरखिलं मधुरम् ॥२॥",
                        "roman": "Chalitam madhuram bhramitam madhuram madhuradhipaterakhilam madhuram",
                        "hindi_meaning": "उनका चलना मधुर है, उनका भ्रमण करना मधुर है; मधुरता के ईश्वर का सब कुछ मधुर है।",
                        "english": "His movements are sweet, His wandering is sweet; everything about the Lord of Sweetness is sweet."
                    }
                ]
            },
            {
                "type": "verse",
                "label_hindi": "श्लोक 3",
                "label_english": "Verse 3",
                "lines": [
                    {
                        "hindi": "वेणुर्मधुरो रेणुर्मधुरः पाणिर्मधुरः पादौ मधुरौ ।",
                        "roman": "Venur madhuro renur madhurah panir madhurah padau madhurau",
                        "hindi_meaning": "उनकी बांसुरी मधुर है, उनके चरणों की धूल मधुर है, उनके हाथ मधुर हैं, उनके चरण मधुर हैं।",
                        "english": "His flute is sweet, the dust of His feet is sweet, His hands are sweet, His feet are sweet."
                    },
                    {
                        "hindi": "नृत्यं मधुरं सख्यं मधुरं मधुराधिपतेरखिलं मधुरम् ॥३॥",
                        "roman": "Nrityam madhuram sakhyam madhuram madhuradhipaterakhilam madhuram",
                        "hindi_meaning": "उनका नृत्य मधुर है, उनकी मित्रता मधुर है; मधुरता के ईश्वर का सब कुछ मधुर है।",
                        "english": "His dance is sweet, His friendship is sweet; everything about the Lord of Sweetness is sweet."
                    }
                ]
            },
            {
                "type": "verse",
                "label_hindi": "श्लोक 4",
                "label_english": "Verse 4",
                "lines": [
                    {
                        "hindi": "गीतं मधुरं पीतं मधुरं भुक्तं मधुरं सुप्तं मधुरम् ।",
                        "roman": "Geetam madhuram peetam madhuram bhuktam madhuram suptam madhuram",
                        "hindi_meaning": "उनके गीत मधुर हैं, उनका पीना मधुर है, उनका भोजन करना मधुर है, उनका शयन मधुर है।",
                        "english": "His song is sweet, His drinking is sweet, His eating is sweet, His sleeping is sweet."
                    },
                    {
                        "hindi": "रूपं मधुरं तिलकं मधुरं मधुराधिपतेरखिलं मधुरम् ॥४॥",
                        "roman": "Roopam madhuram tilakam madhuram madhuradhipaterakhilam madhuram",
                        "hindi_meaning": "उनका रूप मधुर है, उनका तिलक मधुर है; मधुरता के ईश्वर का सब कुछ मधुर है।",
                        "english": "His form is sweet, His tilak is sweet; everything about the Lord of Sweetness is sweet."
                    }
                ]
            },
            {
                "type": "verse",
                "label_hindi": "श्लोक 5",
                "label_english": "Verse 5",
                "lines": [
                    {
                        "hindi": "करणं मधुरं तरणं मधुरं हरणं मधुरं रमणं मधुरम् ।",
                        "roman": "Karanam madhuram taranam madhuram haranam madhuram ramanam madhuram",
                        "hindi_meaning": "उनके कार्य मधुर हैं, उनका उद्धार करना मधुर है, उनका चोरी करना (माखन) मधुर है, उनका प्रेम मधुर है।",
                        "english": "His deeds are sweet, His saving is sweet, His stealing is sweet, His love-play is sweet."
                    },
                    {
                        "hindi": "वमितं मधुरं शमितं मधुरं मधुराधिपतेरखिलं मधुरम् ॥५॥",
                        "roman": "Vamitam madhuram shamitam madhuram madhuradhipaterakhilam madhuram",
                        "hindi_meaning": "उनके शब्द मधुर हैं, उनका शांत रहना मधुर है; मधुरता के ईश्वर का सब कुछ मधुर है।",
                        "english": "His utterances are sweet, His peace is sweet; everything about the Lord of Sweetness is sweet."
                    }
                ]
            },
            {
                "type": "verse",
                "label_hindi": "श्लोक 6",
                "label_english": "Verse 6",
                "lines": [
                    {
                        "hindi": "गुञ्जा मधुरा माला मधुरा यमुना मधुरा वीची मधुरा ।",
                        "roman": "Gunja madhura mala madhura yamuna madhura veechi madhura",
                        "hindi_meaning": "उनकी गुंजा की माला मधुर है, यमुना नदी मधुर है, उसकी लहरें मधुर हैं।",
                        "english": "His berry necklace is sweet, His garland is sweet, the Yamuna river is sweet, its waves are sweet."
                    },
                    {
                        "hindi": "सलिलं मधुरं कमलं मधुरं मधुराधिपतेरखिलं मधुरम् ॥६॥",
                        "roman": "Salilam madhuram kamalam madhuram madhuradhipaterakhilam madhuram",
                        "hindi_meaning": "उसका जल मधुर है, उसके कमल मधुर हैं; मधुरता के ईश्वर का सब कुछ मधुर है।",
                        "english": "Its water is sweet, its lotuses are sweet; everything about the Lord of Sweetness is sweet."
                    }
                ]
            },
            {
                "type": "verse",
                "label_hindi": "श्लोक 7",
                "label_english": "Verse 7",
                "lines": [
                    {
                        "hindi": "गोपी मधुरा लीला मधुरा युक्तं मधुरं मुक्तं मधुरम् ।",
                        "roman": "Gopi madhura leela madhura yuktam madhuram muktam madhuram",
                        "hindi_meaning": "गोपियाँ मधुर हैं, उनकी लीलाएँ मधुर हैं, उनका मिलन मधुर है, उनका बिछड़ना मधुर है।",
                        "english": "His Gopis are sweet, His pastimes are sweet, union with Him is sweet, liberation from Him is sweet."
                    },
                    {
                        "hindi": "दृष्टं मधुरं शिष्टं मधुरं मधुराधिपतेरखिलं मधुरम् ॥७॥",
                        "roman": "Drishtam madhuram shishtam madhuram madhuradhipaterakhilam madhuram",
                        "hindi_meaning": "उनका देखना मधुर है, उनका शिष्टाचार मधुर है; मधुरता के ईश्वर का सब कुछ मधुर है।",
                        "english": "His glance is sweet, His etiquette is sweet; everything about the Lord of Sweetness is sweet."
                    }
                ]
            },
            {
                "type": "verse",
                "label_hindi": "श्लोक 8",
                "label_english": "Verse 8",
                "lines": [
                    {
                        "hindi": "गोपा मधुरा गावो मधुरा यष्टिर्मधुरा सृष्टिर्मधुरा ।",
                        "roman": "Gopa madhura gavo madhura yashtir madhura srishtir madhura",
                        "hindi_meaning": "गोप मधुर हैं, गाएं मधुर हैं, उनकी छड़ी मधुर है, उनकी सृष्टि मधुर है।",
                        "english": "His cowherd friends are sweet, His cows are sweet, His staff is sweet, His creation is sweet."
                    },
                    {
                        "hindi": "दलितं मधुरं फलितं मधुरं मधुराधिपतेरखिलं मधुरम् ॥८॥",
                        "roman": "Dalitam madhuram phalitam madhuram madhuradhipaterakhilam madhuram",
                        "hindi_meaning": "उनका विनाश करना मधुर है, उनका फल देना मधुर है; मधुरता के ईश्वर का सब कुछ मधुर है।",
                        "english": "His trampling is sweet, His fruitfulness is sweet; everything about the Lord of Sweetness is sweet."
                    }
                ]
            }
        ]
        
    if b['slug'] == 'shri-ramachandra-kripalu':
        b['verses'] = [
            {
                "type": "verse",
                "label_hindi": "पद 1",
                "label_english": "Verse 1",
                "lines": [
                    {
                        "hindi": "श्रीरामचन्द्र कृपालु भजु मन हरण भवभय दारुणम् ।",
                        "roman": "Shri Ramachandra kripalu bhaju man haran bhavbhay daarunam",
                        "hindi_meaning": "हे मन! कृपालु श्री रामचन्द्र जी का भजन कर, जो संसार के सभी जन्म-मरण रूपी दारुण भयों को हरने वाले हैं।",
                        "english": "O mind! Sing praises of the merciful Lord Ramachandra, who removes the dreadful fears of worldly existence."
                    },
                    {
                        "hindi": "नव कंज लोचन कंज मुख कर कंज पद कंजारुणम् ॥",
                        "roman": "Nav kanj lochan kanj mukh kar kanj pad kanjarunam",
                        "hindi_meaning": "उनके नेत्र, मुख और हाथ नवीन कमल के समान हैं और उनके चरण लाल कमल के समान हैं।",
                        "english": "His eyes, face, and hands are like blooming lotuses, and His feet are like red lotuses."
                    }
                ]
            },
            {
                "type": "verse",
                "label_hindi": "पद 2",
                "label_english": "Verse 2",
                "lines": [
                    {
                        "hindi": "कंदर्प अगणित अमित छबि नवनील नीरद सुन्दरम् ।",
                        "roman": "Kandarpa aganit amit chhabi navaneel neerada sundaram",
                        "hindi_meaning": "उनकी अपार छवि अनगिनत कामदेवों से भी बढ़कर है, और उनका शरीर नए नीले बादलों के समान सुंदर है।",
                        "english": "His boundless beauty surpasses countless cupids, and His body is as beautiful as a fresh blue raincloud."
                    },
                    {
                        "hindi": "पट पीत मानहु तडित रुचि शुची नौमि जनक सुतावरम् ॥",
                        "roman": "Pat peet maanahu tadit ruchi shuchi naumi janak sutaavaram",
                        "hindi_meaning": "उनके पीले वस्त्रों में बिजली जैसी चमक है, ऐसे परम पवित्र माता सीता के पति श्री राम को मैं नमस्कार करता हूँ।",
                        "english": "His yellow robes shine with the brilliance of lightning; I bow to the pure Lord, the consort of Janaka's daughter."
                    }
                ]
            },
            {
                "type": "verse",
                "label_hindi": "पद 3",
                "label_english": "Verse 3",
                "lines": [
                    {
                        "hindi": "भजु दीनबन्धु दिनेश दानव दैत्यवंश निकन्दनम् ।",
                        "roman": "Bhaju deenabandhu dinesh daanav daityavansh nikandanam",
                        "hindi_meaning": "हे मन! दीनों के बंधु, सूर्य के समान तेजस्वी, और दानव-दैत्यों के वंश का नाश करने वाले प्रभु का भजन कर।",
                        "english": "O mind! Worship the friend of the poor, radiant as the sun, the destroyer of the demon race."
                    },
                    {
                        "hindi": "रघुनन्द आनन्दकन्द कोशल चन्द दशरथ नन्दनम् ॥",
                        "roman": "Raghunand aanandakand koshal chand dasharath nandanam",
                        "hindi_meaning": "जो रघुकुल के आनंद के मूल हैं, कोसलपुर के चंद्रमा हैं और राजा दशरथ के पुत्र हैं।",
                        "english": "The joy of the Raghu dynasty, the root of bliss, the moon of Kosala, and the beloved son of Dasharatha."
                    }
                ]
            },
            {
                "type": "verse",
                "label_hindi": "पद 4",
                "label_english": "Verse 4",
                "lines": [
                    {
                        "hindi": "शिर मुकुट कुंडल तिलक चारु उदार अङ्ग विभूषणम् ।",
                        "roman": "Shir mukut kundal tilak chaaru udaar ang vibhooshanam",
                        "hindi_meaning": "जिनके सिर पर मुकुट, कानों में कुंडल, माथे पर सुंदर तिलक और प्रत्येक अंग पर सुंदर आभूषण हैं।",
                        "english": "Who wears a crown on His head, earrings, a beautiful tilak, and splendid ornaments on every limb."
                    },
                    {
                        "hindi": "आजानुभुज शर चाप धर संग्राम जित खरदूषणम् ॥",
                        "roman": "Aajaanubhuj shar chaap dhar sangraam jit kharadooshanam",
                        "hindi_meaning": "जिनकी भुजाएँ घुटनों तक लंबी हैं, जो धनुष-बाण धारण करते हैं और जिन्होंने संग्राम में खर और दूषण को जीता था।",
                        "english": "Whose arms reach His knees, holding a bow and arrow, the victor over demons Khar and Dushan in battle."
                    }
                ]
            },
            {
                "type": "verse",
                "label_hindi": "पद 5",
                "label_english": "Verse 5",
                "lines": [
                    {
                        "hindi": "इति वदति तुलसीदास शंकर शेष मुनि मन रंजनम् ।",
                        "roman": "Iti vadati Tulsidas shankar shesh muni man ranjanam",
                        "hindi_meaning": "तुलसीदास कहते हैं कि जो भगवान शिव, शेषनाग और मुनियों के मन को आनंदित करने वाले हैं, उनका भजन कर।",
                        "english": "Tulsidas says, sing of Him who brings delight to the minds of Lord Shiva, Sheshanaga, and the sages."
                    },
                    {
                        "hindi": "मम हृदय कंज निवास कुरु कामादि खल दल गंजनम् ॥",
                        "roman": "Mam hriday kanj nivaas kuru kaamadi khal dal ganjanam",
                        "hindi_meaning": "और जो काम, क्रोध आदि दुष्टों के दल का नाश करने वाले हैं, वे प्रभु मेरे हृदय रूपी कमल में निवास करें।",
                        "english": "May He, the destroyer of the host of wicked enemies like lust, dwell forever in the lotus of my heart."
                    }
                ]
            }
        ]

    if b['slug'] == 'vaishnav-jan':
        b['verses'] = [
            {
                "type": "verse",
                "label_hindi": "पद 1",
                "label_english": "Verse 1",
                "lines": [
                    {
                        "hindi": "वैष्णव जन तो तेने कहिये जे पीर परायी जाणे रे।",
                        "roman": "Vaishnav jan to tene kahiye je peer paraayi jaane re",
                        "hindi_meaning": "सच्चा वैष्णव (भगवान का भक्त) वही है जो दूसरों की पीड़ा को जानता और समझता है।",
                        "english": "Call him a true Vaishnava (devotee of Lord Vishnu) who feels the pain of others."
                    },
                    {
                        "hindi": "पर दुःखे उपकार करे तोये मन अभिमान न आणे रे॥",
                        "roman": "Par dukhe upakaar kare toye man abhimaan na aane re",
                        "hindi_meaning": "वह दूसरों के दुखों को दूर करता है, फिर भी अपने मन में कोई अभिमान नहीं लाता।",
                        "english": "He helps those who are in misery, yet never lets pride enter his mind."
                    }
                ]
            },
            {
                "type": "verse",
                "label_hindi": "पद 2",
                "label_english": "Verse 2",
                "lines": [
                    {
                        "hindi": "सकल लोकमां सहुने वंदे, निंदा न करे केनी रे।",
                        "roman": "Sakal lokama sahune vande, ninda na kare keni re",
                        "hindi_meaning": "वह पूरे विश्व में सबका सम्मान करता है और किसी की भी निंदा नहीं करता।",
                        "english": "He respects everyone in the entire world, and does not speak ill of anyone."
                    },
                    {
                        "hindi": "वाच काछ मन निश्चल राखे, धन धन जननी तेनी रे॥",
                        "roman": "Vaach kaachh man nishchal raakhe, dhan dhan janani teni re",
                        "hindi_meaning": "वह अपनी वाणी, कर्म और मन को पवित्र रखता है। ऐसी आत्मा को जन्म देने वाली माता धन्य है।",
                        "english": "He keeps his words, actions, and mind pure. Blessed is the mother who gave birth to such a soul."
                    }
                ]
            },
            {
                "type": "verse",
                "label_hindi": "पद 3",
                "label_english": "Verse 3",
                "lines": [
                    {
                        "hindi": "समदृष्टि ने तृष्णा त्यागी, परस्त्री जेने मात रे।",
                        "roman": "Samadrishti ne trishna tyaagi, parastree jene maat re",
                        "hindi_meaning": "वह सभी को समान दृष्टि से देखता है, उसने लालच त्याग दिया है, और पराई स्त्री उसके लिए माता के समान है।",
                        "english": "He views everyone equally, has renounced all desires, and regards another man's wife as his mother."
                    },
                    {
                        "hindi": "जिह्वा थकी असत्य न बोले, परधन नव झाले हाथ रे॥",
                        "roman": "Jihva thaki asatya na bole, paradhan nav jhaale haath re",
                        "hindi_meaning": "उसकी जीभ कभी झूठ नहीं बोलती, और वह दूसरे के धन को हाथ भी नहीं लगाता।",
                        "english": "His tongue never speaks a lie, and he never touches another's wealth."
                    }
                ]
            },
            {
                "type": "verse",
                "label_hindi": "पद 4",
                "label_english": "Verse 4",
                "lines": [
                    {
                        "hindi": "मोह माया व्यापे नहि जेने, दृढ़ वैराग्य जेना मनमां रे।",
                        "roman": "Moh maaya vyaape nahi jene, dridh vairaagya jena manama re",
                        "hindi_meaning": "मोह और माया उसे जकड़ नहीं पाते, और उसके मन में संसार के प्रति दृढ़ वैराग्य होता है।",
                        "english": "Worldly attachments and illusions do not entangle him; his mind is firmly rooted in detachment."
                    },
                    {
                        "hindi": "रामनाम शुं ताळी लागी, सकल तीरथ तेना तनमां रे॥",
                        "roman": "Ramnaam shun taali laagi, sakal teerath tena tanama re",
                        "hindi_meaning": "वह सदैव राम-नाम की धुन में मग्न रहता है, और उसके शरीर में ही सभी तीर्थों का वास है।",
                        "english": "He is constantly immersed in the name of Lord Ram; all the holy pilgrimage sites reside within his own body."
                    }
                ]
            },
            {
                "type": "verse",
                "label_hindi": "पद 5",
                "label_english": "Verse 5",
                "lines": [
                    {
                        "hindi": "वणलोभी ने कपटरहित छे, काम क्रोध निवार्या रे।",
                        "roman": "Vanlobhi ne kapatrahit chhe, kaam krodh nivaarya re",
                        "hindi_meaning": "वह लोभ और कपट से पूरी तरह मुक्त है, और उसने काम तथा क्रोध पर विजय प्राप्त कर ली है।",
                        "english": "He is free from greed and deceit, and has completely conquered lust and anger."
                    },
                    {
                        "hindi": "भणे नरसैयो तेनुं दर्शन करतां, कुळ एकोतेर तार्या रे॥",
                        "roman": "Bhane Narsaiyo tenu darshan karata, kul ekoter taarya re",
                        "hindi_meaning": "कवि नरसी मेहता कहते हैं कि ऐसे व्यक्ति के दर्शन मात्र से व्यक्ति की इकहत्तर पीढ़ियों का उद्धार हो जाता है।",
                        "english": "Poet Narsi Mehta says, merely catching sight of such a person saves one's seventy-one generations."
                    }
                ]
            }
        ]

with open('data/bhajans.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
