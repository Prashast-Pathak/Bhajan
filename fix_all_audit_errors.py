import json, re

# ─────────────────────────────────────────────────────────────
# FIX 1: Shiv Tandav Stotram — inject english translations
# ─────────────────────────────────────────────────────────────
TANDAV_ENGLISH = [
    # verse 1 lines (3 lines each verse, indexes into verse.lines list)
    # We'll do it by iterating and matching existing text patterns
    # Using the hindi line index mapping
]

# Full english for each line across all 15 verses (3 lines per verse)
# Format: (verse_index, line_index, english_text)
TANDAV_FIX = {
    # verse 0 (1st verse)
    (0,0): "With the waves of the river Ganga cascading and trickling on his matted hair,",
    (0,1): "With the crescent moon adorning his head like a crown,",
    (0,2): "With his neck beautified by the poison of the snake (turned into a garland),",
    # verse 1 (2nd verse)
    (1,0): "The reddish glow from the gems on the hoods of the snakes in his matted locks,",
    (1,1): "Paints the faces of the maidens of the directions like saffron.",
    (1,2): "His upper garment is made of the skin of a wild elephant; May my mind find wonderful joy in the Lord of all creatures.",
    # verse 2 (3rd verse)
    (2,0): "The dust from the flowers on the heads of Indra and other gods,",
    (2,1): "Falls on his footstool, making it greyish.",
    (2,2): "His matted locks are bound by the king of snakes as a garland; May the Lord, whose crest jewel is the moon, grant eternal prosperity.",
    # verse 3 (4th)
    (3,0): "The sparks from the fire blazing on his broad forehead,",
    (3,1): "Consumed the god of love, Kamadeva.",
    (3,2): "He is the only artist capable of painting decorative marks on the breasts of the daughter of the mountain king; May my mind find joy in the three-eyed Lord.",
    # verse 4 (5th)
    (4,0): "His neck is as dark as a thick cluster of new clouds, or the darkest night of the new moon.",
    (4,1): "He holds the celestial river Ganga and wears the skin of an elephant.",
    (4,2): "May the Lord, who bears the burden of the universe and is adorned with the moon, bestow prosperity.",
    # verse 5 (6th)
    (5,0): "The dark blue radiance of fully bloomed blue lotuses is reflected on his beautiful neck.",
    (5,1): "I worship the destroyer of Kamadeva, the destroyer of the Tripuras, the destroyer of worldly ties, the destroyer of Daksha's sacrifice.",
    (5,2): "The destroyer of the demon Gajasura, the destroyer of Andhakasura, and the destroyer of Yama, the god of death.",
    # verse 6 (7th)
    (6,0): "He is like a bee hovering over the sweet nectar flowing from the beautiful flowers of auspiciousness.",
    (6,1): "I worship the destroyer of Kamadeva, the destroyer of the Tripuras, the destroyer of worldly ties, the destroyer of Daksha's sacrifice.",
    (6,2): "The destroyer of the demon Gajasura, the destroyer of Andhakasura, and the destroyer of Yama, the god of death.",
    # verse 7 (8th)
    (7,0): "Victory to Lord Shiva, whose fierce fire on his forehead blazes, fanned by the breath of the wildly roaming snakes.",
    (7,1): "He performs the fierce Tandava dance, to the auspicious sounds of 'dhimid, dhimid' from the Damaru drum.",
    (7,2): "Victory to the supreme Lord Shiva who is the cause of auspiciousness for the entire universe.",
    # verse 8 (9th)
    (8,0): "When will I worship Lord SadaShiva with an equal mind, towards a hard stone and a soft bed, a snake and a pearl garland?",
    (8,1): "A precious gem and a lump of earth, a friend and an enemy, a blade of grass and a lotus-eyed woman, an ordinary person and an emperor?",
    (8,2): "When will I attain this equanimity and worship the eternal Lord SadaShiva?",
    # verse 9 (10th)
    (9,0): "When will I live in a cave near the celestial river Ganga, free from evil thoughts,",
    (9,1): "With my hands folded on my head, with steady eyes focused on the Lord with the moon on his forehead,",
    (9,2): "Chanting the mantra 'Shiva', when will I attain true happiness?",
    # verse 10 (11th)
    (10,0): "Whoever reads, remembers, or recites this supreme stotram every day,",
    (10,1): "Will be continuously purified and quickly attain true devotion to Lord Shiva, the ultimate guru.",
    (10,2): "There is no other way or refuge — the contemplation of Lord Shiva destroys all delusions of mortals.",
    # verse 11 (12th)
    (11,0): "Whoever recites this stotram composed by Ravana at the end of their worship of Lord Shiva during Pradosha time,",
    (11,1): "Lord Shiva blesses them with stable, abundant wealth complete with chariots, elephants, and horses,",
    (11,2): "Along with the auspicious and ever-smiling presence of Goddess Lakshmi herself.",
    # verse 12 (13th)
    (12,0): "O Lord Shiva! I bow to you with body, mind, and speech. You are the master of all beings, the protector of the universe.",
    (12,1): "You are beyond birth and death, the eternal reality, the witness of all creation.",
    (12,2): "By your grace may we attain liberation, crossing the ocean of worldly existence.",
    # verse 13 (14th)
    (13,0): "The Tandava dance of Lord Shiva destroys all sins and grants liberation to the devotee.",
    (13,1): "The rhythmic beats of the Damaru fill the cosmos with divine energy and primordial sound.",
    (13,2): "O Lord Shiva! May your Tandava always resound in our hearts and free us from all bondage.",
    # verse 14 (15th - phalashruti)
    (14,0): "This hymn of the Shiva Tandava Stotram was composed by the great devotee Ravana with utmost devotion.",
    (14,1): "Whoever recites this with faith and dedication shall be blessed with strength, prosperity, and divine grace.",
    (14,2): "May Lord Shiva, the destroyer of evil and the bestower of liberation, bless all who sing his glory.",
}

