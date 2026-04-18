# Claude Content Operating System (6 Pillars)

This is your daily workflow when you want to add content safely.

## Daily Flow (No Confusion Version)
1. Pick the pillar:
   - Bhajans
   - Shlokas
   - Prayers
   - Bhagavad Gita
   - Upanishads
   - Wisdom
2. Open matching template in `templates/pillar-json/`.
3. Open matching prompt in `prompts/claude/`.
4. Give both to Claude and ask: "Fill this template with source-accurate content only."
5. Paste result into the correct file in `/data/`.
6. Run:
   - `bash scripts/publish_content.sh`
7. If it passes, commit and deploy.

## What Runs Automatically in `publish_content.sh`
- JSON structure validation for all 6 pillar files.
- Restricted mantra scan.
- Regeneration of:
  - `sitemap.xml`
  - `robots.txt`
  - `llms.txt`
  - `ai.txt`

## If Validation Fails
- Fix the exact file mentioned in terminal output.
- Re-run `bash scripts/publish_content.sh`.
- Do not deploy until it passes.
