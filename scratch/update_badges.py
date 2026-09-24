import glob

for path in glob.glob('*.html'):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if '<span>ME</span>' in content:
        content = content.replace('<span>ME</span>', '<span class="logo-me-badge">ME</span>')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Updated logo badge in {path}')
