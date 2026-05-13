import os
import glob

def make_links_relative(directory):
    html_files = glob.glob(os.path.join(directory, '**/*.html'), recursive=True)
    count = 0
    
    replacements = {
        'href="https://bhajan.ournakshatra.com/nakshatra/': 'href="/nakshatra/',
        'href="https://bhajan.ournakshatra.com/rashi/': 'href="/rashi/',
        'href="https://bhajan.ournakshatra.com/planet/': 'href="/planet/',
        'href="https://bhajan.ournakshatra.com/remedy/': 'href="/remedy/',
        'href="https://bhajan.ournakshatra.com/tithi/': 'href="/tithi/',
        'href="https://bhajan.ournakshatra.com/muhurat/': 'href="/muhurat/',
        'href="https://bhajan.ournakshatra.com/shloka/': 'href="/shloka/',
        'href="https://bhajan.ournakshatra.com/about.html"': 'href="/about.html"',
        'href="https://bhajan.ournakshatra.com/contact.html"': 'href="/contact.html"',
        'href="https://bhajan.ournakshatra.com/favorites.html"': 'href="/favorites.html"',
        'href="https://ournakshatra.com/nakshatra/': 'href="/nakshatra/', # fix any lingering ournakshatra.com/nakshatra links
        'href="https://ournakshatra.com/rashi/': 'href="/rashi/',
        'href="https://ournakshatra.com/planet/': 'href="/planet/'
    }

    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        for old, new in replacements.items():
            new_content = new_content.replace(old, new)
            
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f"Updated {file}")
            
    print(f"Done! Updated {count} files.")

if __name__ == '__main__':
    make_links_relative('/Users/prashastpathak/Bhajan')
