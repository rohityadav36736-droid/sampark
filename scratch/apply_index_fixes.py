import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace hero-marquee-strip and feature-strip with feature-cards-marquee-section
feature_marquee_html = '''  <!-- Infinite Running Feature Cards Marquee Strip (Matching Image 3) -->
  <section class="feature-cards-marquee-section">
    <div class="feature-marquee-container">
      <div class="feature-marquee-track">
        <!-- 4 Feature Cards -->
        <div class="feature-marquee-card">
          <div class="feature-card-icon">🔒</div>
          <div class="feature-card-info">
            <h4>100% Masked Audio Calls</h4>
            <p>Your actual phone number is never exposed to strangers.</p>
          </div>
        </div>

        <div class="feature-marquee-card">
          <div class="feature-card-icon">📷</div>
          <div class="feature-card-info">
            <h4>Zero App Needed to Scan</h4>
            <p>Scannable with any native iPhone or Android camera.</p>
          </div>
        </div>

        <div class="feature-marquee-card">
          <div class="feature-card-icon">☀️</div>
          <div class="feature-card-info">
            <h4>Heat & UV Weatherproof</h4>
            <p>Engineered for 50°C Delhi heatwaves and heavy monsoons.</p>
          </div>
        </div>

        <div class="feature-marquee-card">
          <div class="feature-card-icon">🚨</div>
          <div class="feature-card-info">
            <h4>Emergency SOS Alerts</h4>
            <p>One-tap emergency broadcast to your family members.</p>
          </div>
        </div>

        <!-- Loop Duplicates for Smooth Infinite 60FPS Flow -->
        <div class="feature-marquee-card">
          <div class="feature-card-icon">🔒</div>
          <div class="feature-card-info">
            <h4>100% Masked Audio Calls</h4>
            <p>Your actual phone number is never exposed to strangers.</p>
          </div>
        </div>

        <div class="feature-marquee-card">
          <div class="feature-card-icon">📷</div>
          <div class="feature-card-info">
            <h4>Zero App Needed to Scan</h4>
            <p>Scannable with any native iPhone or Android camera.</p>
          </div>
        </div>

        <div class="feature-marquee-card">
          <div class="feature-card-icon">☀️</div>
          <div class="feature-card-info">
            <h4>Heat & UV Weatherproof</h4>
            <p>Engineered for 50°C Delhi heatwaves and heavy monsoons.</p>
          </div>
        </div>

        <div class="feature-marquee-card">
          <div class="feature-card-icon">🚨</div>
          <div class="feature-card-info">
            <h4>Emergency SOS Alerts</h4>
            <p>One-tap emergency broadcast to your family members.</p>
          </div>
        </div>
      </div>
    </div>
  </section>'''

# Find from hero-marquee-strip until end of feature-strip
pattern_strip = r'<!-- Hero Bottom Running Smooth Marquee[\s\S]*?<!-- Feature Trust Strip -->[\s\S]*?</section>'
if re.search(pattern_strip, content):
    content = re.sub(pattern_strip, feature_marquee_html, content)
    print("Replaced marquee and feature strip with running feature card marquee!")
else:
    print("pattern_strip not found exact, trying alternate search")
    # try replacing hero-marquee-strip and feature-strip individually
    content = re.sub(r'<div class="hero-marquee-strip">[\s\S]*?</div>\s*</div>', '', content)
    content = re.sub(r'<section class="feature-strip">[\s\S]*?</section>', feature_marquee_html, content)
    print("Alternate replace completed for feature strip")

# 2. Make all product images in index.html clickable links
product_image_links = [
    ('id="card-car-tag"', 'assets/images/car-tag-hd.jpg', 'car-tag'),
    ('id="card-pro-tag"', 'assets/images/product-pro-tag.jpg', 'pro-tag'),
    ('id="card-fleet-tag"', 'assets/images/product-fleet.jpg', 'fleet-tag'),
    ('id="card-bike-tag"', 'assets/images/bike-tag-hd.jpg', 'bike-tag'),
    ('id="card-combo-tag"', 'assets/images/ref-product-gallery.png', 'combo-pack'),
    ('id="card-society-tag"', 'assets/images/ref-car-pack-1.png', 'society-tag'),
]

for card_id, img_src, prod_param in product_image_links:
    old_div = f'<div class="product-img-wrapper">\n            <img src="{img_src}"'
    new_a = f'<a href="product-single.html?id={prod_param}" class="product-img-wrapper" title="View Product Details">\n            <img src="{img_src}"'
    if old_div in content:
        content = content.replace(old_div, new_a)
        # also close tag
        # Find where this block closes </div> before <div class="product-details">
        print(f"Made image clickable for {prod_param}")

