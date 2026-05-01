#!/usr/bin/env python3
"""
Static Build (Cloudflare Pages)

This project is "template-driven": you add content in ONE fixed schema and the
build generates:
- Clean SEO pages: /bhajan/<slug>/ and 4–5 variant subpages per bhajan
- Remedy intent pages: /remedy/<intent>/
- robots.txt, sitemap.xml, llms.txt, ai.txt, /ai-index/
- Safety & copyright validation (fails build on violations)

Run locally:
  python3 scripts/build.py

Cloudflare Pages:
  Build command: python3 scripts/build.py
  Output folder: dist
"""

from __future__ import annotations

import datetime as _dt
import html
import json
import re
import shutil
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Tuple


REPO = Path(__file__).resolve().parents[1]
DIST = (REPO / "dist").resolve()

CONFIG_PATH = (REPO / "site.config.json").resolve()
INTENTS_PATH = (REPO / "content" / "intents.json").resolve()
CONTENT_BHAJANS_DIR = (REPO / "content" / "bhajans").resolve()
DATA_DIR = (REPO / "data").resolve()


ALLOWED_RIGHTS = {"traditional", "original", "permission"}

def _is_placeholder_token(s: str) -> bool:
    t = (s or "").strip()
    return t in ("—", "-", "--", "---")

# Conservative beej syllable detection (Devanagari + roman).
# NOTE: Keep this conservative to avoid false positives on normal Hindi words
# like "हूँ". We only block the most common seed syllables used in beej mantras.
_BEEJ_DEV = ["ह्रीं", "श्रीं", "क्लीं", "ऐं", "दुं", "गं"]
_BEEJ_ROM = ["hrim", "shrim", "shreem", "klim", "aim", "dum", "gam", "glaum", "hraum", "hroum", "shraum", "shroum"]
_BEEJ_RE = re.compile(r"(" + "|".join(map(re.escape, _BEEJ_DEV + _BEEJ_ROM)) + r")", re.IGNORECASE)


def _read_json(p: Path) -> Any:
    return json.loads(p.read_text(encoding="utf-8"))


