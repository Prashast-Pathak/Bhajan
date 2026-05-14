import os
import glob
from pathlib import Path

ROOT = Path('/Users/prashastpathak/Bhajan')

stotras = {
    'surya': {
        'sanskrit': 'जपाकुसुम संकाशं काश्यपेयं महद्युतिम् ।\\nतमोऽरिं सर्वपापघ्नं प्रणतोऽस्मि दिवाकरम् ॥',
        'english': 'Japa Kusuma Sankasham Kashyapeyam Mahadyutim\\nTamorim Sarva Paapaghnam Pranato-Smi Divakaram',
        'meaning': 'I bow to the Sun God (Divakara), who is the color of the hibiscus flower, son of Kashyapa, radiant, the enemy of darkness, and the destroyer of all sins.'
    },
    'chandra': {
        'sanskrit': 'दधिशङ्खतुषाराभं क्षीरोदार्णव सम्भवम् ।\\nनमामि शशिनं सोमं शम्भोर्मुकुट भूषणम् ॥',
        'english': 'Dadhi Shankha Tushaaraabham Ksheero Dhaarnava Sambhavam\\nNamaami Shashinam Somam Shambhor Mukuta Bhooshanam',
        'meaning': 'I bow to the Moon God (Soma), whose hue resembles curd, conch, and snow, born from the milky ocean, who adorns the crest of Lord Shiva.'
    },
    'mangal': {
        'sanskrit': 'धरणीगर्भ सम्भूतं विद्युत्कान्ति समप्रभम् ।\\nकुमारं शक्तिहस्तं तं मङ्गलं प्रणमाम्यहम् ॥',
        'english': 'Dharanee Garbha Sambhootam Vidyut Kaanti Samaprabham\\nKumaaram Shakti Hastam Tam Mangalam Pranamaamyaham',
        'meaning': 'I bow to Mars (Mangala), born from the womb of the Earth, shining with the brilliance of lightning, the youthful wielder of the spear.'
    },
    'budha': {
        'sanskrit': 'प्रियङ्गु कलिकाश्यामं रूपेणाप्रतिमं बुधम् ।\\nसौम्यं सौम्यगुणोपेतं तं बुधं प्रणमाम्यहम् ॥',
        'english': 'Priyangu Kalikaa Shyaamam Roopenaa Pratimam Budham\\nSaumyam Saumya Gunopetam Tam Budham Pranamaamyaham',
        'meaning': 'I bow to Mercury (Budha), dark like the bud of Priyangu, possessing unequalled beauty, gentle, and endowed with gentle qualities.'
    },
    'guru': {
        'sanskrit': 'देवानां च ऋषीणां च गुरुं काञ्चनसन्निभम् ।\\nबुद्धिभूतं त्रिलोकेशं तं नमामि बृहस्पतिम् ॥',
        'english': 'Devaanaam Cha Risheenaam Cha Gurum Kaanchana Sannibham\\nBuddhi Bhootam Trilokesham Tam Namaami Brihaspatim',
        'meaning': 'I bow to Jupiter (Brihaspati), the preceptor of gods and sages, resplendent like gold, the embodiment of wisdom, and the lord of the three worlds.'
    },
    'shukra': {
        'sanskrit': 'हिमकुन्दमृणालाभं दैत्यानां परमं गुरुम् ।\\nसर्वशास्त्रप्रवक्तारं भार्गवं प्रणमाम्यहम् ॥',
        'english': 'Hima Kunda Mrinaalaabham Daityaanaam Paramam Gurum\\nSarva Shaastra Pravaktaaram Bhaargavam Pranamaamyaham',
        'meaning': 'I bow to Venus (Shukra), white like snow, jasmine, and lotus stem, the supreme preceptor of the demons, the exponent of all scriptures.'
    },
    'shani': {
        'sanskrit': 'नीलाञ्जन समाभासं रविपुत्रं यमाग्रजम् ।\\nछायामार्तण्ड सम्भूतं तं नमामि शनैश्चरम् ॥',
        'english': 'Neelaanjana Samaabhaasam Ravi Putram Yamaagrajam\\nChhaayaa Maartanda Sambhootam Tam Namaami Shanaishcharam',
        'meaning': 'I bow to Saturn (Shani), who bears the brilliance of blue collyrium, son of the Sun and elder brother of Yama, born of Chhaya and the Sun.'
    },
    'rahu': {
        'sanskrit': 'अर्धकायं महावीर्यं चन्द्रादित्यविमर्दनम् ।\\nसिंहिकागर्भसम्भूतं तं राहुं प्रणमाम्यहम् ॥',
        'english': 'Ardha Kaayam Mahaa Veeryam Chandraa Ditya Vimardanam\\nSimhikaa Garbha Sambhootam Tam Raahum Pranamaamyaham',
        'meaning': 'I bow to Rahu, having half a body, possessed of immense power, the oppressor of the Moon and the Sun, born from the womb of Simhika.'
    },
    'ketu': {
        'sanskrit': 'पलाशपुष्पसङ्काशं तारकाग्रहमस्तकम् ।\\nरौद्रं रौद्रात्मकं घोरं तं केतुं प्रणमाम्यहम् ॥',
        'english': 'Palaasha Pushpa Sankaasham Taarakaa Graha Mastakam\\nRaudram Raudraatmakam Ghoram Tam Ketum Pranamaamyaham',
        'meaning': 'I bow to Ketu, whose color resembles the Palasha flower, serving as the head of stars and planets, fierce, terrible, and of wrathful nature.'
    }
}

