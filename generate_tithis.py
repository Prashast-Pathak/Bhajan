#!/usr/bin/env python3
"""
generate_tithis.py
Generates 8 auspicious Tithi pages for bhajan.ournakshatra.com
"""

import os

TITHIS_DATA = [
    {"id": "ekadashi", "name": "Ekadashi", "hindi": "एकादशी", "deity": "Lord Vishnu", "description": "The 11th day of each lunar fortnight, considered the most auspicious Tithi for Lord Vishnu's worship.", "fasting": "Complete fast from grains. Only fruits, milk, and water permitted.", "mantra": "Vishnu Sahasranama", "cta": "Find today's Ekadashi time → ournakshatra.com/panchang", "color": "#A8832A"},
    {"id": "chaturthi", "name": "Chaturthi", "hindi": "चतुर्थी", "deity": "Lord Ganesha", "description": "The 4th day of each lunar fortnight dedicated to Lord Ganesha. Sankashti Chaturthi (Krishna Paksha) is especially powerful.", "fasting": "Fast until moonrise. Break fast after seeing the moon and offering modak.", "mantra": "Ganesha Pancharatnam", "cta": "Find the next Chaturthi date → ournakshatra.com/panchang", "color": "#D97706"},
    {"id": "pradosh", "name": "Pradosh Vrat", "hindi": "प्रदोष व्रत", "deity": "Lord Shiva", "description": "The 13th day (Trayodashi) of each lunar fortnight. The twilight period of this day is the most powerful time for Shiva worship.", "fasting": "Fast from sunrise. Break fast after Shiva puja at twilight.", "mantra": "Shiva Panchakshara Stotram — Om Namah Shivaya", "cta": "Find next Pradosh timing → ournakshatra.com/panchang", "color": "#1E40AF"},
    {"id": "purnima", "name": "Purnima (Full Moon)", "hindi": "पूर्णिमा", "deity": "Lord Vishnu / Chandra Dev", "description": "The full moon day is the peak of lunar energy. It is ideal for Satyanarayana Puja, charity, and meditation.", "fasting": "Optional fast. Charity and donation on this day multiply manifold.", "mantra": "Satyanarayana Katha and Vishnu Sahasranama", "cta": "See today's Purnima Tithi → ournakshatra.com/panchang", "color": "#EAB308"},
    {"id": "amavasya", "name": "Amavasya (No Moon)", "hindi": "अमावस्या", "deity": "Pitru Devatas (Ancestors)", "description": "The new moon day is sacred for ancestor worship (Pitru Tarpan). The veil between worlds is thinnest on this day.", "fasting": "Partial fast with one meal. Focus on prayer and Tarpan for ancestors.", "mantra": "Pitru Tarpan Mantra and Shiva prayers", "cta": "Find next Amavasya date → ournakshatra.com/panchang", "color": "#111827"},
    {"id": "navami", "name": "Navami", "hindi": "नवमी", "deity": "Goddess Durga / Lord Ram", "description": "The 9th lunar day. Ram Navami (Chaitra Shukla Navami) celebrates Lord Ram's birth. Durga Navami ends Navratri.", "fasting": "Full fast on Ram Navami and Durga Navami. Break with prasad after puja.", "mantra": "Shri Ram Chandra Kripalu and Durga Chalisa", "cta": "Find Ram Navami & Navratri timings → ournakshatra.com/panchang", "color": "#15803D"},
    {"id": "shivaratri", "name": "Maha Shivaratri", "hindi": "महाशिवरात्रि", "deity": "Lord Shiva", "description": "The great night of Shiva. The most powerful night of the year for Shiva worship, occurring on the 14th day of the Krishna Paksha of Phalguna month.", "fasting": "Full day and night fast. Puja is performed in 4 prahar (night watches).", "mantra": "Om Namah Shivaya — chanted 108, 1008, or 10008 times through the night", "cta": "Get Shivaratri puja muhurat → ournakshatra.com/panchang", "color": "#1E40AF"},
    {"id": "janmashtami", "name": "Janmashtami", "hindi": "जन्माष्टमी", "deity": "Lord Krishna", "description": "The birth celebration of Lord Krishna, occurring on the 8th day (Ashtami) of Krishna Paksha in Bhadrapada month.", "fasting": "Full day fast. Break fast only after midnight (Krishna's birth time).", "mantra": "Hare Krishna Maha Mantra and Achyutashtakam", "cta": "Get Janmashtami puja timing → ournakshatra.com/panchang", "color": "#7C3AED"}
]

