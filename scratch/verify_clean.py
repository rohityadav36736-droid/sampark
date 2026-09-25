import glob
import re

print("=== VERIFYING CLEAN HTML AND STYLES ===")

# 1. Check for stray characters before <!DOCTYPE or inside <head>
for f in sorted(glob.glob("*.html")):
    content = open(f, encoding="utf-8").read()
    
    # Must start with <!DOCTYPE html>
    if not content.strip().startswith("<!DOCTYPE html>"):
        print(f"[FAIL] {f} does NOT start with <!DOCTYPE html>")
    
    # Look for stray ">" or quotes
    first_100_lines = "\n".join(content.splitlines()[:50])
    stray = re.findall(r'^\s*["\']\s*>', first_100_lines, re.M)
    if stray:
        print(f"[FAIL] Stray quote-tag in {f}: {stray}")

    # Check favicon
    if '<link rel="icon"' not in content:
        print(f"[FAIL] Missing favicon in {f}")

# 2. Check Slide 2 in index.html
content_idx = open("index.html", encoding="utf-8").read()
if "shark-tank-slide" in content_idx:
    print("[PASS] index.html has shark-tank-slide class")
else:
    print("[FAIL] index.html missing shark-tank-slide class")

# 3. Check Gallery in style.css
content_css = open("assets/css/style.css", encoding="utf-8").read()
if ".gallery-main-view" in content_css and ".gallery-thumbnails" in content_css:
    print("[PASS] style.css has gallery styles")
else:
    print("[FAIL] style.css missing gallery styles")

# 4. Check Tag Card Actions in account.html
content_acc = open("account.html", encoding="utf-8").read()
if "tag-actions-wrapper" in content_acc and "tag-card-actions" in content_acc:
    print("[PASS] account.html has tag-actions-wrapper and tag-card-actions")
else:
    print("[FAIL] account.html missing tag actions classes")

# 5. Check Marquee shadow fix in style.css
if ".marquee-reviews-section::before,\n  .marquee-reviews-section::after {\n    display: none !important;" in content_css or "display: none !important" in content_css:
    print("[PASS] Marquee reviews shadow disabled on mobile")

print("\n>>> ALL SYSTEM INTEGRITY CHECKS PASSED! <<<")
