import re

with open('scratch/ref_bundle.js', 'r', encoding='utf-8') as f:
    text = f.read()

imgs = re.finditer(r'https://i\.ibb\.co/[^\s"\'`]+', text)
for match in imgs:
    start = max(0, match.start() - 150)
    end = min(len(text), match.end() + 150)
    print("URL:", match.group())
    print("CONTEXT:", text[start:end])
    print("="*60)
