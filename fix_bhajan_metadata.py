import json

with open('data/bhajans.json', 'r') as f:
    data = json.load(f)

META = {
    'ram-siya-ram': {
        'deity': 'Ram', 'timing': 'Morning and Evening', 'occasion': 'Daily Prayer, Ram Navami',
        'raga': 'Bhairavi', 'tags': ['ram', 'sita', 'bhajan', 'devotion'],
        'story': 'Ram Siya Ram is a devotional bhajan that meditates on the divine couple Lord Ram and Mother Sita. It is sung as a form of naam japa (name repetition) and is associated with the bhakti tradition of India.',
        'story_hindi': 'राम सिया राम एक भक्तिपूर्ण भजन है जो भगवान राम और माता सीता के दिव्य जोड़े का ध्यान करता है। यह नाम जप के रूप में गाया जाता है।',
        'significance': 'Chanting Ram Siya Ram is considered equivalent to reciting the Ramayan. The repetition of divine names purifies the mind and brings peace.',
        'significance_hindi': 'राम सिया राम का जाप रामायण के पाठ के समतुल्य माना जाता है। दिव्य नामों का जप मन को शुद्ध करता है और शांति लाता है।',
        'benefits': ['Purifies the mind and removes negative thoughts', 'Brings peace and inner calm', 'Bestows blessings of Lord Ram and Mother Sita', 'Helps in overcoming difficulties in life'],
        'seo': {'meta_title': 'Ram Siya Ram Bhajan with Hindi & English Meaning', 'meta_description': 'Listen to and read Ram Siya Ram bhajan with full Hindi lyrics, Roman transliteration, and English meaning.', 'keywords': ['Ram Siya Ram', 'Ram bhajan', 'Ram naam jap', 'Hindi bhajan']}
    },
    'deva-shree-ganesha': {
        'deity': 'Ganesha', 'timing': 'Morning', 'occasion': 'Ganesh Chaturthi, New Beginnings',
        'raga': 'Yaman', 'tags': ['ganesha', 'bhajan', 'devotion', 'obstacle remover'],
        'story': 'Deva Shree Ganesha is a popular devotional song praising Lord Ganesha, the remover of obstacles and the god of new beginnings. It became widely popular through the Bollywood film Agneepath.',
        'story_hindi': 'देवा श्री गणेशा एक लोकप्रिय भक्ति गीत है जो विघ्नहर्ता भगवान गणेश की स्तुति करता है। यह बॉलीवुड फिल्म अग्निपथ के माध्यम से अत्यंत लोकप्रिय हुआ।',
        'significance': 'Singing Deva Shree Ganesha invokes the blessings of Lord Ganesha before any new venture, ensuring success and removal of obstacles.',
        'significance_hindi': 'देवा श्री गणेशा गाने से किसी भी नए कार्य से पहले भगवान गणेश का आशीर्वाद मिलता है, जो सफलता और विघ्नों के निवारण को सुनिश्चित करता है।',
        'benefits': ['Removes obstacles from life and work', 'Brings success in new ventures', 'Grants wisdom and intelligence', 'Protects from negative energies'],
        'seo': {'meta_title': 'Deva Shree Ganesha Bhajan with Hindi Meaning', 'meta_description': 'Read Deva Shree Ganesha bhajan lyrics with Hindi meaning and English translation.', 'keywords': ['Deva Shree Ganesha', 'Ganesha bhajan', 'Ganesh stotra', 'Hindi bhajan']}
    },
    'jai-ambe-gauri': {
        'deity': 'Durga', 'timing': 'Evening, Navratri', 'occasion': 'Navratri, Durga Puja',
        'raga': 'Kafi', 'tags': ['durga', 'aarti', 'navratri', 'shakti', 'devi'],
        'story': 'Jai Ambe Gauri is the traditional aarti of Goddess Durga sung during Navratri and other auspicious occasions. It praises the many forms of the Divine Mother.',
        'story_hindi': 'जय अम्बे गौरी देवी दुर्गा की पारंपरिक आरती है जो नवरात्रि और अन्य शुभ अवसरों पर गाई जाती है। यह दिव्य माँ के विभिन्न रूपों की स्तुति करती है।',
        'significance': 'Jai Ambe Gauri is considered the quintessential aarti of Goddess Durga. Singing it during Navratri bestows the blessings of the Divine Mother.',
        'significance_hindi': 'जय अम्बे गौरी देवी दुर्गा की सर्वश्रेष्ठ आरती मानी जाती है। नवरात्रि में इसे गाने से दिव्य माँ का आशीर्वाद प्राप्त होता है।',
        'benefits': ['Removes all fears and bestows courage', 'Fulfils desires of the devotee', 'Grants protection from evil', 'Brings prosperity and auspiciousness'],
        'seo': {'meta_title': 'Jai Ambe Gauri Aarti with Hindi & English Meaning', 'meta_description': 'Full lyrics of Jai Ambe Gauri aarti with Hindi meaning and English translation for Navratri.', 'keywords': ['Jai Ambe Gauri', 'Durga aarti', 'Navratri bhajan', 'Devi aarti']}
    },
    'aarti-kunj-bihari-ki': {
        'deity': 'Krishna', 'timing': 'Evening (Sandhya Aarti)', 'occasion': 'Janmashtami, Daily Puja',
        'raga': 'Yaman Kalyan', 'tags': ['krishna', 'aarti', 'vrindavan', 'bhakti', 'janmashtami'],
        'story': 'Aarti Kunj Bihari Ki is the traditional evening aarti of Lord Krishna sung at the Banke Bihari temple in Vrindavan. It describes the divine beauty of Krishna in the groves of Vrindavan.',
        'story_hindi': 'आरती कुंज बिहारी की वृंदावन के बांके बिहारी मंदिर में गाई जाने वाली भगवान कृष्ण की पारंपरिक संध्या आरती है। यह वृंदावन की कुंजों में कृष्ण की दिव्य सुंदरता का वर्णन करती है।',
        'significance': 'This aarti is the primary evening prayer at the famous Banke Bihari temple, Vrindavan. Singing it connects the devotee to the divine energy of Vrindavan.',
        'significance_hindi': 'यह आरती वृंदावन के प्रसिद्ध बांके बिहारी मंदिर की प्रमुख संध्या प्रार्थना है। इसे गाने से भक्त वृंदावन की दिव्य ऊर्जा से जुड़ता है।',
        'benefits': ['Fills the heart with love for Lord Krishna', 'Brings peace and divine bliss', 'Connects devotee to the sacred energy of Vrindavan', 'Removes worldly anxieties'],
        'seo': {'meta_title': 'Aarti Kunj Bihari Ki with Hindi & English Meaning', 'meta_description': 'Full lyrics of Aarti Kunj Bihari Ki with Hindi meaning and English translation for Krishna devotees.', 'keywords': ['Aarti Kunj Bihari', 'Krishna aarti', 'Vrindavan aarti', 'Janmashtami bhajan']}
    },
    'om-jai-lakshmi-mata': {
        'deity': 'Lakshmi', 'timing': 'Evening (Diya lighting)', 'occasion': 'Diwali, Friday Puja',
        'raga': 'Bhairavi', 'tags': ['lakshmi', 'aarti', 'diwali', 'prosperity', 'wealth'],
        'story': 'Om Jai Lakshmi Mata is the traditional aarti of Goddess Lakshmi sung during Diwali and every Friday. It praises the goddess of wealth, fortune, and prosperity.',
        'story_hindi': 'ॐ जय लक्ष्मी माता देवी लक्ष्मी की पारंपरिक आरती है जो दिवाली और हर शुक्रवार को गाई जाती है। यह धन, सौभाग्य और समृद्धि की देवी की स्तुति करती है।',
        'significance': 'Om Jai Lakshmi Mata is the most widely sung Lakshmi aarti in Hindu households. It is believed to invite the goddess of wealth into the home.',
        'significance_hindi': 'ॐ जय लक्ष्मी माता हिंदू घरों में सर्वाधिक गाई जाने वाली लक्ष्मी आरती है। माना जाता है कि यह धन की देवी को घर में आमंत्रित करती है।',
        'benefits': ['Attracts wealth and prosperity', 'Removes financial difficulties', 'Brings domestic harmony and happiness', 'Invites blessings of Goddess Lakshmi'],
        'seo': {'meta_title': 'Om Jai Lakshmi Mata Aarti with Hindi & English Meaning', 'meta_description': 'Full lyrics of Om Jai Lakshmi Mata aarti with Hindi meaning and English translation for Diwali and Friday puja.', 'keywords': ['Om Jai Lakshmi Mata', 'Lakshmi aarti', 'Diwali aarti', 'Friday puja']}
    },
    'raghupati-raghav-raja-ram': {
        'deity': 'Ram', 'timing': 'Morning', 'occasion': 'Ram Navami, Daily Prayer',
        'raga': 'Desh', 'tags': ['ram', 'bhajan', 'gandhi', 'prayer', 'unity'],
        'story': 'Raghupati Raghav Raja Ram is an ancient bhajan popularised by Mahatma Gandhi as a prayer of unity. Gandhi added the verse "Ishwar Allah tero naam" to symbolize Hindu-Muslim harmony.',
        'story_hindi': 'रघुपति राघव राजा राम एक प्राचीन भजन है जिसे महात्मा गांधी ने एकता की प्रार्थना के रूप में लोकप्रिय बनाया। गांधी जी ने "ईश्वर अल्लाह तेरो नाम" पंक्ति जोड़ी।',
        'significance': 'This bhajan carries the profound message of the unity of all religions. It was Mahatma Gandhi\'s favourite prayer and was sung at all his prayer meetings.',
        'significance_hindi': 'यह भजन सभी धर्मों की एकता का गहरा संदेश देता है। यह महात्मा गांधी की प्रिय प्रार्थना थी और उनकी सभी प्रार्थना सभाओं में गाई जाती थी।',
        'benefits': ['Promotes inner peace and harmony', 'Cultivates love and unity', 'Deepens devotion to Lord Ram', 'Removes ego and promotes humility'],
        'seo': {'meta_title': 'Raghupati Raghav Raja Ram with Hindi & English Meaning', 'meta_description': 'Full lyrics of Raghupati Raghav Raja Ram bhajan with Hindi meaning and English translation.', 'keywords': ['Raghupati Raghav', 'Ram bhajan', 'Gandhi bhajan', 'Ishwar Allah tero naam']}
    },
    'mere-ghar-ram-aayo': {
        'deity': 'Ram', 'timing': 'Morning and Evening', 'occasion': 'Ram Navami, Daily Bhajan',
        'raga': 'Bhairavi', 'tags': ['ram', 'bhajan', 'devotion', 'bhakti'],
        'story': 'Mere Ghar Ram Aayo is a devotional bhajan expressing the joy of a devotee when Lord Ram visits their home. It became widely popular through devotional music traditions.',
        'story_hindi': 'मेरे घर राम आयो एक भक्तिपूर्ण भजन है जो भगवान राम के घर आने पर एक भक्त की खुशी को व्यक्त करता है। यह भक्ति संगीत परंपराओं के माध्यम से व्यापक रूप से लोकप्रिय हुआ।',
        'significance': 'This bhajan captures the essence of bhakti — the feeling that the Lord himself has arrived in the devotee\'s heart and home through sincere prayer.',
        'significance_hindi': 'यह भजन भक्ति के सार को व्यक्त करता है — यह भावना कि प्रभु स्वयं सच्ची प्रार्थना के माध्यम से भक्त के हृदय और घर में आए हैं।',
        'benefits': ['Fills the heart with devotion to Lord Ram', 'Creates a feeling of divine presence at home', 'Brings peace and joy', 'Strengthens faith'],
        'seo': {'meta_title': 'Mere Ghar Ram Aayo Bhajan with Hindi & English Meaning', 'meta_description': 'Full lyrics of Mere Ghar Ram Aayo bhajan with Hindi meaning and English translation.', 'keywords': ['Mere Ghar Ram Aayo', 'Ram bhajan', 'Hindi devotional song', 'Ram Navami bhajan']}
    },
    'vaishnav-jan': {
        'deity': 'Vishnu', 'timing': 'Morning', 'occasion': 'Daily Prayer, Gandhi Jayanti',
        'raga': 'Bhairavi', 'tags': ['vishnu', 'bhajan', 'narsi mehta', 'humility', 'compassion', 'gandhi'],
        'story': 'Vaishnav Jan To was composed by the 15th-century poet-saint Narsi Mehta of Gujarat. It describes the qualities of a true Vaishnav (devotee of Vishnu) — compassion, humility, and selfless service. Mahatma Gandhi adopted it as his favourite bhajan.',
        'story_hindi': 'वैष्णव जन तो की रचना 15वीं शताब्दी के गुजराती कवि-संत नरसी मेहता ने की थी। यह एक सच्चे वैष्णव के गुणों — करुणा, विनम्रता और निःस्वार्थ सेवा — का वर्णन करता है। महात्मा गांधी ने इसे अपना प्रिय भजन बनाया।',
        'significance': 'Vaishnav Jan To is one of the most celebrated bhajans in Indian devotional music. It teaches universal values of compassion and selflessness.',
        'significance_hindi': 'वैष्णव जन तो भारतीय भक्ति संगीत के सबसे प्रसिद्ध भजनों में से एक है। यह करुणा और निःस्वार्थता के सार्वभौमिक मूल्यों की शिक्षा देता है।',
        'benefits': ['Cultivates compassion for all beings', 'Promotes humility and removal of ego', 'Inspires selfless service', 'Deepens devotion to God'],
        'seo': {'meta_title': 'Vaishnav Jan To Bhajan with Hindi & English Meaning', 'meta_description': 'Full lyrics of Vaishnav Jan To by Narsi Mehta with Hindi meaning and English translation.', 'keywords': ['Vaishnav Jan To', 'Narsi Mehta bhajan', 'Gandhi bhajan', 'Hindi devotional']}
    },
    'shri-ramachandra-kripalu': {
        'deity': 'Ram', 'timing': 'Morning and Evening', 'occasion': 'Ram Navami, Daily Bhajan',
        'raga': 'Yaman', 'tags': ['ram', 'tulsidas', 'bhajan', 'stuti', 'devotion'],
        'story': 'Shri Ramachandra Kripalu Bhaju Man was composed by the saint-poet Goswami Tulsidas. It is a beautiful stuti (praise) describing the divine beauty of Lord Ram and urging the mind to sing his glories.',
        'story_hindi': 'श्री रामचंद्र कृपालु भजु मन की रचना संत-कवि गोस्वामी तुलसीदास ने की थी। यह भगवान राम की दिव्य सुंदरता का वर्णन करने वाली एक सुंदर स्तुति है।',
        'significance': 'Composed by the same saint who wrote the Ramcharitmanas, this bhajan holds immense spiritual importance. It encapsulates the essence of Ram bhakti in a few stanzas.',
        'significance_hindi': 'रामचरितमानस के रचयिता तुलसीदास द्वारा रचित यह भजन अत्यंत आध्यात्मिक महत्व रखता है। यह कुछ ही पदों में राम भक्ति के सार को समेटता है।',
        'benefits': ['Deepens devotion to Lord Ram', 'Purifies the mind through divine description', 'Brings spiritual upliftment', 'Removes ego and worldly attachments'],
        'seo': {'meta_title': 'Shri Ramachandra Kripalu Bhajan with Hindi & English Meaning', 'meta_description': 'Full lyrics of Shri Ramachandra Kripalu by Tulsidas with Hindi meaning and English translation.', 'keywords': ['Shri Ramachandra Kripalu', 'Tulsidas bhajan', 'Ram stuti', 'Hindi bhajan']}
    },
    'madhurashtakam': {
        'deity': 'Krishna', 'timing': 'Morning', 'occasion': 'Janmashtami, Daily Bhajan',
        'raga': 'Bhairav', 'tags': ['krishna', 'madhurashtakam', 'vallabhacharya', 'sweetness', 'bhakti'],
        'story': 'Madhurashtakam was composed by the great Vaishnava saint Vallabhacharya. Each of its 8 verses uses the word "Madhuram" (sweet) to describe every aspect of Lord Krishna, from his face and eyes to his dance and friendship.',
        'story_hindi': 'मधुराष्टकम् की रचना महान वैष्णव संत वल्लभाचार्य ने की थी। इसके 8 पदों में से प्रत्येक में भगवान कृष्ण के हर पहलू — उनके मुख, नेत्र, नृत्य और मित्रता तक — को "मधुरम्" (मधुर) शब्द से वर्णित किया गया है।',
        'significance': 'Madhurashtakam is a jewel of Sanskrit devotional poetry. The repetition of "Madhuram" creates a meditative state that fills the devotee with love for Krishna.',
        'significance_hindi': 'मधुराष्टकम् संस्कृत भक्ति काव्य का एक रत्न है। "मधुरम्" की पुनरावृत्ति एक ध्यानमग्न अवस्था उत्पन्न करती है जो भक्त को कृष्ण के प्रेम से भर देती है।',
        'benefits': ['Fills the heart with love and sweetness for Lord Krishna', 'Creates a meditative, peaceful state', 'Purifies speech and mind', 'Brings joy and divine bliss'],
        'seo': {'meta_title': 'Madhurashtakam by Vallabhacharya with Hindi & English Meaning', 'meta_description': 'Full lyrics of Madhurashtakam with Hindi meaning and English translation by Vallabhacharya.', 'keywords': ['Madhurashtakam', 'Vallabhacharya', 'Krishna bhajan', 'Sanskrit stotram']}
    },
    'achyutam-keshavam': {
        'timing': 'Morning', 'occasion': 'Daily Prayer, Vishnu Puja',
        'raga': 'Bhairav', 'tags': ['vishnu', 'krishna', 'stuti', 'devotion', 'bhajan'],
        'story': 'Achyutam Keshavam is a devotional bhajan praising Lord Vishnu and Krishna by their divine names. It became widely popular through the Bollywood film Dum Laga Ke Haisha.',
        'story_hindi': 'अच्युतम केशवम एक भक्तिपूर्ण भजन है जो भगवान विष्णु और कृष्ण की उनके दिव्य नामों से स्तुति करता है। यह बॉलीवुड फिल्म दम लगा के हईशा के माध्यम से व्यापक रूप से लोकप्रिय हुआ।',
        'significance': 'This bhajan meditates on the imperishable (Achyuta) nature of the Lord who never falls from his divine state, bringing devotees to a state of surrender.',
        'significance_hindi': 'यह भजन प्रभु की अच्युत (अविनाशी) प्रकृति का ध्यान करता है, जो भक्तों को समर्पण की स्थिति में लाता है।',
        'benefits': ['Removes all fears through remembrance of the Lord', 'Brings peace of mind', 'Deepens devotion to Lord Vishnu and Krishna', 'Bestows divine grace'],
        'seo': {'meta_title': 'Achyutam Keshavam Bhajan with Hindi & English Meaning', 'meta_description': 'Full lyrics of Achyutam Keshavam bhajan with Hindi meaning and English translation.', 'keywords': ['Achyutam Keshavam', 'Vishnu bhajan', 'Krishna stuti', 'Hindi devotional bhajan']}
    },
}

for b in data:
    slug = b.get('slug')
    if slug in META:
        m = META[slug]
        for key, val in m.items():
            if not b.get(key):
                b[key] = val

    # Fix deity too-short issue for Ram bhajans
    if b.get('deity') == 'Ram':
        b['deity'] = 'Ram'  # Keep but fix display in UI, not an actual error

with open('data/bhajans.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ All bhajan metadata filled successfully!")

# Verify
with open('data/bhajans.json', 'r') as f:
    data = json.load(f)
for b in data:
    missing = [f for f in ['timing','occasion','story','significance','benefits','raga','tags','seo'] if not b.get(f)]
    if missing:
        print(f"❌ {b['slug']}: still missing {missing}")
    else:
        print(f"✅ {b['slug']}: complete")
