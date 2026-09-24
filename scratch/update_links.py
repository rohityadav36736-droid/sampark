import glob

for filename in glob.glob('*.html'):
    if filename == 'shark-tank.html':
        continue
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace('href="index.html#shark-tank"', 'href="shark-tank.html"')
    new_content = new_content.replace('href="#shark-tank"', 'href="shark-tank.html"')

    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {filename}')
