import glob
import re

for p in sorted(glob.glob('*.html')):
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    
    sections = re.findall(r'<section[^>]*style=[\'"][^\'"]*padding:[^;\'"]+[\'"]', c)
    if sections:
        print(f"=== {p} ===")
        for s in sections:
            print("  ", s)
