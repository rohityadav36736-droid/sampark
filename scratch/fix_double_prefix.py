import glob
import re

for p in glob.glob('*.html') + glob.glob('assets/js/*.js') + glob.glob('assets/css/*.css'):
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    
    if '91918447777266' in c or '+91918447777266' in c:
        print(f"Found double country code in {p}, fixing...")
        c = c.replace('+91918447777266', '+918447777266')
        c = c.replace('91918447777266', '918447777266')
        with open(p, 'w', encoding='utf-8') as f:
            f.write(c)

print("Double prefix check complete.")
