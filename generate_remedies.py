#!/usr/bin/env python3
"""
generate_remedies.py
Generates 5 Dosha Remedy hub pages for bhajan.ournakshatra.com
"""

import os

REMEDIES_DATA = [
    {"id": "mangal-dosha", "name": "Mangal Dosha", "hindi": "मंगल दोष", "deity": "Lord Hanuman", "primary_mantra": "Hanuman Chalisa", "explanation": "Mangal Dosha occurs when Mars occupies the 1st, 2nd, 4th, 7th, 8th, or 12th house in the birth chart. It is one of the most commonly checked placements before marriage.", "remedies": ["Chant Hanuman Chalisa every Tuesday", "Offer red flowers to Lord Hanuman", "Fast on Tuesdays", "Wear a red coral (Moonga) gemstone after consulting an astrologer"], "cta_text": "Check if you have Mangal Dosha in your Kundali", "cta_link": "https://ournakshatra.com/janam-kundali", "color": "#DC2626"},
    {"id": "kaal-sarp-dosha", "name": "Kaal Sarp Dosha", "hindi": "काल सर्प दोष", "deity": "Lord Shiva", "primary_mantra": "Maha Mrityunjaya Mantra", "explanation": "Kaal Sarp Dosha forms when all planets are hemmed between Rahu and Ketu. It can cause delays in marriage, career struggles, and recurring obstacles.", "remedies": ["Chant the Maha Mrityunjaya Mantra 108 times daily", "Perform Abhishek of Shivalinga on Mondays", "Visit Trimbakeshwar Jyotirlinga for Kaal Sarp Shanti Puja", "Donate black sesame seeds on Saturdays"], "cta_text": "Discover if Kaal Sarp Dosha is active in your chart", "cta_link": "https://ournakshatra.com/yogas", "color": "#111827"},
    {"id": "sade-sati", "name": "Shani Sade Sati", "hindi": "शनि साढ़े साती", "deity": "Shani Dev / Lord Shiva", "primary_mantra": "Shani Chalisa", "explanation": "Sade Sati is a 7.5-year period when Saturn transits through three consecutive signs including your Moon sign. It is a time of karmic reckoning, hard work, and deep transformation.", "remedies": ["Chant Shani Chalisa every Saturday", "Light sesame oil lamp before Shani Dev on Saturdays", "Feed crows black sesame and mustard oil on Saturdays", "Donate black clothing, iron items, or mustard oil to the poor"], "cta_text": "Check your current Sade Sati status live", "cta_link": "https://ournakshatra.com/transits", "color": "#374151"},
    {"id": "pitru-dosha", "name": "Pitru Dosha", "hindi": "पितृ दोष", "deity": "Pitru Devatas (Ancestors)", "primary_mantra": "Pitru Tarpan", "explanation": "Pitru Dosha occurs due to unfulfilled desires or wrongdoings of ancestors. It manifests as repeated family issues, childlessness, or financial stagnation.", "remedies": ["Perform Tarpan on Amavasya (no-moon day)", "Offer water with black sesame seeds to ancestors daily", "Feed Brahmins or the poor on Amavasya", "Perform Shraadh rituals during Pitru Paksha"], "cta_text": "Check if Pitru Dosha exists in your Kundali", "cta_link": "https://ournakshatra.com/janam-kundali", "color": "#78350F"},
    {"id": "guru-chandal", "name": "Guru Chandal Dosha", "hindi": "गुरु चांडाल दोष", "deity": "Lord Vishnu", "primary_mantra": "Vishnu Sahasranama", "explanation": "Guru Chandal Dosha forms when Jupiter is conjunct or aspected by Rahu. It corrupts one's wisdom, ethics, and can lead a person toward false teachers or immoral paths.", "remedies": ["Chant Vishnu Sahasranama every Thursday", "Donate yellow items like turmeric and yellow cloth", "Wear a yellow sapphire (Pukhraj) after consulting an astrologer", "Fast on Thursdays and offer prayers to Lord Vishnu"], "cta_text": "Check your Jupiter placement and active Yogas", "cta_link": "https://ournakshatra.com/yogas", "color": "#A8832A"}
]

