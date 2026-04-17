# Content Policy (Safety + Copyright)

This repository powers a **static** spiritual content site. We want it to be:

- Safe for readers (no dangerous practices)
- Safe for publishing/monetization (AdSense-friendly)
- Respectful and legally compliant

## 1) Copyright rules (non-negotiable)

We publish only:

- **Traditional/public-domain** texts (e.g., classical stotras, chalisa, aartis), and/or
- **Original** translations/meanings/commentary written by us.

We do **not** publish:

- Modern copyrighted song lyrics (film/album devotional songs, modern bhajan recordings) unless we have explicit permission.

### Required field

Every content item must include a `rights` object:

```json
{
  "rights": { "license": "traditional", "source": "traditional/public domain", "notes": "" }
}
```

Allowed `license` values:
- `traditional` (classical / public domain)
- `original` (our original writing)
- `permission` (explicit permission + proof stored privately)

If `license` is missing or unknown, the build will fail.

## 2) Safety rules (non-negotiable)

We do **not** publish:
- Beej (seed) mantras and related “initiation-required” mantras.
- Any text that claims guaranteed medical/financial/legal outcomes.

### Build-time enforcement

The build script rejects any content that appears to contain common beej syllables (in Devanagari or romanized).

If you really must include something borderline in the future, do not merge it into `content/` without an explicit review.

## 3) Tone rules (AdSense-friendly)

Use soft, respectful phrasing:
- ✅ “Traditionally believed…”, “often recited for spiritual support…”
- ❌ “Guaranteed cure…”, “Will remove disease/bring money 100%…”

