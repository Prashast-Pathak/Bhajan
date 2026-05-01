#!/usr/bin/env python3
"""
generate_planets.py
Generates 9 Planet Mantra hub pages for bhajan.ournakshatra.com
Creates: planet/<id>/index.html for all 9 Vedic planets.
"""

import os

# ─────────────────────────────────────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────────────────────────────────────

PLANETS_DATA = [
    {
        "id": "surya",
        "name": "Surya (Sun)",
        "hindi_name": "सूर्य देव",
        "deity": "Lord Ram / Surya Dev",
        "why_deity": (
            "Lord Ram belongs to the Suryavansha (Solar Dynasty) and embodies "
            "the pure, authoritative, and soul-illuminating qualities of the Sun."
        ),
        "mantra_sanskrit": "ॐ ह्रां ह्रीं ह्रौं सः सूर्याय नमः",
        "mantra_hindi": "ओम ह्रां ह्रीं ह्रौं सः सूर्याय नमः",
        "mantra_english": "Om Hraam Hreem Hroum Sah Suryaya Namah",
        "bhajans": [
            "Aditya Hrudayam Stotram",
            "Shri Ram Chandra Kripalu Bhajman",
            "Surya Ashtakam",
        ],
        "when_to_chant": (
            "Chant on Sundays, during Surya Mahadasha, or when seeking confidence, "
            "leadership, and radiant health. The ideal time is at sunrise, facing east, "
            "after bathing. Offering water (Arghya) to the rising Sun while chanting "
            "amplifies the mantra's potency and clears solar afflictions in the birth chart."
        ),
        "color": "#D97706",
        "symbol": "☀",
        "day": "Sunday",
    },
    {
        "id": "chandra",
        "name": "Chandra (Moon)",
        "hindi_name": "चंद्र देव",
        "deity": "Lord Shiva",
        "why_deity": (
            "Lord Shiva wears the crescent moon (Chandrashekhar) on his head, "
            "controlling the mind, emotions, and the cooling lunar energies."
        ),
        "mantra_sanskrit": "ॐ श्रां श्रीं श्रौं सः चन्द्रमसे नमः",
        "mantra_hindi": "ओम श्रां श्रीं श्रौं सः चन्द्रमसे नमः",
        "mantra_english": "Om Shraam Shreem Shroum Sah Chandramase Namah",
        "bhajans": [
            "Shiva Tandava Stotram",
            "Om Namah Shivaya",
            "Chandrashekhara Ashtakam",
        ],
        "when_to_chant": (
            "Chant on Mondays, during Chandra Mahadasha, or to calm anxiety and find "
            "emotional peace. Chanting on Purnima (full moon night) is especially potent. "
            "Sit near a window in the moonlight and offer milk or white flowers to "
            "Lord Shiva. This practice strengthens the Moon in the horoscope and "
            "stabilises the mind."
        ),
        "color": "#1E40AF",
        "symbol": "☽",
        "day": "Monday",
    },
    {
        "id": "mangal",
        "name": "Mangal (Mars)",
        "hindi_name": "मंगल देव",
        "deity": "Lord Hanuman",
        "why_deity": (
            "Lord Hanuman represents supreme courage, physical strength, and protection, "
            "perfectly balancing the fiery and aggressive nature of Mars."
        ),
        "mantra_sanskrit": "ॐ क्रां क्रीं क्रौं सः भौमाय नमः",
        "mantra_hindi": "ओम क्रां क्रीं क्रौं सः भौमाय नमः",
        "mantra_english": "Om Kraam Kreem Kroum Sah Bhaumaya Namah",
        "bhajans": [
            "Hanuman Chalisa",
            "Bajrang Baan",
            "Sankat Mochan Hanuman Ashtak",
        ],
        "when_to_chant": (
            "Chant on Tuesdays, during Mangal Mahadasha, or to cure Mangal Dosha "
            "and overcome fear. The most auspicious time is after sunrise on Tuesday. "
            "Offer red flowers and laddoos to Lord Hanuman. Regular chanting on "
            "Tuesdays is widely recommended for those with Mangal Dosha in their chart "
            "to pacify Mars and reduce conflict in relationships."
        ),
        "color": "#DC2626",
        "symbol": "♂",
        "day": "Tuesday",
    },
    {
        "id": "budha",
        "name": "Budha (Mercury)",
        "hindi_name": "बुध देव",
        "deity": "Lord Ganesha / Vishnu",
        "why_deity": (
            "Lord Ganesha rules intellect, speech, and business, which are the exact "
            "domains of Mercury in Vedic Astrology."
        ),
        "mantra_sanskrit": "ॐ ब्रां ब्रीं ब्रौं सः बुधाय नमः",
        "mantra_hindi": "ओम ब्रां ब्रीं ब्रौं सः बुधाय नमः",
        "mantra_english": "Om Braam Breem Broum Sah Budhaya Namah",
        "bhajans": [
            "Ganesha Pancharatnam",
            "Vakratunda Mahakaya",
            "Vishnu Sahasranama",
        ],
        "when_to_chant": (
            "Chant on Wednesdays, during Budha Mahadasha, or for success in studies "
            "and business. Offer green grass (durva) and green fruits to Lord Ganesha. "
            "Students preparing for exams and professionals in communication, finance, "
            "or trade benefit enormously from daily chanting of this mantra to sharpen "
            "Mercury's analytical and communicative gifts."
        ),
        "color": "#15803D",
        "symbol": "☿",
        "day": "Wednesday",
    },
    {
        "id": "guru",
        "name": "Guru (Jupiter)",
        "hindi_name": "बृहस्पति देव",
        "deity": "Lord Vishnu / Brihaspati",
        "why_deity": (
            "Lord Vishnu is the supreme preserver and represents Dharma, divine wisdom, "
            "and wealth—the core attributes of Jupiter."
        ),
        "mantra_sanskrit": "ॐ ग्रां ग्रीं ग्रौं सः गुरवे नमः",
        "mantra_hindi": "ओम ग्रां ग्रीं ग्रौं सः गुरवे नमः",
        "mantra_english": "Om Graam Greem Groum Sah Gurave Namah",
        "bhajans": [
            "Vishnu Sahasranama",
            "Achyutashtakam",
            "Brihaspati Aarti",
        ],
        "when_to_chant": (
            "Chant on Thursdays, during Guru Mahadasha, or for spiritual growth, "
            "marriage, and prosperity. Offer yellow flowers, turmeric, and chickpea "
            "laddoos. Jupiter governs children, teachers, and higher wisdom—chanting "
            "this mantra on Thursday mornings while wearing yellow clothes is a "
            "time-honoured remedy for a weak or afflicted Jupiter."
        ),
        "color": "#A8832A",
        "symbol": "♃",
        "day": "Thursday",
    },
    {
        "id": "shukra",
        "name": "Shukra (Venus)",
        "hindi_name": "शुक्र देव",
        "deity": "Goddess Lakshmi / Durga",
        "why_deity": (
            "Goddess Lakshmi governs wealth, beauty, luxury, and harmonious "
            "relationships, perfectly mirroring Venus."
        ),
        "mantra_sanskrit": "ॐ द्रां द्रीं द्रौं सः शुक्राय नमः",
        "mantra_hindi": "ओम द्रां द्रीं द्रौं सः शुक्राय नमः",
        "mantra_english": "Om Draam Dreem Droum Sah Shukraya Namah",
        "bhajans": [
            "Mahalakshmi Ashtakam",
            "Sri Suktam",
            "Ya Devi Sarvabhuteshu",
        ],
        "when_to_chant": (
            "Chant on Fridays, during Shukra Mahadasha, or to attract abundance "
            "and marital happiness. Offer white flowers, kheer (rice pudding), and "
            "perfume to Goddess Lakshmi. Venus governs love, art, and luxury—those "
            "facing relationship challenges or financial stagnation find great relief "
            "in this mantra chanted 108 times every Friday."
        ),
        "color": "#C96A1F",
        "symbol": "♀",
        "day": "Friday",
    },
    {
        "id": "shani",
        "name": "Shani (Saturn)",
        "hindi_name": "शनि देव",
        "deity": "Shani Dev / Lord Shiva",
        "why_deity": (
            "Shani Dev is the lord of Karma and justice. Lord Shiva is his guru "
            "and chanting Shiva mantras pacifies Saturn's harsh lessons."
        ),
        "mantra_sanskrit": "ॐ प्रां प्रीं प्रौं सः शनैश्चराय नमः",
        "mantra_hindi": "ओम प्रां प्रीं प्रौं सः शनैश्चराय नमः",
        "mantra_english": "Om Praam Preem Proum Sah Shanaishcharaya Namah",
        "bhajans": [
            "Shani Aarti",
            "Shani Chalisa",
            "Shiva Panchakshara Stotram",
        ],
        "when_to_chant": (
            "Chant on Saturdays, during Sade Sati or Shani Dhaiya, and during "
            "Shani Mahadasha. Offer sesame oil, black sesame seeds, and iron to "
            "Lord Shani. Saturn rewards discipline—chant this mantra during "
            "Shani's hora every Saturday with sincere intent, and you will "
            "transform karmic debts into stepping stones of spiritual growth."
        ),
        "color": "#374151",
        "symbol": "♄",
        "day": "Saturday",
    },
    {
        "id": "rahu",
        "name": "Rahu (North Node)",
        "hindi_name": "राहु",
        "deity": "Goddess Durga / Kali",
        "why_deity": (
            "Fierce forms of the Divine Mother like Durga and Kali cut through "
            "illusions (Maya) and protect against the sudden, chaotic energy of Rahu."
        ),
        "mantra_sanskrit": "ॐ भ्रां भ्रीं भ्रौं सः राहवे नमः",
        "mantra_hindi": "ओम भ्रां भ्रीं भ्रौं सः राहवे नमः",
        "mantra_english": "Om Bhraam Bhreem Bhroum Sah Rahave Namah",
        "bhajans": [
            "Durga Chalisa",
            "Mahishasura Mardini Stotram",
            "Kali Ashtakam",
        ],
        "when_to_chant": (
            "Chant during Rahu Kaal, Rahu Mahadasha, or when facing sudden obstacles "
            "and confusion. Rahu Kaal falls at a specific 90-minute window each day—"
            "chanting during this window is uniquely powerful. Offer blue or black "
            "flowers to Goddess Kali. This mantra guards against deception, hidden "
            "enemies, and the maya-like distortions that Rahu casts over the mind."
        ),
        "color": "#4B5563",
        "symbol": "☊",
        "day": "Rahu Kaal",
    },
    {
        "id": "ketu",
        "name": "Ketu (South Node)",
        "hindi_name": "केतु",
        "deity": "Lord Ganesha",
        "why_deity": (
            "Lord Ganesha is the remover of obstacles. Ketu represents spiritual "
            "liberation (Moksha) but also detachment, which Ganesha guides safely."
        ),
        "mantra_sanskrit": "ॐ स्त्रां स्त्रीं स्त्रौं सः केतवे नमः",
        "mantra_hindi": "ओम स्त्रां स्त्रीं स्त्रौं सः केतवे नमः",
        "mantra_english": "Om Straam Streem Stroum Sah Ketave Namah",
        "bhajans": [
            "Ganesha Chalisa",
            "Sankat Nashan Ganesh Stotram",
        ],
        "when_to_chant": (
            "Chant during Ketu Mahadasha, or to seek spiritual enlightenment and "
            "detach from materialistic pain. Ketu is a spiritual planet—chanting "
            "is most effective during the brahma muhurta (pre-dawn hours) or in "
            "a quiet meditative space. Offer kusha grass and durva to Lord Ganesha. "
            "This mantra accelerates moksha-oriented karma and dissolves past-life "
            "attachments that block present-life progress."
        ),
        "color": "#4B5563",
        "symbol": "☋",
        "day": "Ketu Kaal",
    },
]


