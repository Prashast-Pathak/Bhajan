# Beginner Deployment + Upload Guide (Cloudflare Pages)

This guide assumes you are a complete beginner.

## Part A: Buy Domain (Step-by-Step)
1. Buy domain from Namecheap/Cloudflare Registrar/GoDaddy.
2. Keep registrar login safe.
3. Open Cloudflare and add your domain.
4. Cloudflare gives 2 nameservers.
5. In your registrar panel, replace nameservers with Cloudflare nameservers.
6. Wait until Cloudflare shows domain as Active.

## Part B: Connect GitHub Repo to Cloudflare Pages
1. Push your site repo to GitHub.
2. In Cloudflare Pages: Create Project -> Connect to Git.
3. Select this repo.
4. Build settings for static site:
   - Framework preset: None
   - Build command: (leave empty)
   - Build output directory: `/`
5. Click Deploy.

## Part C: Add Custom Domain
1. Pages project -> Custom domains.
2. Add `yourdomain.com` and `www.yourdomain.com`.
3. Cloudflare auto-creates DNS records.
4. Set one canonical domain (recommended `https://www.yourdomain.com` or root, pick one).

## Part D: Before Every Deploy (Content Upload Checklist)
1. Edit JSON in `/data`.
2. Run:
   - `bash scripts/publish_content.sh`
3. Confirm success.
4. Commit + push.
5. Cloudflare auto-deploys.

## Part E: Update Domain in SEO Files (One-time)
1. Open `config/site.config.json`.
2. Set `base_url` to your final domain.
3. Run:
   - `bash scripts/publish_content.sh`
4. Commit and deploy.

## Part F: How to Work with Claude (Simple)
1. Open one pillar template from `templates/pillar-json/`.
2. Open matching prompt from `prompts/claude/`.
3. In Claude, paste prompt first.
4. Paste template second.
5. Ask: "Return only valid JSON."
6. Paste output to `/data/*.json` and run publish script.

## Part G: Expected Command Outputs

### Command
`bash scripts/publish_content.sh`

### Expected output (success)
- `[1/3] Validating JSON`
- `PASS` lines for all six files
- `[2/3] Generating sitemap/robots/llm crawl files`
- `Generated sitemap.xml, robots.txt, llms.txt, ai.txt`
- `[3/3] Done`

If you see `FAIL`, fix that file and run again.
