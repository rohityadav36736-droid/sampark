import re

with open('scratch/ref_bundle.js', 'r', encoding='utf-8') as f:
    bundle = f.read()

# Look for logo components or markup
logos = re.findall(r'.{0,100}(?:logo|Logo).{0,100}', bundle)
print(f"Total logo mentions: {len(logos)}")
for l in logos[:15]:
    print("---", l.strip())

# Look for image urls
img_urls = set(re.findall(r'https?://[^\s"\'<>]+?\.(?:png|jpg|jpeg|svg|webp)', bundle))
print("\nExternal image URLs:")
for u in img_urls:
    print(u)

# Look for relative /assets/
rel_assets = set(re.findall(r'/assets/[^"\'\s]+\.(?:png|jpg|jpeg|svg|webp|pdf)', bundle))
print("\nRelative assets:")
for a in rel_assets:
    print(a)
