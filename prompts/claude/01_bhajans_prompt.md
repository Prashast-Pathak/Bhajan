# Claude Prompt: Bhajans JSON Writer

Task: Fill `templates/pillar-json/bhajans.template.json` format.

Writing style:
- Emotional, devotional, human, clear.
- Explain story and significance in plain language.
- Benefits must be non-guarantee devotional phrasing.

Mandatory checks:
- `verses[].lines[]` must include `hindi`, `roman`, `hindi_meaning`, `english`.
- `seo` fields must be short and natural.
- `slug` must be lowercase-hyphen style.

Output: valid JSON array only.
