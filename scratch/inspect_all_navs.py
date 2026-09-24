import glob
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

for p in sorted(glob.glob('*.html')):
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    
    desktop_nav = re.search(r'<nav class="nav-menu">.*?</nav>', c, re.DOTALL)
    drawer_nav = re.search(r'<nav class="drawer-nav">.*?</nav>', c, re.DOTALL)
    
    print(f"=== {p} ===")
    if desktop_nav:
        print("Desktop:", desktop_nav.group().replace('\n', ' '))
    if drawer_nav:
        print("Drawer:", drawer_nav.group().replace('\n', ' '))
