import os
import re

PLANET_DATA = {
    "surya": {
        "significance": "In Vedic Astrology, Surya (the Sun) is the king of the planetary cabinet. It represents the soul (Atmakaraka), ego, father, authority, government, career, and overall vitality. A well-placed Sun gives natural leadership abilities, unshakeable confidence, high self-esteem, and robust physical health. It illuminates the birth chart, providing the drive and stamina required to overcome life's obstacles and achieve immense worldly and spiritual success.",
        "symptoms": "When Surya is weak, debilitated (in Libra), or afflicted by malefic planets like Rahu or Saturn, the native may suffer from a lack of confidence, persistent self-doubt, and low self-esteem. Physical symptoms often include poor eyesight, heart conditions, lethargy, and bone-related ailments. The person may struggle with authority figures, face obstacles in government-related matters, experience a strained relationship with their father, or find it difficult to gain recognition and respect in their career.",
        "benefits": "Regularly chanting the Surya mantra invokes the divine energy of the Sun. Spiritually, it purifies the soul and burns away past negative karma. Materially, it brings success in career, favors from the government, and enhanced leadership qualities. It instills courage, sharpens the intellect, and bestows a radiant aura. Medically, the vibrations of the mantra are believed to improve vitality, strengthen the heart, and alleviate bone and eye diseases.",
        "ritual": "For maximum efficacy, the Surya mantra should be chanted early in the morning, ideally at sunrise. After bathing, stand facing the East. Offer Arghya (water mixed with red flowers, red sandalwood powder, and a pinch of raw rice) to the rising Sun from a copper vessel. Keep your gaze fixed softly on the Sun or close your eyes and visualize a brilliant golden light at your heart center. Chant the mantra 108 times using a Ruby or Rudraksha mala.",
        "faqs": [
            {"q": "Can I chant the Surya mantra at night?", "a": "It is highly recommended to chant Surya mantras during the daytime, preferably at sunrise, when the solar energy is most potent. Chanting at night is generally avoided in traditional practice."},
            {"q": "What should I donate to strengthen Surya?", "a": "Donating wheat, jaggery, copper items, red clothes, or red lentils (Masoor dal) on Sundays helps pacify an afflicted Sun."},
            {"q": "How many days should I chant the mantra?", "a": "A typical Sankalpa (vow) involves chanting the mantra 108 times daily for 40 consecutive days, starting on a Sunday, to see significant positive shifts in your aura."}
        ]
    },
    "chandra": {
        "significance": "Chandra (the Moon) is the queen of the planetary cabinet, governing the mind (Manaskaraka), emotions, mother, intuition, and inner peace. Because the mind processes all experiences, a strong Moon is essential for happiness and emotional stability. It controls bodily fluids, fertility, and psychological well-being. A well-placed Moon grants a calm demeanor, strong intuition, and a nurturing, empathetic personality.",
        "symptoms": "An afflicted or weak Moon (such as debilitation in Scorpio or conjunction with Rahu/Ketu forming a Grahan Yoga) leads to emotional instability, chronic anxiety, depression, and mood swings. The native might suffer from insomnia, irrational fears, or a strained relationship with their mother. Physically, it can manifest as frequent colds, respiratory issues, hormonal imbalances, or digestive problems rooted in stress.",
        "benefits": "Chanting the Chandra mantra brings profound inner peace and emotional equilibrium. It soothes a hyperactive mind, reduces anxiety, and enhances focus and memory. Spiritually, it deepens intuition and psychic abilities. Materially, it improves relationships, particularly with maternal figures, and fosters public support and popularity. It is highly beneficial for those seeking mental clarity and creative inspiration.",
        "ritual": "The Chandra mantra should ideally be chanted on Mondays or during the evening/night hours. After bathing, wear white or light-colored clothes and sit facing the Northwest. Use a Sphatik (clear quartz) or Pearl mala for chanting. Keep a vessel of pure water nearby while chanting 108 times. Offering milk or white flowers to a Shivalinga on Mondays also greatly enhances the positive effects of the Moon.",
        "faqs": [
            {"q": "Who should chant the Chandra mantra?", "a": "Anyone experiencing stress, anxiety, emotional turbulence, or those with a weak Moon or Kemadruma Yoga in their birth chart should chant this mantra."},
            {"q": "What are the best items to donate for Chandra?", "a": "Donating milk, rice, silver, white clothes, or sugar on Mondays, especially to women or the elderly, is considered highly auspicious for strengthening the Moon."},
            {"q": "Can women chant this mantra during their cycle?", "a": "Traditional Vedic practice suggests resting and doing mental chanting (Manasika Japa) without using a physical mala during this time."}
        ]
    },
    "mangal": {
        "significance": "Mangal (Mars) is the commander-in-chief of the planetary cabinet, representing courage, raw energy, physical strength, siblings, and property. It is the driving force that allows us to take action and defend ourselves. A strong Mars provides vitality, discipline, logical reasoning, and the willpower to conquer enemies and overcome obstacles. It is the planet of passion, ambition, and athletic prowess.",
        "symptoms": "When Mars is weak, debilitated (in Cancer), or forms a Mangal Dosha, the native may suffer from a lack of energy, cowardice, or an inability to take action. Conversely, an afflicted Mars can lead to uncontrolled anger, aggression, impulsiveness, and frequent accidents or surgeries. The native might face property disputes, massive debts (Rina), or continuous conflicts with siblings and partners.",
        "benefits": "Chanting the Mangal mantra channels martial energy into constructive ambition. It removes lethargy, instills immense courage, and helps one overcome fear and adversaries. It is the ultimate remedy for clearing debts and winning legal disputes or property-related issues. Spiritually, it cultivates discipline and focus. For those with Mangal Dosha (Kuja Dosha), it helps harmonize marital life and reduce friction in relationships.",
        "ritual": "Tuesdays are dedicated to Mars. Sit facing the South, preferably on a red asana (mat), wearing red or copper-colored clothes. The mantra should be chanted 108 times using a Red Coral or Rudraksha mala. Lighting a ghee lamp and offering red flowers (like hibiscus) or jaggery enhances the energy. Worshipping Lord Hanuman alongside Mars is highly recommended for complete protection.",
        "faqs": [
            {"q": "Does this mantra cure Mangal Dosha?", "a": "Regular chanting significantly reduces the aggressive and disruptive effects of Mangal Dosha, bringing harmony to marriage and partnerships."},
            {"q": "What are the best donations for Mars?", "a": "Donating red lentils (Masoor dal), jaggery, copper utensils, or red clothes on Tuesdays to young men or celibates is highly beneficial."},
            {"q": "Can chanting Mangal mantra help with debts?", "a": "Yes, Mars represents loans and debts. Chanting this mantra, especially the Rinamochan Mangal Stotram, is a powerful Vedic remedy for clearing financial burdens."}
        ]
    },
    "budha": {
        "significance": "Budha (Mercury) is the prince of the planets, governing intellect, communication, speech, logic, business, and commerce. It represents the analytical mind, memory, and our ability to comprehend complex information. A strong Mercury grants excellent public speaking skills, a sharp memory, a great sense of humor, and success in business, writing, mathematics, and astrology.",
        "symptoms": "A weak or afflicted Mercury (debilitated in Pisces) manifests as poor memory, speech impediments (like stuttering or stammering), and difficulty in articulating thoughts. The native might suffer from nervous system disorders, skin diseases, or anxiety. In professional life, it leads to miscommunications, poor decision-making, struggles in business, and frequent losses in trade or investments.",
        "benefits": "Chanting the Budha mantra sharpens the intellect, improves memory, and enhances analytical skills. It is highly beneficial for students, writers, public speakers, and business people. It cures speech defects and nervous disorders, bringing a calming effect to the nervous system. The mantra aids in making logical, profitable decisions in commerce and removes the confusion of the mind.",
        "ritual": "Wednesdays are ruled by Mercury. Sit facing the North, wearing green or light-colored clothes. Use an Emerald or Green Jade mala, or a simple Rudraksha mala, to chant the mantra 108 times. Offering green grass (Durva) to Lord Ganesha on Wednesdays before chanting the Mercury mantra yields exceptional results, as Ganesha is the presiding deity of intellect.",
        "faqs": [
            {"q": "Is this mantra good for students?", "a": "Yes, the Budha mantra is highly recommended for students to improve concentration, grasping power, and academic performance."},
            {"q": "What should I donate for Mercury?", "a": "Donating green gram (Moong dal), green clothes, educational materials (books, pens) to students, or feeding green grass to cows on Wednesdays is very effective."},
            {"q": "Can it cure skin problems?", "a": "Since Mercury rules the skin and nervous system, aligning with its energy through mantra chanting and proper medical care can accelerate healing."}
        ]
    },
    "guru": {
        "significance": "Guru (Jupiter), also known as Brihaspati, is the greatest benefic planet. It represents wisdom, wealth, fortune, children, higher education, and spirituality. Jupiter expands everything it touches, bringing abundance and grace. A strong Jupiter grants a philosophical mindset, strong moral values, respect in society, financial prosperity, and divine protection against various afflictions in the birth chart.",
        "symptoms": "When Jupiter is weak, debilitated (in Capricorn), or afflicted by Rahu (Guru Chandal Yoga), the native experiences a lack of wisdom, pessimism, and financial struggles. They may face delays in marriage, difficulties in childbirth or raising children, and a lack of respect or recognition. Physically, an afflicted Jupiter can cause liver problems, obesity, or issues with blood sugar.",
        "benefits": "Chanting the Guru mantra attracts boundless fortune, prosperity, and divine grace. It clears obstacles in higher education and marriage. Spiritually, it awakens the inner guru, providing deep wisdom and clarity of purpose. It offers immense protection against accidents and negative energies. For married couples, it brings harmony and blesses them with healthy, intelligent progeny.",
        "ritual": "Thursdays are the days of Brihaspati. Sit facing the Northeast (Ishan kona) wearing yellow clothes. Use a Haldi (Turmeric) mala or a yellow Topaz mala to chant the mantra 108 times. Apply a saffron or turmeric tilak on your forehead before starting. Offering yellow flowers, gram dal (Chana dal), or yellow sweets amplifies the divine blessings.",
        "faqs": [
            {"q": "Can the Guru mantra help in getting married?", "a": "Yes, Jupiter is the primary significator of a husband in a woman's chart, and it governs the institution of marriage. Chanting this mantra removes delays in finding a life partner."},
            {"q": "What are the best donations for Jupiter?", "a": "Donating yellow items like Chana dal, turmeric, yellow clothes, or spiritual books to teachers or priests on Thursdays is highly auspicious."},
            {"q": "Is it beneficial for financial growth?", "a": "Absolutely. Jupiter is the Karaka (significator) of wealth. Regular chanting opens up new avenues for income and ensures long-term financial stability."}
        ]
    },
    "shukra": {
        "significance": "Shukra (Venus) is the planet of love, beauty, luxury, art, and romance. It governs all the pleasures of life, including marriage, vehicles, fine arts, and material comforts. A strong Venus brings a charismatic personality, a loving partner, financial abundance, and an appreciation for aesthetics. It is the key planet for a happy, harmonious marital life and success in creative fields.",
        "symptoms": "A weak or afflicted Venus (debilitated in Virgo) leads to a lack of physical charm, relationship failures, and marital discord. The native may struggle to accumulate wealth or experience financial instability despite hard work. They might face reproductive issues, kidney problems, or lack the enjoyment of material comforts. Life may feel devoid of passion, creativity, and luxury.",
        "benefits": "Chanting the Shukra mantra enhances personal magnetism, beauty, and attractiveness. It resolves conflicts in relationships and brings profound harmony to married life. Materially, it attracts luxury, wealth, and comforts like property and vehicles. For artists and creators, it bestows immense creativity and public recognition. It also helps heal ailments related to the reproductive system.",
        "ritual": "Fridays are dedicated to Venus. Sit facing the Southeast, wearing clean, bright white or pink clothes. The mantra should be chanted 108 times using a Sphatik (clear quartz) or Lotus seed (Kamal Gatta) mala. Using fragrant incense, wearing mild perfume, and offering white flowers or sweets made of milk creates the perfect vibratory environment for Venus.",
        "faqs": [
            {"q": "How does Shukra mantra help in love life?", "a": "Venus governs romance and attraction. Chanting its mantra clears misunderstandings, increases mutual affection, and helps attract a compatible and loving partner."},
            {"q": "What should be donated for Venus?", "a": "Donating white items like milk, curd, rice, sugar, white clothes, or cosmetics to women on Fridays strengthens Venus."},
            {"q": "Can I chant it for financial gain?", "a": "Yes, Venus is a key planet for liquid wealth and luxury. Activating Venus energy attracts financial prosperity and a comfortable lifestyle."}
        ]
    },
    "shani": {
        "significance": "Shani (Saturn) is the strict judge and taskmaster of the planetary system. It represents karma, discipline, hard work, delay, and longevity. Saturn is not an enemy, but a teacher who enforces the universal law of cause and effect. A well-placed Saturn bestows immense patience, organizational skills, spiritual depth, and long-lasting success built on a foundation of hard work and truth.",
        "symptoms": "When Saturn is weak, debilitated (in Aries), or malefic in transit (like Sade Sati or Dhaiya), it causes immense struggles, delays, and obstacles in every endeavor. The native may experience chronic illnesses, joint pains, depression, and a pervasive sense of sorrow. Professional life is marked by instability, job losses, or lack of reward for hard work. Financial blockages and legal troubles are common.",
        "benefits": "Chanting the Shani mantra pacifies the harsh effects of Saturn, especially during Sade Sati. It replaces fear and anxiety with discipline and immense mental endurance. It clears the path of karmic blockages, reduces delays in career and marriage, and protects against chronic diseases and accidents. Ultimately, it brings spiritual grounding and lasting, stable success.",
        "ritual": "Saturdays are ruled by Saturn. Sit facing the West after sunset, wearing dark blue or black clothes. Chant the mantra 108 times using a Rudraksha or Black Agate mala. Lighting a mustard oil lamp under a Peepal tree and offering black sesame seeds or iron nails is a deeply traditional and effective way to honor Lord Shani.",
        "faqs": [
            {"q": "Is it safe to chant the Shani mantra at home?", "a": "Yes, it is perfectly safe to chant the mantra at home with a pure heart and respectful intention. Avoid chanting it with fear; chant it with devotion and acceptance of your karma."},
            {"q": "What is the best donation for Shani?", "a": "Donating black sesame seeds, mustard oil, black clothes, iron, or leather footwear to the poor and disabled on Saturdays is the most effective remedy."},
            {"q": "Does this mantra reduce the effects of Sade Sati?", "a": "Yes, regular chanting is one of the most powerful remedies to mitigate the struggles and mental anguish experienced during the 7.5 years of Sade Sati."}
        ]
    },
    "rahu": {
        "significance": "Rahu (the North Node of the Moon) is a shadow planet representing materialism, obsession, illusions, foreign lands, and sudden events. It is the ultimate disruptor, breaking traditions and expanding boundaries. While considered a malefic, a well-placed Rahu can grant sudden wealth, immense worldly success, technological brilliance, and the ability to outsmart competitors in the modern, digital age.",
        "symptoms": "An afflicted Rahu creates a life of illusions, confusion, and sudden downfalls. The native may suffer from undiagnosable illnesses, phobias, paranoia, or addiction to intoxicants and gambling. It causes constant restlessness, betrayal by friends, and sudden losses of wealth or reputation. The person is often drawn into unethical practices or feels completely disconnected from reality.",
        "benefits": "Chanting the Rahu mantra cuts through the fog of illusion and mental confusion. It protects the native from hidden enemies, black magic, and sudden accidents. Materially, it can turn the obsessive energy of Rahu into focused ambition, bringing unexpected gains, success in foreign lands, and breakthroughs in technology or research. It brings sudden, positive shifts in fortune.",
        "ritual": "Saturdays or Wednesdays during nighttime are best for Rahu. Sit facing the Southwest, wearing dark blue or grey clothes. Chant the mantra 108 times using an Onyx, Sandalwood, or Rudraksha mala. Keeping a piece of sandalwood nearby or offering blue flowers can help pacify Rahu's erratic energy.",
        "faqs": [
            {"q": "Can Rahu mantra cure addictions?", "a": "Rahu governs obsessions and intoxicants. Chanting this mantra brings mental clarity and strengthens the willpower needed to overcome addictive behaviors."},
            {"q": "What should be donated for Rahu?", "a": "Donating black or dark blue blankets, mustard oil, coconuts, or sweeping the floor of a temple helps appease Rahu."},
            {"q": "Is Rahu always bad?", "a": "No, in the modern world, Rahu represents IT, foreign trade, and innovation. When its energy is properly channeled, it brings immense worldly success."}
        ]
    },
    "ketu": {
        "significance": "Ketu (the South Node of the Moon) is the planet of liberation (Mokshakaraka), spirituality, detachment, and sudden endings. It represents past life karma, intuition, and deep esoteric knowledge. Ketu removes materialism from our lives to push us toward spiritual awakening. A well-placed Ketu grants deep psychic abilities, mastery over occult sciences, and an innate sense of detachment from worldly drama.",
        "symptoms": "When Ketu is afflicted, it causes sudden, inexplicable losses, deep feelings of isolation, and a complete lack of direction in life. The native may suffer from mysterious health issues, allergies, or viral infections that doctors cannot diagnose. It brings sudden breaks in relationships, career instability, and a pervasive sense of emptiness or depression. There may be a tendency towards self-destructive behavior.",
        "benefits": "Chanting the Ketu mantra transforms isolation into profound spiritual peace. It develops intuition, psychic awareness, and deep wisdom. It is the ultimate remedy for breaking free from past-life karmic patterns and sudden, recurring misfortunes. It protects against hidden enemies, viral diseases, and snake bites, ultimately leading the soul toward liberation (Moksha).",
        "ritual": "Tuesdays or Thursdays are suitable for Ketu. Sit facing the Northwest, wearing multi-colored, grey, or earthy tones. Chant the mantra 108 times using a Lapis Lazuli, Ashwagandha root, or Rudraksha mala. Since Ketu is a headless, chaotic energy, chanting the mantra with deep inner focus and surrender to the divine is essential.",
        "faqs": [
            {"q": "How does Ketu mantra help spiritually?", "a": "Ketu is the planet of spiritual enlightenment. Its mantra deepens meditation, enhances intuition, and helps detach from toxic, materialistic attachments."},
            {"q": "What are the donations for Ketu?", "a": "Donating multi-colored blankets, black and white sesame seeds, or feeding stray dogs is highly effective in pacifying Ketu's malefic effects."},
            {"q": "Can it help with mysterious illnesses?", "a": "Yes, Ketu governs undiagnosable and viral diseases. The vibratory energy of the mantra brings healing and clarity to hidden physical ailments."}
        ]
    }
}

