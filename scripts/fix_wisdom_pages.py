"""Phase 3: Add emotional→planetary root cause CTAs to all 12 Wisdom topic pages."""
from pathlib import Path

ROOT = Path('/Users/prashastpathak/Bhajan')

# Map each life topic to a planetary root cause and relevant Jyotish tool
WISDOM_CTA = {
    'anxiety': {
        'planet': 'Chandra (Moon)', 'slug': 'chandra',
        'cause': 'Anxiety often stems from an afflicted Moon in the birth chart. The Moon governs the mind and emotions.',
        'tool': 'Check your Moon placement', 'url': 'https://ournakshatra.com/janam_landing.html',
        'remedy': 'Chandra Mantra', 'remedy_url': '/planet/chandra/'
    },
    'anger': {
        'planet': 'Mangal (Mars)', 'slug': 'mangal',
        'cause': 'Anger is amplified by a strong or afflicted Mars. Mars governs aggression, courage, and temper.',
        'tool': 'Check your Mars placement', 'url': 'https://ournakshatra.com/janam_landing.html',
        'remedy': 'Mangal Mantra', 'remedy_url': '/planet/mangal/'
    },
    'fear': {
        'planet': 'Shani (Saturn)', 'slug': 'shani',
        'cause': 'Deep-seated fear is often linked to Saturn transits like Sade Sati. Saturn teaches through restriction and patience.',
        'tool': 'Check your Sade Sati status', 'url': 'https://ournakshatra.com/',
        'remedy': 'Shani Chalisa', 'remedy_url': '/planet/shani/'
    },
    'grief': {
        'planet': 'Ketu', 'slug': 'ketu',
        'cause': 'Grief and detachment are Ketu themes. Ketu governs past-life karma, spiritual loss, and moksha.',
        'tool': 'Check Ketu in your chart', 'url': 'https://ournakshatra.com/janam_landing.html',
        'remedy': 'Ketu Mantra', 'remedy_url': '/planet/ketu/'
    },
    'failure': {
        'planet': 'Shani (Saturn)', 'slug': 'shani',
        'cause': 'Repeated setbacks can indicate a challenging Saturn period. Saturn delays but never denies.',
        'tool': 'Check your Dasha timeline', 'url': 'https://ournakshatra.com/janam_landing.html',
        'remedy': 'Shani Mantra', 'remedy_url': '/planet/shani/'
    },
    'love': {
        'planet': 'Shukra (Venus)', 'slug': 'shukra',
        'cause': 'Love, relationships, and beauty are governed by Venus. A weak Venus can cause difficulties in relationships.',
        'tool': 'Check Venus in your chart', 'url': 'https://ournakshatra.com/janam_landing.html',
        'remedy': 'Shukra Mantra', 'remedy_url': '/planet/shukra/'
    },
    'success': {
        'planet': 'Surya (Sun)', 'slug': 'surya',
        'cause': 'Success, confidence, and leadership are Sun qualities. A strong Sun in the chart indicates fame and authority.',
        'tool': 'Check Sun placement', 'url': 'https://ournakshatra.com/janam_landing.html',
        'remedy': 'Surya Mantra', 'remedy_url': '/planet/surya/'
    },
    'patience': {
        'planet': 'Shani (Saturn)', 'slug': 'shani',
        'cause': 'Patience is Saturn\'s greatest teaching. Those going through Sade Sati learn patience through adversity.',
        'tool': 'Check Sade Sati phase', 'url': 'https://ournakshatra.com/',
        'remedy': 'Shani Chalisa', 'remedy_url': '/planet/shani/'
    },
    'death': {
        'planet': 'Ketu', 'slug': 'ketu',
        'cause': 'The soul\'s journey beyond death is a Ketu theme. Ketu represents moksha — liberation from the cycle of rebirth.',
        'tool': 'Check your spiritual yogas', 'url': 'https://ournakshatra.com/janam_landing.html',
        'remedy': 'Ketu Mantra', 'remedy_url': '/planet/ketu/'
    },
    'duty': {
        'planet': 'Surya (Sun)', 'slug': 'surya',
        'cause': 'Dharma and duty are governed by the Sun and Jupiter. Your 10th house reveals your karmic duty in this life.',
        'tool': 'Check your 10th house', 'url': 'https://ournakshatra.com/janam_landing.html',
        'remedy': 'Surya Mantra', 'remedy_url': '/planet/surya/'
    },
    'morning-prayer': {
        'planet': 'Surya (Sun)', 'slug': 'surya',
        'cause': 'Morning prayers align with Surya (Sun) energy. The Sun represents the soul, vitality, and divine connection.',
        'tool': 'Check your Sun sign', 'url': 'https://ournakshatra.com/janam_landing.html',
        'remedy': 'Surya Stotra', 'remedy_url': '/planet/surya/'
    },
    'forgiveness': {
        'planet': 'Guru (Jupiter)', 'slug': 'guru',
        'cause': 'Forgiveness is a Jupiter quality — wisdom, compassion, and dharma. A strong Jupiter enables letting go.',
        'tool': 'Check Jupiter in your chart', 'url': 'https://ournakshatra.com/janam_landing.html',
        'remedy': 'Guru Mantra', 'remedy_url': '/planet/guru/'
    },
}

for slug, info in WISDOM_CTA.items():
    fp = ROOT / 'wisdom' / slug / 'index.html'
    if not fp.exists():
        print(f"Skip {slug}: not found")
        continue

    content = fp.read_text()
    if 'planetary-root-cta' in content:
        print(f"Already done: {slug}")
        continue

    cta_html = f"""
<!-- ── Planetary Root Cause CTA (Phase 3) ─── -->
<div id="planetary-root-cta" style="position:fixed; bottom:0; left:0; right:0; z-index:90; padding:12px 16px; background:linear-gradient(135deg, rgba(245,240,232,0.97), rgba(237,230,216,0.97)); border-top:2px solid #C96A1F; backdrop-filter:blur(12px); -webkit-backdrop-filter:blur(12px); display:flex; align-items:center; justify-content:center; gap:12px; flex-wrap:wrap;">
  <span style="font-size:14px; color:#5C3D20;">🪐 <strong>Jyotish Root:</strong> {info['cause'].split('.')[0]}.</span>
  <a href="{info['remedy_url']}" style="padding:6px 14px; background:#C96A1F; color:#fff; border-radius:50px; font-size:12px; font-weight:700; text-decoration:none;">🪔 {info['remedy']}</a>
  <a href="{info['url']}" target="_blank" style="padding:6px 14px; background:linear-gradient(135deg,#C9A84C,#C96A1F); color:#fff; border-radius:50px; font-size:12px; font-weight:700; text-decoration:none;">✨ {info['tool']} →</a>
</div>
"""

    content = content.replace('</body>', cta_html + '\n</body>')
    fp.write_text(content)
    print(f"Fixed: {slug}")

print("Done — all Wisdom topic pages updated.")