DEITY_ICONS = {
    "Lord Hanuman":           "🐒",
    "Lord Shiva":             "🔱",
    "Shani Dev / Lord Shiva": "⚖️",
    "Pitru Devatas (Ancestors)": "🪔",
    "Lord Vishnu":            "🌸",
}

SEVERITY_MAP = {
    "mangal-dosha":   ("Moderate to High", "Mangal Dosha is most significant when found in the 7th or 8th house. Its effects are strongest before age 28 and can be considerably reduced through consistent remedies and a compatible partner."),
    "kaal-sarp-dosha":("High",             "Kaal Sarp Dosha is considered one of the most impactful planetary afflictions. Its severity depends on the specific type (Anant, Kulik, etc.) and the strength of Rahu and Ketu in the chart. Professional guidance is strongly advised."),
    "sade-sati":      ("Moderate",         "Sade Sati is a natural karmic cycle experienced by everyone roughly three times in a lifetime. While it brings hardship, sincere spiritual practice dramatically softens its intensity. It is not a curse — it is a teacher."),
    "pitru-dosha":    ("Moderate to High", "Pitru Dosha can span generations if unaddressed. The good news is that sincere Shraadh rituals and ancestor veneration can resolve it relatively quickly. Perform these rites with pure intention during Pitru Paksha each year."),
    "guru-chandal":   ("Moderate",         "Guru Chandal Dosha's severity depends heavily on Jupiter's overall strength in the chart. If Jupiter is exalted or in its own sign, the Rahu influence is weaker. A learned Jyotishi should assess the full chart before concluding its strength."),
}

def hex_to_rgba(hex_color, alpha=0.12):
    h = hex_color.lstrip('#')
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"

