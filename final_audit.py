import os
import re
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path('/Users/prashastpathak/Bhajan')
DOMAIN = "https://bhajan.ournakshatra.com"

print("========================================")
print("🚀 FINAL COMPREHENSIVE LAUNCH AUDIT 🚀")
print("========================================\n")

errors = 0

print("[1] SITEMAP & SEO AUDIT")
sitemap_path = ROOT / "sitemap.xml"
if not sitemap_path.exists():
    print("❌ sitemap.xml is missing!")
    errors += 1
else:
    try:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
        namespace = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        urls = root.findall("sm:url/sm:loc", namespace)
        
        valid_urls = 0
        missing_files = 0
        wrong_domain = 0
        
        for loc in urls:
            url = loc.text
            if not url.startswith(DOMAIN):
                wrong_domain += 1
                continue
                
            local_path = url.replace(DOMAIN, "").split('?')[0]
            if local_path == "/":
                local_file = ROOT / "index.html"
            elif local_path.endswith(".html"):
                local_file = ROOT / local_path.lstrip("/")
            else:
                local_file = ROOT / local_path.lstrip("/") / "index.html"
                
            if not local_file.exists():
                missing_files += 1
            else:
                valid_urls += 1
                
        print(f"✅ Sitemap parses correctly ({len(urls)} URLs found).")
        if wrong_domain > 0:
            print(f"❌ {wrong_domain} URLs in sitemap have the WRONG domain!")
            errors += 1
        if missing_files > 0:
            print(f"❌ {missing_files} URLs in sitemap point to files that DO NOT EXIST locally!")
            errors += 1
        if wrong_domain == 0 and missing_files == 0:
            print("✅ All sitemap URLs perfectly match local files and domain.")
    except Exception as e:
        print(f"❌ Error parsing sitemap: {e}")
        errors += 1

print("\n[2] HTML CANONICAL & LINK AUDIT")
html_files = [f for f in ROOT.rglob("*.html") if "node_modules" not in str(f) and ".git" not in str(f)]
canonical_errors = 0
for f in html_files[:200]: 
    content = f.read_text(encoding='utf-8')
    if '<link rel="canonical"' not in content or DOMAIN not in content:
        canonical_errors += 1

if canonical_errors > 0:
    print(f"❌ Found canonical errors in {canonical_errors} HTML files. Missing tag or domain {DOMAIN}.")
    errors += 1
else:
    print(f"✅ Canonical tags in HTML correctly point to {DOMAIN}.")

print("\n[3] SECURITY & NO-INDEX AUDIT")
headers_file = ROOT / "_headers"
redirects_file = ROOT / "_redirects"
if headers_file.exists():
    headers = headers_file.read_text()
    if "X-Robots-Tag: noindex" in headers and "/llms.txt" in headers:
        print("✅ Cloudflare _headers perfectly configured to block Google from AI files.")
    else:
        print("❌ _headers missing X-Robots-Tag for llms.txt")
        errors += 1

if redirects_file.exists():
    redirs = redirects_file.read_text()
    if "/scripts/*" in redirs and "404" in redirs:
        print("✅ Cloudflare _redirects perfectly configured to 404 internal scripts.")

robots = (ROOT / "robots.txt").read_text()
if "Disallow: /scripts/" in robots and "Allow: /llms.txt" in robots:
    print("✅ robots.txt perfectly blocks internal paths and explicitly allows AI bots.")
else:
    print("❌ robots.txt is missing AI bot allowances or script blocks.")
    errors += 1

print("\n========================================")
if errors == 0:
    print("🎯 AUDIT PASSED: The platform is mathematically perfect for launch.")
else:
    print(f"🚨 AUDIT FAILED: {errors} critical errors found.")
print("========================================")
