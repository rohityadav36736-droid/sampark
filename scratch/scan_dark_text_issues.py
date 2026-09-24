import glob
import re

html_files = sorted(glob.glob('*.html'))

print("Scanning for dark sections and heading colors...")

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        c = fp.read()
    
    # Check if any h1/h2/h3 has dark color inline
    dark_headings = re.findall(r'<h[1-6][^>]*style="[^"]*color:\s*(?:#0|#1|#2|black|var\(--text-main\)|var\(--dark\))[^"]*"[^>]*>', c, re.I)
    if dark_headings:
        print(f"[{f}] Potential dark inline heading: {dark_headings}")
        
    # Check if there are any sections with dark background
    dark_sections = re.findall(r'<section[^>]*style="[^"]*background:\s*(?:#0|#1|rgb\(0|radial-gradient\([^)]*#0)[^"]*"[^>]*>', c, re.I)
    if dark_sections:
        print(f"[{f}] Dark sections count: {len(dark_sections)}")

print("Dark section scan completed.")
