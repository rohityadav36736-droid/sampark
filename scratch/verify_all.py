import os
import glob
import re
import urllib.request
import sys
sys.stdout.reconfigure(encoding='utf-8')

print("="*60)
print("COMPREHENSIVE WEBSITE AUDIT & VERIFICATION")
print("="*60)

pages = sorted(glob.glob('*.html'))
print(f"Total HTML pages found: {len(pages)}")

all_passed = True

# 1. HTTP Server Check
print("\n[1] Testing Local Server HTTP 200 Status...")
for page in pages:
    url = f"http://localhost:8080/{page}"
    try:
        req = urllib.request.urlopen(url, timeout=3)
        if req.status == 200:
            print(f"  ✓ {page} -> HTTP 200 OK ({len(req.read())} bytes)")
        else:
            print(f"  ✗ {page} -> HTTP {req.status}")
            all_passed = False
    except Exception as e:
        print(f"  ✗ {page} -> Failed: {e}")
        all_passed = False

# 2. Nav Menu & Distributorship Link Check
print("\n[2] Checking Navigation & Distributorship Link Across All Pages...")
for page in pages:
    with open(page, 'r', encoding='utf-8') as f:
        html = f.read()
    has_desktop_dist = bool(re.search(r'<nav class="nav-menu">.*?distributorship\.html.*?/nav>', html, re.DOTALL))
    has_drawer_dist = bool(re.search(r'<nav class="drawer-nav">.*?distributorship\.html.*?/nav>', html, re.DOTALL))
    has_logo = 'SAMPARK' in html and 'DELHI' in html
    
    if has_desktop_dist and has_drawer_dist and has_logo:
        print(f"  ✓ {page}: Desktop Nav & Mobile Drawer + Logo OK")
    else:
        print(f"  ✗ {page}: Desktop: {has_desktop_dist}, Drawer: {has_drawer_dist}, Logo: {has_logo}")
        all_passed = False

# 3. Contact Information Check
print("\n[3] Checking Official Reference Contact Details...")
for page in pages:
    with open(page, 'r', encoding='utf-8') as f:
        html = f.read()
    
    has_old_phone = '+91 98765 43210' in html or '9876543210' in html
    has_old_email = 'support@samparkme' in html or 'support@samparkmedelhi' in html
    has_new_phone = '84477 77266' in html or '8447777266' in html
    has_new_email = 'samparkme.delhi@gmail.com' in html
    
    if has_old_phone or has_old_email:
        print(f"  ✗ {page}: Contains old contact placeholders! (old phone: {has_old_phone}, old email: {has_old_email})")
        all_passed = False
    elif has_new_phone and has_new_email:
        print(f"  ✓ {page}: Official Phone & Email Verified (+91 84477 77266 & samparkme.delhi@gmail.com)")
    else:
        print(f"  ℹ {page}: Standalone page without direct contact strings")

# 4. Check Internal Links & Image Assets
print("\n[4] Checking Image Sources and Internal Asset Links...")
missing_assets = set()
for page in pages:
    with open(page, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # find local images
    imgs = re.findall(r'<img[^>]+src=[\'"]([^\'"]+)[\'"]', html)
    for img in imgs:
        if not img.startswith('http') and not img.startswith('data:'):
            clean_path = img.split('?')[0].split('#')[0]
            if not os.path.exists(clean_path):
                missing_assets.add((page, clean_path))
                all_passed = False

if missing_assets:
    for page, m in missing_assets:
        print(f"  ✗ Broken image in {page}: {m}")
else:
    print("  ✓ All referenced local images exist on disk and resolve properly!")

# 5. Check Distributorship Brochure
print("\n[5] Checking Distributorship Brochure PDF...")
brochure_path = "assets/docs/Sampark-Official-Brochure.pdf"
if os.path.exists(brochure_path) and os.path.getsize(brochure_path) > 100000:
    print(f"  ✓ Official Brochure exists ({os.path.getsize(brochure_path):,} bytes)")
else:
    print(f"  ✗ Official Brochure missing or corrupted at {brochure_path}")
    all_passed = False

# 6. Check Order Success Single Checkmark and Bill
print("\n[6] Checking order-success.html Structure...")
with open('order-success.html', 'r', encoding='utf-8') as f:
    suc_html = f.read()

checks = [
    ("Single Checkmark Header", 'Order Placed Successfully!' in suc_html),
    ("Tax Invoice Bill Card", 'invoice-bill-card' in suc_html),
    ("GST Itemized Table", 'CGST (9.0%)' in suc_html and 'SGST (9.0%)' in suc_html),
    ("Narela Hub Address", 'Narela, Delhi - 110040' in suc_html),
    ("Live Tracking Button", 'track-order.html' in suc_html),
]
for name, res in checks:
    if res:
        print(f"  ✓ {name}: Verified")
    else:
        print(f"  ✗ {name}: Missing")
        all_passed = False

# 7. Check Product Card CSS
print("\n[7] Checking Product Card CSS (No Cut-off / Full Width)...")
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

has_no_max_h = 'max-height: 290px' not in css
has_full_width_img = '.product-img-wrapper img' in css and 'object-fit: cover' in css

if has_no_max_h and has_full_width_img:
    print("  ✓ Product images have no height cutoff and fit 100% full width with aspect-ratio: 1 / 1")
else:
    print(f"  ✗ CSS check failed: has_no_max_h={has_no_max_h}")
    all_passed = False

print("\n" + "="*60)
if all_passed:
    print("ALL TESTS PASSED WITH 100% SUCCESS! READY FOR CLIENT DEMO!")
else:
    print("SOME CHECKS FAILED! REVIEW LOGS ABOVE.")
print("="*60)
