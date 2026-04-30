import json

with open('data/wisdom.json', 'r') as f:
    data = json.load(f)

for t in data['topics']:
    if t['title_english'] == 'Morning Wisdom':
        t['quotes'] = [
            {
                "id": "w011-q001",
                "source": "Rig Veda",
                "source_ref": "Rig Veda 3.62.10 (Gayatri Mantra)",
                "sanskrit": "तत्सवितुर्वरेण्यं भर्गो देवस्य धीमहि। धियो यो नः प्रचोदयात्॥",
                "roman": "Tat Savitur Varenyam Bhargo Devasya Dhimahi. Dhiyo Yo Nah Prachodayat.",
                "hindi": "हम उस प्राणस्वरूप, दुःखनाशक, सुखस्वरूप, श्रेष्ठ, तेजस्वी, पापनाशक, देवस्वरूप परमात्मा को अंतरात्मा में धारण करें। वह परमात्मा हमारी बुद्धि को सन्मार्ग में प्रेरित करे।",
                "english": "We meditate on the adorable glory of the radiant sun; may he inspire our intelligence.",
                "application_english": "Start your day by invoking the highest intelligence. The morning sets the tone for your entire day; beginning with a prayer for clarity ensures you make wise decisions.",
                "application_hindi": "अपने दिन की शुरुआत सर्वोच्च बुद्धि का आह्वान करके करें। सुबह की प्रार्थना आपके पूरे दिन को सही दिशा देती है और स्पष्टता लाती है।",
                "tags": ["morning", "clarity", "intelligence"]
            },
            {
                "id": "w011-q002",
                "source": "Bhagavad Gita",
                "source_ref": "Bhagavad Gita 2.47",
                "sanskrit": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन।",
                "roman": "Karmanyevadhikaraste Ma Phaleshu Kadachana.",
                "hindi": "तुम्हारा अधिकार केवल कर्म करने में है, उसके फलों में कभी नहीं।",
                "english": "You have a right to perform your prescribed duty, but you are not entitled to the fruits of action.",
                "application_english": "As you begin your workday, focus entirely on your actions and efforts rather than obsessing over outcomes. This removes morning anxiety and replaces it with focused energy.",
                "application_hindi": "अपने दिन की शुरुआत करते समय, परिणामों की चिंता करने के बजाय पूरी तरह से अपने कर्मों और प्रयासों पर ध्यान केंद्रित करें। इससे चिंता दूर होती है।",
                "tags": ["action", "focus", "morning"]
            }
        ]
    elif t['title_english'] == 'Forgiveness':
        t['quotes'] = [
            {
                "id": "w012-q001",
                "source": "Mahabharata",
                "source_ref": "Vana Parva",
                "sanskrit": "क्षमा ब्रह्म क्षमा सत्यं क्षमा भूतं च भावि च। क्षमा तपः क्षमा शौचं क्षमयेदं धृतं जगत्॥",
                "roman": "Kshama Brahma Kshama Satyam Kshama Bhutam Cha Bhavi Cha. Kshama Tapah Kshama Shaucham Kshamayedam Dhritam Jagat.",
                "hindi": "क्षमा ब्रह्म है, क्षमा सत्य है, क्षमा ही भूत और भविष्य है। क्षमा तप है, क्षमा पवित्रता है और क्षमा ने ही इस संपूर्ण जगत को धारण किया हुआ है।",
                "english": "Forgiveness is Brahma, forgiveness is truth, forgiveness is past and future. Forgiveness is austerity, forgiveness is purity, and by forgiveness is the universe held together.",
                "application_english": "Forgiveness is not a sign of weakness; it is the ultimate strength that sustains life. Letting go of past grievances purifies your own mind and liberates you from carrying the weight of anger.",
                "application_hindi": "क्षमा कमजोरी नहीं, बल्कि जीवन को बनाए रखने वाली परम शक्ति है। पुरानी शिकायतों को छोड़ना आपके मन को शुद्ध करता है और क्रोध के बोझ से मुक्त करता है।",
                "tags": ["forgiveness", "strength", "purity"]
            },
            {
                "id": "w012-q002",
                "source": "Bhagavad Gita",
                "source_ref": "Bhagavad Gita 16.3",
                "sanskrit": "तेजः क्षमा धृतिः शौचमद्रोहो नातिमानिता। भवन्ति सम्पदं दैवीमभिजातस्य भारत॥",
                "roman": "Tejaḥ kṣamā dhṛtiḥ śaucam adroho nātimānitā. Bhavanti sampadaṃ daivīm abhijātasya bhārata.",
                "hindi": "तेज, क्षमा, धैर्य, पवित्रता, किसी से शत्रुता न रखना और अभिमान न करना — हे भरतवंशी, ये दैवी प्रकृति को प्राप्त हुए व्यक्ति के लक्षण हैं।",
                "english": "Vigor, forgiveness, fortitude, purity, freedom from envy and from the passion for honor—these belong to the one endowed with divine nature, O descendant of Bharata.",
                "application_english": "Forgiveness (Kshama) is considered a divine quality. Practicing it brings you closer to your higher spiritual self and protects your inner peace from being hijacked by others' actions.",
                "application_hindi": "क्षमा एक दैवी गुण है। इसका अभ्यास आपको आध्यात्मिक रूप से उन्नत करता है और आपकी आंतरिक शांति की रक्षा करता है।",
                "tags": ["divine qualities", "peace", "forgiveness"]
            }
        ]

with open('data/wisdom.json', 'w') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Populated Wisdom topics.")
