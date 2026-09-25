import re, os, glob

# Unified Components Generator
def get_top_announcement():
    return '''  <!-- Top Announcement Bar -->
  <div class="top-announcement">
    <div class="container">
      <div style="display:flex; align-items:center; gap:10px;">
        <span class="top-announcement-pill">🌟 Shark Tank Featured</span>
        <span>Over 50,000+ Vehicles Protected Across Delhi NCR, Noida & Gurugram</span>
      </div>
      <div class="top-announcement-right">
        <a href="track-order.html">Track Order</a>
        <a href="contact.html">Delhi Experience Hub</a>
      </div>
    </div>
  </div>'''

def get_header(active_page):
    active_map = {
        'home': 'active' if active_page == 'home' else '',
        'shop': 'active' if active_page in ['shop', 'products', 'product-single'] else '',
        'shark': 'active' if active_page == 'shark' else '',
        'dist': 'active' if active_page == 'dist' else '',
        'contact': 'active' if active_page == 'contact' else '',
        'account': 'active' if active_page in ['account', 'login', 'signup'] else '',
        'track': 'active' if active_page == 'track' else '',
    }

    return f'''  <!-- Main Sticky Header (Calibrated for Perfect Mobile Display) -->
  <header class="site-header">
    <div class="container header-container">
      <a href="index.html" class="brand-logo" id="header-brand-logo">
        <div class="brand-logo-icon">S</div>
        <div class="brand-logo-text">
          <span class="brand-logo-name">SAMPARK<span class="logo-me-badge">DELHI</span></span>
          <span class="brand-logo-badge">Delhi NCR Safety</span>
        </div>
      </a>

      <!-- Desktop Navigation Menu -->
      <nav class="nav-menu">
        <a href="index.html" class="nav-link {active_map['home']}">Home</a>
        <a href="shop.html" class="nav-link {active_map['shop']}">Shop <span class="nav-tag-badge">TAGS</span></a>
        <a href="shark-tank.html" class="nav-link {active_map['shark']}">Shark Tank</a>
        <a href="distributorship.html" class="nav-link {active_map['dist']}">Distributorship</a>
        <a href="contact.html" class="nav-link {active_map['contact']}">Contact & Hub</a>
        <a href="account.html" class="nav-link {active_map['account']}">My Account</a>
      </nav>

      <!-- Action Buttons -->
      <div class="header-actions">
        <a href="cart.html" class="cart-icon-btn" aria-label="Shopping Cart">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="9" cy="21" r="1"></circle>
            <circle cx="20" cy="21" r="1"></circle>
            <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
          </svg>
          <span class="cart-counter">0</span>
        </a>

        <a href="shop.html" class="header-cta-btn" id="header-cta-buy">
          <span>Buy ₹199</span>
        </a>

        <!-- Mobile Toggle Hamburger -->
        <button class="mobile-toggle" aria-label="Open Mobile Menu" id="mobile-menu-btn">
          <span></span>
          <span></span>
          <span></span>
        </button>
      </div>
    </div>
  </header>

  <!-- Mobile Drawer Overlay -->
  <div class="mobile-drawer" id="mobile-drawer">
    <div class="drawer-content">
      <div class="drawer-header">
        <div class="brand-logo">
          <div class="brand-logo-icon">S</div>
          <div class="brand-logo-text">
            <span class="brand-logo-name">SAMPARK<span class="logo-me-badge">DELHI</span></span>
            <span class="brand-logo-badge">Smart Auto Privacy</span>
          </div>
        </div>
        <button class="drawer-close">&times;</button>
      </div>

      <nav class="drawer-nav">
        <a href="index.html" class="{active_map['home']}">🏠 Home</a>
        <a href="shop.html" class="{active_map['shop']}">🏷️ Shop Smart Tags</a>
        <a href="shark-tank.html" class="{active_map['shark']}">🦈 Shark Tank Pitch</a>
        <a href="distributorship.html" class="{active_map['dist']}">🤝 Distributorship (B2B)</a>
        <a href="contact.html" class="{active_map['contact']}">📍 Contact & Hub</a>
        <a href="track-order.html" class="{active_map['track']}">📦 Track Your Order</a>
        <a href="account.html" class="{active_map['account']}">👤 My Account & Tags</a>
      </nav>

      <div style="margin-top:auto; display:flex; flex-direction:column; gap:8px;">
        <a href="shop.html" class="btn btn-primary btn-block">Order Your Tag Now</a>
        <a href="login.html" class="btn btn-outline btn-block">Driver Login / Signup</a>
      </div>
    </div>
  </div>'''

