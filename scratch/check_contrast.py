import glob
import re

print("Checking contrast issues...")
for p in glob.glob('*.html'):
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Check for dark text inside dark sections
    dark_sections = re.findall(r'<section[^>]*class=[\'"][^\'"]*(?:dark|hero-slider)[^\'"]*[\'"][^>]*>.*?</section>', c, re.DOTALL)
    for s in dark_sections:
        bad_texts = re.findall(r'style=[\'"][^\'"]*color:\s*(?:#000|#0F172A|#111|var\(--dark-900\))[^\'"]*[\'"][^>]*>(.*?)<', s)
        if bad_texts:
            print(f"Possible dark text on dark in {p}:", bad_texts[:3])

print("Contrast check done.")