def generate_html(d):
    color      = d["color"]
    soft       = hex_to_rgba(color, 0.10)
    mid        = hex_to_rgba(color, 0.22)
    icon       = DEITY_ICONS.get(d["deity"], "✦")
    sev_level, sev_text = SEVERITY_MAP[d["id"]]

    # severity badge colour
    if "High" in sev_level and "Moderate" not in sev_level:
        sev_color = "#DC2626"
    elif "Moderate to High" in sev_level:
        sev_color = "#EA580C"
    else:
        sev_color = "#D97706"

    remedy_steps = ""
    for i, step in enumerate(d["remedies"], 1):
        remedy_steps += f"""
        <div class="step">
          <div class="step-num" style="background:{color};color:#fff;">{i}</div>
          <div class="step-text">{step}</div>
        </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{d['name']} Remedy — Bhajan & Mantra | bhajan.ournakshatra.com</title>
  <meta name="description" content="Learn about {d['name']}, its effects, primary mantra, and step-by-step remedial actions. Deity: {d['deity']}." />
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
        radial-gradient(circle at 12% 88%, var(--accent-mid) 0%, transparent 38%),
        radial-gradient(circle at 88% 12%, var(--accent-mid) 0%, transparent 32%);
      pointer-events: none;
    }}
    .hero-tag {{
      display: inline-flex; align-items: center; gap: 8px;
      font-size: 0.67rem; font-weight: 700; letter-spacing: .22em;
      text-transform: uppercase; color: var(--accent);
      border: 1px solid var(--accent); border-radius: 20px;
      padding: 4px 14px; margin-bottom: 20px; position: relative;
    }}
    .hero-hindi {{
      font-family: var(--font-hindi);
      font-size: clamp(2.8rem, 9vw, 5.8rem);
      color: var(--accent); line-height: 1.05;
      position: relative; margin-bottom: 8px;
    }}
    .hero-name {{
      font-size: clamp(1.1rem, 3vw, 1.55rem);
      font-weight: 300; letter-spacing: .32em;
      text-transform: uppercase; color: var(--text-sec);
      position: relative; margin-bottom: 14px;
    }}
    .hero-deity {{
      display: inline-flex; align-items: center; gap: 8px;
      font-size: 0.88rem; color: var(--text-muted);
      position: relative;
    }}
    .hero-deity strong {{ color: var(--accent); font-weight: 700; }}

    /* ── CONTENT ── */
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

    /* ── EXPLANATION ── */
    .explanation-text {{
      font-size: 1rem; color: var(--text-sec); line-height: 1.85;
    }}

    /* ── MANTRA BOX ── */
    .mantra-box {{
      display: flex; align-items: center; gap: 20px;
      background: var(--surface2);
      border-radius: 10px; padding: 20px 22px;
      border: 1px solid var(--border);
    }}
    .mantra-icon {{
      font-size: 2.4rem; flex-shrink: 0; line-height: 1;
    }}
    .mantra-label {{
      font-size: 0.64rem; font-weight: 700; letter-spacing: .18em;
      text-transform: uppercase; color: var(--text-muted); margin-bottom: 5px;
    }}
    .mantra-name {{
      font-size: 1.25rem; font-weight: 900; color: var(--accent);
    }}
    .mantra-sub {{
      font-size: 0.82rem; color: var(--text-muted); margin-top: 3px;
    }}

    /* ── REMEDY STEPS ── */
    .step {{
      display: flex; align-items: flex-start; gap: 16px;
      padding: 15px 0;
      border-bottom: 1px solid var(--border);
    }}
    .step:last-child {{ border-bottom: none; padding-bottom: 0; }}
    .step-num {{
      width: 32px; height: 32px; border-radius: 50%;
      display: flex; align-items: center; justify-content: center;
      font-size: 0.78rem; font-weight: 900; flex-shrink: 0; margin-top: 1px;
    }}
    .step-text {{
      font-size: 0.97rem; color: var(--text-sec);
      line-height: 1.7; padding-top: 4px;
    }}

    /* ── WARNING BOX ── */
    .warning-box {{
      background: #FEF3C7;
      border: 1px solid #F59E0B;
      border-left: 5px solid var(--saffron);
      border-radius: var(--radius);
      padding: 22px 24px;
      animation: fadeUp .45s ease both;
    }}
    .warning-header {{
      display: flex; align-items: center; gap: 10px; margin-bottom: 12px;
    }}
    .warning-badge {{
      font-size: 0.65rem; font-weight: 900; letter-spacing: .18em;
      text-transform: uppercase; background: var(--saffron); color: #fff;
      border-radius: 20px; padding: 3px 12px;
    }}
    .severity-level {{
      font-size: 0.78rem; font-weight: 700;
      color: {sev_color};
      background: rgba({','.join(str(int(sev_color.lstrip('#')[i:i+2], 16)) for i in (0,2,4))}, 0.1);
      border: 1px solid {sev_color};
      border-radius: 20px; padding: 2px 10px;
    }}
    .warning-title {{
      font-size: 0.88rem; font-weight: 900;
      color: #92400E; margin-bottom: 8px;
    }}
    .warning-text {{
      font-size: 0.93rem; color: #78350F; line-height: 1.75;
    }}

    /* ── CTA BANNER ── */
    .cta-banner {{
      background: linear-gradient(135deg, var(--maroon) 0%, {color} 100%);
      border-radius: var(--radius);
      padding: 40px 32px; text-align: center;
      position: relative; overflow: hidden;
    }}
    .cta-banner::before {{
      content: '⚕';
      position: absolute; font-size: 10rem;
      color: rgba(255,255,255,0.04);
      top: -30px; right: -10px; line-height: 1;
      pointer-events: none;
    }}
    .cta-eyebrow {{
      font-size: 0.65rem; font-weight: 700; letter-spacing: .24em;
      text-transform: uppercase; color: rgba(255,255,255,.55);
      margin-bottom: 12px;
    }}
    .cta-headline {{
      font-size: clamp(1.1rem, 3vw, 1.6rem);
      font-weight: 900; color: #fff; line-height: 1.25;
      margin-bottom: 24px;
    }}
    .cta-headline em {{
      font-style: normal;
      border-bottom: 2px solid rgba(255,255,255,.45);
    }}
    .cta-btn {{
      display: inline-block; background: #fff; color: var(--maroon);
      font-weight: 900; font-size: 0.85rem; letter-spacing: .1em;
      text-transform: uppercase; text-decoration: none;
      padding: 14px 32px; border-radius: 30px;
      transition: transform .2s, box-shadow .2s;
    }}
    .cta-btn:hover {{ transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,0,0,.28); }}
    .cta-sub {{
      margin-top: 14px;
      font-size: 0.76rem; color: rgba(255,255,255,.5);
    }}
    .cta-sub a {{
      color: rgba(255,255,255,.75); text-decoration: underline;
    }}

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
      .mantra-box {{ flex-direction: column; gap: 12px; }}
    }}
  </style>
</head>
<body>

<header>
  <a href="https://bhajan.ournakshatra.com" class="logo">NAKSHATRA <em>✦</em> BHAJAN</a>
  <nav><a href="https://ournakshatra.com/yogas" target="_blank">View Yogas</a></nav>
</header>

<div class="hero">
  <div class="hero-tag">⚠ Dosha Remedy Guide</div>
  <div class="hero-hindi">{d['hindi']}</div>
  <div class="hero-name">{d['name']}</div>
  <div class="hero-deity">{icon} Presiding Deity: <strong>{d['deity']}</strong></div>
</div>

<main class="content-wrapper">

  <!-- Explanation -->
  <div class="card" style="animation-delay:.05s">
    <div class="card-header">
      <div class="card-icon">📖</div>
      <div class="card-title">What is {d['name']}?</div>
    </div>
    <div class="card-body">
      <p class="explanation-text">{d['explanation']}</p>
    </div>
  </div>

  <!-- Primary Mantra -->
  <div class="card" style="animation-delay:.10s">
    <div class="card-header">
      <div class="card-icon">🎵</div>
      <div class="card-title">Primary Mantra / Bhajan for Remedy</div>
    </div>
    <div class="card-body">
      <div class="mantra-box">
        <div class="mantra-icon">{icon}</div>
        <div>
          <div class="mantra-label">Recommended Daily Practice</div>
          <div class="mantra-name">{d['primary_mantra']}</div>
          <div class="mantra-sub">Dedicated to {d['deity']} · Recite with sincere devotion</div>
        </div>
      </div>
    </div>
  </div>

  <!-- Remedial Steps -->
  <div class="card" style="animation-delay:.15s">
    <div class="card-header">
      <div class="card-icon">🪴</div>
      <div class="card-title">Step-by-Step Remedial Actions</div>
    </div>
    <div class="card-body">
      {remedy_steps}
    </div>
  </div>

  <!-- Severity Warning -->
  <div class="warning-box" style="animation-delay:.20s">
    <div class="warning-header">
      <div class="warning-badge">⚠ Severity Notice</div>
      <div class="severity-level">Severity: {sev_level}</div>
    </div>
    <div class="warning-title">Important Guidance for {d['name']}</div>
    <p class="warning-text">{sev_text}</p>
  </div>

  <!-- CTA Banner -->
  <div class="cta-banner" style="animation-delay:.25s">
    <div class="cta-eyebrow">✦ Know Your Chart ✦</div>
    <div class="cta-headline">
      <em>{d['cta_text']}</em>
    </div>
    <a class="cta-btn" href="{d['cta_link']}" target="_blank" rel="noopener">
      Check at ournakshatra.com →
    </a>
    <div class="cta-sub">
      Also explore all planetary Yogas at <a href="https://ournakshatra.com/yogas" target="_blank">ournakshatra.com/yogas</a>
    </div>
  </div>

</main>

<footer>
  <p>© 2024 <a href="https://bhajan.ournakshatra.com">bhajan.ournakshatra.com</a> — Dosha Remedies &amp; Bhakti for Every Soul</p>
</footer>

</body>
</html>
"""

def main():
    created = 0
    for d in REMEDIES_DATA:
        dir_path = os.path.join("remedy", d["id"])
        os.makedirs(dir_path, exist_ok=True)
        file_path = os.path.join(dir_path, "index.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(generate_html(d))
        created += 1
        print(f"  ✓  {file_path}")
    print(f"\n✅  Done — {created}/5 Dosha Remedy pages generated in remedy/")

if __name__ == "__main__":
    main()