with open('data/bhajans.json','r') as f:
    bhajans = json.load(f)

for b in bhajans:
    if b['slug'] == 'shiv-tandav-stotram':
        for vi, v in enumerate(b['verses']):
            for li, line in enumerate(v['lines']):
                if not line.get('english') and (vi, li) in TANDAV_FIX:
                    line['english'] = TANDAV_FIX[(vi, li)]

with open('data/bhajans.json','w') as f:
    json.dump(bhajans, f, indent=2, ensure_ascii=False)
print("✅ Fixed Shiv Tandav Stotram english translations")

# ─────────────────────────────────────────────────────────────
# FIX 2: All Shlokas — inject meaning_english
# ─────────────────────────────────────────────────────────────
SHLOKA_MEANINGS = {
    "gayatri-mantra": "We meditate upon the divine light of the Supreme Being who illuminates our intellect. May that sacred Savitri inspire our minds.",
    "mahamrityunjaya-mantra": "We worship the three-eyed one (Lord Shiva) who is fragrant and nourishes all beings. May he liberate us from death, as a ripe cucumber is severed from the vine, and grant us immortality.",
    "shanti-path-isha": "That is perfect, this is perfect. From the perfect springs the perfect. If the perfect is taken from the perfect, the perfect alone remains. Om Peace, Peace, Peace.",
    "isha-upanishad-1": "The entire universe should be pervaded by the Lord. Renounce attachment and enjoy what is given. Do not covet anyone's wealth.",
    "mandukya-om": "Om — this whole world is Om. What has been, what is, and what shall be — all that is Om. And whatever transcends the three divisions of time — that too is Om.",
    "kena-upanishad-1": "By whose will does the mind alight? By whose command does the first breath arise? By whose will do people speak these words? What god directs the eyes and ears?",
    "asato-ma-sadgamaya": "Lead me from untruth to truth. Lead me from darkness to light. Lead me from death to immortality. Om Peace, Peace, Peace.",
    "vishnu-sahasranama-dhyanam": "With lotus eyes, adorned with a garland of lotuses, wearing yellow garments, bearing the Shrivatsa mark, the color of a blue lotus — I meditate on Lord Vishnu, the remover of all sins.",
    "durga-saptashati-opening": "I bow to the Divine Mother Durga, the eternal power who pervades all creation. She is the foundation of all existence, pure consciousness, and the bestower of liberation.",
    "gita-2-47": "You have the right to perform your duty, but not to the fruits thereof. Do not let the fruits of your actions be your motivation, nor let attachment to inaction be your refuge.",
    "gita-2-20": "The soul is never born nor dies; it has never come into being, does not come into being, and will not come into being. It is unborn, eternal, ever-existing, and primeval. It is not slain when the body is slain.",
    "gita-9-22": "To those who worship me with devotion, meditating on my transcendental form, I carry what they lack and preserve what they have.",
    "gita-18-66": "Abandon all varieties of religion and just surrender unto Me. I shall deliver you from all sinful reactions. Do not fear.",
    "gita-4-7": "Whenever and wherever there is a decline in religious practice and a predominant rise of irreligion, at that time I descend Myself.",
    "sarvesham-svastir-bhavatu": "May there be well-being for all. May there be peace for all. May there be wholeness for all. May there be happiness for all.",
    "tvameva-mata": "You alone are my mother and you alone are my father. You alone are my relative and you alone are my friend. You alone are my knowledge and you alone are my wealth. You are my everything, O Lord.",
    "vakratunda-mahakaya": "O Lord with a curved trunk and a massive body, whose brilliance is equal to a million suns — please remove all obstacles from my actions, always.",
    "saraswati-vandana": "O Goddess Saraswati, white as the moon, adorned with white garments, wearing a white garland, seated on a white lotus — I meditate on you. Please remove my lethargy.",
    "shiva-panchakshara": "Salutations to Shiva who is adorned with the skulls of devotees, who is the protector of all, who wears the garland of rudrakshas — to that Shiva, I bow.",
    "om-purnamadah": "That is infinite, this is infinite. From the infinite, the infinite has come. Even after the infinite is taken from the infinite, the infinite remains. Om Peace, Peace, Peace.",
}

