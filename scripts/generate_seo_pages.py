#!/usr/bin/env python3
import json
import html
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
OUT = ROOT
BASE_URL = "https://bhajan.ournakshatra.com"

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def build_schema(title, desc, url):
    schema = {
        "@context": "https://schema.org",
        "@type": "CreativeWork",
        "name": title,
        "description": desc,
        "url": url,
        "inLanguage": ["hi", "en", "sa"]
    }
    return json.dumps(schema, indent=4)

def inject_seo(template_html, slug, seo_title, seo_desc, canonical_url, schema_json, scroll_hash=""):
    """
    Takes the master UI HTML and injects perfectly optimized SEO metadata,
    JSON-LD, and the auto-scroll + slug logic without changing the design.
    """
    # Replace standard title
    import re
    html_out = re.sub(r'<title.*?</title>', f'<title>{seo_title}</title>', template_html, flags=re.IGNORECASE)
    
    # Replace meta description
    html_out = re.sub(r'<meta.*?name="description".*?>', f'<meta name="description" content="{seo_desc}">', html_out, flags=re.IGNORECASE)
    
    # Replace or Inject canonical link
    if re.search(r'<link.*?rel="canonical".*?>', html_out, flags=re.IGNORECASE):
        html_out = re.sub(r'<link.*?rel="canonical".*?>', f'<link rel="canonical" href="{canonical_url}">', html_out, flags=re.IGNORECASE)
    else:
        html_out = html_out.replace('</head>', f'  <link rel="canonical" href="{canonical_url}">\n</head>')
    
    # Fix asset paths since the generated files are deeper in the directory structure
    # Change href="bhajans.html" to href="/bhajans.html" etc.
    html_out = html_out.replace('href="index.html"', 'href="/index.html"')
    html_out = html_out.replace('href="bhajans.html"', 'href="/bhajans.html"')
    html_out = html_out.replace('href="bhagavad-gita.html"', 'href="/bhagavad-gita.html"')
    html_out = html_out.replace('href="wisdom.html"', 'href="/wisdom.html"')
    html_out = html_out.replace('href="shlokas.html"', 'href="/shlokas.html"')
    html_out = html_out.replace('href="prayers.html"', 'href="/prayers.html"')
    html_out = html_out.replace('href="upanishads.html"', 'href="/upanishads.html"')
    html_out = html_out.replace('href="favorites.html"', 'href="/favorites.html"')
    html_out = html_out.replace('href="about.html"', 'href="/about.html"')
    html_out = html_out.replace('href="contact.html"', 'href="/contact.html"')
    html_out = html_out.replace('href="privacy-policy.html"', 'href="/privacy-policy.html"')
    html_out = html_out.replace('href="bhajan.html?slug=', 'href="/bhajan.html?slug=')
    html_out = html_out.replace("href='bhajan.html?slug=", "href='/bhajan.html?slug=")
    html_out = html_out.replace('href="bhajans.html?', 'href="/bhajans.html?')
    html_out = html_out.replace('src="manifest.json"', 'src="/manifest.json"')
    html_out = html_out.replace('href="manifest.json"', 'href="/manifest.json"')
    # CRITICAL: Fix data fetch paths — generated pages are 2 levels deep so
    # relative fetch('data/...') would look in the wrong folder. Force absolute.
    html_out = html_out.replace("fetch('data/", "fetch('/data/")
    html_out = html_out.replace('fetch("data/', 'fetch("/data/')

    # Inject the Schema, Prerendered Slug, and Auto-Scroll Script into <head>
    scroll_script = ""
    if scroll_hash:
        scroll_script = f"""
        setTimeout(function() {{
            var el = document.getElementById('{scroll_hash}');
            if(el) {{
                el.scrollIntoView({{behavior: 'smooth', block: 'center'}});
                el.style.borderLeft = '4px solid #C96A1F';
                el.style.backgroundColor = '#fff5ee';
            }}
        }}, 800);
        """

    head_injection = f"""
    <script type="application/ld+json">{schema_json}</script>
    <script>
        window.__PRERENDERED_SLUG__ = "{slug}";
        window.addEventListener('load', function() {{ {scroll_script} }});
    </script>
    """
    html_out = html_out.replace("</head>", f"{head_injection}\n</head>")
    
    return html_out

def write_page(route, html_content):
    path = OUT / route / "index.html"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html_content, encoding="utf-8")

def safe(v):
    return html.escape(str(v or ""))

