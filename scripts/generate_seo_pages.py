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

def generate_ssr_html(item):
    """Generates server-side rendered HTML for Googlebot indexing."""
    title = item.get('title_hindi') or item.get('title_english') or item.get('name_english') or item.get('name_hindi') or 'Title'
    desc = item.get('description_english') or item.get('intro_english') or item.get('theme_english') or ''
    
    html_out = f'<div id="ssr-content" style="padding: 20px;">\n'
    html_out += f'<h1>{safe(title)}</h1>\n'
    html_out += f'<p>{safe(desc)}</p>\n'
    
    if "verses" in item:
        for v in item["verses"]:
            html_out += "<div class='verse-block'>\n"
            if "lines" in v:
                for l in v["lines"]:
                    html_out += f"<p>{safe(l.get('hindi', ''))}</p>\n"
                    html_out += f"<p>{safe(l.get('meaning_hindi', ''))}</p>\n"
                    html_out += f"<p>{safe(l.get('meaning_en', ''))}</p>\n"
            elif "sanskrit" in v: # For Gita
                html_out += f"<p>{safe(v.get('sanskrit', ''))}</p>\n"
                html_out += f"<p>{safe(v.get('hindi_translation', ''))}</p>\n"
                html_out += f"<p>{safe(v.get('english_translation', ''))}</p>\n"
            html_out += "</div>\n"
            
    if "quotes" in item:
        for q in item["quotes"]:
            html_out += f"<blockquote>{safe(q.get('quote_english', ''))}</blockquote>\n"
            
    html_out += f'</div>\n'
    return html_out

