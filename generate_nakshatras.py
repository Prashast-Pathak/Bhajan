#!/usr/bin/env python3
"""
generate_nakshatras.py
Generates 27 Nakshatra Devotion hub pages for bhajan.ournakshatra.com
"""

import os
import json

NAKSHATRAS_DATA = [
    {"id": "ashwini", "name": "Ashwini", "sanskrit": "अश्विनी", "deity": "Ashwini Kumaras (Physicians of Gods)", "traits": "People born in Ashwini are quick, energetic, pioneering, and possess strong healing abilities. They love movement and travel.", "famous": "Yukio Mishima, Warren Buffett", "color": "#DC2626"},
    {"id": "bharani", "name": "Bharani", "sanskrit": "भरणी", "deity": "Yama (Lord of Dharma & Death)", "traits": "Fierce, passionate, and determined. They undergo massive transformations in life and have strong creative and destructive urges.", "famous": "Carl Jung, Elton John", "color": "#991B1B"},
    {"id": "krittika", "name": "Krittika", "sanskrit": "कृत्तिका", "deity": "Agni (God of Fire)", "traits": "Sharp, analytical, and highly ambitious. They have a purifying presence and a strong appetite for leadership and knowledge.", "famous": "Bill Clinton, Mick Jagger", "color": "#EA580C"},
    {"id": "rohini", "name": "Rohini", "sanskrit": "रोहिणी", "deity": "Brahma (The Creator)", "traits": "Charming, magnetic, and deeply connected to beauty, agriculture, and material growth. Highly family-oriented.", "famous": "Queen Victoria, Barack Obama", "color": "#C96A1F"},
    {"id": "mrigashira", "name": "Mrigashira", "sanskrit": "मृगशिरा", "deity": "Soma / Chandra (Moon God)", "traits": "Gentle, inquisitive, and always searching for meaning. Excellent communicators and romantic at heart.", "famous": "Brooke Shields, Salman Rushdie", "color": "#1E40AF"},
    {"id": "ardra", "name": "Ardra", "sanskrit": "आर्द्रा", "deity": "Rudra / Shiva (The Storm God)", "traits": "Highly intellectual, emotionally intense, and capable of weathering great storms. They rebuild strongly after destruction.", "famous": "Albert Einstein, Taylor Swift", "color": "#111827"},
    {"id": "punarvasu", "name": "Punarvasu", "sanskrit": "पुनर्वसु", "deity": "Aditi (Mother of Gods)", "traits": "Optimistic, nurturing, and spiritually inclined. They often experience a 'return of light' or second chances in life.", "famous": "Ramana Maharshi, Harrison Ford", "color": "#EAB308"},
    {"id": "pushya", "name": "Pushya", "sanskrit": "पुष्य", "deity": "Brihaspati (Guru of Gods)", "traits": "Considered the most auspicious Nakshatra. Highly spiritual, caring, traditionally minded, and excellent providers.", "famous": "Mick Jagger, Clint Eastwood", "color": "#F59E0B"},
    {"id": "ashlesha", "name": "Ashlesha", "sanskrit": "आश्लेषा", "deity": "Naga Devata (Serpent Gods)", "traits": "Deeply intuitive, mystical, and sometimes secretive. They possess intense hypnotic charm and raw Kundalini energy.", "famous": "Mahatma Gandhi, Queen Elizabeth II", "color": "#166534"},
    {"id": "magha", "name": "Magha", "sanskrit": "मघा", "deity": "Pitrus (Ancestors)", "traits": "Regal, proud, and deeply connected to lineage. They seek authority, respect, and want to leave a lasting legacy.", "famous": "Winston Churchill, Paramahansa Yogananda", "color": "#A8832A"},
    {"id": "purva-phalguni", "name": "Purva Phalguni", "sanskrit": "पूर्वाफाल्गुनी", "deity": "Bhaga (God of Delight)", "traits": "Relaxed, social, and deeply romantic. They love the arts, luxury, and experiencing the joyful side of life.", "famous": "Madonna, John F. Kennedy", "color": "#BE185D"},
    {"id": "uttara-phalguni", "name": "Uttara Phalguni", "sanskrit": "उत्तराफाल्गुनी", "deity": "Aryaman (God of Patronage)", "traits": "Dependable, noble, and excellent friends. They are focused on contracts, partnerships, and social obligations.", "famous": "Sean Connery, Alexander the Great", "color": "#B91C1C"},
    {"id": "hasta", "name": "Hasta", "sanskrit": "हस्त", "deity": "Savitar (The Sun of Dawn)", "traits": "Highly skilled with their hands, detail-oriented, and witty. Great healers, craftsmen, and manifesting abilities.", "famous": "Jimmy Carter, Marie Curie", "color": "#0D9488"},
    {"id": "chitra", "name": "Chitra", "sanskrit": "चित्रा", "deity": "Vishwakarma (Divine Architect)", "traits": "Dynamic, charismatic, and obsessed with structure and aesthetics. They are the artists and architects of the zodiac.", "famous": "Steve Jobs, George Washington", "color": "#0369A1"},
    {"id": "swati", "name": "Swati", "sanskrit": "स्वाति", "deity": "Vayu (Wind God)", "traits": "Independent, diplomatic, and freedom-loving. They scatter their energy like the wind but adapt beautifully to change.", "famous": "Charlie Chaplin, Nelson Mandela", "color": "#6D28D9"},
    {"id": "vishakha", "name": "Vishakha", "sanskrit": "विशाखा", "deity": "Indra-Agni (Gods of Lightning & Fire)", "traits": "Extremely goal-oriented, determined, and competitive. They achieve great success in the second half of life.", "famous": "Buddha, Jimmy Carter", "color": "#B45309"},
    {"id": "anuradha", "name": "Anuradha", "sanskrit": "अनुराधा", "deity": "Mitra (God of Friendship)", "traits": "Devoted, friendly, and capable of leading group efforts. They thrive in foreign lands and spiritual environments.", "famous": "Jimi Hendrix, Saddam Hussein", "color": "#1D4ED8"},
    {"id": "jyeshtha", "name": "Jyeshtha", "sanskrit": "ज्येष्ठा", "deity": "Indra (King of Gods)", "traits": "Fiercely protective, authoritative, and the 'eldest' in spirit. They achieve positions of extreme power.", "famous": "Albert Einstein, Mozart", "color": "#991B1B"},
    {"id": "mula", "name": "Mula", "sanskrit": "मूल", "deity": "Nirrti / Kali (Goddess of Destruction)", "traits": "Direct, researchers, and root-diggers. They break things down to the absolute core to find the truth.", "famous": "Dalai Lama, Arnold Schwarzenegger", "color": "#111827"},
    {"id": "purva-ashadha", "name": "Purva Ashadha", "sanskrit": "पूर्वाषाढा", "deity": "Apas (Water Goddess)", "traits": "Invincible, proud, and highly emotional. They have a patient, purifying nature but are unstoppable once moving.", "famous": "Adolf Hitler, Ernest Hemingway", "color": "#0284C7"},
    {"id": "uttara-ashadha", "name": "Uttara Ashadha", "sanskrit": "उत्तराषाढा", "deity": "Vishvedevas (Universal Gods)", "traits": "Virtuous, traditional, and incredibly enduring. They are the ultimate late-bloomers who achieve lasting victory.", "famous": "Abraham Lincoln, George Washington", "color": "#B45309"},
    {"id": "shravana", "name": "Shravana", "sanskrit": "श्रवण", "deity": "Vishnu (The Preserver)", "traits": "Great listeners, highly academic, and spiritually receptive. They make excellent teachers and counselors.", "famous": "Muhammad Ali, Bruce Willis", "color": "#A8832A"},
    {"id": "dhanishtha", "name": "Dhanishtha", "sanskrit": "धनिष्ठा", "deity": "Ashta Vasus (Elements of Light)", "traits": "Wealthy, musical, and highly social. They have excellent rhythm in life and often gain fame.", "famous": "Marilyn Monroe, Princess Diana", "color": "#D97706"},
    {"id": "shatabhisha", "name": "Shatabhisha", "sanskrit": "शतभिषा", "deity": "Varuna (God of Cosmic Waters)", "traits": "Mysterious, healing, and reclusive. They possess hidden wisdom and excel in medicine, astrology, and tech.", "famous": "Robin Williams, Elvis Presley", "color": "#4338CA"},
    {"id": "purva-bhadrapada", "name": "Purva Bhadrapada", "sanskrit": "पूर्वभाद्रपदा", "deity": "Aja Ekapad (One-footed Goat/Dragon)", "traits": "Eccentric, intense, and deeply mystical. They walk between the material and spiritual worlds.", "famous": "Martin Luther King, Michael Jackson", "color": "#7E22CE"},
    {"id": "uttara-bhadrapada", "name": "Uttara Bhadrapada", "sanskrit": "उत्तरभाद्रपदा", "deity": "Ahir Budhanya (Serpent of the Deep)", "traits": "Wise, compassionate, and highly protected. They are the peaceful warriors who provide for others.", "famous": "Hillary Clinton, Indira Gandhi", "color": "#1E3A8A"},
    {"id": "revati", "name": "Revati", "sanskrit": "रेवती", "deity": "Pushan (Nourisher & Guide)", "traits": "The most empathetic, wealthy, and gentle souls. They love animals, children, and act as guides to others.", "famous": "Rabindranath Tagore, Angelina Jolie", "color": "#0F766E"}
]

