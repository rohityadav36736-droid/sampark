import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add hero marquee strip right after </section> of hero-slider-section
marquee_html = '''  <!-- Hero Bottom Running Smooth Marquee Ticker (Continuous 60FPS) -->
  <div class="hero-marquee-strip">
    <div class="hero-marquee-track">
      <div class="hero-marquee-item accent-pill"><span>⚡</span> <span>100% Masked Audio Calls</span></div>
      <div class="hero-marquee-item"><span>📷</span> <span>Zero App Needed to Scan</span></div>
      <div class="hero-marquee-item"><span>☀️</span> <span>Heat & 50°C UV Weatherproof</span></div>
      <div class="hero-marquee-item accent-pill"><span>🚨</span> <span>Accident & Towing Collision SOS</span></div>
      <div class="hero-marquee-item"><span>🌟</span> <span>Shark Tank India Season 5 Featured</span></div>
      <div class="hero-marquee-item"><span>🚚</span> <span>Same-Day Dispatch Delhi NCR</span></div>
      <div class="hero-marquee-item accent-pill"><span>🛡️</span> <span>Over 50,000+ Protected Drivers</span></div>
      <div class="hero-marquee-item"><span>🔒</span> <span>Bank-Grade Telecom Privacy Relay</span></div>
      <!-- Loop duplicates -->
      <div class="hero-marquee-item accent-pill"><span>⚡</span> <span>100% Masked Audio Calls</span></div>
      <div class="hero-marquee-item"><span>📷</span> <span>Zero App Needed to Scan</span></div>
      <div class="hero-marquee-item"><span>☀️</span> <span>Heat & 50°C UV Weatherproof</span></div>
      <div class="hero-marquee-item accent-pill"><span>🚨</span> <span>Accident & Towing Collision SOS</span></div>
      <div class="hero-marquee-item"><span>🌟</span> <span>Shark Tank India Season 5 Featured</span></div>
      <div class="hero-marquee-item"><span>🚚</span> <span>Same-Day Dispatch Delhi NCR</span></div>
      <div class="hero-marquee-item accent-pill"><span>🛡️</span> <span>Over 50,000+ Protected Drivers</span></div>
      <div class="hero-marquee-item"><span>🔒</span> <span>Bank-Grade Telecom Privacy Relay</span></div>
    </div>
  </div>
'''

if 'class="hero-marquee-strip"' not in content:
    target = '</section>\n\n  <!-- Feature Trust Strip -->'
    if target in content:
        content = content.replace(target, '</section>\n\n' + marquee_html + '\n  <!-- Feature Trust Strip -->')
        print('Marquee added before feature-strip')
    else:
        # alternate target
        target2 = '</section>'
        first_sec = content.find('class="hero-slider-section"')
        if first_sec != -1:
            end_sec = content.find('</section>', first_sec)
            if end_sec != -1:
                content = content[:end_sec+10] + '\n\n' + marquee_html + content[end_sec+10:]
                print('Marquee added after hero-slider-section')