# Also replace closing div of product-img-wrapper with </a>
content = re.sub(
    r'(<a href="product-single\.html\?id=[^"]*" class="product-img-wrapper"[^>]*>\s*<img [^>]*>)\s*</div>',
    r'\1\n          </a>',
    content
)

# 3. Reset Simulator Section to exact clean desktop format + clean mobile format (Point 4)
simulator_html = '''        <!-- Controls Column (Original clean desktop & responsive layout) -->
        <div>
          <h3 style="font-size:1.3rem; margin-bottom:12px;">Choose a Scenario to Test:</h3>
          <p style="color:var(--text-muted); font-size:0.88rem; margin-bottom:18px;">
            Imagine your car is parked at a crowded Delhi metro or mall parking lot. Select what the person scanning your tag wants to say:
          </p>

          <div style="display:flex; flex-direction:column; gap:10px; margin-bottom:20px;">
            <button onclick="runSimulator('Car Double Parked', '🚗 Moving Request: Please move your car, parking blocked.')" class="btn btn-outline sim-scenario-btn active" style="text-align:left; justify-content:flex-start; border-radius:12px; padding:12px; display:flex; align-items:center; gap:12px; width:100%;">
              <span style="font-size:1.3rem;">🚗</span> <strong style="color:var(--dark-900);">Car Double Parked / Move Request</strong>
            </button>
            <button onclick="runSimulator('Headlights Left On', '💡 Car Alert: Your headlamps are switched ON in parking.')" class="btn btn-outline sim-scenario-btn" style="text-align:left; justify-content:flex-start; border-radius:12px; padding:12px; display:flex; align-items:center; gap:12px; width:100%;">
              <span style="font-size:1.3rem;">💡</span> <strong style="color:var(--dark-900);">Headlights Left Switched ON</strong>
            </button>
            <button onclick="runSimulator('Tow Truck Warning', '🚨 Urgent Alert: Traffic police tow van is approaching your car.')" class="btn btn-outline sim-scenario-btn" style="text-align:left; justify-content:flex-start; border-radius:12px; padding:12px; display:flex; align-items:center; gap:12px; width:100%;">
              <span style="font-size:1.3rem;">🚨</span> <strong style="color:var(--dark-900);">Tow Truck Approaching Warning</strong>
            </button>
            <button onclick="runSimulator('Accident SOS', '⚠️ Emergency: Vehicle involved in minor collision.')" class="btn btn-outline sim-scenario-btn" style="text-align:left; justify-content:flex-start; border-radius:12px; padding:12px; display:flex; align-items:center; gap:12px; width:100%;">
              <span style="font-size:1.3rem;">⚠️</span> <strong style="color:var(--dark-900);">Emergency Collision SOS</strong>
            </button>
          </div>

          <div style="background:#ECFDF5; border:1px solid #10B981; border-radius:10px; padding:12px; font-size:0.82rem; color:#065F46;">
            🔒 <strong>The Result:</strong> The scanner clicks "Call Owner". Sampark's cloud proxy dials your phone. Neither party can view the other's real phone number!
          </div>
        </div>'''

pattern_sim = r'<!-- Controls Column -->[\s\S]*?<!-- Simulated Phone Screen Column -->'
if re.search(pattern_sim, content):
    content = re.sub(pattern_sim, simulator_html + '\n\n        <!-- Simulated Phone Screen Column -->', content)
    print("Simulator section restored to clean desktop layout!")

# 4. Comparison Table (Image 1 fix - no cutoff on mobile)
table_pattern = r'<div style="background:#FFFFFF; border:1px solid var\(--border-light\); border-radius:var\(--radius-xl\); overflow-x:auto; box-shadow:var\(--shadow-sm\);">\s*<table style="width:100%; min-width:620px; border-collapse:collapse; text-align:left; font-size:0.9rem;">'
table_replacement = '<div class="comparison-table-wrapper">\n        <table class="comparison-table">'
if re.search(table_pattern, content):
    content = re.sub(table_pattern, table_replacement, content)
    print("Comparison table updated to responsive class!")
else:
    # search more broadly
    content = re.sub(r'min-width:620px;', '', content)
    content = content.replace('<table style="width:100%;', '<table class="comparison-table" style="width:100%;')
    print("Removed min-width 620px from table")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("index.html successfully updated!")
