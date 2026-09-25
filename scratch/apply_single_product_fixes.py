import re

with open('product-single.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add '● One time purchase, COD Available' below price block
target_price = '''          <div class="price-block">
            <span class="price-current">₹199</span>
            <span class="price-original">₹499</span>
            <span class="price-save">60% OFF Today</span>
          </div>'''

new_price_block = '''          <div class="price-block">
            <span class="price-current">₹199</span>
            <span class="price-original">₹499</span>
            <span class="price-save">60% OFF Today</span>
          </div>

          <!-- Feature Tag from Image 2 -->
          <div style="display:flex; align-items:center; gap:8px; margin: 10px 0 16px 0; font-size:0.86rem; font-weight:700; color:#1E293B;">
            <span style="color:#FFCC00; font-size:1.15rem; line-height:1;">●</span>
            <span>One time purchase, COD Available</span>
          </div>'''

if target_price in content:
    content = content.replace(target_price, new_price_block)
    print("Added 'One time purchase' badge to product-single.html")

# 2. Add the 9 Feature Icons Grid and Specifications Card right after Guarantee Highlights
features_and_specs_html = '''          <!-- 9 Feature Icons Grid Card Matching Image 2 -->
          <div class="product-features-grid-card">
            <div class="feature-grid-item">
              <div class="feature-grid-icon icon-blue">📞</div>
              <div class="feature-grid-label">Masked Audio Calls</div>
            </div>
            <div class="feature-grid-item">
              <div class="feature-grid-icon icon-green">💬</div>
              <div class="feature-grid-label">WhatsApp Notifications</div>
            </div>
            <div class="feature-grid-item">
              <div class="feature-grid-icon icon-red">📄</div>
              <div class="feature-grid-label">PDF Tag (Offline)</div>
            </div>
            <div class="feature-grid-item">
              <div class="feature-grid-icon icon-purple">📹</div>
              <div class="feature-grid-label">Masked Video Calls</div>
            </div>
            <div class="feature-grid-item">
              <div class="feature-grid-icon icon-teal">🔄</div>
              <div class="feature-grid-label">Call Back Caller</div>
            </div>
            <div class="feature-grid-item">
              <div class="feature-grid-icon icon-green2">📍</div>
              <div class="feature-grid-label">Check Location</div>
            </div>
            <div class="feature-grid-item">
              <div class="feature-grid-icon icon-orange">💬</div>
              <div class="feature-grid-label">Offline SMS Available</div>
            </div>
            <div class="feature-grid-item">
              <div class="feature-grid-icon icon-red2">🎧</div>
              <div class="feature-grid-label">Live Support Always</div>
            </div>
            <div class="feature-grid-item">
              <div class="feature-grid-icon icon-orange2">🔔</div>
              <div class="feature-grid-label">Emergency Alerts</div>
            </div>
          </div>

          <!-- Specifications Card Matching Image 2 -->
          <div class="product-specs-card">
            <h3>Specifications</h3>
            <div class="specs-table">
              <div class="specs-row">
                <span class="specs-label">Material</span>
                <span class="specs-value">Premium Waterproof PVC</span>
              </div>
              <div class="specs-row">
                <span class="specs-label">Size</span>
                <span class="specs-value">Standard (fits all vehicles)</span>
              </div>
              <div class="specs-row">
                <span class="specs-label">Warranty</span>
                <span class="specs-value">1 Year Replacement</span>
              </div>
            </div>

            <div class="specs-highlight-bullet">
              <span style="color:#FFCC00; font-size:1.1rem; line-height:1;">●</span>
              <span>Get updates about your parked vehicle on your phone, WhatsApp and Masked call. Buy the One Time Pack Now.</span>
            </div>

            <div class="specs-checklist">
              <div class="checklist-item">☑️ Masked Audio and Video Call</div>
              <div class="checklist-item">☑️ SMS And WhatsApp</div>
              <div class="checklist-item">☑️ Manage your tag from the APP</div>
              <div class="checklist-item">☑️ One time purchase, COD Available</div>
            </div>

            <div class="specs-community-note">
              <p>They Cant see your phone number ⭐</p>
              <p>The Tag will help you keep your vehicle out of danger while its in parking.</p>
              <p>Anyone getting bothered will be able to contact you easily.</p>
              <p>Join our 1M User Community,</p>
              <p><strong>Lets Make India Great !</strong></p>
            </div>
          </div>'''

target_guarantee = '''          <!-- Guarantee Highlights -->
          <div style="border-top:1px solid var(--border-light); padding-top:16px; display:grid; grid-template-columns:1fr 1fr; gap:10px;">
            <div style="font-size:0.8rem; color:#475569; font-weight:600;">
              🛡️ 100% Privacy Calling Proxy
            </div>
            <div style="font-size:0.8rem; color:#475569; font-weight:600;">
              🌦️ All-Weather Heat & Rainproof
            </div>
            <div style="font-size:0.8rem; color:#475569; font-weight:600;">
              📱 Zero App Needed for Scanners
            </div>
            <div style="font-size:0.8rem; color:#475569; font-weight:600;">
              ♾️ Lifetime Cloud Connectivity
            </div>
          </div>'''

if target_guarantee in content:
    content = content.replace(target_guarantee, target_guarantee + '\n\n' + features_and_specs_html)
    print("Added 9 Features Grid & Specifications Card to product-single.html")

# 3. Add Sticky Mobile Buy Bar before </body>
sticky_buy_bar_html = '''  <!-- Sticky Bottom Buy Bar on Mobile (Matching Image 2) -->
  <div class="mobile-sticky-buy-bar">
    <div class="buy-bar-price">
      <div class="price-val" id="mobile-buy-bar-price">₹199</div>
      <div class="price-sub">Cash on Delivery</div>
    </div>
    <button class="buy-bar-btn" id="mobile-sticky-buy-btn">
      BUY NOW
    </button>
  </div>'''

if 'class="mobile-sticky-buy-bar"' not in content:
    content = content.replace('</body>', sticky_buy_bar_html + '\n\n</body>')
    print("Added mobile sticky buy bar to product-single.html")

# 4. Wire the sticky buy button in script
script_sync = '''    document.getElementById('mobile-sticky-buy-btn').addEventListener('click', () => {
      document.getElementById('buy-now-page-btn').click();
    });'''

if 'mobile-sticky-buy-btn' not in content:
    pass
else:
    if 'document.getElementById(\'mobile-sticky-buy-btn\')' not in content:
        content = content.replace('window.location.href = \'checkout.html\';\n    });', 'window.location.href = \'checkout.html\';\n    });\n\n' + script_sync)
        # Also update mobile-buy-bar-price when currentProd is set
        content = content.replace('if (priceDisplay) priceDisplay.textContent = \'₹\' + currentProd.price;', 'if (priceDisplay) priceDisplay.textContent = \'₹\' + currentProd.price;\n    const mobilePriceEl = document.getElementById(\'mobile-buy-bar-price\');\n    if (mobilePriceEl) mobilePriceEl.textContent = \'₹\' + currentProd.price;')

with open('product-single.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("product-single.html updated completely!")
