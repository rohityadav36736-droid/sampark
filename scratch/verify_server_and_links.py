import urllib.request
import glob
import re

files = sorted(glob.glob('*.html'))
all_pass = True

print(f"Total HTML files to verify: {len(files)}")
for f in files:
    url = f"http://localhost:8080/{f}"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=5) as resp:
            status = resp.status
            content = resp.read().decode('utf-8', errors='ignore')
            
            nav_match = re.search(r'<nav class="nav-menu">.*?</nav>', content, re.DOTALL)
            has_home = ('Home</a>' in nav_match.group(0)) if nav_match else False
            has_shop = ('shop.html' in nav_match.group(0)) if nav_match else False
            has_quote_bug = 'active>' in content
            
            ok = (status == 200) and has_home and has_shop and (not has_quote_bug)
            if not ok:
                all_pass = False
            
            print(f"{f:22} | HTTP {status} | Home: {has_home} | Shop: {has_shop} | Bug-Free: {not has_quote_bug}")
    except Exception as e:
        all_pass = False
        print(f"{f:22} | EXCEPTION: {e}")

print(f"\nFinal Verification Status: {'ALL PASSED' if all_pass else 'SOME FAILED'}")