DEITY_ICONS = {
    "Lord Vishnu":                  "🌸",
    "Lord Ganesha":                 "🐘",
    "Lord Shiva":                   "🔱",
    "Lord Vishnu / Chandra Dev":    "🌕",
    "Pitru Devatas (Ancestors)":    "🪔",
    "Goddess Durga / Lord Ram":     "🏹",
    "Lord Krishna":                 "🦚",
}

TITHI_NUMBERS = {
    "ekadashi":   "11th Tithi",
    "chaturthi":  "4th Tithi",
    "pradosh":    "13th Tithi",
    "purnima":    "15th Tithi",
    "amavasya":   "New Moon",
    "navami":     "9th Tithi",
    "shivaratri": "14th Tithi",
    "janmashtami":"8th Tithi",
}

FAST_TYPE = {
    "ekadashi":   ("Nirjala / Phalahar", "⭕ Strict"),
    "chaturthi":  ("Until Moonrise",     "🟡 Moderate"),
    "pradosh":    ("Sunrise to Twilight","🟡 Moderate"),
    "purnima":    ("Optional",           "🟢 Flexible"),
    "amavasya":   ("Partial — One Meal", "🟡 Moderate"),
    "navami":     ("Full Day",           "⭕ Strict"),
    "shivaratri": ("Full Day & Night",   "🔴 Most Intense"),
    "janmashtami":("Full Day to Midnight","⭕ Strict"),
}

def hex_to_rgba(hex_color, alpha=0.12):
    h = hex_color.lstrip('#')
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"

