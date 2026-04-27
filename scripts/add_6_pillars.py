import json
import os

def get_max_id(items):
    return max([item.get('id', 0) for item in items], default=0)

# 1. Bhajans
with open('data/bhajans.json', 'r', encoding='utf-8') as f:
    bhajans = json.load(f)

new_bhajan = {
    "id": get_max_id(bhajans) + 1,
    "slug": "govind-bolo-hari-gopal-bolo",
    "title_hindi": "गोविंद बोलो हरि गोपाल बोलो",
    "title_roman": "Govind Bolo Hari Gopal Bolo",
    "title_english": "Chant the Name of Govind and Hari",
    "deity": "Krishna",
    "deity_color": "#1E3A8A",
    "language": "Hindi",
    "festival": ["Janmashtami", "Holi"],
    "occasion": "Kirtan, Daily Devotion",
    "timing": "Anytime",
    "raga": "Desh/Pahari",
    "composer": "Traditional",
    "duration_minutes": 5,
    "tags": ["krishna", "govind", "hari", "kirtan", "joy"],
    "description_hindi": "भगवान कृष्ण के नामों का एक अत्यंत लोकप्रिय और आनंदमयी कीर्तन।",
    "description_english": "A highly popular and joyful kirtan chanting the holy names of Lord Krishna.",
    "lyrics": [
        {
            "type": "refrain",
            "label_hindi": "स्थायी",
            "label_english": "Refrain",
            "lines": [
                {
                    "hindi": "गोविंद बोलो हरि गोपाल बोलो।",
                    "roman": "Govind bolo Hari Gopal bolo.",
                    "hindi_meaning": "गोविंद (कृष्ण) का नाम जपो, हरि और गोपाल का नाम जपो।",
                    "english": "Chant the name of Govind, chant the name of Hari and Gopal."
                },
                {
                    "hindi": "राधा रमण हरि गोविंद बोलो॥",
                    "roman": "Radha raman Hari Govind bolo.",
                    "hindi_meaning": "राधा को आनंद देने वाले हरि और गोविंद का नाम जपो।",
                    "english": "Chant the name of Hari and Govind, who brings joy to Radha."
                }
            ],
            "source_name": "Traditional Kirtan",
            "source_ref": "Common tradition",
            "source_line_index": ""
        }
    ],
    "related": ["achyutam-keshavam"],
    "seo": {
        "meta_title": "Govind Bolo Hari Gopal Bolo - Krishna Bhajan & Kirtan | Sanatan Gyan Sagar",
        "meta_description": "Sing Govind Bolo Hari Gopal Bolo with Hindi meaning and English translation. Experience the joy of Krishna Kirtan.",
        "keywords": ["govind bolo", "krishna kirtan", "hare krishna"]
    },
    "source_name": "Traditional",
    "source_ref": "Oral tradition",
    "source_edition": "General",
    "is_excerpt": False,
    "excerpt_range": "full",
    "verification_notes": "1000% safe, universally accepted kirtan. No beej mantras."
}
bhajans.append(new_bhajan)
with open('data/bhajans.json', 'w', encoding='utf-8') as f:
    json.dump(bhajans, f, indent=2, ensure_ascii=False)

# 2. Shlokas
with open('data/shlokas.json', 'r', encoding='utf-8') as f:
    shlokas = json.load(f)

new_shloka = {
    "id": get_max_id(shlokas) + 1,
    "slug": "guru-stotram",
    "title_hindi": "गुरु स्तोत्रम् (गुरुर्ब्रह्मा)",
    "title_english": "Guru Stotram (Gurur Brahma)",
    "sanskrit": "गुरुर्ब्रह्मा गुरुर्विष्णुः गुरुर्देवो महेश्वरः।\nगुरुः साक्षात् परब्रह्म तस्मै श्रीगुरवे नमः॥",
    "hindi": "गुरु ही ब्रह्मा हैं, गुरु ही विष्णु हैं, गुरु ही देव महेश्वर (शिव) हैं।\nगुरु ही साक्षात् परब्रह्म हैं, उन श्री गुरु को मेरा नमस्कार है।",
    "roman": "Gurur Brahma Gurur Vishnu, Gurur Devo Maheshwarah.\nGuru Sakshat Parabrahma, Tasmai Shri Gurave Namah.",
    "english": "The Guru is Brahma, the Guru is Vishnu, the Guru is Lord Maheshwara (Shiva).\nThe Guru is verily the Supreme Absolute, Salutations to that revered Guru.",
    "word_by_word": [
        {"sanskrit": "गुरुः", "roman": "guruh", "english": "Guru/Teacher"},
        {"sanskrit": "ब्रह्मा", "roman": "brahma", "english": "Creator"}
    ],
    "commentary_hindi": "यह स्तोत्र गुरु की महिमा का गान करता है, उन्हें त्रिदेवों और परब्रह्म के समान मानता है।",
    "commentary_english": "This verse glorifies the Guru, equating the spiritual teacher with the Holy Trinity and the Supreme Absolute.",
    "deity": "Guru",
    "source": "Skanda Purana (Guru Gita)",
    "tags": ["guru", "teacher", "wisdom", "gratitude"],
    "audio_hint": "Slow and reverent chant.",
    "related_shlokas": [],
    "cross_links": [],
    "featured": True,
    "priority": 1,
    "occasion": "Before studies, honoring teachers",
    "source_name": "Skanda Purana",
    "source_ref": "Guru Gita",
    "source_edition": "Traditional",
    "source_color": "#FF8C00",
    "is_excerpt": True,
    "excerpt_range": "Verse 1",
    "verification_notes": "1000% safe, universal verse. No beej mantras."
}
shlokas.append(new_shloka)
with open('data/shlokas.json', 'w', encoding='utf-8') as f:
    json.dump(shlokas, f, indent=2, ensure_ascii=False)

