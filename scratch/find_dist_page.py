import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/ref_bundle.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Find route definition
m = re.search(r'path:\s*["\']/?distributorship["\'],\s*element:\s*([^,}]+)', text)
if m:
    print("Element:", m.group(1))

# Or find text that appears on distributorship page
for word in ["distributor", "tier", "50 units", "wholesale", "Starter Pack"]:
    matches = [i.start() for i in re.finditer(word, text, re.IGNORECASE)]
    print(f"Matches for '{word}':", len(matches))
    if matches:
        snippet = text[max(0, matches[0] - 100):min(len(text), matches[0] + 500)]
        print(f"--- First snippet for '{word}':\n", snippet[:300])