# ─────────────────────────────────────────────────────────────────────────────
# HTML GENERATOR
# ─────────────────────────────────────────────────────────────────────────────

def make_bhajan_items(bhajans: list[str], color: str) -> str:
    items = ""
    for b in bhajans:
        items += f"""
                    <li class="bhajan-item">
                        <span class="bhajan-dot" style="background:{color};"></span>
                        <a href="https://bhajan.ournakshatra.com/search?q={b.replace(' ', '+')}"
                           class="bhajan-link">{b}</a>
                    </li>"""
    return items


def generate_html(planet: dict) -> str:
    color      = planet["color"]
    name       = planet["name"]
    hindi_name = planet["hindi_name"]
    deity      = planet["deity"]
    why_deity  = planet["why_deity"]
    ms         = planet["mantra_sanskrit"]
    mh         = planet["mantra_hindi"]
    me         = planet["mantra_english"]
    when       = planet["when_to_chant"]
    symbol     = planet["symbol"]
    day        = planet["day"]
    pid        = planet["id"]
    bhajan_html = make_bhajan_items(planet["bhajans"], color)

    # Compute a lighter tint of the planet color for subtle backgrounds (10% opacity)
    # We do this inline via CSS rgba — just pass the hex and let CSS handle it
    # Also compute a semi-transparent version for gradient overlays
    # We'll use a CSS custom property scoped to the page.

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{name} Mantra | Planet Mantras | NAKSHATRA</title>
    <meta name="description"
          content="Learn the {name} mantra, ruling deity {deity}, recommended bhajans, and when to chant for astrological blessings." />

    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Tiro+Devanagari+Hindi:ital@0;1&family=Lato:wght@300;400;700;900&display=swap"
          rel="stylesheet" />

    <style>
        /* ── Global CSS Variables ─────────────────────────────── */
        :root {{
            --bg:           #F5F0E8;
            --surface:      #EDE6D8;
            --surface2:     #E6DDD0;
            --saffron:      #C96A1F;
            --maroon:       #6E1515;
            --gold:         #A8832A;
            --text:         #2A1A08;
            --text-sec:     #5C3D20;
            --text-muted:   #8C6A45;
            --border:       #D9CDBA;
            --radius:       12px;
            --font-hindi:   'Tiro Devanagari Hindi', serif;
            --font-ui:      'Lato', sans-serif;

            /* ── Planet-specific accent (dynamic per page) ── */
            --planet-color: {color};
        }}

        /* ── Reset & Base ─────────────────────────────────────── */
        *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

        html {{ scroll-behavior: smooth; }}

        body {{
            background: var(--bg);
            color: var(--text);
            font-family: var(--font-ui);
            font-size: 16px;
            line-height: 1.7;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }}

        a {{ color: var(--planet-color); text-decoration: none; transition: opacity .2s; }}
        a:hover {{ opacity: .75; }}

        img {{ max-width: 100%; display: block; }}

        /* ── Sticky Header ────────────────────────────────────── */
        .site-header {{
            position: sticky;
            top: 0;
            z-index: 100;
            background: var(--maroon);
            border-bottom: 3px solid var(--planet-color);
            padding: 0 1.5rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
            height: 64px;
            box-shadow: 0 2px 12px rgba(0,0,0,.35);
        }}

        .site-header .logo {{
            display: flex;
            align-items: center;
            gap: .55rem;
            text-decoration: none;
        }}

        .site-header .logo-symbol {{
            font-size: 1.6rem;
            color: var(--planet-color);
            line-height: 1;
        }}

        .site-header .logo-text {{
            font-family: var(--font-ui);
            font-weight: 900;
            font-size: 1.25rem;
            letter-spacing: .12em;
            color: #fff;
        }}

        .site-header .logo-sub {{
            font-size: .65rem;
            color: rgba(255,255,255,.6);
            letter-spacing: .15em;
            display: block;
            margin-top: -2px;
        }}

        .header-nav {{
            display: flex;
            gap: 1.5rem;
            align-items: center;
        }}

        .header-nav a {{
            color: rgba(255,255,255,.8);
            font-size: .85rem;
            font-weight: 700;
            letter-spacing: .06em;
            text-transform: uppercase;
            text-decoration: none;
            transition: color .2s;
        }}

        .header-nav a:hover {{ color: var(--planet-color); }}

        /* ── Content Wrapper ──────────────────────────────────── */
        .content-wrapper {{
            flex: 1;
            max-width: 860px;
            width: 100%;
            margin: 0 auto;
            padding: 2.5rem 1.5rem 4rem;
        }}

        /* ── Hero Banner ──────────────────────────────────────── */
        .hero-banner {{
            background: var(--surface);
            border: 2px solid var(--planet-color);
            border-radius: var(--radius);
            padding: 2.5rem 2rem 2rem;
            margin-bottom: 2.5rem;
            position: relative;
            overflow: hidden;
            box-shadow: 0 4px 24px rgba(0,0,0,.08);
        }}

        .hero-banner::before {{
            content: '{symbol}';
            position: absolute;
            right: -0.5rem;
            top: 50%;
            transform: translateY(-50%);
            font-size: 9rem;
            color: var(--planet-color);
            opacity: .08;
            line-height: 1;
            pointer-events: none;
            user-select: none;
        }}

        .hero-banner .planet-symbol {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            width: 56px;
            height: 56px;
            border-radius: 50%;
            border: 2.5px solid var(--planet-color);
            color: var(--planet-color);
            font-size: 1.9rem;
            margin-bottom: 1rem;
            background: rgba(255,255,255,.5);
        }}

        .hero-banner .planet-name {{
            font-family: var(--font-ui);
            font-size: 2.1rem;
            font-weight: 900;
            color: var(--planet-color);
            line-height: 1.15;
            margin-bottom: .25rem;
        }}

        .hero-banner .planet-hindi {{
            font-family: var(--font-hindi);
            font-size: 1.5rem;
            color: var(--text-sec);
            margin-bottom: .5rem;
        }}

        .hero-banner .deity-tag {{
            display: inline-block;
            background: var(--planet-color);
            color: #fff;
            font-size: .78rem;
            font-weight: 700;
            letter-spacing: .1em;
            text-transform: uppercase;
            padding: .3rem .85rem;
            border-radius: 99px;
            margin-top: .4rem;
        }}

        .hero-banner .auspicious-day {{
            display: inline-flex;
            align-items: center;
            gap: .4rem;
            margin-left: .6rem;
            font-size: .78rem;
            font-weight: 700;
            color: var(--text-muted);
            letter-spacing: .06em;
            text-transform: uppercase;
        }}

        /* ── Section Cards ────────────────────────────────────── */
        .section-card {{
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius);
            padding: 1.75rem 1.75rem;
            margin-bottom: 1.75rem;
            box-shadow: 0 2px 8px rgba(0,0,0,.04);
        }}

        .section-card .section-label {{
            font-size: .72rem;
            font-weight: 700;
            letter-spacing: .16em;
            text-transform: uppercase;
            color: var(--planet-color);
            margin-bottom: .6rem;
            display: flex;
            align-items: center;
            gap: .5rem;
        }}

        .section-card .section-label::after {{
            content: '';
            flex: 1;
            height: 1px;
            background: var(--border);
        }}

        .section-card h2 {{
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--text);
            margin-bottom: .75rem;
        }}

        .section-card p {{
            color: var(--text-sec);
            line-height: 1.8;
        }}

        /* ── Why Deity ────────────────────────────────────────── */
        .why-deity-card {{
            border-left: 4px solid var(--planet-color);
        }}

        /* ── Mantra Card ──────────────────────────────────────── */
        .mantra-card {{
            border: 2px solid var(--planet-color);
            background: var(--surface2);
            border-radius: var(--radius);
            padding: 2rem 1.75rem;
            margin-bottom: 1.75rem;
            position: relative;
            overflow: hidden;
        }}

        .mantra-card::after {{
            content: 'ॐ';
            position: absolute;
            right: 1.25rem;
            top: 50%;
            transform: translateY(-50%);
            font-family: var(--font-hindi);
            font-size: 6rem;
            color: var(--planet-color);
            opacity: .07;
            pointer-events: none;
            user-select: none;
        }}

        .mantra-card .mantra-row {{
            margin-bottom: 1.25rem;
        }}

        .mantra-card .mantra-row:last-child {{ margin-bottom: 0; }}

        .mantra-card .mantra-lang {{
            font-size: .68rem;
            font-weight: 700;
            letter-spacing: .18em;
            text-transform: uppercase;
            color: var(--planet-color);
            margin-bottom: .3rem;
        }}

        .mantra-card .mantra-text-devanagari {{
            font-family: var(--font-hindi);
            font-size: 1.55rem;
            color: var(--text);
            line-height: 1.5;
        }}

        .mantra-card .mantra-text-hindi {{
            font-family: var(--font-hindi);
            font-size: 1.2rem;
            color: var(--text-sec);
        }}

        .mantra-card .mantra-text-english {{
            font-family: var(--font-ui);
            font-size: 1.05rem;
            font-style: italic;
            color: var(--text-muted);
            letter-spacing: .02em;
        }}

        .mantra-card .divider {{
            border: none;
            border-top: 1px dashed var(--border);
            margin: 1rem 0;
        }}

        /* ── Bhajan List ──────────────────────────────────────── */
        .bhajan-list {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: .7rem;
            margin-top: .5rem;
        }}

        .bhajan-item {{
            display: flex;
            align-items: center;
            gap: .75rem;
        }}

        .bhajan-dot {{
            width: 9px;
            height: 9px;
            border-radius: 50%;
            flex-shrink: 0;
        }}

        .bhajan-link {{
            font-size: 1rem;
            font-weight: 700;
            color: var(--text-sec);
            text-decoration: none;
            transition: color .2s;
        }}

        .bhajan-link:hover {{
            color: var(--planet-color);
        }}

        /* ── Timing Section ───────────────────────────────────── */
        .timing-icon {{
            display: inline-block;
            font-size: 1.3rem;
            color: var(--planet-color);
            margin-right: .35rem;
            vertical-align: middle;
        }}

        /* ── Cross-Link CTA Banner ────────────────────────────── */
        .cta-banner {{
            background: var(--surface2);
            border: 2px solid var(--planet-color);
            border-radius: var(--radius);
            padding: 1.75rem 2rem;
            margin: 2.5rem 0 0;
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1.25rem;
            flex-wrap: wrap;
            box-shadow: 0 4px 18px rgba(0,0,0,.1);
            position: relative;
            overflow: hidden;
        }}

        .cta-banner::before {{
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, transparent 60%, color-mix(in srgb, {color} 15%, transparent));
            pointer-events: none;
        }}

        .cta-banner .cta-text {{
            flex: 1;
        }}

        .cta-banner .cta-eyebrow {{
            font-size: .72rem;
            font-weight: 700;
            letter-spacing: .16em;
            text-transform: uppercase;
            color: var(--planet-color);
            margin-bottom: .3rem;
        }}

        .cta-banner .cta-headline {{
            font-size: 1.15rem;
            font-weight: 900;
            color: var(--text);
            line-height: 1.35;
        }}

        .cta-banner .cta-headline em {{
            font-style: normal;
            color: var(--planet-color);
        }}

        .cta-banner .cta-btn {{
            display: inline-flex;
            align-items: center;
            gap: .5rem;
            background: var(--planet-color);
            color: #fff;
            font-family: var(--font-ui);
            font-weight: 700;
            font-size: .9rem;
            letter-spacing: .06em;
            padding: .75rem 1.5rem;
            border-radius: 99px;
            text-decoration: none;
            white-space: nowrap;
            transition: opacity .2s, transform .15s;
            box-shadow: 0 3px 12px rgba(0,0,0,.2);
        }}

        .cta-banner .cta-btn:hover {{
            opacity: .88;
            transform: translateY(-1px);
        }}

        .cta-banner .cta-btn .arrow {{
            font-size: 1rem;
        }}

        /* ── Footer ───────────────────────────────────────────── */
        .site-footer {{
            background: var(--maroon);
            color: rgba(255,255,255,.65);
            text-align: center;
            padding: 1.75rem 1.5rem;
            font-size: .82rem;
            border-top: 3px solid var(--saffron);
        }}

        .site-footer a {{
            color: var(--saffron);
            text-decoration: none;
            font-weight: 700;
        }}

        .site-footer a:hover {{ color: #fff; }}

        .footer-nav {{
            display: flex;
            gap: 1.5rem;
            justify-content: center;
            margin-bottom: .75rem;
            flex-wrap: wrap;
        }}

        .footer-divider {{
            border: none;
            border-top: 1px solid rgba(255,255,255,.1);
            margin: .75rem 0;
        }}

        /* ── Breadcrumb ───────────────────────────────────────── */
        .breadcrumb {{
            display: flex;
            align-items: center;
            gap: .4rem;
            font-size: .8rem;
            color: var(--text-muted);
            margin-bottom: 1.5rem;
            flex-wrap: wrap;
        }}

        .breadcrumb a {{
            color: var(--text-muted);
            text-decoration: none;
            transition: color .2s;
        }}

        .breadcrumb a:hover {{ color: var(--planet-color); }}

        .breadcrumb .sep {{
            color: var(--border);
        }}

        .breadcrumb .current {{
            color: var(--planet-color);
            font-weight: 700;
        }}

        /* ── Responsive ───────────────────────────────────────── */
        @media (max-width: 600px) {{
            .hero-banner .planet-name {{ font-size: 1.6rem; }}
            .hero-banner::before {{ font-size: 6rem; opacity: .06; }}
            .cta-banner {{ flex-direction: column; align-items: flex-start; }}
            .header-nav {{ display: none; }}
            .mantra-card .mantra-text-devanagari {{ font-size: 1.25rem; }}
        }}
    </style>
</head>
<body>

    <!-- ── STICKY HEADER ────────────────────────────────────── -->
    <header class="site-header">
        <a class="logo" href="https://bhajan.ournakshatra.com">
            <span class="logo-symbol">ॐ</span>
            <span>
                <span class="logo-text">NAKSHATRA</span>
                <span class="logo-sub">Bhajan &amp; Mantra</span>
            </span>
        </a>
        <nav class="header-nav">
            <a href="https://bhajan.ournakshatra.com">Home</a>
            <a href="https://bhajan.ournakshatra.com/planets/" style="color:var(--planet-color);">Planets</a>
            <a href="https://ournakshatra.com/janam-kundali">Free Kundali</a>
        </nav>
    </header>

    <!-- ── MAIN CONTENT ──────────────────────────────────────── -->
    <main class="content-wrapper">

        <!-- Breadcrumb -->
        <nav class="breadcrumb" aria-label="Breadcrumb">
            <a href="https://bhajan.ournakshatra.com">Home</a>
            <span class="sep">›</span>
            <a href="https://bhajan.ournakshatra.com/planets/">Planet Mantras</a>
            <span class="sep">›</span>
            <span class="current">{name}</span>
        </nav>

        <!-- ── HERO BANNER ────────────────────────────────── -->
        <section class="hero-banner" aria-label="Planet overview">
            <div class="planet-symbol" aria-hidden="true">{symbol}</div>
            <h1 class="planet-name">{name}</h1>
            <div class="planet-hindi">{hindi_name}</div>
            <span class="deity-tag">Ruling Deity: {deity}</span>
            <span class="auspicious-day">🗓 Auspicious Day: {day}</span>
        </section>

        <!-- ── WHY THIS DEITY ─────────────────────────────── -->
        <div class="section-card why-deity-card">
            <div class="section-label">Why This Deity?</div>
            <h2>The Cosmic Connection</h2>
            <p>{why_deity}</p>
        </div>

        <!-- ── MANTRA SECTION ─────────────────────────────── -->
        <div class="section-label" style="font-size:.72rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--planet-color);margin-bottom:.75rem;display:flex;align-items:center;gap:.5rem;">
            The Sacred Mantra
            <span style="flex:1;height:1px;background:var(--border);display:block;"></span>
        </div>
        <div class="mantra-card" aria-label="Mantra texts">
            <div class="mantra-row">
                <div class="mantra-lang">Sanskrit</div>
                <div class="mantra-text-devanagari">{ms}</div>
            </div>
            <hr class="divider" />
            <div class="mantra-row">
                <div class="mantra-lang">Hindi</div>
                <div class="mantra-text-hindi">{mh}</div>
            </div>
            <hr class="divider" />
            <div class="mantra-row">
                <div class="mantra-lang">English Transliteration</div>
                <div class="mantra-text-english">{me}</div>
            </div>
        </div>

        <!-- ── RECOMMENDED BHAJANS ────────────────────────── -->
        <div class="section-card">
            <div class="section-label">Recommended Bhajans</div>
            <h2>Sacred Songs for {name}</h2>
            <ul class="bhajan-list">{bhajan_html}
            </ul>
        </div>

        <!-- ── WHEN TO CHANT ──────────────────────────────── -->
        <div class="section-card">
            <div class="section-label">Astrological Guidance</div>
            <h2><span class="timing-icon" aria-hidden="true">🕐</span>When to Chant</h2>
            <p>{when}</p>
        </div>

        <!-- ── MANDATORY CROSS-LINK CTA ───────────────────── -->
        <div class="cta-banner" role="complementary" aria-label="Free Kundali offer">
            <div class="cta-text">
                <div class="cta-eyebrow">Vedic Astrology · Free Report</div>
                <p class="cta-headline">
                    Is <em>{name}</em> weak in your birth chart?<br>
                    Calculate your <em>free Kundali</em> now at ournakshatra.com
                </p>
            </div>
            <a href="https://ournakshatra.com/janam-kundali"
               class="cta-btn"
               target="_blank"
               rel="noopener noreferrer">
                Get Free Kundali
                <span class="arrow" aria-hidden="true">→</span>
            </a>
        </div>

    </main>

    <!-- ── FOOTER ────────────────────────────────────────────── -->
    <footer class="site-footer">
        <nav class="footer-nav" aria-label="Footer links">
            <a href="https://bhajan.ournakshatra.com">Bhajan Home</a>
            <a href="https://bhajan.ournakshatra.com/planets/">All Planets</a>
            <a href="https://ournakshatra.com/janam-kundali">Free Kundali</a>
            <a href="https://ournakshatra.com">OurNakshatra</a>
        </nav>
        <hr class="footer-divider" />
        <p>
            &copy; 2025 <a href="https://ournakshatra.com">OurNakshatra.com</a> &mdash;
            All mantras are for spiritual and educational purposes.
        </p>
    </footer>

</body>
</html>
"""


# ─────────────────────────────────────────────────────────────────────────────
# MAIN — create files
# ─────────────────────────────────────────────────────────────────────────────

def main() -> None:
    base_dir = "planet"
    created = []

    for planet in PLANETS_DATA:
        pid        = planet["id"]
        output_dir = os.path.join(base_dir, pid)
        os.makedirs(output_dir, exist_ok=True)

        filepath  = os.path.join(output_dir, "index.html")
        html      = generate_html(planet)

        with open(filepath, "w", encoding="utf-8") as fh:
            fh.write(html)

        created.append(filepath)
        print(f"  ✓  {filepath}  [{planet['name']}]  color={planet['color']}")

    print(f"\n{'─'*50}")
    print(f"  Done! {len(created)} pages generated under ./{base_dir}/")
    print(f"{'─'*50}\n")


if __name__ == "__main__":
    main()