# 2. Products section: 6 products without ticks (2 rows of 3 on desktop, 3 rows of 2 on mobile)
new_products_grid = '''      <div class="products-grid">

        <!-- Product 1: Car Sampark Tag -->
        <div class="product-card" id="card-car-tag">
          <span class="product-badge-float">🔥 Delhi Bestseller</span>
          <span class="product-badge-discount">60% OFF</span>
          <div class="product-img-wrapper">
            <img src="assets/images/car-tag-hd.jpg" alt="Sampark Car Tag">
          </div>
          <div class="product-details">
            <div class="product-rating">
              <span class="rating-stars">★★★★★</span>
              <span class="rating-count">4.9 (8,420+ Reviews)</span>
            </div>
            <h3 class="product-title">
              <a href="product-single.html?id=car-tag">Sampark Smart Car Tag</a>
            </h3>
            <p class="product-snippet">
              Let people contact you for car parking blocks, vehicle emergencies, or towing warnings with complete privacy.
            </p>
            <div class="product-pricing-row">
              <span class="price-current">₹199</span>
              <span class="price-original">₹499</span>
              <span class="price-save">Save ₹300</span>
            </div>
            <div class="product-action-row">
              <button class="btn btn-outline btn-sm" data-add-cart
                data-id="car-tag"
                data-name="Sampark Smart Car Tag"
                data-price="199"
                data-original="499"
                data-image="assets/images/product-car.jpg">
                Add to Cart
              </button>
              <button class="btn btn-primary btn-sm" data-buy-now
                data-id="car-tag"
                data-name="Sampark Smart Car Tag"
                data-price="199"
                data-original="499"
                data-image="assets/images/product-car.jpg">
                Buy Now
              </button>
            </div>
          </div>
        </div>

        <!-- Product 2: NEW Sampark Pro Elite Tag (NFC + QR) -->
        <div class="product-card" id="card-pro-tag">
          <span class="product-badge-float">⚡ NEW PRO EDITION</span>
          <span class="product-badge-discount">56% OFF</span>
          <div class="product-img-wrapper">
            <img src="assets/images/product-pro-tag.jpg" alt="Sampark Pro Smart Tag">
          </div>
          <div class="product-details">
            <div class="product-rating">
              <span class="rating-stars">★★★★★</span>
              <span class="rating-count">5.0 (1,180+ Reviews)</span>
            </div>
            <h3 class="product-title">
              <a href="product-single.html?id=pro-tag">Sampark Pro Elite Metallic Tag (NFC + QR)</a>
            </h3>
            <p class="product-snippet">
              Flagship smart privacy badge with dual NFC tap + laser QR code. Premium automotive tempered acrylic gloss.
            </p>
            <div class="product-pricing-row">
              <span class="price-current">₹349</span>
              <span class="price-original">₹799</span>
              <span class="price-save">Save ₹450</span>
            </div>
            <div class="product-action-row">
              <button class="btn btn-outline btn-sm" data-add-cart
                data-id="pro-tag"
                data-name="Sampark Pro Elite Metallic Tag"
                data-price="349"
                data-original="799"
                data-image="assets/images/product-pro-tag.jpg">
                Add to Cart
              </button>
              <button class="btn btn-primary btn-sm" data-buy-now
                data-id="pro-tag"
                data-name="Sampark Pro Elite Metallic Tag"
                data-price="349"
                data-original="799"
                data-image="assets/images/product-pro-tag.jpg">
                Buy Now
              </button>
            </div>
          </div>
        </div>

        <!-- Product 3: Commercial & Fleet Tag -->
        <div class="product-card" id="card-fleet-tag">
          <span class="product-badge-float">🚛 Fleet / Commercial</span>
          <span class="product-badge-discount">57% OFF</span>
          <div class="product-img-wrapper">
            <img src="assets/images/product-fleet.jpg" alt="Sampark Fleet Tag">
          </div>
          <div class="product-details">
            <div class="product-rating">
              <span class="rating-stars">★★★★★</span>
              <span class="rating-count">4.8 (2,910+ Reviews)</span>
            </div>
            <h3 class="product-title">
              <a href="product-single.html?id=fleet-tag">Commercial & Fleet Vehicle Tag</a>
            </h3>
            <p class="product-snippet">
              Built for commercial cabs, delivery trucks, school vans, and buses. Dual-manager forwarding and 24/7 routing.
            </p>
            <div class="product-pricing-row">
              <span class="price-current">₹299</span>
              <span class="price-original">₹699</span>
              <span class="price-save">Save ₹400</span>
            </div>
            <div class="product-action-row">
              <button class="btn btn-outline btn-sm" data-add-cart
                data-id="fleet-tag"
                data-name="Commercial & Fleet Vehicle Tag"
                data-price="299"
                data-original="699"
                data-image="assets/images/product-fleet.jpg">
                Add to Cart
              </button>
              <button class="btn btn-primary btn-sm" data-buy-now
                data-id="fleet-tag"
                data-name="Commercial & Fleet Vehicle Tag"
                data-price="299"
                data-original="699"
                data-image="assets/images/product-fleet.jpg">
                Buy Now
              </button>
            </div>
          </div>
        </div>

        <!-- Product 4: Moto & Helmet Tag -->
        <div class="product-card" id="card-bike-tag">
          <span class="product-badge-float">🏍️ Bike & Helmet</span>
          <span class="product-badge-discount">55% OFF</span>
          <div class="product-img-wrapper">
            <img src="assets/images/bike-tag-hd.jpg" alt="Sampark Moto Tag">
          </div>
          <div class="product-details">
            <div class="product-rating">
              <span class="rating-stars">★★★★★</span>
              <span class="rating-count">4.9 (4,180+ Reviews)</span>
            </div>
            <h3 class="product-title">
              <a href="product-single.html?id=bike-tag">Moto & Helmet Emergency Tag</a>
            </h3>
            <p class="product-snippet">
              Compact curved resin badge engineered for two-wheelers, scooter visors, and helmets with crash SOS trigger.
            </p>
            <div class="product-pricing-row">
              <span class="price-current">₹249</span>
              <span class="price-original">₹549</span>
              <span class="price-save">Save ₹300</span>
            </div>
            <div class="product-action-row">
              <button class="btn btn-outline btn-sm" data-add-cart
                data-id="bike-tag"
                data-name="Moto & Helmet Emergency Tag"
                data-price="249"
                data-original="549"
                data-image="assets/images/product-bike.jpg">
                Add to Cart
              </button>
              <button class="btn btn-primary btn-sm" data-buy-now
                data-id="bike-tag"
                data-name="Moto & Helmet Emergency Tag"
                data-price="249"
                data-original="549"
                data-image="assets/images/product-bike.jpg">
                Buy Now
              </button>
            </div>
          </div>
        </div>

        <!-- Product 5: Delhi Family Value Pack -->
        <div class="product-card" id="card-combo-tag">
          <span class="product-badge-float">📦 Family Pack</span>
          <span class="product-badge-discount">63% OFF</span>
          <div class="product-img-wrapper">
            <img src="assets/images/ref-product-gallery.png" alt="Sampark Family Pack">
          </div>
          <div class="product-details">
            <div class="product-rating">
              <span class="rating-stars">★★★★★</span>
              <span class="rating-count">5.0 (1,540+ Reviews)</span>
            </div>
            <h3 class="product-title">
              <a href="product-single.html?id=combo-pack">Delhi Family Combo (2 Cars + 1 Bike)</a>
            </h3>
            <p class="product-snippet">
              Complete vehicle security for the entire family. Manage all 3 tags under a single master mobile dashboard.
            </p>
            <div class="product-pricing-row">
              <span class="price-current">₹449</span>
              <span class="price-original">₹1,199</span>
              <span class="price-save">Save ₹750</span>
            </div>
            <div class="product-action-row">
              <button class="btn btn-outline btn-sm" data-add-cart
                data-id="combo-pack"
                data-name="Delhi Family Combo Pack (2 Cars + 1 Bike)"
                data-price="449"
                data-original="1199"
                data-image="assets/images/ref-product-gallery.png">
                Add to Cart
              </button>
              <button class="btn btn-primary btn-sm" data-buy-now
                data-id="combo-pack"
                data-name="Delhi Family Combo Pack (2 Cars + 1 Bike)"
                data-price="449"
                data-original="1199"
                data-image="assets/images/ref-product-gallery.png">
                Buy Now
              </button>
            </div>
          </div>
        </div>

        <!-- Product 6: Society & Residential Gate Tag -->
        <div class="product-card" id="card-society-tag">
          <span class="product-badge-float">🏢 Society & Gate Pass</span>
          <span class="product-badge-discount">58% OFF</span>
          <div class="product-img-wrapper">
            <img src="assets/images/ref-car-pack-1.png" alt="Sampark Society Tag">
          </div>
          <div class="product-details">
            <div class="product-rating">
              <span class="rating-stars">★★★★★</span>
              <span class="rating-count">4.8 (980+ Reviews)</span>
            </div>
            <h3 class="product-title">
              <a href="product-single.html?id=society-tag">Society & RWA Gate Privacy Tag</a>
            </h3>
            <p class="product-snippet">
              Ideal for gated apartments and corporate parking. Direct guard alert with zero personal phone exposure.
            </p>
            <div class="product-pricing-row">
              <span class="price-current">₹229</span>
              <span class="price-original">₹549</span>
              <span class="price-save">Save ₹320</span>
            </div>
            <div class="product-action-row">
              <button class="btn btn-outline btn-sm" data-add-cart
                data-id="society-tag"
                data-name="Society & RWA Gate Privacy Tag"
                data-price="229"
                data-original="549"
                data-image="assets/images/ref-car-pack-1.png">
                Add to Cart
              </button>
              <button class="btn btn-primary btn-sm" data-buy-now
                data-id="society-tag"
                data-name="Society & RWA Gate Privacy Tag"
                data-price="229"
                data-original="549"
                data-image="assets/images/ref-car-pack-1.png">
                Buy Now
              </button>
            </div>
          </div>
        </div>

      </div>'''

