"""Phase 3: Add Atmakaraka/tool CTAs to all 5 Upanishad pages."""
from pathlib import Path

ROOT = Path('/Users/prashastpathak/Bhajan')

UPANISHAD_CTA = {
    'isha-upanishad': {
        'name': 'Isha Upanishad',
        'theme': 'The Lord pervades everything — renunciation and action coexist.',
        'cta_title': 'Who is the Lord of Your Chart?',
        'cta_text': 'The Isha Upanishad reveals that the divine pervades all. In Jyotish, your Atmakaraka planet represents the lord of your soul. Discover which planet guides your spiritual evolution.',
        'btn': 'Find Your Atmakaraka',
        'url': 'https://ournakshatra.com/janam_landing.html'
    },
    'kena-upanishad': {
        'name': 'Kena Upanishad',
        'theme': 'Who directs the mind? The power behind all powers.',
        'cta_title': 'What Drives Your Mind?',
        'cta_text': 'The Kena Upanishad asks: "Who directs the mind?" In Vedic astrology, the Moon and its Nakshatra reveal the deep drivers of your consciousness. Discover the cosmic force behind your thoughts.',
        'btn': 'Check Your Moon Nakshatra',
        'url': 'https://ournakshatra.com/janam_landing.html'
    },
    'katha-upanishad': {
        'name': 'Katha Upanishad',
        'theme': 'Nachiketa learns the secret of death and the eternal Self.',
        'cta_title': 'What Does Your 8th House Reveal?',
        'cta_text': 'The Katha Upanishad confronts mortality to reveal immortality. In Jyotish, the 8th house governs transformation, death, and rebirth. Understanding your 8th house reveals your deepest karmic patterns.',
        'btn': 'Explore Your Birth Chart',
        'url': 'https://ournakshatra.com/janam_landing.html'
    },
    'mandukya-upanishad': {
        'name': 'Mandukya Upanishad',
        'theme': 'AUM — the four states of consciousness.',
        'cta_title': 'Your Spiritual Path in the Stars',
        'cta_text': 'The Mandukya Upanishad decodes AUM as the key to consciousness. In your birth chart, the 12th house and Ketu reveal your path to moksha. Discover the spiritual yogas hidden in your Kundali.',
        'btn': 'Check Moksha Yogas',
        'url': 'https://ournakshatra.com/janam_landing.html'
    },
    'mundaka-upanishad': {
        'name': 'Mundaka Upanishad',
        'theme': 'Higher vs lower knowledge — Brahman is the target.',
        'cta_title': 'Higher Knowledge in Your Chart',
        'cta_text': 'The Mundaka Upanishad distinguishes para (higher) from apara (lower) knowledge. Jupiter in your chart governs wisdom and spiritual growth. See if your Guru is strong enough to guide you to Brahman.',
        'btn': 'Check Jupiter Strength',
        'url': 'https://ournakshatra.com/janam_landing.html'
    },
}

for slug, info in UPANISHAD_CTA.items():
    fp = ROOT / 'upanishad' / slug / 'index.html'
    if not fp.exists():
        print(f"Skip {slug}: not found")
        continue

    content = fp.read_text()
    if 'upanishad-jyotish-cta' in content:
        print(f"Already done: {slug}")
        continue

    cta_html = f"""
<!-- ── Upanishad → Jyotish CTA (Phase 3) ─── -->
<div id="upanishad-jyotish-cta" style="max-width:800px; margin:30px auto 20px; padding:24px; background:linear-gradient(135deg, rgba(201,106,31,0.06), rgba(168,131,42,0.06)); border:1px solid rgba(201,168,76,0.3); border-radius:12px; text-align:center;">
  <h3 style="font-size:18px; color:#C96A1F; font-weight:800; margin:0 0 8px 0;">✨ {info['cta_title']}</h3>
  <p style="font-size:14px; color:#5C3D20; line-height:1.7; margin:0 0 16px 0; max-width:600px; margin-left:auto; margin-right:auto;">
    {info['cta_text']}
  </p>
  <div style="display:flex; flex-wrap:wrap; gap:10px; justify-content:center;">
    <a href="{info['url']}" target="_blank" style="display:inline-flex; align-items:center; gap:6px; padding:10px 22px; background:linear-gradient(135deg,#C9A84C,#C96A1F); color:#fff; border-radius:50px; font-size:14px; font-weight:700; text-decoration:none; box-shadow:0 4px 14px rgba(201,106,31,0.3);">
      {info['btn']} →
    </a>
    <a href="/planet/guru/" style="display:inline-flex; align-items:center; gap:6px; padding:10px 22px; background:rgba(255,255,255,0.7); color:#5C3D20; border:1px solid #D9CDBA; border-radius:50px; font-size:13px; font-weight:600; text-decoration:none;">
      🪔 Chant Guru Mantra
    </a>
  </div>
</div>
"""

    content = content.replace('</body>', cta_html + '\n</body>')
    fp.write_text(content)
    print(f"Fixed: {slug}")

print("Done — all 5 Upanishad pages updated.")