def get_whatsapp():
    return '''  <!-- Fixed Floating Chat on WhatsApp Widget (Pure Icon) -->
  <a href="https://wa.me/918447777266?text=Hello%20Sampark%20Delhi%2C%20I%20have%20a%20question%20about%20smart%20vehicle%20tags."
     target="_blank" rel="noopener noreferrer" class="floating-whatsapp" id="floating-whatsapp-btn" aria-label="Chat on WhatsApp">
    <svg viewBox="0 0 24 24"><path d="M12.04 2C6.516 2 2.028 6.488 2.028 12.012c0 1.954.56 3.784 1.536 5.334L2 22l4.81-1.523c1.488.887 3.226 1.385 5.23 1.385 5.524 0 10.012-4.488 10.012-10.012S17.564 2 12.04 2zm5.432 12.382c-.301-.15-1.78-.879-2.056-.98-.275-.1-.475-.15-.675.15-.199.3-.774.98-.949 1.18-.175.2-.349.225-.65.075-.301-.15-1.272-.469-2.423-1.496-.895-.798-1.5-1.784-1.675-2.084-.175-.3-.019-.462.131-.611.136-.134.301-.35.451-.525.15-.175.2-.3.3-.5.1-.2.05-.375-.025-.525-.075-.15-.675-1.628-.925-2.228-.243-.585-.49-.505-.675-.515-.175-.01-.375-.01-.575-.01s-.525.075-.8.375c-.275.3-1.05 1.025-1.05 2.5s1.075 2.899 1.225 3.1c.15.2 2.115 3.23 5.124 4.53.716.31 1.275.495 1.71.634.719.229 1.373.197 1.89.12.576-.086 1.78-.727 2.03-1.428.25-.7.25-1.302.175-1.428-.075-.126-.275-.201-.576-.351z"/></svg>
    <span class="whatsapp-pulse"></span>
  </a>'''

pages_meta = {
    'index.html': 'home',
    'shop.html': 'shop',
    'products.html': 'shop',
    'product-single.html': 'shop',
    'shark-tank.html': 'shark',
    'distributorship.html': 'dist',
    'contact.html': 'contact',
    'track-order.html': 'track',
    'cart.html': 'shop',
    'checkout.html': 'shop',
    'account.html': 'account',
    'login.html': 'account',
    'signup.html': 'account',
    'order-success.html': 'home',
}

for fname, page_key in pages_meta.items():
    if not os.path.exists(fname):
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Standardize Header and Top announcement and Drawer
    # Pattern to find from top announcement or site header until after mobile drawer
    # Find start of body
    body_idx = html.find('<body')
    if body_idx != -1:
        body_end = html.find('>', body_idx) + 1
        
        # Find where mobile drawer ends
        drawer_end = html.find('</div>\n  </div>', body_end)
        # Check if mobile-drawer is inside
        if drawer_end != -1 and 'mobile-drawer' in html[body_end:drawer_end+15]:
            end_header_block = drawer_end + len('</div>\n  </div>')
            new_header_block = '\n\n' + get_top_announcement() + '\n\n' + get_header(page_key)
            html = html[:body_end] + new_header_block + html[end_header_block:]
            print(f'Synchronized header & drawer in {fname}')
        else:
            # Alternate search for site-header
            header_start = html.find('<header class="site-header">')
            if header_start != -1:
                # check if top announcement before it
                top_start = html.find('<div class="top-announcement">', body_end)
                replace_start = top_start if top_start != -1 and top_start < header_start else header_start
                # find end of drawer
                drawer_start = html.find('<div class="mobile-drawer"', header_start)
                if drawer_start != -1:
                    d_close = html.find('</div>\n  </div>', drawer_start)
                    if d_close != -1:
                        replace_end = d_close + len('</div>\n  </div>')
                        new_header_block = get_top_announcement() + '\n\n' + get_header(page_key)
                        html = html[:replace_start] + new_header_block + html[replace_end:]
                        print(f'Synchronized header (alt) in {fname}')

    # 2. Standardize WhatsApp button to pure icon
    # Replace any existing floating-whatsapp or fixed-whatsapp-btn
    html = re.sub(
        r'<!--.*?WhatsApp.*?-->\s*<a href="https://wa\.me/[^"]*"[^>]*>[\s\S]*?</a>',
        get_whatsapp(),
        html
    )
    # Also if no comment before it
    if 'id="floating-whatsapp-btn"' not in html:
        # insert before </body>
        html = html.replace('</body>', get_whatsapp() + '\n\n</body>')

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)

print('All pages headers and whatsapp icons synchronized!')