def _write_text(p: Path, s: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(s, encoding="utf-8")


def _write_json(p: Path, obj: Any) -> None:
    _write_text(p, json.dumps(obj, ensure_ascii=False, indent=2) + "\n")


def _esc(s: Any) -> str:
    return html.escape(str(s or ""), quote=True)


def _load_config() -> Dict[str, Any]:
    if not CONFIG_PATH.exists():
        raise SystemExit("Missing site.config.json")
    cfg = _read_json(CONFIG_PATH)
    if not isinstance(cfg, Mapping):
        raise SystemExit("Invalid site.config.json")
    origin = str(cfg.get("origin") or "").strip().rstrip("/")
    astrology_origin = str(cfg.get("astrology_origin") or "").strip().rstrip("/")
    if not origin.startswith("https://"):
        raise SystemExit("site.config.json: origin must start with https://")
    if not astrology_origin.startswith("https://"):
        raise SystemExit("site.config.json: astrology_origin must start with https://")
    return dict(cfg)


def _iter_text(obj: Any) -> Iterable[str]:
    if obj is None:
        return []
    if isinstance(obj, str):
        return [obj]
    if isinstance(obj, Mapping):
        out: List[str] = []
        for v in obj.values():
            out.extend(_iter_text(v))
        return out
    if isinstance(obj, list):
        out2: List[str] = []
        for v in obj:
            out2.extend(_iter_text(v))
        return out2
    return [str(obj)]


def _detect_beej(texts: Iterable[str]) -> Optional[str]:
    for t in texts:
        m = _BEEJ_RE.search(t or "")
        if m:
            return m.group(1)
    return None


def _reject_placeholders_in_lines(item: Mapping[str, Any]) -> None:
    verses = item.get("verses")
    if not isinstance(verses, list):
        return
    for vb in verses:
        if not isinstance(vb, Mapping):
            continue
        lines = vb.get("lines")
        if not isinstance(lines, list):
            continue
        for ln in lines:
            if not isinstance(ln, Mapping):
                continue
            for k in ("hindi", "roman", "hindi_meaning", "english"):
                v = str(ln.get(k) or "")
                if _is_placeholder_token(v):
                    raise ValueError(f"placeholder_token_in_line:{k}")


def _validate_rights(item: Mapping[str, Any]) -> None:
    rights = item.get("rights")
    if not isinstance(rights, Mapping):
        raise ValueError("rights_missing")
    lic = str(rights.get("license") or "").strip().lower()
    if lic not in ALLOWED_RIGHTS:
        raise ValueError(f"rights_license_invalid:{lic or 'missing'}")


def _require_str(item: Mapping[str, Any], key: str) -> str:
    v = str(item.get(key) or "").strip()
    if not v or _is_placeholder_token(v):
        raise ValueError(f"missing:{key}")
    return v


def _validate_bhajan(item: Mapping[str, Any]) -> None:
    slug = _require_str(item, "slug")
    if not re.fullmatch(r"[a-z0-9][a-z0-9\-]*", slug):
        raise ValueError(f"bad_slug:{slug}")
    _require_str(item, "type")
    _require_str(item, "deity")
    _require_str(item, "language")
    _require_str(item, "title_hindi")
    _require_str(item, "title_roman")
    _require_str(item, "title_english")

    seo = item.get("seo")
    if not isinstance(seo, Mapping) or not str(seo.get("meta_title") or "").strip():
        raise ValueError("missing_seo_meta_title")
    if not str(seo.get("meta_description") or "").strip():
        raise ValueError("missing_seo_meta_description")

    verses = item.get("verses")
    if not isinstance(verses, list) or not verses:
        raise ValueError("missing_verses")
    for vb in verses:
        if not isinstance(vb, Mapping):
            raise ValueError("bad_verse_block")
        lines = vb.get("lines")
        if not isinstance(lines, list) or not lines:
            raise ValueError("empty_verse_lines")
        for ln in lines:
            if not isinstance(ln, Mapping):
                raise ValueError("bad_line")
            # User asked: Sanskrit/Hindi/English should be properly written — disallow placeholders.
            h = str(ln.get("hindi") or "").strip()
            r = str(ln.get("roman") or "").strip()
            if not h or not r:
                raise ValueError("line_missing_hindi_or_roman")
            if _is_placeholder_token(h) or _is_placeholder_token(r):
                raise ValueError("placeholder_token_in_required_line")

    _validate_rights(item)

    safety = item.get("safety") if isinstance(item.get("safety"), Mapping) else {}
    disallow_beej = True
    if isinstance(safety, Mapping) and safety.get("disallow_beej") is False:
        disallow_beej = False
    if disallow_beej:
        hit = _detect_beej(_iter_text(item))
        if hit:
            raise ValueError(f"beej_detected:{hit}")

    # No placeholder tokens in verse lines/meanings.
    _reject_placeholders_in_lines(item)


def _load_bhajans() -> List[Dict[str, Any]]:
    items: List[Dict[str, Any]] = []
    if not CONTENT_BHAJANS_DIR.exists():
        return items
    for p in sorted(CONTENT_BHAJANS_DIR.glob("*.json")):
        raw = _read_json(p)
        if not isinstance(raw, Mapping):
            raise SystemExit(f"Invalid JSON: {p}")
        item = dict(raw)
        try:
            _validate_bhajan(item)
        except Exception as exc:
            raise SystemExit(f"Bhajan validation failed: {p.name}: {exc}") from exc
        items.append(item)
    # Unique slugs
    seen = set()
    for it in items:
        s = it["slug"]
        if s in seen:
            raise SystemExit(f"Duplicate bhajan slug: {s}")
        seen.add(s)
    return items


def _load_intents() -> Dict[str, Any]:
    if not INTENTS_PATH.exists():
        return {"version": "1.0", "intents": []}
    raw = _read_json(INTENTS_PATH)
    if not isinstance(raw, Mapping):
        raise SystemExit("Invalid content/intents.json")
    intents = raw.get("intents") if isinstance(raw.get("intents"), list) else []
    clean = []
    for it in intents:
        if not isinstance(it, Mapping):
            continue
        key = str(it.get("key") or "").strip()
        if not re.fullmatch(r"[a-z0-9_]+", key):
            continue
        clean.append(dict(it))
    return {"version": str(raw.get("version") or "1.0"), "intents": clean}


def _variant_specs_for_bhajan(b: Mapping[str, Any]) -> List[Tuple[str, str]]:
    specs: List[Tuple[str, str]] = []
    if b.get("story") or b.get("story_hindi"):
        specs.append(("story", "Story"))
    if b.get("benefits"):
        specs.append(("benefits", "Benefits"))
    specs.append(("how-to", "How to Chant"))
    specs.append(("faq", "FAQ"))
    specs.append(("astrology", "Astrology Support"))
    return specs[:5]


def _page_shell(
    *,
    cfg: Mapping[str, Any],
    title: str,
    description: str,
    canonical: str,
    body_html: str,
    lang: str = "hi",
) -> str:
    site_name = str(cfg.get("site_name") or "Sanatan Gyan Sagar")
    return f"""<!doctype html>
<html lang="{_esc(lang)}">
<head>
  <meta charset="utf-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1"/>
  <title>{_esc(title)}</title>
  <meta name="description" content="{_esc(description)}"/>
  <meta name="robots" content="index,follow"/>
  <link rel="canonical" href="{_esc(canonical)}"/>
  <link rel="alternate" type="text/plain" href="/llms.txt" title="LLMs"/>
  <link rel="alternate" type="text/plain" href="/ai.txt" title="AI"/>
  <link rel="icon" href="/favicon.ico"/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Tiro+Devanagari+Hindi:ital@0;1&family=Lato:wght@300;400;700&display=swap" rel="stylesheet"/>
  <style>
    :root {{
      --bg:#F5F0E8;--surface:#EDE6D8;--saffron:#C96A1F;--maroon:#6E1515;--text:#2A1A08;--text-sec:#5C3D20;
      --text-muted:#8C6A45;--border:#D9CDBA;--shadow:0 2px 12px rgba(42,26,8,0.08);
      --font-hindi:'Tiro Devanagari Hindi',serif;--font-ui:'Lato',sans-serif;
    }}
    *{{box-sizing:border-box}}
    body{{margin:0;background:var(--bg);color:var(--text);font-family:var(--font-ui);line-height:1.65}}
    header{{position:sticky;top:0;z-index:20;background:rgba(245,240,232,.92);backdrop-filter:blur(12px);border-bottom:1px solid var(--border)}}
    .hdr{{max-width:1100px;margin:0 auto;height:60px;display:flex;align-items:center;justify-content:space-between;padding:0 16px;gap:10px}}
    .logo{{text-decoration:none;display:flex;align-items:center;gap:10px}}
    .om{{width:40px;height:40px;border-radius:999px;display:flex;align-items:center;justify-content:center;color:#fff;
      background:linear-gradient(135deg,var(--saffron),var(--maroon));font-family:var(--font-hindi);font-size:20px}}
    .lt{{display:flex;flex-direction:column;line-height:1.15}}
    .lt b{{font-family:var(--font-hindi);color:var(--maroon);font-size:17px}}
    .lt span{{font-size:10px;color:var(--text-muted);display:none}}
    @media(min-width:480px){{.lt span{{display:block}}}}
    nav a{{text-decoration:none;color:var(--text-sec);font-size:13px;padding:6px 10px;border-radius:8px;min-height:44px;display:flex;align-items:center}}
    nav a:hover{{background:var(--surface);color:var(--saffron)}}
    main{{max-width:980px;margin:0 auto;padding:22px 16px 80px}}
    .k{{font-size:12px;color:var(--text-muted)}}
    h1{{font-family:var(--font-hindi);color:var(--maroon);font-size:34px;line-height:1.2;margin:10px 0 10px}}
    .card{{background:rgba(237,230,216,.75);border:1px solid var(--border);border-radius:16px;padding:16px;box-shadow:var(--shadow)}}
    .pillrow{{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px}}
    .pill{{text-decoration:none;color:var(--text-sec);border:1px solid var(--border);background:rgba(255,255,255,.6);padding:7px 10px;border-radius:999px;font-size:13px}}
    .pill:hover{{border-color:rgba(201,106,31,.45);color:var(--saffron)}}
    footer{{border-top:1px solid var(--border);background:rgba(245,240,232,.8)}}
    .ftr{{max-width:980px;margin:0 auto;padding:18px 16px;color:var(--text-muted);font-size:12px;line-height:1.6}}
    .cta{{display:inline-flex;align-items:center;gap:8px;text-decoration:none;background:var(--saffron);color:#fff;padding:10px 14px;border-radius:12px;font-weight:700}}
    .cta:hover{{background:var(--maroon)}}
    .muted{{color:var(--text-muted)}}
  </style>
</head>
<body>
  <header>
    <div class="hdr">
      <a class="logo" href="/" aria-label="Home">
        <div class="om">ॐ</div>
        <div class="lt"><b>{_esc(cfg.get("site_name_hindi") or site_name)}</b><span>{_esc(cfg.get("brand_tagline_en") or "")}</span></div>
      </a>
      <nav aria-label="Primary">
        <a href="/bhajans.html">Bhajans</a>
        <a href="/shlokas.html">Shlokas</a>
        <a href="/bhagavad-gita.html">Gita</a>
      </nav>
    </div>
  </header>
  <main>
    {body_html}
  </main>
  <footer><div class="ftr">
    <div><strong>Disclaimer:</strong> This content is for devotional/educational use. No guarantees or medical/legal claims.</div>
    <div class="muted">© {int(_dt.datetime.now().year)} {html.escape(site_name)} · <a href="/disclaimer/">Disclaimer</a> · <a href="/terms/">Terms</a> · <a href="/privacy-policy.html">Privacy</a></div>
  </div></footer>
</body>
</html>
"""


def _render_bhajan_page(cfg: Mapping[str, Any], b: Mapping[str, Any], *, canonical_path: str, variant_key: str = "") -> str:
    origin = str(cfg["origin"]).rstrip("/")
    canonical = origin + canonical_path

    title_h = str(b.get("title_hindi") or "").strip()
    title_r = str(b.get("title_roman") or "").strip()
    display = " — ".join([x for x in [title_h, title_r] if x]).strip(" — ") or b["slug"]

    meta_title = str(((b.get("seo") or {}).get("meta_title")) or display).strip()
    meta_desc = str(((b.get("seo") or {}).get("meta_description")) or "").strip()
    if variant_key:
        meta_title = f"{meta_title} — {variant_key}".strip()

    pills = []
    pills.append(f'<a class="pill" href="/bhajan/{_esc(b["slug"])}/">Main</a>')
    for key, label in _variant_specs_for_bhajan(b):
        pills.append(f'<a class="pill" href="/bhajan/{_esc(b["slug"])}/{_esc(key)}/">{_esc(label)}</a>')
    pill_html = '<div class="pillrow">' + "".join(pills) + "</div>"

    deity = str(b.get("deity") or "Deity")
    intent_keys = ((b.get("crosslinks") or {}).get("astrology_intents") or []) if isinstance(b.get("crosslinks"), Mapping) else []
    intent_keys = [str(x).strip() for x in intent_keys if str(x).strip()]
    intents_links = ""
    if intent_keys:
        links = "".join([f'<a class="pill" href="/remedy/{_esc(k)}/">{_esc(k.replace("_"," "))}</a>' for k in intent_keys])
        intents_links = f'<div class="k" style="margin-top:10px">Remedy intents:</div><div class="pillrow">{links}</div>'

    astrology_origin = str(cfg["astrology_origin"]).rstrip("/")
    cta = (
        f'<p style="margin-top:14px"><a class="cta" href="{_esc(astrology_origin)}/janam-kundali?utm_source=bhajan&utm_medium=cta&utm_campaign={_esc(b["slug"])}">Compute your chart on ournakshatra.com →</a></p>'
    )

    body = f"""
      <div class="k">{_esc(deity)} · {_esc(b.get("type") or "bhajan")}</div>
      <h1>{_esc(display)}</h1>
      <div class="card">
        <div class="k">Quick context</div>
        <div style="margin-top:6px;color:rgba(92,61,32,.92)">{_esc(b.get("significance_hindi") or b.get("significance") or "")}</div>
        {pill_html}
        {intents_links}
        {cta}
      </div>
    """

    if not variant_key:
        # Render first verse block (keeps page rich, not thin).
        verses = b.get("verses") if isinstance(b.get("verses"), list) else []
        if verses:
            vb = verses[0] if isinstance(verses[0], Mapping) else None
            if vb:
                label = str(vb.get("label_hindi") or vb.get("label_english") or "").strip()
                lines = vb.get("lines") if isinstance(vb.get("lines"), list) else []
                line_html = []
                for ln in lines[:16]:
                    if not isinstance(ln, Mapping):
                        continue
                    h = str(ln.get("hindi") or "").strip()
                    r = str(ln.get("roman") or "").strip()
                    hm = str(ln.get("hindi_meaning") or "").strip()
                    em = str(ln.get("english") or "").strip()
                    line_html.append(
                        f"<p style='margin:10px 0'><span style='font-family:var(--font-hindi);font-size:20px'>{_esc(h)}</span><br/>"
                        f"<span class='muted'>{_esc(r)}</span><br/>"
                        f"<span style='color:rgba(42,26,8,.85)'>{_esc(hm or em)}</span></p>"
                    )
                body += f"<div class='card' style='margin-top:14px'><div class='k'>{_esc(label or 'Verses')}</div>{''.join(line_html)}</div>"

    elif variant_key == "story":
        body += f"<div class='card' style='margin-top:14px'><div class='k'>Story</div><p style='margin-top:8px'>{_esc(b.get('story_hindi') or b.get('story') or '')}</p></div>"
    elif variant_key == "benefits":
        ben = b.get("benefits") if isinstance(b.get("benefits"), list) else []
        lis = "".join([f"<li>{_esc(x)}</li>" for x in ben[:12]])
        body += f"<div class='card' style='margin-top:14px'><div class='k'>Benefits (traditional / devotional)</div><ul style='margin:10px 0 0 18px'>{lis}</ul></div>"
    elif variant_key == "how-to":
        wts = b.get("when_to_sing") if isinstance(b.get("when_to_sing"), Mapping) else {}
        times = wts.get("time") if isinstance(wts.get("time"), list) else []
        occ = wts.get("occasion") if isinstance(wts.get("occasion"), list) else []
        body += (
            "<div class='card' style='margin-top:14px'>"
            "<div class='k'>How to chant (simple)</div>"
            "<p style='margin-top:8px'>Choose a calm time, sit comfortably, and recite with attention. Keep it gentle and consistent.</p>"
            f"<p style='margin-top:8px'><strong>Suggested times:</strong> {_esc(', '.join(map(str, times)) or 'Any calm time')}</p>"
            f"<p style='margin-top:6px'><strong>Occasions:</strong> {_esc(', '.join(map(str, occ)) or 'Daily devotion')}</p>"
            "<p class='muted' style='margin-top:10px'>Note: devotional guidance, not a guarantee.</p>"
            "</div>"
        )
    elif variant_key == "faq":
        body += (
            "<div class='card' style='margin-top:14px'><div class='k'>FAQ</div>"
            "<p style='margin-top:8px'><strong>Is this a guaranteed remedy?</strong><br/>No. Use it as devotional/educational support.</p>"
            "<p style='margin-top:10px'><strong>How often should I read?</strong><br/>Start small (3–7 days). Consistency matters.</p>"
            "<p style='margin-top:10px'><strong>What next?</strong><br/>Compute your chart and check full context (strength + timing).</p>"
            "</div>"
        )
    elif variant_key == "astrology":
        intents = intent_keys or ["general_blessings"]
        lis = "".join([f"<li><a href='/remedy/{_esc(k)}/'>{_esc(k.replace('_',' '))}</a></li>" for k in intents])
        body += (
            "<div class='card' style='margin-top:14px'><div class='k'>Astrology support</div>"
            "<p style='margin-top:8px'>This page can be suggested as devotional support for certain findings (never as a guarantee).</p>"
            f"<ul style='margin:10px 0 0 18px'>{lis}</ul>"
            f"<p style='margin-top:12px'><a class='cta' href='{_esc(astrology_origin)}/janam-kundali?utm_source=bhajan&utm_medium=remedy&utm_campaign={_esc(b['slug'])}'>Compute your chart →</a></p>"
            "</div>"
        )

    return _page_shell(cfg=cfg, title=meta_title, description=meta_desc, canonical=canonical, body_html=body, lang="hi")


def _build_bhajan_pages(cfg: Mapping[str, Any], bhajans: List[Mapping[str, Any]]) -> List[str]:
    urls: List[str] = []
    for b in bhajans:
        slug = str(b["slug"])
        base_path = f"/bhajan/{slug}/"
        _write_text(DIST / "bhajan" / slug / "index.html", _render_bhajan_page(cfg, b, canonical_path=base_path))
        urls.append(base_path)
        for key, _label in _variant_specs_for_bhajan(b):
            v_path = f"/bhajan/{slug}/{key}/"
            _write_text(
                DIST / "bhajan" / slug / key / "index.html",
                _render_bhajan_page(cfg, b, canonical_path=v_path, variant_key=key),
            )
            urls.append(v_path)
    return urls


def _build_remedy_pages(cfg: Mapping[str, Any], intents: Mapping[str, Any], bhajans: List[Mapping[str, Any]]) -> List[str]:
    origin = str(cfg["origin"]).rstrip("/")
    astrology_origin = str(cfg["astrology_origin"]).rstrip("/")
    urls: List[str] = []

    intent_list = intents.get("intents") if isinstance(intents.get("intents"), list) else []
    for it in intent_list:
        if not isinstance(it, Mapping):
            continue
        key = str(it.get("key") or "").strip()
        title = str(it.get("title") or key).strip()
        desc = str(it.get("description") or "").strip()
        matches = []
        for b in bhajans:
            ks = ((b.get("crosslinks") or {}).get("astrology_intents") or []) if isinstance(b.get("crosslinks"), Mapping) else []
            ks = [str(x).strip() for x in ks]
            if key in ks:
                matches.append(b)

        links = []
        for b in matches[:12]:
            links.append(
                f"<li><a href='/bhajan/{_esc(b['slug'])}/'>{_esc(b.get('title_hindi') or b.get('title_roman') or b['slug'])}</a></li>"
            )
        items_html = "<ul style='margin:10px 0 0 18px'>" + "".join(links) + "</ul>" if links else "<p class='muted'>No items mapped yet.</p>"

        page_body = (
            f"<div class='k'>Remedy intent</div><h1>{_esc(title)}</h1>"
            f"<p class='muted'>{_esc(desc)}</p>"
            f"<div class='card' style='margin-top:14px'><div class='k'>Suggested devotional readings</div>{items_html}</div>"
            f"<p style='margin-top:14px'><a class='cta' href='{_esc(astrology_origin)}/janam-kundali?utm_source=bhajan&utm_medium=remedy&utm_campaign={_esc(key)}'>Compute your chart →</a></p>"
        )
        _write_text(
            DIST / "remedy" / key / "index.html",
            _page_shell(
                cfg=cfg,
                title=f"{title} — Remedies (Traditional) | {cfg.get('site_name')}",
                description=desc or f"Traditional devotional support pages for {title}.",
                canonical=origin + f"/remedy/{key}/",
                body_html=page_body,
            ),
        )
        urls.append(f"/remedy/{key}/")

    # Index page
    cards = []
    for it in intent_list:
        if isinstance(it, Mapping):
            key = str(it.get("key") or "").strip()
            title = str(it.get("title") or key).strip()
            if key:
                cards.append(f"<a class='pill' href='/remedy/{_esc(key)}/'>{_esc(title)}</a>")
    idx_body = "<div class='k'>Remedy / Support</div><h1>Remedy pages</h1><p class='muted'>Traditional devotional support pages linked from astrology findings.</p>"
    idx_body += "<div class='pillrow' style='margin-top:14px'>" + "".join(cards) + "</div>"
    _write_text(
        DIST / "remedy" / "index.html",
        _page_shell(
            cfg=cfg,
            title=f"Remedy pages | {cfg.get('site_name')}",
            description="Traditional devotional support pages mapped to astrology findings.",
            canonical=origin + "/remedy/",
            body_html=idx_body,
        ),
    )
    urls.append("/remedy/")
    return urls


def _build_ai_files(cfg: Mapping[str, Any], extra_urls: List[str]) -> List[str]:
    origin = str(cfg["origin"]).rstrip("/")
    body = (
        "<div class='k'>AI index</div><h1>AI Index</h1>"
        "<p class='muted'>High-signal entry pages for discovery and citation.</p>"
        "<div class='card' style='margin-top:14px'><ul style='margin:0 0 0 18px'>"
        f"<li><a href='/'>Home</a></li>"
        f"<li><a href='/bhajans.html'>Bhajans (Index)</a></li>"
        f"<li><a href='/shlokas.html'>Shlokas (Index)</a></li>"
        f"<li><a href='/bhagavad-gita.html'>Bhagavad Gita</a></li>"
        f"<li><a href='/remedy/'>Remedy pages</a></li>"
        + "".join([f"<li><a href='{_esc(u)}'>{_esc(u)}</a></li>" for u in extra_urls[:8]])
        + "</ul></div>"
    )
    _write_text(
        DIST / "ai-index" / "index.html",
        _page_shell(
            cfg=cfg,
            title=f"AI Index | {cfg.get('site_name')}",
            description="High-signal entry pages for AI and humans.",
            canonical=origin + "/ai-index/",
            body_html=body,
        ),
    )

    llms = "\n".join(
        [
            f"# {cfg.get('site_name')} — LLMs",
            f"Origin: {origin}",
            "",
            "## Key entry pages",
            f"- {origin}/ai-index/",
            f"- {origin}/sitemap.xml",
            f"- {origin}/robots.txt",
            "",
            "## Pillars",
            f"- Bhajans: {origin}/bhajans.html",
            f"- Shlokas: {origin}/shlokas.html",
            f"- Gita: {origin}/bhagavad-gita.html",
            f"- Remedy pages: {origin}/remedy/",
            "",
        ]
    )
    ai = "\n".join(
        [
            f"# AI access — {cfg.get('site_name')}",
            f"Origin: {origin}",
            "",
            "This is a public devotional/educational site. Please respect robots.txt and any noindex signals.",
            "",
            "Preferred discovery:",
            f"- {origin}/ai-index/",
            f"- {origin}/sitemap.xml",
            f"- {origin}/robots.txt",
            "",
        ]
    )
    _write_text(DIST / "llms.txt", llms + "\n")
    _write_text(DIST / "ai.txt", ai + "\n")

    # Machine-readable GEO feed (simple, stable).
    ai_index_json = {
        "site": {"name": cfg.get("site_name"), "origin": origin, "generated_at_utc": _dt.datetime.utcnow().isoformat()},
        "entrypoints": {
            "ai_index": f"{origin}/ai-index/",
            "ai_index_json": f"{origin}/ai-index.json",
            "llms_txt": f"{origin}/llms.txt",
            "ai_txt": f"{origin}/ai.txt",
            "sitemap": f"{origin}/sitemap.xml",
            "robots": f"{origin}/robots.txt",
        },
        "pillars": [
            {"url": f"{origin}/bhajans.html", "title": "Bhajans"},
            {"url": f"{origin}/shlokas.html", "title": "Shlokas"},
            {"url": f"{origin}/bhagavad-gita.html", "title": "Bhagavad Gita"},
            {"url": f"{origin}/remedy/", "title": "Remedy pages"},
        ],
        "examples": [{"url": origin + u, "title": u} for u in extra_urls[:10]],
        "cross_funnel": {"astrology_origin": str(cfg.get("astrology_origin") or "").rstrip("/")},
    }
    _write_json(DIST / "ai-index.json", ai_index_json)

    return ["/ai-index/", "/ai-index.json", "/llms.txt", "/ai.txt"]


def _build_legal_pages(cfg: Mapping[str, Any]) -> List[str]:
    origin = str(cfg["origin"]).rstrip("/")
    terms_body = (
        "<div class='k'>Legal</div><h1>Terms</h1>"
        "<div class='card' style='margin-top:14px'>"
        "<p>This site provides devotional/educational content. You may read and share for personal devotion. Do not misuse content to make medical/legal/financial claims.</p>"
        "<p style='margin-top:10px'><strong>No guarantees:</strong> we do not guarantee outcomes from any practice.</p>"
        "<p style='margin-top:10px'><strong>Copyright:</strong> we publish traditional/public-domain texts and/or our original meanings. If you believe something infringes, contact us.</p>"
        "</div>"
    )
    _write_text(
        DIST / "terms" / "index.html",
        _page_shell(
            cfg=cfg,
            title=f"Terms | {cfg.get('site_name')}",
            description="Terms for using this devotional/educational site.",
            canonical=origin + "/terms/",
            body_html=terms_body,
        ),
    )
    disc_body = (
        "<div class='k'>Legal</div><h1>Disclaimer</h1>"
        "<div class='card' style='margin-top:14px'>"
        "<p>This site is for devotion and education. It does not provide medical, legal, or professional advice.</p>"
        "<p style='margin-top:10px'>Any spiritual benefits described are traditional beliefs and not guaranteed outcomes.</p>"
        "<p style='margin-top:10px'><strong>Safety:</strong> We avoid initiation-required and beej mantras on purpose.</p>"
        "</div>"
    )
    _write_text(
        DIST / "disclaimer" / "index.html",
        _page_shell(
            cfg=cfg,
            title=f"Disclaimer | {cfg.get('site_name')}",
            description="Devotional/educational disclaimer and safety notes.",
            canonical=origin + "/disclaimer/",
            body_html=disc_body,
        ),
    )
    return ["/terms/", "/disclaimer/"]


def _write_security_headers() -> None:
    headers = "\n".join(
        [
            "/*",
            "  X-Content-Type-Options: nosniff",
            "  X-Frame-Options: SAMEORIGIN",
            "  Referrer-Policy: strict-origin-when-cross-origin",
            "  Permissions-Policy: geolocation=(), microphone=(), camera=()",
            "",
            "/data/*",
            "  Cache-Control: public, max-age=300",
            "",
        ]
    )
    _write_text(DIST / "_headers", headers + "\n")


def _copy_static_source(cfg: Mapping[str, Any]) -> None:
    origin = str(cfg["origin"]).rstrip("/")
    old = "https://bhajan.ournakshatra.com"

    def _should_copy(p: Path) -> bool:
        rel = p.relative_to(REPO)
        if rel.parts[0] in (".git", "content", "scripts", "dist"):
            return False
        if rel.suffix in (".docx", ".csv", ".md"):
            return False
        # Legacy root JSON files are ignored; we rebuild data outputs.
        if rel.suffix == ".json" and rel.parts[0] != "data":
            return False
        return True

    for p in REPO.rglob("*"):
        if p.is_dir():
            continue
        if not _should_copy(p):
            continue
        rel = p.relative_to(REPO)
        target = DIST / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        data = p.read_bytes()
        try:
            text = data.decode("utf-8")
        except Exception:
            shutil.copy2(p, target)
            continue
        text = text.replace(old, origin)
        _write_text(target, text)

    # Keep legacy query route as a noindex redirect helper.
    legacy = """<!doctype html><html lang="en"><head><meta charset="utf-8"/><meta name="robots" content="noindex,follow"/><meta name="viewport" content="width=device-width,initial-scale=1"/><title>Redirecting…</title></head>
<body style="font-family:system-ui;padding:24px">
  <p>Redirecting…</p>
  <script>
    const slug = new URLSearchParams(location.search).get('slug');
    if(slug){ location.replace('/bhajan/' + encodeURIComponent(slug) + '/'); }
    else { location.replace('/bhajans.html'); }
  </script>
</body></html>"""
    _write_text(DIST / "bhajan.html", legacy)


def _build_data_files(bhajans: List[Mapping[str, Any]]) -> None:
    (DIST / "data").mkdir(parents=True, exist_ok=True)
    # Copy other pillar JSONs as-is (existing site templates still use them).
    if DATA_DIR.exists():
        for p in DATA_DIR.glob("*.json"):
            shutil.copy2(p, DIST / "data" / p.name)
    # Write bhajans index used by bhajans.html.
    # The existing UI expects fields like timing/topics/composer and an excerpt line.
    out = []
    for b in bhajans:
        timing = b.get("timing") if isinstance(b.get("timing"), list) else []
        topics = b.get("topics") if isinstance(b.get("topics"), list) else []
        tags = b.get("tags") if isinstance(b.get("tags"), list) else []
        # Provide just enough verse structure for the list excerpt UI.
        excerpt_verses = []
        verses = b.get("verses") if isinstance(b.get("verses"), list) else []
        if verses and isinstance(verses[0], Mapping):
            vb = verses[0]
            lines = vb.get("lines") if isinstance(vb.get("lines"), list) else []
            if lines and isinstance(lines[0], Mapping):
                excerpt_verses = [{"lines": [lines[0]]}]
        out.append(
            {
                "id": b.get("id"),
                "slug": b.get("slug"),
                "deity": b.get("deity"),
                "deity_color": b.get("deity_color"),
                "title_hindi": b.get("title_hindi"),
                "title_roman": b.get("title_roman"),
                "title_english": b.get("title_english"),
                "language": b.get("language"),
                "duration_minutes": b.get("duration_minutes"),
                "tags": tags,
                "topics": topics,
                "timing": ", ".join([str(x) for x in timing if str(x).strip()]),
                "composer": b.get("composer") or "Traditional",
                "featured": bool(b.get("featured")),
                "priority": int(b.get("priority") or 0),
                "seo": b.get("seo") if isinstance(b.get("seo"), Mapping) else {},
                "related": b.get("related") if isinstance(b.get("related"), list) else [],
                "verses": excerpt_verses,
            }
        )
    _write_json(DIST / "data" / "bhajans.json", out)


def _build_sitemap(cfg: Mapping[str, Any], paths: List[str]) -> None:
    origin = str(cfg["origin"]).rstrip("/")
    lastmod = _dt.datetime.utcnow().date().isoformat()

    def _url(loc: str, pri: str = "0.7", freq: str = "weekly") -> str:
        return (
            "  <url>\n"
            f"    <loc>{html.escape(origin + loc)}</loc>\n"
            f"    <lastmod>{lastmod}</lastmod>\n"
            f"    <changefreq>{freq}</changefreq>\n"
            f"    <priority>{pri}</priority>\n"
            "  </url>\n"
        )

    base = [
        ("/", "1.0", "daily"),
        ("/bhajans.html", "0.9", "weekly"),
        ("/shlokas.html", "0.9", "weekly"),
        ("/bhagavad-gita.html", "0.8", "weekly"),
        ("/ai-index/", "0.6", "weekly"),
        ("/remedy/", "0.6", "weekly"),
        ("/terms/", "0.2", "monthly"),
        ("/disclaimer/", "0.2", "monthly"),
    ]

    seen = set()
    xml_parts = []
    for loc, pri, freq in base:
        if loc in seen:
            continue
        seen.add(loc)
        xml_parts.append(_url(loc, pri, freq))

    for loc in paths:
        if not loc.startswith("/"):
            continue
        if loc in seen:
            continue
        seen.add(loc)
        xml_parts.append(_url(loc, "0.7", "monthly"))

    xml = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(xml_parts)
        + "</urlset>\n"
    )
    _write_text(DIST / "sitemap.xml", xml)


def _build_robots(cfg: Mapping[str, Any]) -> None:
    origin = str(cfg["origin"]).rstrip("/")
    txt = "\n".join(
        [
            "User-agent: *",
            "Allow: /",
            "",
            "Disallow: /favorites.html",
            "Disallow: /bhajan.html",
            "",
            f"Sitemap: {origin}/sitemap.xml",
            "",
        ]
    )
    _write_text(DIST / "robots.txt", txt + "\n")


def main() -> int:
    cfg = _load_config()
    bhajans = _load_bhajans()
    intents = _load_intents()

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True, exist_ok=True)

    _copy_static_source(cfg)
    _build_data_files(bhajans)

    bhajan_paths = _build_bhajan_pages(cfg, bhajans)
    remedy_paths = _build_remedy_pages(cfg, intents, bhajans)
    legal_paths = _build_legal_pages(cfg)
    ai_paths = _build_ai_files(cfg, extra_urls=bhajan_paths[:10])

    all_paths = bhajan_paths + remedy_paths + legal_paths + ai_paths
    _build_sitemap(cfg, all_paths)
    _build_robots(cfg)
    _write_security_headers()

    print(f"[build] origin={cfg['origin']} bhajans={len(bhajans)} pages={len(all_paths)} dist={DIST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