# 3. Prayers
with open('data/prayers.json', 'r', encoding='utf-8') as f:
    prayers_data = json.load(f)

prayers = prayers_data['prayers']
new_prayer = {
    "id": get_max_id(prayers) + 1,
    "slug": "bhojan-mantra",
    "title_hindi": "भोजन मन्त्र",
    "title_english": "Food Blessing (Bhojan Mantra)",
    "deity": "Annapurna",
    "deity_color": "#22C55E",
    "occasion": "Before meals",
    "duration_minutes": 1,
    "difficulty": "Beginner",
    "language": "Sanskrit",
    "intro_hindi": "भोजन करने से पूर्व अन्नदेवता और परमात्मा को धन्यवाद देने का मन्त्र।",
    "intro_english": "A mantra chanted before meals to offer gratitude to the Divine for the food.",
    "materials_needed": ["Food"],
    "steps": [
        {
            "step_number": 1,
            "title_hindi": "हाथ जोड़कर मन्त्र बोलें",
            "title_english": "Join hands and chant",
            "instruction_hindi": "भोजन को प्रणाम करें और 'ब्रह्मार्पणं ब्रह्म हविः...' बोलें।",
            "instruction_english": "Respect the food and chant 'Brahmarpanam Brahma Havih...'.",
            "mantras": [
                {
                    "sanskrit": "ब्रह्मार्पणं ब्रह्म हविर्ब्रह्माग्नौ ब्रह्मणा हुतम्।\nब्रह्मैव तेन गन्तव्यं ब्रह्मकर्मसमाधिना॥",
                    "roman": "Brahmārpaṇaṁ brahma havir brahmāgnau brahmaṇā hutam.\nBrahmaiva tena gantavyaṁ brahma-karma-samādhinā.",
                    "meaning_hindi": "समर्पण की क्रिया ब्रह्म है, हवि ब्रह्म है, अग्नि ब्रह्म है। जो कर्म में ब्रह्म देखता है, वह ब्रह्म को प्राप्त होता है।",
                    "meaning_english": "The act of offering is Brahman, the oblation is Brahman. Brahman alone is attained by him who sees Brahman in all actions."
                }
            ],
            "is_core_mantra": True
        }
    ],
    "benefits": ["Cultivates gratitude", "Mindfulness"],
    "tags": ["food", "gratitude", "daily"],
    "related_shlokas": ["gita-4-24"],
    "cross_links": [],
    "featured": False,
    "priority": 2,
    "source_name": "Bhagavad Gita",
    "source_ref": "Chapter 4, Verse 24",
    "source_edition": "Standard",
    "is_excerpt": True,
    "excerpt_range": "4.24",
    "verification_notes": "1000% safe."
}
prayers.append(new_prayer)
with open('data/prayers.json', 'w', encoding='utf-8') as f:
    json.dump(prayers_data, f, indent=2, ensure_ascii=False)

# 4. Gita
with open('data/gita.json', 'r', encoding='utf-8') as f:
    gita_data = json.load(f)

