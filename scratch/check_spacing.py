import glob
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

for p in sorted(glob.glob('*.html')):
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # check min-height or large paddings
    min_h = re.findall(r'min-height:[^;\'"]+', c)
    large_pads = re.findall(r'padding(?:-bottom|-top)?:\s*(?:[89]\d|1\d\d)px', c)
    footer_m = re.findall(r'margin-bottom:\s*(?:[5-9]\d|1\d\d)px', c)
    
    print(f"=== {p} ===")
    if min_h: print("  min-height:", min_h)
    if large_pads: print("  large padding:", set(large_pads))
    if footer_m: print("  large margin:", set(footer_m))