def generate():
    for d in ["bhajan", "shloka", "prayer", "upanishad", "wisdom", "gita"]:
        p = OUT / d
        if p.exists():
            import shutil
            shutil.rmtree(p)

    # 1. BHAJANS
    b_template = (ROOT / "bhajan.html").read_text(encoding="utf-8")
    bhajans = load_json(DATA / "bhajans.json")
    
    # ONLY generate pages for bhajans that actually have content (verses)
    bhajans = [b for b in bhajans if b.get("verses") and len(b.get("verses")) > 0]
    b_intents = [
        {"suffix": "", "title_append": "Lyrics & Meaning"},
        {"suffix": "-hindi-lyrics", "title_append": "Hindi Lyrics (हिंदी में)"},
        {"suffix": "-english-meaning", "title_append": "English Meaning"},
        {"suffix": "-benefits", "title_append": "Chanting Benefits"},
        {"suffix": "-audio-song", "title_append": "Audio Info"},
        {"suffix": "-pdf", "title_append": "PDF Free Download"},
        {"suffix": "-fast-chanting", "title_append": "Fast Chanting Version"}
    ]
    b_count = 0
    for item in bhajans:
        slug = item["slug"]
        base_t = item.get("title_roman", slug)
        for i in b_intents:
            route = f"bhajan/{slug}{i['suffix']}"
            seo_t = f"{base_t} {i['title_append']} | {item.get('title_hindi', '')}"
            seo_d = f"Read the {i['title_append']} of {base_t}."
            base_route = f"bhajan/{slug}"
            canonical = f"{BASE_URL}/{base_route}/"
            schema = build_schema(seo_t, seo_d, f"{BASE_URL}/{route}/")
            out_html = inject_seo(b_template, slug, seo_t, seo_d, canonical, schema)
            write_page(route, out_html)
            b_count += 1
        
        # Verse Level
        verses = item.get("verses", [])
        v_idx = 1
        for v in verses:
            v_type = (v.get("type") or "verse").lower()
            v_label = v.get("label_english") or f"Verse {v_idx}"
            
            # Meaning and Lyrics pages for the specific verse
            v_intents = [
                {"suffix": f"-{v_type}-{v_idx}-lyrics", "t": f"Lyrics"},
                {"suffix": f"-{v_type}-{v_idx}-meaning", "t": f"Meaning"}
            ]
            for i in v_intents:
                route = f"bhajan/{slug}{i['suffix']}"
                seo_t = f"{base_t} {v_label} {i['t']} | Sanatan Gyan Sagar"
                seo_d = f"Complete meaning and translation for {v_label} of {base_t}."
                base_route = f"bhajan/{slug}"
                canonical = f"{BASE_URL}/{base_route}/"
                schema = build_schema(seo_t, seo_d, f"{BASE_URL}/{route}/")
                # Auto-scroll to line-v_idx-0 (The ID format in bhajan.html is line-{vi}-{li})
                out_html = inject_seo(b_template, slug, seo_t, seo_d, canonical, schema, scroll_hash=f"line-{v_idx-1}-0")
                write_page(route, out_html)
                b_count += 1
            v_idx += 1

    # 2. SHLOKAS
    s_template = (ROOT / "shlokas.html").read_text(encoding="utf-8")
    shlokas = load_json(DATA / "shlokas.json")
    s_intents = ["", "-meaning", "-sanskrit-lyrics", "-benefits"]
    s_count = 0
    for item in shlokas:
        slug = item["slug"]
        base_t = item.get("title_roman", slug)
        for i in s_intents:
            route = f"shloka/{slug}{i}"
            seo_t = f"{base_t} {i.replace('-',' ').title()} | Sanatan Gyan Sagar"
            seo_d = f"Read the {i.replace('-',' ')} of {base_t}."
            base_route = f"shloka/{slug}"
            canonical = f"{BASE_URL}/{base_route}/"
            schema = build_schema(seo_t, seo_d, f"{BASE_URL}/{route}/")
            out_html = inject_seo(s_template, slug, seo_t, seo_d, canonical, schema)
            write_page(route, out_html)
            s_count += 1

    # 3. PRAYERS
    p_template = (ROOT / "prayers.html").read_text(encoding="utf-8")
    prayers = load_json(DATA / "prayers.json").get("prayers", [])
    p_intents = ["", "-steps", "-meaning"]
    p_count = 0
    for item in prayers:
        slug = item["slug"]
        base_t = item.get("title_english", slug)
        for i in p_intents:
            route = f"prayer/{slug}{i}"
            seo_t = f"{base_t} {i.replace('-',' ').title()} | Sanatan Gyan Sagar"
            seo_d = f"Step by step guide for {base_t}."
            base_route = f"prayer/{slug}"
            canonical = f"{BASE_URL}/{base_route}/"
            schema = build_schema(seo_t, seo_d, f"{BASE_URL}/{route}/")
            out_html = inject_seo(p_template, slug, seo_t, seo_d, canonical, schema)
            write_page(route, out_html)
            p_count += 1

    # 4. UPANISHADS
    u_template = (ROOT / "upanishads.html").read_text(encoding="utf-8")
    upanishads = load_json(DATA / "upanishads.json")
    u_intents = ["", "-quotes", "-summary"]
    u_count = 0
    for item in upanishads:
        slug = item["slug"]
        base_t = item.get("name_english", slug)
        for i in u_intents:
            route = f"upanishad/{slug}{i}"
            seo_t = f"{base_t} {i.replace('-',' ').title()} | Sanatan Gyan Sagar"
            seo_d = f"Key verses and summary from the {base_t}."
            base_route = f"upanishad/{slug}"
            canonical = f"{BASE_URL}/{base_route}/"
            schema = build_schema(seo_t, seo_d, f"{BASE_URL}/{route}/")
            out_html = inject_seo(u_template, slug, seo_t, seo_d, canonical, schema)
            write_page(route, out_html)
            u_count += 1

    # 5. WISDOM
    w_template = (ROOT / "wisdom.html").read_text(encoding="utf-8")
    wisdom = load_json(DATA / "wisdom.json").get("topics", [])
    w_intents = ["", "-quotes", "-spiritual-meaning"]
    w_count = 0
    for item in wisdom:
        slug = item["slug"]
        base_t = item.get("title_english", slug)
        for i in w_intents:
            route = f"wisdom/{slug}{i}"
            seo_t = f"{base_t} {i.replace('-',' ').title()} | Spiritual Wisdom"
            seo_d = f"Hindu spiritual quotes and wisdom about {base_t}."
            base_route = f"wisdom/{slug}"
            canonical = f"{BASE_URL}/{base_route}/"
            schema = build_schema(seo_t, seo_d, f"{BASE_URL}/{route}/")
            out_html = inject_seo(w_template, slug, seo_t, seo_d, canonical, schema)
            write_page(route, out_html)
            w_count += 1

    # 6. BHAGAVAD GITA
    g_template = (ROOT / "bhagavad-gita.html").read_text(encoding="utf-8")
    gita_chapters = load_json(DATA / "gita.json").get("chapters", [])
    g_count = 0
    for ch in gita_chapters:
        c_num = ch.get("chapter")
        verses = ch.get("verses", [])
        for v in verses:
            v_num = v.get("verse")
            slug = f"gita-{c_num}-{v_num}"
            
            # The Gita template uses ?chapter=X&verse=Y
            # We will hijack the slug variable logic here uniquely
            v_intents = ["", "-meaning", "-sanskrit"]
            for i in v_intents:
                route = f"gita/{c_num}/{v_num}{i}"
                seo_t = f"Bhagavad Gita Chapter {c_num} Verse {v_num} {i.replace('-',' ').title()}"
                seo_d = f"Read Bhagavad Gita Chapter {c_num} Verse {v_num} meaning and translation."
                base_route = f"gita/{c_num}/{v_num}"
                canonical = f"{BASE_URL}/{base_route}/"
                schema = build_schema(seo_t, seo_d, f"{BASE_URL}/{route}/")
                
                # Special Gita JS injection to bypass URL params
                gita_injection = f"""
                <script type="application/ld+json">{schema}</script>
                <script>
                    window.__PRERENDERED_CHAPTER__ = "{c_num}";
                    window.__PRERENDERED_VERSE__ = "{v_num}";
                </script>
                """
                out_html = g_template.replace("</head>", f"{gita_injection}\n</head>")
                # Fix standard meta stuff
                import re
                out_html = re.sub(r'<title.*?</title>', f'<title>{seo_t}</title>', out_html, flags=re.IGNORECASE)
                out_html = re.sub(r'<meta.*?name="description".*?>', f'<meta name="description" content="{seo_d}">', out_html, flags=re.IGNORECASE)
                out_html = re.sub(r'<link.*?rel="canonical".*?>', f'<link rel="canonical" href="{canonical}">', out_html, flags=re.IGNORECASE)
                
                # Fix paths
                out_html = out_html.replace('href="', 'href="/').replace('href="//', 'href="/').replace('href="/http', 'href="http')
                
                write_page(route, out_html)
                g_count += 1

    total = b_count + s_count + p_count + u_count + w_count + g_count
    print(f"Generated {total} EXACT CLONE Programmatic SEO Pages!")
    print(f"  Bhajans: {b_count}")
    print(f"  Shlokas: {s_count}")
    print(f"  Prayers: {p_count}")
    print(f"  Upanishads: {u_count}")
    print(f"  Wisdom: {w_count}")
    print(f"  Gita: {g_count}")

if __name__ == "__main__":
    generate()