BHAJAN_MAP = {
    "ashwini":           [("Ashwini Kumaras Stotram", "अश्विनौ देवभिषजौ"), ("Dhanvantari Mantra", "ॐ नमो भगवते वासुदेवाय"), ("Healing Ashtakam", "रोगान् शेषान् पहंसि तुष्टरुप")],
    "bharani":           [("Yama Stuti", "यमाय धर्मराजाय मृत्यवे चान्तकाय च"), ("Mritunjaya Mantra", "ॐ त्र्यम्बकं यजामहे"), ("Kala Bhairava Ashtakam", "देवराज सेव्यमान पावनांघ्रि पंकजम्")],
    "krittika":          [("Agni Stotram", "अग्निमीळे पुरोहितं यज्ञस्य देवमृत्विजम्"), ("Subrahmanya Kavacham", "कार्तिकेय महाबाहो"), ("Pavamana Suktam", "पवमानः सोमो अद्य")],
    "rohini":            [("Brahma Stuti", "नमो ब्रह्मण्य देवाय"), ("Saraswati Vandana", "या कुन्देन्दु तुषार हार धवला"), ("Shri Suktam", "हिरण्यवर्णां हरिणीं")],
    "mrigashira":        [("Chandra Kavacham", "दधिशंखतुषाराभं"), ("Soma Stotram", "सोमं मनसि संयोज्य"), ("Mrigashira Dhyanam", "मृगशीर्षे शीतलं सौम्यरूपम्")],
    "ardra":             [("Shiva Tandava Stotram", "जटाटवीगलज्जलप्रवाहपावितस्थले"), ("Rudrashtakam", "नमामीशमीशान निर्वाणरूपम्"), ("Maha Mrityunjaya Mantra", "ॐ त्र्यम्बकं यजामहे सुगन्धिम्")],
    "punarvasu":         [("Aditi Stuthi", "अदितिर्द्यौरदितिरन्तरिक्षम्"), ("Devi Mahatmyam", "या देवी सर्वभूतेषु मातृरूपेण"), ("Punarvasu Sukta", "पुनर्नो देव्यदिते")],
    "pushya":            [("Brihaspati Stotra", "देवानां च ऋषीणां च गुरुम्"), ("Guru Stotram", "गुरुर्ब्रह्मा गुरुर्विष्णुः"), ("Pushya Nakshatra Mantra", "ॐ पुष्य पुष्टिदाय नमः")],
    "ashlesha":          [("Naga Stotram", "अनन्तं वासुकिं शेषं"), ("Sarpa Suktam", "नमोऽस्तु सर्पेभ्यो"), ("Kundalini Stuti", "कुण्डलिनी महाशक्ति")],
    "magha":             [("Pitru Tarpan Mantra", "ॐ पितृभ्यः स्वधा नमः"), ("Pitru Stotram", "अर्चितानाममराणां च पितृणाम्"), ("Magha Dhyana", "मघा नक्षत्रे पितृस्वरूपम्")],
    "purva-phalguni":    [("Bhaga Stuti", "भगाय पूर्वफाल्गुने"), ("Lalita Sahasranama", "ललिता सहस्रनाम स्तोत्रम्"), ("Ananda Lahari", "शिवः शक्त्या युक्तो")],
    "uttara-phalguni":   [("Aryaman Sukta", "आर्यमणं वरुणं"), ("Vivah Mantra", "ॐ सोमः प्रथमो विविदे"), ("Uttara Phalguni Stuti", "उत्तरफाल्गुनी आर्यमन् देव")],
    "hasta":             [("Savitar Sukta", "तत् सवितुर्वरेण्यम्"), ("Hasta Nakshatra Mantra", "ॐ सवित्रे नमः"), ("Dhanvantari Stotra", "नमामि धन्वंतरिमादिदेवम्")],
    "chitra":            [("Vishwakarma Stuti", "ॐ विश्वकर्मने नमः"), ("Twashtr Mantra", "त्वष्टारं नव्यसा मह"), ("Chitra Dhyana", "चित्रं देवानामुद्गाद् अनीकम्")],
    "swati":             [("Vayu Stotram", "वायुर्वाति शिवः"), ("Hanuman Chalisa", "जय हनुमान ज्ञान गुण सागर"), ("Swati Nakshatra Mantra", "ॐ वायवे नमः")],
    "vishakha":          [("Indragni Sukta", "इन्द्राग्नी आ गतं"), ("Shakti Stotram", "शक्ति महाशक्ति"), ("Vishakha Dhyana", "विशाखायां शक्रानलस्वरूपम्")],
    "anuradha":          [("Mitra Stuti", "मित्रस्य चर्षणीधृतो"), ("Vishnu Sahasranama", "विश्वम् विष्णुः"), ("Anuradha Mantra", "ॐ मित्राय नमः")],
    "jyeshtha":          [("Indra Stuti", "इन्द्रं विश्वा अवीवृधन्"), ("Mahendra Mantra", "ॐ इन्द्राय नमः"), ("Jyeshtha Nakshatra Dhyana", "ज्येष्ठा नक्षत्रे इन्द्र स्वरूपम्")],
    "mula":              [("Kali Stotram", "क्रीं क्रीं क्रीं"), ("Nirriti Sukta", "निऋत्यै नमः"), ("Mula Mantra Stuti", "ॐ मूलाय निरृत्यै नमः")],
    "purva-ashadha":     [("Apas Sukta", "अपो हि ष्ठा मयोभुवः"), ("Varuna Stotram", "वरुणस्य उत्तम्भनम्"), ("Purva Ashadha Dhyana", "पूर्वाषाढायां अप् देवतास्वरूपम्")],
    "uttara-ashadha":    [("Vishvedeva Sukta", "विश्वे देवासो"), ("Uttara Ashadha Mantra", "ॐ विश्वेभ्यो देवेभ्यो नमः"), ("Apraajita Stotram", "अपराजितं जयदाम्")],
    "shravana":          [("Vishnu Stuti", "शान्ताकारं भुजगशयनं"), ("Shravana Mantra", "ॐ विष्णवे नमः"), ("Achyutashtakam", "अच्युतं केशवम्")],
    "dhanishtha":        [("Ashta Vasus Stuti", "वसवो वसुधा वसु"), ("Dhanishtha Mantra", "ॐ वसुभ्यो नमः"), ("Kubera Stotram", "धनदाय नमस्तुभ्यम्")],
    "shatabhisha":       [("Varuna Mantra", "ॐ वरुणाय नमः"), ("Shatabhisha Dhyana", "शतभिषायां वरुण देवतास्वरूपम्"), ("Navagraha Stotra", "ब्रह्मा मुरारिः त्रिपुरान्तकारी")],
    "purva-bhadrapada":  [("Aja Ekapad Mantra", "ॐ अज एकपादे नमः"), ("Shiva Panchakshara", "नागेन्द्रहाराय त्रिलोचनाय"), ("Purva Bhadra Dhyana", "पूर्वभाद्रपदायाम् अज एकपाद स्वरूपम्")],
    "uttara-bhadrapada": [("Ahir Budhanya Mantra", "ॐ अहिर्बुध्न्याय नमः"), ("Uttara Bhadra Dhyana", "उत्तरभाद्रपदायाम् अहिर्बुध्न्य स्वरूपम्"), ("Shanti Mantra", "ॐ शं नो मित्रः")],
    "revati":            [("Pushan Sukta", "पूषन् एकर्षे यम सूर्य"), ("Revati Dhyana", "रेवत्यां पूषन् देवतास्वरूपम्"), ("Ganesha Atharvashirsha", "त्वं ब्रह्मा त्वं विष्णुस्त्वम्")]
}

