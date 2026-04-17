# Cloudflare Pages Deployment (Beginner)

This repo is a **static** site. You do not need a VPS.

## 1) Create a Cloudflare Pages project

1. Open Cloudflare dashboard → **Pages**
2. **Create a project** → Connect to GitHub
3. Select this repo: `Prashast-Pathak/Bhajan`

## 2) Build settings

- **Framework preset:** None
- **Build command:** `python3 scripts/build.py`
- **Build output directory:** `dist`

## 3) Set your domain

Recommended for funnel + trust:
- `bhajan.ournakshatra.com`

In Cloudflare Pages → Custom domains:
1. Add `bhajan.ournakshatra.com`
2. Cloudflare will guide DNS setup

## 4) Canonical URLs (important)

This site uses `site.config.json` as the **single source of truth** for canonical origin.

Before going live, confirm:

```json
{
  "origin": "https://bhajan.ournakshatra.com",
  "astrology_origin": "https://ournakshatra.com"
}
```

If you use a different domain, update `origin` and redeploy.

## 5) What gets generated automatically

When you run the build, it generates:
- Clean SEO pages:
  - `/bhajan/<slug>/`
  - `/bhajan/<slug>/story/`
  - `/bhajan/<slug>/benefits/`
  - `/bhajan/<slug>/how-to/`
  - `/bhajan/<slug>/faq/`
  - `/bhajan/<slug>/astrology/`
- Remedy intent pages:
  - `/remedy/<intent>/`
- GEO/AEO discovery:
  - `/ai-index/`, `/ai-index.json`, `/llms.txt`, `/ai.txt`
- SEO infra:
  - `/robots.txt`, `/sitemap.xml`
- Safety headers:
  - `dist/_headers`

## 6) Adding new content (safe workflow)

Add one JSON file per item:
- `content/bhajans/<slug>.json`

Rules enforced by the build:
- `rights.license` must be `traditional|original|permission`
- Beej syllables are blocked (safety)
- Placeholder dashes like `—` as missing values in verse lines are blocked

Then push to GitHub → Cloudflare Pages auto-deploys.
