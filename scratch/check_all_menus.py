import glob, re

for f in sorted(glob.glob('*.html')):
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    m = re.search(r'<nav class="nav-menu">.*?</nav>', c, re.DOTALL)
    d = re.search(r'<nav class="drawer-nav">.*?</nav>', c, re.DOTALL)
    broken_m = ('active>' in m.group(0)) if m else False
    broken_d = ('active>' in d.group(0)) if d else False
    print(f"{f:22} | desktop nav: {bool(m)} (broken: {broken_m}) | drawer nav: {bool(d)} (broken: {broken_d})")
