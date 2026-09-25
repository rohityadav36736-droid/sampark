import glob
import re

print("=== DIAGNOSING ALL 5 ISSUES ===")

# Check Issue 5: Stray "> in HTML files
print("\n--- Check 5: Stray characters near top ---")
for f in sorted(glob.glob("*.html")):
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    head_part = content[:1500]
    for i, line in enumerate(head_part.splitlines()):
        if line.strip() in ['">', '>', '">', '">']:
            print(f"FOUND STRAY in {f} line {i+1}: {repr(line)}")
        elif re.search(r'^\s*["\']\s*>', line):
            print(f"FOUND STRAY PATTERN in {f} line {i+1}: {repr(line)}")

# Also look at favicon lines in all html files:
print("\n--- Favicon lines ---")
for f in sorted(glob.glob("*.html")):
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    for match in re.finditer(r'<link[^>]*rel=["\'](?:shortcut )?icon["\'][^>]*>', content):
        print(f"{f}: {match.group(0)[:80]}")

# Check Issue 1: product-single.html gallery structure and CSS
print("\n--- Check 1: product-single.html gallery ---")
with open("product-single.html", "r", encoding="utf-8") as file:
    ps_content = file.read()
if "gallery-thumbnails" in ps_content:
    print("gallery-thumbnails found in product-single.html")

# Check Issue 2: account.html tag-card-actions
print("\n--- Check 2: account.html tag buttons ---")
with open("account.html", "r", encoding="utf-8") as file:
    acc_content = file.read()
print("tag-card-actions count:", acc_content.count("tag-card-actions"))

# Check Issue 3: interactive tag studio in index.html
print("\n--- Check 3: custom-preview / tag studio in index.html ---")
with open("index.html", "r", encoding="utf-8") as file:
    idx_content = file.read()
for line in idx_content.splitlines():
    if "custom-preview" in line or "Interactive Tag Studio" in line:
        print(line[:100])

# Check Issue 4: marquee reviews white shadow in style.css
print("\n--- Check 4: marquee-reviews white shadow in style.css ---")
with open("assets/css/style.css", "r", encoding="utf-8") as file:
    css_content = file.read()
for i, line in enumerate(css_content.splitlines()):
    if "marquee-reviews-section::before" in line or "marquee-reviews-section::after" in line:
        print(f"line {i+1}: {line}")