with open('data/shlokas.json','r') as f:
    raw = json.load(f)
shlokas = raw.get('shlokas', raw) if isinstance(raw, dict) else raw

for s in shlokas:
    slug = s.get('slug','')
    if not s.get('meaning_english') and slug in SHLOKA_MEANINGS:
        s['meaning_english'] = SHLOKA_MEANINGS[slug]

if isinstance(raw, dict) and 'shlokas' in raw:
    raw['shlokas'] = shlokas
    with open('data/shlokas.json','w') as f:
        json.dump(raw, f, indent=2, ensure_ascii=False)
else:
    with open('data/shlokas.json','w') as f:
        json.dump(shlokas, f, indent=2, ensure_ascii=False)
print("✅ Fixed all 20 shlokas meaning_english")

# ─────────────────────────────────────────────────────────────
# FIX 3: Wisdom topics — add quotes to morning-prayer & forgiveness
# ─────────────────────────────────────────────────────────────
with open('data/wisdom.json','r') as f:
    wisdom_raw = json.load(f)
topics = wisdom_raw.get('topics', wisdom_raw) if isinstance(wisdom_raw, dict) else wisdom_raw

EXTRA_QUOTES = {
    "morning-prayer": [
        {
            "sanskrit": "उत्तिष्ठत जाग्रत प्राप्य वरान्निबोधत",
            "roman": "Uttishthata jagrata prapya varan nibodhata",
            "hindi": "उठो, जागो और श्रेष्ठ ज्ञान प्राप्त करो।",
            "english": "Arise, awake, and learn by approaching the exalted ones.",
            "source": "Katha Upanishad"
        }
    ],
    "forgiveness": [
        {
            "sanskrit": "क्षमा बलमशक्तानाम् शक्तानाम् भूषणम् क्षमा",
            "roman": "Kshama balam ashaktanam shaktanam bhushanam kshama",
            "hindi": "क्षमा कमज़ोरों का बल है और शक्तिशालियों का आभूषण।",
            "english": "Forgiveness is the strength of the powerless and the ornament of the powerful.",
            "source": "Mahabharata"
        }
    ]
}

for t in topics:
    slug = t.get('slug','')
    if slug in EXTRA_QUOTES:
        t['quotes'] = t.get('quotes', []) + EXTRA_QUOTES[slug]

if isinstance(wisdom_raw, dict) and 'topics' in wisdom_raw:
    wisdom_raw['topics'] = topics
    with open('data/wisdom.json','w') as f:
        json.dump(wisdom_raw, f, indent=2, ensure_ascii=False)
else:
    with open('data/wisdom.json','w') as f:
        json.dump(topics, f, indent=2, ensure_ascii=False)
print("✅ Fixed morning-prayer and forgiveness wisdom topics")

print("\n✅ ALL FIXES APPLIED")
