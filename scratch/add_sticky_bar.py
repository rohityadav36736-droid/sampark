import glob

sticky_bar = '''  <!-- Mobile Sticky Bottom Action Bar -->
  <div class="mobile-sticky-bottom-bar">
    <a href="https://wa.me/918447777948?text=Hello%20Sampark%20Delhi%2C%20I%20want%20to%20order%20the%20Smart%20QR%20Tag" target="_blank" class="sticky-whatsapp-btn" aria-label="WhatsApp Us">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
        <path d="M12.031 6.172c-3.181 0-5.767 2.586-5.768 5.766-.001 1.298.38 2.27 1.019 3.287l-.711 2.598 2.669-.699c.969.586 1.961.948 3.287.948 3.181 0 5.767-2.586 5.767-5.766.001-3.18-2.585-5.766-5.766-5.766zm9.969 5.766c0 5.514-4.486 10-10 10-1.823 0-3.539-.49-5.032-1.341l-5.968 1.563 1.591-5.808c-.961-1.554-1.523-3.385-1.523-5.346 0-5.514 4.486-10 10-10 5.514 0 10 4.486 10 10z"/>
      </svg>
      <span>WhatsApp</span>
    </a>
    <a href="products.html" class="sticky-buy-btn">
      <span>⚡ Buy Smart Tag — ₹199</span>
    </a>
  </div>
'''

target_pages = ['products.html', 'product-single.html', 'contact.html', 'track-order.html']

for page in target_pages:
    with open(page, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'mobile-sticky-bottom-bar' not in content:
        content = content.replace('</body>', sticky_bar + '\n</body>')
        with open(page, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Added sticky bar to {page}')
