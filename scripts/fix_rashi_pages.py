"""Phase 3: Add Rashi lord planet → planet stotra link + free Kundali CTA to all 12 Rashi pages."""
import re
from pathlib import Path

ROOT = Path('/Users/prashastpathak/Bhajan')

RASHI_MAP = {
    'mesh':      {'name': 'Mesh (Aries)',       'lord': 'Mangal', 'planet_slug': 'mangal',  'color': '#DC2626', 'emoji': '♈'},
    'vrishabha': {'name': 'Vrishabha (Taurus)',  'lord': 'Shukra', 'planet_slug': 'shukra',  'color': '#16A34A', 'emoji': '♉'},
    'mithuna':   {'name': 'Mithuna (Gemini)',    'lord': 'Budha',  'planet_slug': 'budha',   'color': '#16A34A', 'emoji': '♊'},
    'karka':     {'name': 'Karka (Cancer)',      'lord': 'Chandra','planet_slug': 'chandra', 'color': '#64748B', 'emoji': '♋'},
    'simha':     {'name': 'Simha (Leo)',         'lord': 'Surya',  'planet_slug': 'surya',   'color': '#D97706', 'emoji': '♌'},
    'kanya':     {'name': 'Kanya (Virgo)',       'lord': 'Budha',  'planet_slug': 'budha',   'color': '#16A34A', 'emoji': '♍'},
    'tula':      {'name': 'Tula (Libra)',        'lord': 'Shukra', 'planet_slug': 'shukra',  'color': '#EC4899', 'emoji': '♎'},
    'vrischika': {'name': 'Vrischika (Scorpio)', 'lord': 'Mangal', 'planet_slug': 'mangal',  'color': '#DC2626', 'emoji': '♏'},
    'dhanu':     {'name': 'Dhanu (Sagittarius)', 'lord': 'Guru',   'planet_slug': 'guru',    'color': '#EAB308', 'emoji': '♐'},
    'makara':    {'name': 'Makara (Capricorn)',  'lord': 'Shani',  'planet_slug': 'shani',   'color': '#1E3A5F', 'emoji': '♑'},
    'kumbha':    {'name': 'Kumbha (Aquarius)',   'lord': 'Shani',  'planet_slug': 'shani',   'color': '#1E3A5F', 'emoji': '♒'},
    'meena':     {'name': 'Meena (Pisces)',      'lord': 'Guru',   'planet_slug': 'guru',    'color': '#EAB308', 'emoji': '♓'},
}

for slug, info in RASHI_MAP.items():
    fp = ROOT / 'rashi' / slug / 'index.html'
    if not fp.exists():
        print(f"Skip {slug}: file not found")
        continue

    content = fp.read_text()

    if 'Rashi Lord Stotra' in content:
        print(f"Already done: {slug}")
        continue

    block = f"""
<!-- ── Rashi Lord Stotra Link ─────────────────────────────── -->
<div class="card" style="animation-delay:.25s; border-left:4px solid {info['color']};">
<div class="card-header">
<div class="card-icon" style="background:{info['color']}; color:#fff;">{info['emoji']}</div>
<div class="card-title">Rashi Lord Stotra — {info['lord']} Mantra</div>
</div>
<div class="card-body">
<p style="margin-bottom:12px; line-height:1.7;">
{info['name']} is ruled by <strong>{info['lord']}</strong>. Chanting the {info['lord']} mantra strengthens your Rashi lord and brings balance to your chart.
</p>
<a href="/planet/{info['planet_slug']}/" style="display:inline-flex; align-items:center; gap:6px; padding:8px 18px; background:{info['color']}; color:#fff; border-radius:50px; font-size:13px; font-weight:700; text-decoration:none;">
🪔 Chant {info['lord']} Stotra →
</a>
</div>
</div>
<!-- ── Free Kundali CTA ─────────────────────────────── -->
<a class="p2-kundali" href="https://ournakshatra.com/janam_landing.html" rel="noopener" target="_blank" style="display:flex; align-items:center; justify-content:space-between; padding:16px 20px; background:linear-gradient(135deg, rgba(201,106,31,0.08), rgba(168,131,42,0.08)); border:1px solid rgba(201,168,76,0.3); border-radius:12px; text-decoration:none; margin-top:16px; transition:0.2s;">
<div>
<div style="font-size:12px; font-weight:700; letter-spacing:.12em; text-transform:uppercase; color:#C96A1F; margin-bottom:4px;">✦ Free Vedic Birth Chart ✦</div>
<div style="font-size:15px; font-weight:700; color:#2A1A08;">Check if {info['lord']} is strong or weak in your Kundali</div>
<div style="font-size:12px; color:#8C6A45; margin-top:2px;">Free Kundali at ournakshatra.com — instant results</div>
</div>
<span style="font-size:14px; font-weight:700; padding:8px 16px; background:linear-gradient(135deg, #C9A84C, #C96A1F); color:#fff; border-radius:50px; white-space:nowrap;">Get Free Kundali →</span>
</a>
"""

    # Insert before </main>
    if '</main>' in content:
        content = content.replace('</main>', block + '\n</main>')
        fp.write_text(content)
        print(f"Fixed: {slug}")
    else:
        print(f"No </main> found in {slug}")

print("Done — all 12 Rashi pages updated.")
