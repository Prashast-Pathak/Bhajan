#!/usr/bin/env python3
"""
Injects 'Jyotish' navigation dropdown into ALL root HTML pages
covering: planet, nakshatra, rashi, remedy, tithi, muhurat
Also updates mobile drawer menu on index.html.
"""
from pathlib import Path
import re

ROOT = Path('/Users/prashastpathak/Bhajan')

# ── The new dropdown nav CSS (inject once per file) ───────────
DROPDOWN_CSS = """
    /* ── Jyotish Dropdown Nav ─── */
    .nav-dropdown { position: relative; }
    .nav-dropdown > a { display: flex; align-items: center; gap: 4px; cursor: pointer; }
    .nav-dropdown > a::after { content: '▾'; font-size: .65rem; opacity: .7; }
    .dropdown-menu {
      display: none;
      position: absolute;
      top: calc(100% + 8px);
      left: 50%;
      transform: translateX(-50%);
      background: var(--surface, #EDE6D8);
      border: 1px solid var(--border, #D9CDBA);
      border-radius: 10px;
      padding: 10px 0;
      min-width: 520px;
      box-shadow: 0 8px 32px rgba(0,0,0,.16);
      z-index: 999;
      display: none;
    }
    .nav-dropdown:hover .dropdown-menu,
    .nav-dropdown:focus-within .dropdown-menu { display: block; }
    .dropdown-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 0;
    }
    .dropdown-col { padding: 8px 0; }
    .dropdown-col-title {
      font-size: .62rem;
      font-weight: 900;
      letter-spacing: .16em;
      text-transform: uppercase;
      color: var(--saffron, #C96A1F);
      padding: 4px 18px 8px;
      border-bottom: 1px solid var(--border, #D9CDBA);
      margin-bottom: 4px;
    }
    .dropdown-menu a {
      display: block;
      font-size: .78rem;
      font-weight: 600;
      color: var(--text-sec, #5C3D20);
      padding: 5px 18px;
      text-decoration: none;
      border-radius: 0;
      transition: background .15s, color .15s;
    }
    .dropdown-menu a:hover {
      background: var(--surface2, #E6DDD0);
      color: var(--saffron, #C96A1F);
    }
    @media(max-width:600px) { .nav-dropdown { display: none; } }
"""

# ── The dropdown HTML to inject after existing nav links ──────
DROPDOWN_HTML = """      <div class="nav-dropdown">
        <a href="#" onclick="return false;" role="button" aria-haspopup="true">🔭 Jyotish</a>
        <div class="dropdown-menu" role="menu">
          <div class="dropdown-grid">
            <div class="dropdown-col">
              <div class="dropdown-col-title">🪐 Navagraha</div>
              <a href="/planet/surya/">☀ Surya (Sun)</a>
              <a href="/planet/chandra/">☽ Chandra (Moon)</a>
              <a href="/planet/mangal/">♂ Mangal (Mars)</a>
              <a href="/planet/budha/">☿ Budha (Mercury)</a>
              <a href="/planet/guru/">♃ Guru (Jupiter)</a>
              <a href="/planet/shukra/">♀ Shukra (Venus)</a>
              <a href="/planet/shani/">♄ Shani (Saturn)</a>
              <a href="/planet/rahu/">☊ Rahu</a>
              <a href="/planet/ketu/">☋ Ketu</a>
            </div>
            <div class="dropdown-col">
              <div class="dropdown-col-title">⭐ Nakshatras</div>
              <a href="/nakshatra/ashwini/">Ashwini</a>
              <a href="/nakshatra/bharani/">Bharani</a>
              <a href="/nakshatra/krittika/">Krittika</a>
              <a href="/nakshatra/rohini/">Rohini</a>
              <a href="/nakshatra/mrigashira/">Mrigashira</a>
              <a href="/nakshatra/ardra/">Ardra</a>
              <a href="/nakshatra/punarvasu/">Punarvasu</a>
              <a href="/nakshatra/pushya/">Pushya</a>
              <a href="/nakshatra/ashlesha/">Ashlesha</a>
              <a href="/nakshatra/magha/">Magha</a>
              <a href="/nakshatra/purva-phalguni/">Purva Phalguni</a>
              <a href="/nakshatra/uttara-phalguni/">Uttara Phalguni</a>
              <a href="/nakshatra/hasta/">Hasta</a>
              <a href="/nakshatra/chitra/">Chitra</a>
              <a href="/nakshatra/swati/">Swati</a>
              <a href="/nakshatra/vishakha/">Vishakha</a>
              <a href="/nakshatra/anuradha/">Anuradha</a>
              <a href="/nakshatra/jyeshtha/">Jyeshtha</a>
              <a href="/nakshatra/mula/">Mula</a>
              <a href="/nakshatra/purva-ashadha/">Purva Ashadha</a>
              <a href="/nakshatra/uttara-ashadha/">Uttara Ashadha</a>
              <a href="/nakshatra/shravana/">Shravana</a>
              <a href="/nakshatra/dhanishtha/">Dhanishtha</a>
              <a href="/nakshatra/shatabhisha/">Shatabhisha</a>
              <a href="/nakshatra/purva-bhadrapada/">Purva Bhadrapada</a>
              <a href="/nakshatra/uttara-bhadrapada/">Uttara Bhadrapada</a>
              <a href="/nakshatra/revati/">Revati</a>
            </div>
            <div class="dropdown-col">
              <div class="dropdown-col-title">♈ Rashis</div>
              <a href="/rashi/mesh/">Mesh (Aries)</a>
              <a href="/rashi/vrishabha/">Vrishabha (Taurus)</a>
              <a href="/rashi/mithuna/">Mithuna (Gemini)</a>
              <a href="/rashi/karka/">Karka (Cancer)</a>
              <a href="/rashi/simha/">Simha (Leo)</a>
              <a href="/rashi/kanya/">Kanya (Virgo)</a>
              <a href="/rashi/tula/">Tula (Libra)</a>
              <a href="/rashi/vrischika/">Vrischika (Scorpio)</a>
              <a href="/rashi/dhanu/">Dhanu (Sagittarius)</a>
              <a href="/rashi/makara/">Makara (Capricorn)</a>
              <a href="/rashi/kumbha/">Kumbha (Aquarius)</a>
              <a href="/rashi/meena/">Meena (Pisces)</a>
              <div class="dropdown-col-title" style="margin-top:10px;">🛡️ Remedies</div>
              <a href="/remedy/mangal-dosha/">Mangal Dosha</a>
              <a href="/remedy/kaal-sarp-dosha/">Kaal Sarp Dosha</a>
              <a href="/remedy/sade-sati/">Sade Sati</a>
              <a href="/remedy/pitru-dosha/">Pitru Dosha</a>
              <a href="/remedy/guru-chandal/">Guru Chandal</a>
              <div class="dropdown-col-title" style="margin-top:10px;">🌙 Tithi & Muhurat</div>
              <a href="/tithi/ekadashi/">Ekadashi</a>
              <a href="/tithi/purnima/">Purnima</a>
              <a href="/tithi/amavasya/">Amavasya</a>
              <a href="/muhurat/vivah/">Vivah Muhurat</a>
              <a href="/muhurat/griha-pravesh/">Griha Pravesh</a>
            </div>
          </div>
        </div>
      </div>"""

