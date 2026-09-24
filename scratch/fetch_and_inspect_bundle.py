import urllib.request
import re

url = 'https://samparkmedelhi.com/assets/index-cx2jKWsA.js'
print('Fetching JS bundle...')
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req, timeout=15).read().decode('utf-8')

with open('scratch/ref_bundle.js', 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Saved bundle ({len(content)} chars). Inspecting...')

# Look for logo
for line in content.split(';'):
    if 'logo' in line.lower() and len(line) < 300:
        print('LOGO MENTION:', line.strip())

# Look for images and svg
imgs = set(re.findall(r'https?://[^\s"\'<>]+\.(?:png|jpg|jpeg|svg|webp)', content))
print('\nExternal images:')
for img in imgs:
    print(img)

rel = set(re.findall(r'/assets/[a-zA-Z0-9_-]+\.(?:png|jpg|jpeg|svg|webp|pdf)', content))
print('\nRelative assets:')
for r in rel:
    print(r)