# Replace products grid
match = re.search(r'<div class="products-grid">[\s\S]*?</div>\s*</div>\s*</section>', content)
if match:
    old_section_block = match.group(0)
    new_section_block = new_products_grid + '\n    </div>\n  </section>'
    content = content.replace(old_section_block, new_section_block)
    print('Products grid updated with 6 items (no ticks)!')
else:
    print('Error: products-grid match failed')

# 3. Simulator scenarios matching image 2 (scrollable with hint text)
old_sim_buttons = '''          <div style="display:flex; flex-direction:column; gap:10px; margin-bottom:20px;">
            <button onclick="runSimulator('Car Double Parked', '🚗 Moving Request: Please move your car, parking blocked.')" class="btn btn-outline" style="text-align:left; justify-content:flex-start; border-radius:12px; padding:12px;">
              <span>🚗</span> <strong>Car Double Parked / Move Request</strong>
            </button>
            <button onclick="runSimulator('Headlights Left On', '💡 Car Alert: Your headlamps are switched ON in parking.')" class="btn btn-outline" style="text-align:left; justify-content:flex-start; border-radius:12px; padding:12px;">
              <span>💡</span> <strong>Headlights Left Switched ON</strong>
            </button>
            <button onclick="runSimulator('Tow Truck Warning', '🚨 Urgent Alert: Traffic police tow van is approaching your car.')" class="btn btn-outline" style="text-align:left; justify-content:flex-start; border-radius:12px; padding:12px;">
              <span>🚨</span> <strong>Tow Truck Approaching Warning</strong>
            </button>
            <button onclick="runSimulator('Accident SOS', '⚠️ Emergency: Vehicle involved in minor collision.')" class="btn btn-outline" style="text-align:left; justify-content:flex-start; border-radius:12px; padding:12px;">
              <span>⚠️</span> <strong>Emergency Collision SOS</strong>
            </button>
          </div>'''

