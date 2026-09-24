import glob
import re

for p in sorted(glob.glob('*.html')):
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # check for bottom fixed / sticky bars
    sticky = re.findall(r'<div[^>]*class=[\'"][^\'"]*(?:sticky|floating|bottom)[^\'"]*[\'"][^>]*>.*?</div\s*>', c, re.DOTALL)
    print(f"=== {p} ===")
    if sticky:
        for s in sticky:
            print("STICKY/BOTTOM ELEMENT:", s[:150].replace('\n', ' '))
    else:
        print("No sticky/bottom elements found")
