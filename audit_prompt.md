# 🕉️ Sanatan Gyan Sagar — Comprehensive Audit & Verification Prompt

**Role**: You are a Senior Spiritual Data Auditor and Full-Stack Quality Engineer.
**Context**: You are auditing "सनातन ज्ञान सागर" (Sanatan Gyan Sagar), a spiritual library platform.
**Goal**: Ensure the platform is 100% functional, content-complete, and spiritually safe for the public.

---

## 1. Spiritual Safety & Content Integrity Audit
- **Beej Mantra Check**: Scan all Devanagari and Roman lyrics. Identify and flag any "Beej Mantras" (seed sounds) intended only for initiated practitioners.
  - *Restricted List*: Hreem (ह्रीं), Shreem (श्रीं), Kleem (क्लीं), Aim (ऐं), Hum (हूँ), Phat (फट्), etc.
  - *Action*: These must be removed or replaced with devotional descriptors.
- **Prescriptive Language Check**: Ensure no content makes deterministic health or fortune-telling claims (e.g., "This mantra cures cancer" or "Reciting this guaranteed wealth").
  - *Language Standard*: Change to "Devotees believe...", "Traditionally recited for...", or "Said to inspire...".
- **Sanskrit Accuracy**: Cross-verify core mantras (Gayatri, Mahamrityunjaya, Hanuman Chalisa) against authentic Vedic/Pauranic sources. Match line breaks and pauses (| and ||).

## 2. Technical Infrastructure Audit
- **Data Fetches**: Verify that every `.html` page uses absolute paths to fetch JSON data from the `/data/` directory (not relative root). 
  - *Correct*: `fetch('/data/bhajans.json')`
- **Field Mappings**: Ensure JS logic attributes match JSON keys (e.g., `s.hindi` vs `s.hindi_meaning`).
- **PWA Readiness**: 
  - [ ] Is `manifest.json` linked in the `<head>` of EVERY page?
  - [ ] Is `sw.js` (Service Worker) registered in the `<head>` of EVERY page?
  - [ ] Does the Service Worker cache all 6 content JSON files?

## 3. PRD Milestone Verification
- **Bhajans (15 Target)**: verify `data/bhajans.json` contains exactly 15 items.
- **Wisdom (12 Topics)**: verify `data/wisdom.json` contains: Anxiety, Failure, Death, Love, Anger, Success, Patience, Grief, Fear, Duty, **Morning**, and **Forgiveness**.
- **Gita Presence**: Check if Chapter 1 (47 verses) and Chapter 2 (72 verses) are fully present with translations.

## 4. UI/UX "Perfection" Check
- **Faulty Links**: Check the bottom nav and header nav on every page. No 404s.
- **Mobile Targets**: Ensure all buttons (Close, Save, Share) are at least 44x44px.
- **Hindi Display**: Verify default font size for Devnagari is 22px (`--hindi-size`).

---

**Output Requirement**: Provide a "Pass/Fail/Fix" report for every item above. If "Fix", provide the exact code or JSON snippet required to resolve it.