for p in stotras.keys():
    file_path = ROOT / "planet" / p / "index.html"
    if not file_path.exists():
        print(f"Skipping {p}, file not found")
        continue

    content = file_path.read_text()
    
    # Check if already injected
    if "Stotra (Veda Vyasa)" in content:
        print(f"Already fixed {p}")
        continue
    
    capitalized_planet = p.capitalize()
    s = stotras[p]
    
    sanskrit_html = s['sanskrit'].replace('\\n', '<br>')
    english_html = s['english'].replace('\\n', '<br>')
    
    stotra_html = f"""
        <!-- ── STOTRA SECTION ─────────────────────────────── -->
        <div class="section-label" style="margin-top:2rem; font-size:.72rem;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--planet-color);margin-bottom:.75rem;display:flex;align-items:center;gap:.5rem;">
            Navagraha Stotra (Veda Vyasa)
            <span style="flex:1;height:1px;background:var(--border);display:block;"></span>
        </div>
        <div class="mantra-card" aria-label="{capitalized_planet} Stotra text">
            <div class="mantra-row">
                <div class="mantra-lang">Sanskrit</div>
                <div class="mantra-text-devanagari" style="font-size:1.25rem;">{sanskrit_html}</div>
            </div>
            <hr class="divider" />
            <div class="mantra-row">
                <div class="mantra-lang">English</div>
                <div class="mantra-text-english" style="font-style:normal;">{english_html}</div>
            </div>
            <hr class="divider" />
            <div class="mantra-row">
                <div class="mantra-lang">Meaning</div>
                <div class="mantra-text-english">{s['meaning']}</div>
            </div>
        </div>
        
        <!-- ── ASTROLOGY TOOL LINKS ─────────────────────────────── -->
        <div class="section-card" style="background:rgba(217, 119, 6, 0.05); border-color:var(--planet-color);">
            <div class="section-label">Astrology Insights</div>
            <h2 style="font-size:1.1rem; margin-bottom:10px;">Check Your {capitalized_planet} Status</h2>
            <ul style="list-style:none; display:flex; flex-direction:column; gap:8px;">
                <li><span style="color:var(--planet-color);">➤</span> <a href="https://ournakshatra.com/" style="font-weight:bold; color:var(--text-sec);">Sky Today: {capitalized_planet} is in which Rashi today? Check impact</a></li>
                <li><span style="color:var(--planet-color);">➤</span> <a href="https://ournakshatra.com/" style="font-weight:bold; color:var(--text-sec);">Read: What happens during {capitalized_planet} Mahadasha — complete guide</a></li>
            </ul>
        </div>
"""
    
    # Inject after the Mantra Card, before Recommended Bhajans
    # Find the end of the Mantra Card
    mantra_card_end = "<!-- ── RECOMMENDED BHAJANS ────────────────────────── -->"
    if mantra_card_end in content:
        content = content.replace(mantra_card_end, stotra_html + "\\n        " + mantra_card_end)
        file_path.write_text(content)
        print(f"Fixed {p}")
    else:
        print(f"Could not find insertion point for {p}")

print("Done.")
