import glob
import re

floating_wa_html = '''  <!-- Fixed Floating Chat on WhatsApp Widget -->
  <a href="https://wa.me/918447777266?text=Hello%20Sampark%20Delhi%2C%20I%20need%20help%20with%20my%20order"
     target="_blank" rel="noopener noreferrer" class="floating-whatsapp" id="floating-whatsapp-btn" aria-label="Chat on WhatsApp">
    <svg viewBox="0 0 24 24"><path d="M12.04 2C6.516 2 2.028 6.488 2.028 12.012c0 1.954.56 3.784 1.536 5.334L2 22l4.81-1.523c1.488.887 3.226 1.385 5.23 1.385 5.524 0 10.012-4.488 10.012-10.012S17.564 2 12.04 2zm5.432 12.382c-.301-.15-1.78-.879-2.056-.98-.275-.1-.475-.15-.675.15-.199.3-.774.98-.949 1.18-.175.2-.349.225-.65.075-.301-.15-1.272-.469-2.423-1.496-.895-.798-1.5-1.784-1.675-2.084-.175-.3-.019-.462.131-.611.136-.134.301-.35.451-.525.15-.175.2-.3.3-.5.1-.2.05-.375-.025-.525-.075-.15-.675-1.628-.925-2.228-.243-.585-.49-.505-.675-.515-.175-.01-.375-.01-.575-.01s-.525.075-.8.375c-.275.3-1.05 1.025-1.05 2.5s1.075 2.899 1.225 3.1c.15.2 2.115 3.23 5.124 4.53.716.31 1.275.495 1.71.634.719.229 1.373.197 1.89.12.576-.086 1.78-.727 2.03-1.428.25-.7.25-1.302.175-1.428-.075-.126-.275-.201-.576-.351z"/></svg>
    <span class="whatsapp-text">Chat on WhatsApp</span>
    <span class="whatsapp-pulse"></span>
  </a>'''

for p in sorted(glob.glob('*.html')):
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()

    filename = p.replace('\\', '/').split('/')[-1]

    # 1. Remove mobile-sticky-bottom-bar completely
    c = re.sub(r'<!-- Mobile Sticky Bottom.*?-->\s*<div class="mobile-sticky-bottom-bar">.*?</div>', '', c, flags=re.DOTALL)
    c = re.sub(r'<div class="mobile-sticky-bottom-bar">.*?</div>', '', c, flags=re.DOTALL)

    # 2. Remove old floating-whatsapp if any
    c = re.sub(r'<!-- Floating WhatsApp.*?-->\s*<a[^>]*class="floating-whatsapp"[^>]*>.*?</a>', '', c, flags=re.DOTALL)
    c = re.sub(r'<a[^>]*class="floating-whatsapp"[^>]*>.*?</a>', '', c, flags=re.DOTALL)

    # 3. In distributorship.html, remove Official Hub Contact Section (screenshot)
    if filename == 'distributorship.html':
        c = re.sub(r'<!-- Official Hub Contact Section -->\s*<section.*?</section>', '', c, flags=re.DOTALL)

    # 4. In index.html, remove delhi-hub-section
    if filename == 'index.html':
        c = re.sub(r'<!-- Sampark Delhi Hub & Experience Center -->\s*<section class="delhi-hub-section".*?</section>', '', c, flags=re.DOTALL)

    # 5. Insert clean floating WhatsApp widget right before toast-container or </body>
    if '<div class="toast-container">' in c:
        c = c.replace('<div class="toast-container">', f'{floating_wa_html}\n\n  <div class="toast-container">')
    elif '</body>' in c:
        c = c.replace('</body>', f'{floating_wa_html}\n</body>')

    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)

    print(f"Updated {filename}")

print("All HTML files cleaned and unified with fixed floating WhatsApp widget!")
