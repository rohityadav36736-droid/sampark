import glob
import re

for path in sorted(glob.glob('*.html')):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    nav_match = re.search(r'<nav class="nav-menu">.*?</nav>', content, re.DOTALL)
    drawer_match = re.search(r'<nav class="drawer-nav">.*?</nav>', content, re.DOTALL)
    print(f"=== {path} ===")
    if nav_match:
        print("NAV:", ' '.join(re.findall(r'<a[^>]+>.*?</a>', nav_match.group(), re.DOTALL)))
    else:
        print("NO NAV MENU")
