import re

for file_name in ['prayers.html', 'shlokas.html', 'wisdom.html', 'upanishads.html']:
    with open(file_name, 'r') as f:
        content = f.read()

    # Find the data variable name: allShlokas, allPrayers, etc.
    data_var_match = re.search(r'let (all\w+) = \[\];', content)
    if not data_var_match:
        continue
    data_var = data_var_match.group(1)

    # 1. Replace initHash assignment
    content = re.sub(
        r'const initHash = window\.location\.hash\.slice\(1\);',
        'const initSlug = window.__PRERENDERED_SLUG__ || new URLSearchParams(window.location.search).get("slug") || window.location.hash.slice(1);',
        content
    )
    
    # 2. Replace hash assignment in wisdom (if any)
    content = re.sub(
        r'const hash = window\.location\.hash\.slice\(1\);',
        'const initSlug = window.__PRERENDERED_SLUG__ || new URLSearchParams(window.location.search).get("slug") || window.location.hash.slice(1);',
        content
    )

    # 3. Replace the if statement
    content = re.sub(r'if \(initHash\) \{', 'if (initSlug) {', content)
    content = re.sub(r'if \(hash\) \{', 'if (initSlug) {', content)

    # 4. Replace the find call
    content = re.sub(
        r'const found = ' + data_var + r'\.find\(s => s\.slug === initHash\);',
        f'const found = {data_var}.find(s => s.slug === initSlug);',
        content
    )
    content = re.sub(
        r'const found = allData\.find\(s => s\.slug === initSlug\);',
        f'const found = {data_var}.find(s => s.slug === initSlug);',
        content
    )
    content = re.sub(
        r'openModal\(hash\)',
        'openModal(initSlug)',
        content
    )

    with open(file_name, 'w') as f:
        f.write(content)
    print(f"Fixed {file_name}")