def hex_to_rgba(hex_color, alpha=0.15):
    h = hex_color.lstrip('#')
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"

def generate_html(n):
    color = n["color"]
    color_soft = hex_to_rgba(color, 0.12)
    color_mid  = hex_to_rgba(color, 0.30)
    bhajans = BHAJAN_MAP.get(n["id"], [
        ("Nakshatra Mantra", "ॐ नमः शिवाय"),
        ("Devi Stotram", "या देवी सर्वभूतेषु"),
        ("Universal Prayer", "ॐ सर्वे भवन्तु सुखिनः")
    ])
    famous_list = [f.strip() for f in n["famous"].split(",")]

    bhajan_items = ""
    for i, (title, mantra) in enumerate(bhajans, 1):
        bhajan_items += f"""
        <div class="bhajan-card" style="animation-delay:{i*0.1}s">
          <div class="bhajan-num" style="background:{color};color:#fff;">{i}</div>
          <div class="bhajan-body">
            <div class="bhajan-title">{title}</div>
            <div class="bhajan-mantra">{mantra}</div>
          </div>
        </div>"""

    famous_items = "".join(f'<li class="famous-item"><span class="famous-dot" style="background:{color}"></span>{p}</li>' for p in famous_list)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{n['name']} Nakshatra — Bhajan & Devotion | bhajan.ournakshatra.com</title>
  <meta name="description" content="Explore the devotion, bhajans, mantras, and divine nature of {n['name']} Nakshatra. Ruled by {n['deity']}." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Tiro+Devanagari+Hindi:ital@0;1&family=Lato:wght@300;400;700;900&display=swap" rel="stylesheet" />
  <style>
    :root {{
      --bg: #F5F0E8;
      --surface: #EDE6D8;
      --surface2: #E6DDD0;
      --saffron: #C96A1F;
      --maroon: #6E1515;
      --gold: #A8832A;
      --text: #2A1A08;
      --text-sec: #5C3D20;
      --text-muted: #8C6A45;
      --border: #D9CDBA;
      --radius: 12px;
      --font-hindi: 'Tiro Devanagari Hindi', serif;
      --font-ui: 'Lato', sans-serif;
      --accent: {color};
      --accent-soft: {color_soft};
      --accent-mid: {color_mid};
    }}
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      font-family: var(--font-ui);
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
      line-height: 1.7;
    }}

    /* ── HEADER ── */
    header {{
      position: sticky;
      top: 0;
      z-index: 100;
      background: rgba(245,240,232,0.92);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      padding: 0 24px;
      height: 60px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .logo {{
      font-family: var(--font-ui);
      font-weight: 900;
      font-size: 1.05rem;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--maroon);
      text-decoration: none;
    }}
    .logo span {{ color: var(--accent); }}
    nav a {{
      font-size: 0.82rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--text-sec);
      text-decoration: none;
      padding: 6px 14px;
      border-radius: 20px;
      border: 1px solid var(--border);
      transition: all 0.2s;
    }}
    nav a:hover {{ background: var(--accent); color: #fff; border-color: var(--accent); }}

    /* ── HERO BANNER ── */
    .hero {{
      position: relative;
      overflow: hidden;
      padding: 72px 24px 56px;
      text-align: center;
      border-bottom: 4px solid var(--accent);
      background:
        radial-gradient(ellipse 70% 60% at 50% 0%, var(--accent-soft) 0%, transparent 70%),
        var(--bg);
    }}
    .hero::before {{
      content: '';
      position: absolute;
      inset: 0;
      background-image:
        radial-gradient(circle at 20% 80%, var(--accent-mid) 0%, transparent 40%),
        radial-gradient(circle at 80% 20%, var(--accent-mid) 0%, transparent 35%);
      pointer-events: none;
    }}
    .hero-number {{
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 700;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--accent);
      border: 1px solid var(--accent);
      border-radius: 20px;
      padding: 4px 14px;
      margin-bottom: 20px;
      position: relative;
    }}
    .hero-sanskrit {{
      font-family: var(--font-hindi);
      font-size: clamp(2.8rem, 8vw, 5.5rem);
      color: var(--accent);
      line-height: 1.1;
      position: relative;
      margin-bottom: 4px;
    }}
    .hero-name {{
      font-size: clamp(1.1rem, 3vw, 1.6rem);
      font-weight: 300;
      letter-spacing: 0.3em;
      text-transform: uppercase;
      color: var(--text-sec);
      position: relative;
      margin-bottom: 18px;
    }}
    .hero-deity {{
      font-size: 0.9rem;
      color: var(--text-muted);
      font-weight: 400;
      position: relative;
    }}
    .hero-deity strong {{ color: var(--accent); font-weight: 700; }}

    /* ── CONTENT WRAPPER ── */
    .content-wrapper {{
      max-width: 760px;
      margin: 0 auto;
      padding: 48px 24px 80px;
      display: flex;
      flex-direction: column;
      gap: 40px;
    }}

    /* ── SECTION CARD ── */
    .card {{
      background: var(--surface);
      border-radius: var(--radius);
      border: 1px solid var(--border);
      overflow: hidden;
      animation: fadeUp 0.5s ease both;
    }}
    @keyframes fadeUp {{
      from {{ opacity: 0; transform: translateY(16px); }}
      to   {{ opacity: 1; transform: translateY(0); }}
    }}
    .card-header {{
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 18px 24px 14px;
      border-bottom: 1px solid var(--border);
    }}
    .card-icon {{
      width: 36px;
      height: 36px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      flex-shrink: 0;
      background: var(--accent-soft);
      border: 2px solid var(--accent);
    }}
    .card-title {{
      font-size: 0.7rem;
      font-weight: 900;
      letter-spacing: 0.2em;
      text-transform: uppercase;
      color: var(--accent);
    }}
    .card-body {{ padding: 22px 24px; }}

    /* ── DEITY SECTION ── */
    .deity-text {{
      font-size: 1rem;
      color: var(--text-sec);
      line-height: 1.8;
    }}

    /* ── BHAJAN CARDS ── */
    .bhajan-card {{
      display: flex;
      align-items: flex-start;
      gap: 16px;
      padding: 16px 0;
      border-bottom: 1px solid var(--border);
      animation: fadeUp 0.5s ease both;
    }}
    .bhajan-card:last-child {{ border-bottom: none; padding-bottom: 0; }}
    .bhajan-num {{
      width: 32px;
      height: 32px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.78rem;
      font-weight: 900;
      flex-shrink: 0;
      margin-top: 2px;
    }}
    .bhajan-title {{
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--text);
      margin-bottom: 4px;
    }}
    .bhajan-mantra {{
      font-family: var(--font-hindi);
      font-size: 0.95rem;
      color: var(--text-muted);
      line-height: 1.5;
    }}

    /* ── TRAITS ── */
    .traits-text {{
      font-size: 1rem;
      color: var(--text-sec);
      line-height: 1.85;
      padding-left: 16px;
      border-left: 3px solid var(--accent);
    }}

    /* ── FAMOUS ── */
    .famous-list {{
      list-style: none;
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .famous-item {{
      display: flex;
      align-items: center;
      gap: 8px;
      background: var(--surface2);
      border: 1px solid var(--border);
      border-radius: 20px;
      padding: 6px 14px;
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--text-sec);
    }}
    .famous-dot {{
      width: 8px;
      height: 8px;
      border-radius: 50%;
      flex-shrink: 0;
    }}

    /* ── CROSS-LINK BANNER ── */
    .cta-banner {{
      background: linear-gradient(135deg, var(--maroon) 0%, {color} 100%);
      border-radius: var(--radius);
      padding: 36px 32px;
      text-align: center;
      position: relative;
      overflow: hidden;
      border: none;
    }}
    .cta-banner::before {{
      content: '✦';
      position: absolute;
      font-size: 8rem;
      color: rgba(255,255,255,0.04);
      top: -20px;
      right: -10px;
      line-height: 1;
    }}
    .cta-banner::after {{
      content: '✦';
      position: absolute;
      font-size: 5rem;
      color: rgba(255,255,255,0.06);
      bottom: -10px;
      left: 10px;
      line-height: 1;
    }}
    .cta-eyebrow {{
      font-size: 0.68rem;
      font-weight: 700;
      letter-spacing: 0.22em;
      text-transform: uppercase;
      color: rgba(255,255,255,0.65);
      margin-bottom: 10px;
    }}
    .cta-headline {{
      font-size: clamp(1.2rem, 3vw, 1.7rem);
      font-weight: 900;
      color: #fff;
      line-height: 1.25;
      margin-bottom: 22px;
    }}
    .cta-headline em {{
      font-style: normal;
      border-bottom: 2px solid rgba(255,255,255,0.5);
    }}
    .cta-btn {{
      display: inline-block;
      background: #fff;
      color: var(--maroon);
      font-weight: 900;
      font-size: 0.88rem;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      text-decoration: none;
      padding: 14px 32px;
      border-radius: 30px;
      transition: transform 0.2s, box-shadow 0.2s;
      position: relative;
    }}
    .cta-btn:hover {{ transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,0,0,0.25); }}

    /* ── FOOTER ── */
    footer {{
      text-align: center;
      padding: 28px 24px;
      font-size: 0.78rem;
      color: var(--text-muted);
      border-top: 1px solid var(--border);
    }}
    footer a {{ color: var(--accent); text-decoration: none; font-weight: 600; }}

    @media (max-width: 480px) {{
      .hero {{ padding: 52px 16px 40px; }}
      .card-body, .card-header {{ padding-left: 16px; padding-right: 16px; }}
      .cta-banner {{ padding: 28px 20px; }}
    }}
  </style>
