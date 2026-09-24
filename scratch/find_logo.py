import re

with open('scratch/ref_bundle.js', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for "SAMPARK" or "Sampark"
matches = [m.start() for m in re.finditer(r'SAMPARK', text)]
print(f"Total SAMPARK matches: {len(matches)}")
for idx in matches[:10]:
    print("--- MATCH AT", idx, "---")
    snippet = text[max(0, idx - 100):min(len(text), idx + 200)]
    # print safely without encoding issues
    print(snippet.encode('ascii', errors='replace').decode('ascii'))
