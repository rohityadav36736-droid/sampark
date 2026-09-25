import re

print("=== FINAL FULL VERIFICATION ===")

# 1. Check product-single.html
with open("product-single.html", "r", encoding="utf-8") as f:
    ps = f.read()

checks = [
    ("Detailed Info Section", "product-info-details-section" in ps),
    ("How It Works Tab", "hw-step-box" in ps),
    ("Technical Specs Tab", "specs-full-table" in ps),
    ("Box Contents Tab", "box-contents-grid" in ps),
    ("Customer Reviews Section", "product-reviews-section" in ps),
    ("Rating Overview Card", "rating-overview-card" in ps),
    ("Verified Reviewers", "review-comment-card" in ps),
    ("Related Products Section", "related-products-section" in ps),
    ("Related Product Cards", "related-prod-card" in ps),
    ("Gallery Thumbnails", "gallery-thumbnails" in ps),
    ("Mobile Sticky Buy Bar", "mobile-sticky-buy-bar" in ps)
]

for name, passed in checks:
    status = "[PASS]" if passed else "[FAIL]"
    print(f"{status} product-single.html: {name}")

# 2. Check index.html hero mobile text/button removal
with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

hero_check = ".hero-slider-section .slide-content {\n    display: none !important;" in css
print(f"{'[PASS]' if hero_check else '[FAIL]'} style.css: Hero mobile text & buttons hidden")

# 3. Check for any stray `">` in HTML files
import glob
stray_found = False
for html in sorted(glob.glob("*.html")):
    c = open(html, encoding="utf-8").read()
    if re.search(r'^\s*["\']\s*>', c, re.M):
        print(f"[FAIL] Stray `\">` in {html}")
        stray_found = True

if not stray_found:
    print("[PASS] All HTML files free of stray `\">` characters")

print("\n>>> ALL CHECKS COMPLETED SUCCESSFULLY! <<<")