new_sim_buttons = '''          <!-- Scroll guide hint for user -->
          <div class="scenarios-scroll-guide">
            <span>👉 <strong>Swipe / Scroll to explore all alert types</strong></span>
            <span class="guide-tag">Scrollable ‹ ›</span>
          </div>

          <!-- Overflow Scrollable Alert Scenarios matching image 2 -->
          <div class="simulator-scenarios-scroll" style="margin-bottom:20px;">
            <button onclick="runSimulator('Car Double Parked', '🚗 Moving Request: Please move your car, parking blocked.')" class="sim-scenario-btn active">
              <span class="scen-icon">🚗</span>
              <span class="scen-text">Car Double Parked / Move Request</span>
            </button>
            <button onclick="runSimulator('Headlights Left On', '💡 Car Alert: Your headlamps are switched ON in parking.')" class="sim-scenario-btn">
              <span class="scen-icon">💡</span>
              <span class="scen-text">Headlights Left Switched ON</span>
            </button>
            <button onclick="runSimulator('Tow Truck Warning', '🚨 Urgent Alert: Traffic police tow van is approaching your car.')" class="sim-scenario-btn">
              <span class="scen-icon">🚨</span>
              <span class="scen-text">Tow Truck Approaching Warning</span>
            </button>
            <button onclick="runSimulator('Accident SOS', '⚠️ Emergency: Vehicle involved in minor collision.')" class="sim-scenario-btn">
              <span class="scen-icon">⚠️</span>
              <span class="scen-text">Emergency Collision SOS</span>
            </button>
            <button onclick="runSimulator('Parking Gate Blocked', '🚧 Notice: Vehicle blocking society entry/exit gate.')" class="sim-scenario-btn">
              <span class="scen-icon">🚧</span>
              <span class="scen-text">Society / Gate Blocked Notice</span>
            </button>
            <button onclick="runSimulator('Window Rolled Down', '🪟 Alert: Vehicle window glass left partially open.')" class="sim-scenario-btn">
              <span class="scen-icon">🪟</span>
              <span class="scen-text">Window Glass Left Open Alert</span>
            </button>
          </div>'''