def generate_html_block(planet_key, data):
    # Extract colors based on planet (could use default if not specified, but let's just use CSS variables)
    html = f'''
<!-- ── ASTROLOGICAL SIGNIFICANCE ────────────────────── -->
<div class="section-card">
    <div class="section-label">Astrological Significance</div>
    <h2>What Does {data['name'] if 'name' in data else planet_key.capitalize()} Represent?</h2>
    <p>{data['significance']}</p>
</div>

<!-- ── SYMPTOMS OF AFFLICTION ───────────────────────── -->
<div class="section-card">
    <div class="section-label">Signs of Affliction</div>
    <h2>Symptoms of a Weak {data['name'] if 'name' in data else planet_key.capitalize()}</h2>
    <p>{data['symptoms']}</p>
</div>

<!-- ── BENEFITS ─────────────────────────────────────── -->
<div class="section-card">
    <div class="section-label">Mantra Benefits</div>
    <h2>Deep-Dive Benefits of the Mantra</h2>
    <p>{data['benefits']}</p>
</div>

<!-- ── RITUAL PROCESS ───────────────────────────────── -->
<div class="section-card">
    <div class="section-label">Puja & Ritual</div>
    <h2>Detailed Chanting Process</h2>
    <p>{data['ritual']}</p>
</div>

<!-- ── FREQUENTLY ASKED QUESTIONS ───────────────────── -->
<div class="section-card">
    <div class="section-label">FAQ</div>
    <h2>Frequently Asked Questions</h2>
    <div itemscope itemtype="https://schema.org/FAQPage" style="display:flex; flex-direction:column; gap:16px; margin-top:12px;">
'''
    for faq in data['faqs']:
        html += f'''
        <div itemscope itemprop="mainEntity" itemtype="https://schema.org/Question" style="border-bottom:1px dashed var(--border); padding-bottom:12px;">
            <h3 itemprop="name" style="font-size:1.05rem; font-weight:700; color:var(--text); margin-bottom:6px;">{faq['q']}</h3>
            <div itemscope itemprop="acceptedAnswer" itemtype="https://schema.org/Answer">
                <p itemprop="text" style="font-size:0.95rem; color:var(--text-sec); line-height:1.6;">{faq['a']}</p>
            </div>
        </div>
'''
    html += '''
    </div>
</div>
'''
    return html

def process_all():
    base_dir = "/Users/prashastpathak/Bhajan/planet"
    updated_count = 0
    
    for planet, data in PLANET_DATA.items():
        file_path = os.path.join(base_dir, planet, "index.html")
        if not os.path.exists(file_path):
            print(f"Skipping {planet}, file not found")
            continue
            
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # We need to inject the new blocks right BEFORE the "<!-- ── MANDATORY CROSS-LINK CTA ───────────────────── -->"
        target_comment = "<!-- ── MANDATORY CROSS-LINK CTA ───────────────────── -->"
        
        # Check if already injected
        if "Astrological Significance" in content and "Symptoms of a Weak" in content:
            print(f"{planet} is already enriched. Skipping.")
            continue
            
        if target_comment in content:
            injection_html = generate_html_block(planet, data)
            new_content = content.replace(target_comment, injection_html + "\n" + target_comment)
            
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            updated_count += 1
            print(f"Enriched {planet} successfully! (Added ~400 words of semantic text + FAQ Schema)")
        else:
            print(f"Could not find injection target in {planet}")
            
    print(f"\nDone! Enriched {updated_count} planet pages with rich AdSense-ready content.")

if __name__ == "__main__":
    process_all()
