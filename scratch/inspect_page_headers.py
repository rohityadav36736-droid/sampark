import glob
import re

for f in sorted(glob.glob("*.html")):
    c = open(f, encoding="utf-8").read()
    header_m = re.search(r'<header class="site-header">[\s\S]*?</header>', c)
    if header_m:
        print(f"=== {f} ===")
        # Print first 3 lines of header
        for l in header_m.group(0).splitlines()[:5]:
            print("  ", l.strip())
    else:
        print(f"!!! {f} HAS NO SITE-HEADER !!!")
