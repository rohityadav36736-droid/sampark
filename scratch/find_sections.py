import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for idx, line in enumerate(lines):
    if '<section' in line:
        print(f"Line {idx+1}: {line.strip()[:100]}")
    elif 'product' in line.lower() and ('card' in line.lower() or 'grid' in line.lower()):
        print(f"Line {idx+1} [prod]: {line.strip()[:100]}")
