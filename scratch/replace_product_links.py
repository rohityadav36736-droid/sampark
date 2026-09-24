import glob

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    if 'products.html' in c:
        c = c.replace('href="products.html"', 'href="shop.html"')
        # Also clean up any double comments
        c = c.replace('<!-- Desktop Navigation Menu -->\n            <!-- Desktop Navigation Menu -->', '<!-- Desktop Navigation Menu -->')
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(c)
        print(f"Updated {f}")
print("Done!")