def inject_seo(template_html, slug, seo_title, seo_desc, canonical_url, schema_json, ssr_content="", scroll_hash=""):
    """
    Takes the master UI HTML and injects perfectly optimized SEO metadata,
    JSON-LD, SSR content and the auto-scroll + slug logic.
    """
    import re
    html_out = re.sub(r'<title.*?</title>', f'<title>{seo_title}</title>', template_html, flags=re.IGNORECASE)
    html_out = re.sub(r'<meta.*?name="description".*?>', f'<meta name="description" content="{seo_desc}">', html_out, flags=re.IGNORECASE)
    
    if re.search(r'<link.*?rel="canonical".*?>', html_out, flags=re.IGNORECASE):
        html_out = re.sub(r'<link.*?rel="canonical".*?>', f'<link rel="canonical" href="{canonical_url}">', html_out, flags=re.IGNORECASE)
    else:
        html_out = html_out.replace('</head>', f'  <link rel="canonical" href="{canonical_url}">\n</head>')
    
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
    html_out = html_out.replace("fetch('data/", "fetch('/data/")
    html_out = html_out.replace('fetch("data/', 'fetch("/data/')

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

    # Inject OpenGraph tags and SSR script
    head_injection = f"""
    <meta property="og:title" content="{seo_title}">
    <meta property="og:description" content="{seo_desc}">
    <meta property="og:url" content="{canonical_url}">
    <meta property="og:type" content="article">
    <meta property="og:image" content="{BASE_URL}/icon-512.png">
    <meta name="twitter:card" content="summary_large_image">
    <script type="application/ld+json">{schema_json}</script>
    <script>
        window.__PRERENDERED_SLUG__ = "{slug}";
        window.addEventListener('load', function() {{ {scroll_script} }});
    </script>
    """
    html_out = html_out.replace("</head>", f"{head_injection}\n</head>")
    
    # Inject SSR Content right inside <main id="content-wrapper"> or equivalent
    if ssr_content:
        # For general pages it's usually <div class="content-wrapper" id="content-wrapper">
        html_out = html_out.replace('<div class="loading">', f'{ssr_content}\n<div class="loading">')
        # For Gita it's <main id="main-content"
        html_out = html_out.replace('<div id="loading-state">', f'{ssr_content}\n<div id="loading-state">')
    
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
    b_intents = [{"suffix": "", "title_append": ""}]
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
            ssr = generate_ssr_html(item)
            out_html = inject_seo(b_template, slug, seo_t, seo_d, canonical, schema, ssr_content=ssr)
            write_page(route, out_html)
            b_count += 1
        
        

    # 2. SHLOKAS
    s_template = (ROOT / "shlokas.html").read_text(encoding="utf-8")
    shlokas = load_json(DATA / "shlokas.json")
    s_intents = [""]
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
            ssr = generate_ssr_html(item)
            out_html = inject_seo(s_template, slug, seo_t, seo_d, canonical, schema, ssr_content=ssr)
            write_page(route, out_html)
            s_count += 1

    # 3. PRAYERS
    p_template = (ROOT / "prayers.html").read_text(encoding="utf-8")
    prayers = load_json(DATA / "prayers.json").get("prayers", [])
    p_intents = [""]
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
            ssr = generate_ssr_html(item)
            out_html = inject_seo(p_template, slug, seo_t, seo_d, canonical, schema, ssr_content=ssr)
            write_page(route, out_html)
            p_count += 1

    # 4. UPANISHADS
    u_template = (ROOT / "upanishads.html").read_text(encoding="utf-8")
    upanishads = load_json(DATA / "upanishads.json")
    u_intents = [""]
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
            ssr = generate_ssr_html(item)
            out_html = inject_seo(u_template, slug, seo_t, seo_d, canonical, schema, ssr_content=ssr)
            write_page(route, out_html)
            u_count += 1

    # 5. WISDOM
    w_template = (ROOT / "wisdom.html").read_text(encoding="utf-8")
    wisdom = load_json(DATA / "wisdom.json").get("topics", [])
    w_intents = [""]
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
            ssr = generate_ssr_html(item)
            out_html = inject_seo(w_template, slug, seo_t, seo_d, canonical, schema, ssr_content=ssr)
            write_page(route, out_html)
            w_count += 1

    # 6. BHAGAVAD GITA
    g_template = (ROOT / "bhagavad-gita.html").read_text(encoding="utf-8")
    gita_chapters = load_json(DATA / "gita.json").get("chapters", [])
    g_count = 0
    for ch in gita_chapters:
        c_num = ch.get("chapter")
        
        # 1. Generate the Chapter Hub Page
        route_ch = f"gita/{c_num}"
        seo_t_ch = f"Bhagavad Gita Chapter {c_num} | Sanatan Gyan Sagar"
        seo_d_ch = f"Read Bhagavad Gita Chapter {c_num} with translation and meaning."
        base_route_ch = route_ch
        canonical_ch = f"{BASE_URL}/{base_route_ch}/"
        schema_ch = build_schema(seo_t_ch, seo_d_ch, f"{BASE_URL}/{route_ch}/")
        
        gita_injection_ch = f"""
        <meta property="og:title" content="{seo_t_ch}">
        <meta property="og:description" content="{seo_d_ch}">
        <meta property="og:url" content="{canonical_ch}">
        <meta property="og:type" content="article">
        <meta property="og:image" content="{BASE_URL}/icon-512.png">
        <meta name="twitter:card" content="summary_large_image">
        <script type="application/ld+json">{schema_ch}</script>
        <script>
            window.__PRERENDERED_CHAPTER__ = "{c_num}";
        </script>
        """
        out_html_ch = g_template.replace("</head>", f"{gita_injection_ch}\n</head>")
        
        # Inject SSR
        ssr_ch = generate_ssr_html(ch)
        out_html_ch = out_html_ch.replace('<div id="loading-state">', f'{ssr_ch}\n<div id="loading-state">')
        
        import re
        out_html_ch = re.sub(r'<title.*?</title>', f'<title>{seo_t_ch}</title>', out_html_ch, flags=re.IGNORECASE)
        out_html_ch = re.sub(r'<meta.*?name="description".*?>', f'<meta name="description" content="{seo_d_ch}">', out_html_ch, flags=re.IGNORECASE)
        out_html_ch = re.sub(r'<link.*?rel="canonical".*?>', f'<link rel="canonical" href="{canonical_ch}">', out_html_ch, flags=re.IGNORECASE)
        out_html_ch = out_html_ch.replace('href="', 'href="/').replace('href="//', 'href="/').replace('href="/http', 'href="http')
        out_html_ch = out_html_ch.replace("fetch('data/", "fetch('/data/").replace('fetch("data/', 'fetch("/data/')
        out_html_ch = out_html_ch.replace('src="manifest.json"', 'src="/manifest.json"')
        write_page(route_ch, out_html_ch)
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