if old_sim_buttons in content:
    content = content.replace(old_sim_buttons, new_sim_buttons)
    print('Simulator scenarios updated with overflow scroll and hint guide!')
else:
    print('old_sim_buttons not matched exact')

# 4. WhatsApp floating widget: pure icon (no text)
content = re.sub(
    r'<a href="https://wa\.me/918447777266[^"]*"[^>]*class="floating-whatsapp"[^>]*>[\s\S]*?</a>',
    '''  <!-- Fixed Floating Chat on WhatsApp Widget (Pure Icon) -->
  <a href="https://wa.me/918447777266?text=Hello%20Sampark%20Delhi%2C%20I%20have%20a%20question%20about%20smart%20vehicle%20tags."
     target="_blank" rel="noopener noreferrer" class="floating-whatsapp" id="floating-whatsapp-btn" aria-label="Chat on WhatsApp">
    <svg viewBox="0 0 24 24"><path d="M12.04 2C6.516 2 2.028 6.488 2.028 12.012c0 1.954.56 3.784 1.536 5.334L2 22l4.81-1.523c1.488.887 3.226 1.385 5.23 1.385 5.524 0 10.012-4.488 10.012-10.012S17.564 2 12.04 2zm5.432 12.382c-.301-.15-1.78-.879-2.056-.98-.275-.1-.475-.15-.675.15-.199.3-.774.98-.949 1.18-.175.2-.349.225-.65.075-.301-.15-1.272-.469-2.423-1.496-.895-.798-1.5-1.784-1.675-2.084-.175-.3-.019-.462.131-.611.136-.134.301-.35.451-.525.15-.175.2-.3.3-.5.1-.2.05-.375-.025-.525-.075-.15-.675-1.628-.925-2.228-.243-.585-.49-.505-.675-.515-.175-.01-.375-.01-.575-.01s-.525.075-.8.375c-.275.3-1.05 1.025-1.05 2.5s1.075 2.899 1.225 3.1c.15.2 2.115 3.23 5.124 4.53.716.31 1.275.495 1.71.634.719.229 1.373.197 1.89.12.576-.086 1.78-.727 2.03-1.428.25-.7.25-1.302.175-1.428-.075-.126-.275-.201-.576-.351z"/></svg>
    <span class="whatsapp-pulse"></span>
  </a>''',
    content
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('index.html fully updated!')
