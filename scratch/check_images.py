import glob
import re
import os

img_refs = set()
for html in glob.glob('*.html'):
    with open(html, 'r', encoding='utf-8') as f:
        text = f.read()
        matches = re.findall(r'src=["\']([^"\']+\.(?:png|jpg|jpeg|svg|webp))["\']', text)
        for m in matches:
            img_refs.add((html, m))

missing = []
for html, path in img_refs:
    if not path.startswith('http') and not os.path.exists(path):
        missing.append((html, path))

if missing:
    print('Missing images:', missing)
else:
    print('All referenced images exist locally! Total unique paths:', len(img_refs))