</head>
<body>

<header>
  <a href="https://bhajan.ournakshatra.com" class="logo">NAKSHATRA <span>✦</span> BHAJAN</a>
  <nav>
    <a href="https://ournakshatra.com/nakshatra" target="_blank">Find Yours</a>
  </nav>
</header>

<div class="hero">
  <div class="hero-number">Janma Nakshatra</div>
  <div class="hero-sanskrit">{n['sanskrit']}</div>
  <div class="hero-name">{n['name']} Nakshatra</div>
  <div class="hero-deity">Ruling Deity: <strong>{n['deity']}</strong></div>
</div>

<main class="content-wrapper">

  <!-- Deity -->
  <div class="card" style="animation-delay:0.05s">
    <div class="card-header">
      <div class="card-icon">🪔</div>
      <div class="card-title">Ruling Deity &amp; Cosmic Role</div>
    </div>
    <div class="card-body">
      <p class="deity-text">
        The presiding deity of <strong>{n['name']}</strong> Nakshatra is <strong style="color:var(--accent)">{n['deity']}</strong>.
        This divine force shapes the soul of every being born under this star, imparting their celestial qualities, cosmic duties,
        and spiritual gifts. By devotion to this deity through bhajan and mantra, native souls harmonise with their
        highest dharmic potential and unlock the blessings encoded in their birth star.
      </p>
    </div>
  </div>

  <!-- Bhajans -->
  <div class="card" style="animation-delay:0.1s">
    <div class="card-header">
      <div class="card-icon">🎵</div>
      <div class="card-title">Recommended Bhajans &amp; Mantras</div>
    </div>
    <div class="card-body">
      {bhajan_items}
    </div>
  </div>

  <!-- Traits -->
  <div class="card" style="animation-delay:0.15s">
    <div class="card-header">
      <div class="card-icon">🌟</div>
      <div class="card-title">Personality &amp; Nature</div>
    </div>
    <div class="card-body">
      <p class="traits-text">{n['traits']}</p>
    </div>
  </div>

  <!-- Famous -->
  <div class="card" style="animation-delay:0.2s">
    <div class="card-header">
      <div class="card-icon">👑</div>
      <div class="card-title">Famous Personalities</div>
    </div>
    <div class="card-body">
      <ul class="famous-list">
        {famous_items}
      </ul>
    </div>
  </div>

  <!-- CTA Banner -->
  <div class="cta-banner">
    <div class="cta-eyebrow">✦ Discover Your Star ✦</div>
    <div class="cta-headline">
      Find your <em>Janma Nakshatra</em> in seconds →
    </div>
    <a class="cta-btn" href="https://ournakshatra.com/nakshatra" target="_blank" rel="noopener">
      Calculate at ournakshatra.com
    </a>
  </div>

</main>

<footer>
  <p>© 2024 <a href="https://bhajan.ournakshatra.com">bhajan.ournakshatra.com</a> — Sacred Devotion for Every Nakshatra</p>
</footer>

</body>
</html>
"""

def main():
    created = 0
    for n in NAKSHATRAS_DATA:
        dir_path = os.path.join("nakshatra", n["id"])
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, "index.html")
        html = generate_html(n)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        created += 1
        print(f"  ✓  {file_path}")
    print(f"\n✅  Done — {created}/27 Nakshatra pages generated in nakshatra/")

if __name__ == "__main__":
    main()