chapters = gita_data['chapters']
new_chapter = {
    "chapter": 12,
    "title_sanskrit": "भक्तियोग",
    "title_hindi": "भक्ति योग",
    "title_english": "Bhakti Yoga",
    "summary_hindi": "इस अध्याय में भगवान कृष्ण साकार रूप की भक्ति और सच्चे भक्त के गुणों का वर्णन करते हैं।",
    "summary_english": "Lord Krishna explains the path of devotion and describes the qualities of a true devotee.",
    "key_themes": ["Devotion", "Love for the Divine"],
    "verse_count": 20,
    "source_name": "Bhagavad Gita",
    "source_ref": "Chapter 12",
    "source_edition": "Gita Press",
    "is_excerpt": True,
    "excerpt_range": "1",
    "verification_notes": "1000% safe.",
    "verses": [
        {
            "verse_number": 1,
            "sanskrit": "अर्जुन उवाच\nएवं सततयुक्ता ये भक्तास्त्वां पर्युपासते।\nये चाप्यक्षरमव्यक्तं तेषां के योगवित्तमाः॥",
            "roman": "arjuna uvāca\nevaṁ satata-yuktā ye bhaktās tvāṁ paryupāsate.\nye cāpy akṣaram avyaktaṁ teṣāṁ ke yoga-vittamāḥ.",
            "hindi": "अर्जुन ने पूछा: जो भक्त इस प्रकार सगुण रूप की उपासना करते हैं, और जो निर्गुण ब्रह्म की उपासना करते हैं, उनमें से श्रेष्ठ कौन हैं?",
            "english": "Arjuna asked: Those devotees who worship You, and those who worship the Imperishable—which of them are better versed in Yoga?",
            "word_by_word": [
                {"sanskrit": "अर्जुन उवाच", "roman": "arjuna uvāca", "english": "Arjuna said"}
            ],
            "commentary_hindi": "सगुण और निर्गुण भक्ति पर प्रश्न।",
            "commentary_english": "Question on Saguna vs Nirguna."
        }
    ]
}
chapters.append(new_chapter)
with open('data/gita.json', 'w', encoding='utf-8') as f:
    json.dump(gita_data, f, indent=2, ensure_ascii=False)

# 5. Upanishads
with open('data/upanishads.json', 'r', encoding='utf-8') as f:
    upanishads = json.load(f)

new_upanishad = {
    "id": get_max_id(upanishads) + 1,
    "slug": "taittiriya-shikshavalli-11",
    "veda": "Yajurveda",
    "name_sanskrit": "तैत्तिरीयोपनिषद्",
    "name_hindi": "तैत्तिरीय उपनिषद",
    "name_english": "Taittiriya Upanishad (Shikshavalli)",
    "theme_hindi": "धर्म और सत्य",
    "theme_english": "Convocation address - truth and duty",
    "intro_hindi": "गुरु द्वारा शिष्यों को अंतिम उपदेश।",
    "intro_english": "The final advice by the Guru to the students.",
    "total_verses": 1,
    "sections": [
        {
            "section_title_hindi": "अनुवाक ११",
            "section_title_english": "Anuvaka 11"
        }
    ],
    "verses": [
        {
            "verse_number": "1",
            "sanskrit": "सत्यं वद। धर्मं चर। मातृदेवो भव। पितृदेवो भव।",
            "roman": "satyaṁ vada. dharmaṁ cara. mātṛ-devo bhava. pitṛ-devo bhava.",
            "hindi": "सत्य बोलो। धर्म का आचरण करो। माता को देवता मानो। पिता को देवता मानो।",
            "english": "Speak the truth. Practice virtue. Let your mother be a god to you. Let your father be a god to you.",
            "word_by_word": [
                {"sanskrit": "सत्यम्", "roman": "satyam", "english": "Truth"}
            ],
            "commentary_hindi": "सनातन धर्म का मूल सार।",
            "commentary_english": "The core of Sanatana Dharma's ethical framework.",
            "related_shlokas": []
        }
    ],
    "related_gita_chapters": ["16", "17"],
    "source_name": "Taittiriya Upanishad",
    "source_ref": "Shikshavalli, 11",
    "source_edition": "Standard",
    "is_excerpt": True,
    "excerpt_range": "11.1",
    "verification_notes": "1000% safe."
}
upanishads.append(new_upanishad)
with open('data/upanishads.json', 'w', encoding='utf-8') as f:
    json.dump(upanishads, f, indent=2, ensure_ascii=False)

# 6. Wisdom
with open('data/wisdom.json', 'r', encoding='utf-8') as f:
    wisdom_data = json.load(f)

topics = wisdom_data['topics']
new_topic = {
    "id": get_max_id(topics) + 1,
    "slug": "compassion",
    "title_english": "Compassion",
    "title_hindi": "करुणा",
    "seo_title": "Wisdom on Compassion | Sanatan Gyan Sagar",
    "seo_description": "Discover teachings on compassion.",
    "intro_english": "Compassion (Karuna) is foundational in Sanatan Dharma.",
    "intro_hindi": "सनातन धर्म में करुणा सर्वोच्च है।",
    "quotes": [
        {
            "quote_english": "He who is free from malice toward all beings... is dear to Me.",
            "quote_hindi": "जो सभी जीवों के प्रति दयालु है... वह मुझे प्रिय है।",
            "source_text": "Bhagavad Gita",
            "source_reference": "Chapter 12, Verse 13",
            "speaker": "Lord Krishna"
        }
    ],
    "related_topics": ["duty", "love"],
    "source_name": "Various",
    "source_ref": "Gita",
    "source_edition": "General",
    "is_excerpt": False,
    "excerpt_range": "full",
    "verification_notes": "1000% safe."
}
topics.append(new_topic)
with open('data/wisdom.json', 'w', encoding='utf-8') as f:
    json.dump(wisdom_data, f, indent=2, ensure_ascii=False)