def generate_html(t):
    color     = t["color"]
    soft      = hex_to_rgba(color, 0.10)
    mid       = hex_to_rgba(color, 0.22)
    icon      = DEITY_ICONS.get(t["deity"], "✦")
    tnum      = TITHI_NUMBERS.get(t["id"], "")
    fast_label, fast_badge = FAST_TYPE.get(t["id"], ("", ""))

    # cta url: strip display text, keep actual link part
    panchang_url = "https://ournakshatra.com/panchang"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{t['name']} — Tithi Guide, Fasting & Mantra | bhajan.ournakshatra.com</title>
  <meta name="description" content="{t['name']}: deity {t['deity']}, fasting rules, primary mantra and spiritual significance of this sacred lunar day." />
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
      --accent-soft: {soft};
      --accent-mid: {mid};
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
      position: sticky; top: 0; z-index: 100;
      background: rgba(245,240,232,0.94);
      backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--border);
      padding: 0 28px; height: 62px;
      display: flex; align-items: center; justify-content: space-between;
    }}
    .logo {{
      font-weight: 900; font-size: 1rem;
      letter-spacing: .14em; text-transform: uppercase;
      color: var(--maroon); text-decoration: none;
    }}
    .logo em {{ font-style: normal; color: var(--accent); }}
    nav a {{
      font-size: 0.8rem; font-weight: 700; letter-spacing: .08em;
      text-transform: uppercase; color: var(--text-sec);
      text-decoration: none; padding: 6px 16px;
      border-radius: 20px; border: 1px solid var(--border);
      transition: all .2s;
    }}
    nav a:hover {{ background: var(--accent); color: #fff; border-color: var(--accent); }}

    /* ── MOON PHASE STRIP ── */
    .phase-strip {{
      background: var(--surface2);
      border-bottom: 1px solid var(--border);
      padding: 8px 28px;
      display: flex; align-items: center; gap: 16px;
      font-size: 0.72rem; font-weight: 700;
      letter-spacing: .12em; text-transform: uppercase;
      color: var(--text-muted); overflow-x: auto;
    }}
    .phase-item {{
      white-space: nowrap; padding: 4px 12px;
      border-radius: 14px; border: 1px solid var(--border);
      transition: all .2s; cursor: default;
    }}
    .phase-item.active {{
      background: var(--accent); color: #fff; border-color: var(--accent);
    }}

    /* ── HERO ── */
    .hero {{
      position: relative; overflow: hidden;
      padding: 68px 24px 54px; text-align: center;
      border-bottom: 4px solid var(--accent);
      background:
        radial-gradient(ellipse 80% 65% at 50% 0%, var(--accent-soft) 0%, transparent 70%),
        var(--bg);
    }}
    .hero::before {{
      content: '';
      position: absolute; inset: 0;
      background:
        radial-gradient(circle at 12% 85%, var(--accent-mid) 0%, transparent 38%),
        radial-gradient(circle at 88% 15%, var(--accent-mid) 0%, transparent 32%);
      pointer-events: none;
    }}
    .hero-icon {{
      font-size: 3.2rem; line-height: 1; margin-bottom: 14px;
      position: relative;
      filter: drop-shadow(0 2px 10px var(--accent-mid));
    }}
    .hero-tag {{
      display: inline-flex; align-items: center; gap: 8px;
      font-size: 0.67rem; font-weight: 700; letter-spacing: .22em;
      text-transform: uppercase; color: var(--accent);
      border: 1px solid var(--accent); border-radius: 20px;
      padding: 4px 14px; margin-bottom: 18px; position: relative;
    }}
    .hero-hindi {{
      font-family: var(--font-hindi);
      font-size: clamp(2.8rem, 9vw, 5.8rem);
      color: var(--accent); line-height: 1.05;
      position: relative; margin-bottom: 8px;
    }}
    .hero-name {{
      font-size: clamp(1rem, 3vw, 1.5rem);
      font-weight: 300; letter-spacing: .34em;
      text-transform: uppercase; color: var(--text-sec);
      position: relative; margin-bottom: 10px;
    }}
    .hero-deity {{
      font-size: 0.88rem; color: var(--text-muted); position: relative;
    }}
    .hero-deity strong {{ color: var(--accent); font-weight: 700; }}

    /* ── LAYOUT ── */
    .content-wrapper {{
      max-width: 740px; margin: 0 auto;
      padding: 44px 24px 80px;
      display: flex; flex-direction: column; gap: 32px;
    }}

    /* ── CARDS ── */
    .card {{
      background: var(--surface);
      border-radius: var(--radius);
      border: 1px solid var(--border);
      overflow: hidden;
      animation: fadeUp .45s ease both;
    }}
    @keyframes fadeUp {{
      from {{ opacity: 0; transform: translateY(14px); }}
      to   {{ opacity: 1; transform: translateY(0); }}
    }}
    .card-header {{
      display: flex; align-items: center; gap: 12px;
      padding: 16px 22px 13px;
      border-bottom: 1px solid var(--border);
      background: var(--surface2);
    }}
    .card-icon {{
      width: 34px; height: 34px; border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      font-size: 1rem; flex-shrink: 0;
      background: var(--accent-soft);
      border: 2px solid var(--accent);
    }}
    .card-title {{
      font-size: 0.67rem; font-weight: 900;
      letter-spacing: .2em; text-transform: uppercase;
      color: var(--accent);
    }}
    .card-body {{ padding: 20px 22px; }}

    /* ── DESCRIPTION ── */
    .desc-text {{
      font-size: 1rem; color: var(--text-sec); line-height: 1.85;
    }}

    /* ── FASTING CARD ── */
    .fast-grid {{
      display: grid; grid-template-columns: 1fr 1fr; gap: 14px;
    }}
    @media (max-width: 480px) {{ .fast-grid {{ grid-template-columns: 1fr; }} }}
    .fast-chip {{
      background: var(--surface2); border: 1px solid var(--border);
      border-radius: 10px; padding: 16px 18px;
    }}
    .fast-chip-label {{
      font-size: 0.62rem; font-weight: 700; letter-spacing: .16em;
      text-transform: uppercase; color: var(--text-muted); margin-bottom: 6px;
    }}
    .fast-chip-value {{
      font-size: 0.95rem; font-weight: 700; color: var(--text);
    }}
    .fast-rule {{
      margin-top: 16px; grid-column: 1 / -1;
      background: var(--accent-soft);
      border: 1px solid var(--accent);
      border-left: 4px solid var(--accent);
      border-radius: 0 10px 10px 0;
      padding: 14px 18px;
      font-size: 0.95rem; color: var(--text-sec); line-height: 1.7;
    }}

    /* ── MANTRA BOX ── */
    .mantra-highlight {{
      display: flex; align-items: center; gap: 20px;
      background: var(--surface2); border-radius: 10px;
      padding: 20px 22px; border: 1px solid var(--border);
    }}
    .mantra-icon-lg {{
      font-size: 2.6rem; flex-shrink: 0; line-height: 1;
    }}
    .mantra-label {{
      font-size: 0.62rem; font-weight: 700; letter-spacing: .18em;
      text-transform: uppercase; color: var(--text-muted); margin-bottom: 5px;
    }}
    .mantra-name {{
      font-size: 1.2rem; font-weight: 900; color: var(--accent);
      line-height: 1.3;
    }}
    .mantra-sub {{
      font-size: 0.82rem; color: var(--text-muted); margin-top: 4px;
    }}

    /* ── CTA BANNER ── */
    .cta-banner {{
      background: linear-gradient(135deg, var(--maroon) 0%, {color} 100%);
      border-radius: var(--radius);
      padding: 40px 32px; text-align: center;
      position: relative; overflow: hidden;
    }}
    .cta-banner::before {{
      content: '🌙';
      position: absolute; font-size: 8rem;
      opacity: 0.07;
      top: -20px; right: 0; line-height: 1;
      pointer-events: none;
    }}
    .cta-eyebrow {{
      font-size: 0.65rem; font-weight: 700; letter-spacing: .24em;
      text-transform: uppercase; color: rgba(255,255,255,.55);
      margin-bottom: 12px;
    }}
    .cta-headline {{
      font-size: clamp(1.1rem, 3vw, 1.55rem);
      font-weight: 900; color: #fff; line-height: 1.3;
      margin-bottom: 24px;
    }}
    .cta-headline em {{
      font-style: normal;
      border-bottom: 2px solid rgba(255,255,255,.4);
    }}
    .cta-btn {{
      display: inline-block; background: #fff; color: var(--maroon);
      font-weight: 900; font-size: 0.85rem; letter-spacing: .1em;
      text-transform: uppercase; text-decoration: none;
      padding: 14px 32px; border-radius: 30px;
      transition: transform .2s, box-shadow .2s;
    }}
    .cta-btn:hover {{ transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,0,0,.28); }}

    /* ── FOOTER ── */
    footer {{
      text-align: center; padding: 26px 24px;
      font-size: 0.76rem; color: var(--text-muted);
      border-top: 1px solid var(--border);
    }}
    footer a {{ color: var(--saffron); text-decoration: none; font-weight: 600; }}

    @media (max-width: 480px) {{
      .hero {{ padding: 50px 16px 40px; }}
      .card-body, .card-header {{ padding-left: 14px; padding-right: 14px; }}
      .cta-banner {{ padding: 28px 18px; }}
      .mantra-highlight {{ flex-direction: column; gap: 12px; }}
    }}
  </style>
</head>
<body>

<header>
  <a href="https://bhajan.ournakshatra.com" class="logo">NAKSHATRA <em>✦</em> BHAJAN</a>
  <nav><a href="{panchang_url}" target="_blank">Panchang</a></nav>
</header>

<div class="phase-strip">
  <span>Lunar Tithis:</span>
  <span class="phase-item">Pratipada</span>
  <span class="phase-item">Chaturthi</span>
  <span class="phase-item">Ekadashi</span>
  <span class="phase-item">Trayodashi</span>
  <span class="phase-item">Chaturdashi</span>
  <span class="phase-item">Purnima</span>
  <span class="phase-item">Amavasya</span>
  <span class="phase-item active">{t['name'].split('(')[0].strip()}</span>
</div>

<div class="hero">
  <div class="hero-icon">{icon}</div>
  <div class="hero-tag">☽ {tnum} · Sacred Tithi</div>
  <div class="hero-hindi">{t['hindi']}</div>
  <div class="hero-name">{t['name']}</div>
  <div class="hero-deity">Presiding Deity: <strong>{t['deity']}</strong></div>
</div>

<main class="content-wrapper">

  <!-- Description -->
  <div class="card" style="animation-delay:.05s">
    <div class="card-header">
      <div class="card-icon">📖</div>
      <div class="card-title">About {t['name']}</div>
    </div>
    <div class="card-body">
      <p class="desc-text">{t['description']}</p>
    </div>
  </div>

  <!-- Fasting -->
  <div class="card" style="animation-delay:.10s">
    <div class="card-header">
      <div class="card-icon">🌿</div>
      <div class="card-title">Fasting Guidance (Upvas Vidhi)</div>
    </div>
    <div class="card-body">
      <div class="fast-grid">
        <div class="fast-chip">
          <div class="fast-chip-label">Fast Type</div>
          <div class="fast-chip-value">{fast_label}</div>
        </div>
        <div class="fast-chip">
          <div class="fast-chip-label">Intensity</div>
          <div class="fast-chip-value">{fast_badge}</div>
        </div>
        <div class="fast-rule">{t['fasting']}</div>
      </div>
    </div>
  </div>

  <!-- Mantra -->
  <div class="card" style="animation-delay:.15s">
    <div class="card-header">
      <div class="card-icon">🎵</div>
      <div class="card-title">Primary Mantra / Stotram</div>
    </div>
    <div class="card-body">
      <div class="mantra-highlight">
        <div class="mantra-icon-lg">{icon}</div>
        <div>
          <div class="mantra-label">Recite on this Tithi</div>
          <div class="mantra-name">{t['mantra']}</div>
          <div class="mantra-sub">Offered with devotion to {t['deity']}</div>
        </div>
      </div>
    </div>
  </div>

  <!-- CTA Banner -->
  <div class="cta-banner" style="animation-delay:.20s">
    <div class="cta-eyebrow">✦ Live Panchang ✦</div>
    <div class="cta-headline">
      <em>{t['cta'].split('→')[0].strip()}</em>
    </div>
    <a class="cta-btn" href="{panchang_url}" target="_blank" rel="noopener">
      View Panchang → ournakshatra.com
    </a>
  </div>

</main>

<footer>
  <p>© 2024 <a href="https://bhajan.ournakshatra.com">bhajan.ournakshatra.com</a> — Sacred Tithi Guide &amp; Lunar Devotion</p>
</footer>

</body>
</html>
"""

def main():
    created = 0
    for t in TITHIS_DATA:
        dir_path = os.path.join("tithi", t["id"])
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, "index.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(generate_html(t))
        created += 1
        print(f"  ✓  {file_path}")
    print(f"\n✅  Done — {created}/8 Tithi pages generated in tithi/")

if __name__ == "__main__":
    main()