# ── Mobile drawer section ─────────────────────────────────────
MOBILE_JYOTISH = """    <div class="menu-divider"></div>
    <div style="padding:8px 20px 4px;font-size:.65rem;font-weight:900;letter-spacing:.16em;text-transform:uppercase;color:var(--saffron);">🔭 JYOTISH HUBS</div>
    <a href="/planet/surya/">🪐 Navagraha Mantras</a>
    <a href="/nakshatra/ashwini/">⭐ 27 Nakshatra Pages</a>
    <a href="/rashi/mesh/">♈ 12 Rashi Pages</a>
    <a href="/remedy/mangal-dosha/">🛡️ Dosha Remedies</a>
    <a href="/tithi/ekadashi/">🌙 Sacred Tithis</a>
    <a href="/muhurat/vivah/">🔔 Auspicious Muhurats</a>"""

# ── ROOT PAGES to update ──────────────────────────────────────
ROOT_PAGES = list(ROOT.glob('*.html'))
updated = 0

for page in ROOT_PAGES:
    content = page.read_text(encoding='utf-8')
    original = content
    changed = False

    # ── 1. Inject dropdown CSS ────────────────────────────────
    if 'nav-dropdown' not in content and '</style>' in content:
        # Inject before last </style>
        content = content.replace('</style>', f'{DROPDOWN_CSS}\n  </style>', 1)
        changed = True

    # ── 2. Inject dropdown into desktop nav ───────────────────
    if 'nav-dropdown' not in content or 'dropdown-menu' not in content:
        # Find the closing </nav> of the desktop nav and insert before it
        if 'desktop-nav' in content:
            content = content.replace(
                '</nav>',
                f'{DROPDOWN_HTML}\n    </nav>',
                1  # Only first nav
            )
            changed = True

    # ── 3. Update mobile menu drawer ─────────────────────────
    if page.name == 'index.html' and 'JYOTISH HUBS' not in content:
        # Insert jyotish section before the last </div> of mobile-menu-links
        content = content.replace(
            '    <div class="menu-divider"></div>\n    <a href="favorites.html">',
            f'{MOBILE_JYOTISH}\n    <div class="menu-divider"></div>\n    <a href="favorites.html">'
        )
        changed = True

    if changed:
        page.write_text(content, encoding='utf-8')
        updated += 1
        print(f"  ✓ Updated: {page.name}")

print(f"\n✅ Done — Jyotish nav injected into {updated} root pages!")
print("   Next: git add -A && git commit && git push")
