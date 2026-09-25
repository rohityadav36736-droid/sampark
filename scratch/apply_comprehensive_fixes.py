import re

print("=== Starting Comprehensive Final Polish & Bugfix Script ===")

# -------------------------------------------------------------
# 1. Update product-single.html
# -------------------------------------------------------------
with open("product-single.html", "r", encoding="utf-8") as f:
    ps_content = f.read()

# Fix script price selectors and ensure mobile buy button is wired correctly
# In script:
# Replace:
#   const priceDisplay = document.querySelector('.current-price');
#   if (priceDisplay) priceDisplay.textContent = '₹' + currentProd.price;
#   const mobilePriceEl = document.getElementById('mobile-buy-bar-price');
#   if (mobilePriceEl) mobilePriceEl.textContent = '₹' + currentProd.price;
#   const origDisplay = document.querySelector('.original-price');
#   if (origDisplay) origDisplay.textContent = '₹' + currentProd.originalPrice;

old_script_block = """    const priceDisplay = document.querySelector('.current-price');
    if (priceDisplay) priceDisplay.textContent = '₹' + currentProd.price;
    const mobilePriceEl = document.getElementById('mobile-buy-bar-price');
    if (mobilePriceEl) mobilePriceEl.textContent = '₹' + currentProd.price;
    const origDisplay = document.querySelector('.original-price');
    if (origDisplay) origDisplay.textContent = '₹' + currentProd.originalPrice;"""

new_script_block = """    const priceDisplay = document.querySelector('.price-current');
    if (priceDisplay) priceDisplay.textContent = '₹' + currentProd.price;
    const mobilePriceEl = document.getElementById('mobile-buy-bar-price');
    if (mobilePriceEl) mobilePriceEl.textContent = '₹' + currentProd.price;
    const origDisplay = document.querySelector('.price-original');
    if (origDisplay) origDisplay.textContent = '₹' + currentProd.originalPrice;"""

if old_script_block in ps_content:
    ps_content = ps_content.replace(old_script_block, new_script_block)
    print("Fixed price selectors in product-single.html script")

# Move the mobile sticky buy bar to appear BEFORE the script, right above </body>
sticky_bar_html = """  <!-- Sticky Bottom Buy Bar on Mobile (Matching Image 2) -->
  <div class="mobile-sticky-buy-bar" id="mobile-sticky-buy-bar">
    <div class="buy-bar-price">
      <div class="price-val" id="mobile-buy-bar-price">₹199</div>
      <div class="price-sub">Cash on Delivery</div>
    </div>
    <button class="buy-bar-btn" id="mobile-sticky-buy-btn" type="button">
      BUY NOW
    </button>
  </div>"""

# Remove existing sticky bar if present at bottom
ps_content = re.sub(r'<!-- Sticky Bottom Buy Bar on Mobile[\s\S]*?</div>\s*</div>\s*(?=</body>)', '', ps_content)

# Insert sticky bar before </script>
insert_before_script = sticky_bar_html + "\n\n  <script>"
ps_content = ps_content.replace("  <script>", insert_before_script, 1)

# Ensure mobile sticky buy button click works
old_sticky_click = """    document.getElementById('mobile-sticky-buy-btn').addEventListener('click', () => {
      document.getElementById('buy-now-page-btn').click();
    });"""

new_sticky_click = """    const mobileStickyBtn = document.getElementById('mobile-sticky-buy-btn');
    if (mobileStickyBtn) {
      mobileStickyBtn.addEventListener('click', () => {
        const buyNowBtn = document.getElementById('buy-now-page-btn');
        if (buyNowBtn) buyNowBtn.click();
      });
    }"""

if old_sticky_click in ps_content:
    ps_content = ps_content.replace(old_sticky_click, new_sticky_click)
    print("Fixed mobile sticky button event listener")

with open("product-single.html", "w", encoding="utf-8") as f:
    f.write(ps_content)
print("Saved product-single.html successfully!")


# -------------------------------------------------------------
# 2. Update shark-tank.html comparison table
# -------------------------------------------------------------
with open("shark-tank.html", "r", encoding="utf-8") as f:
    st_content = f.read()

# Replace inline table wrapper with comparison-table-wrapper and table with comparison-table
st_content = re.sub(
    r'<div style="background:#FFFFFF; border:1px solid var\(--border-light\); border-radius:var\(--radius-xl\); overflow-x:auto; box-shadow:var\(--shadow-sm\); max-width:850px; margin:0 auto;">',
    '<div class="comparison-table-wrapper" style="max-width:850px; margin:0 auto;">',
    st_content
)
st_content = re.sub(
    r'<table style="width:100%; border-collapse:collapse; text-align:left; font-size:0.9rem;">',
    '<table class="comparison-table">',
    st_content
)

with open("shark-tank.html", "w", encoding="utf-8") as f:
    f.write(st_content)
print("Saved shark-tank.html successfully!")


# -------------------------------------------------------------
# 3. Update index.html simulator & feature cards marquee
# -------------------------------------------------------------
with open("index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

# Seamless Marquee: ensure 4 sets of 4 cards (16 cards total) so that loop never runs out
feature_cards_single_set = """        <div class="feature-marquee-card">
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
        </div>"""

full_marquee_track = f"""      <div class="feature-marquee-track">
{feature_cards_single_set}
{feature_cards_single_set}
{feature_cards_single_set}
{feature_cards_single_set}
      </div>"""

idx_content = re.sub(
    r'<div class="feature-marquee-track">[\s\S]*?</div>\s*</div>\s*</section>',
    full_marquee_track + '\n    </div>\n  </section>',
    idx_content
)
print("Updated feature marquee track with 4 seamless sets in index.html")

# Simulator in index.html:
# Setup clean desktop vertical buttons, and on mobile smooth horizontal scroll track with subtle indicator
# Also ensure the column container has min-width: 0 so it never blows out or cuts off text.
simulator_clean_markup = """      <div class="simulator-box">
        <!-- Controls Column -->
        <div class="sim-controls-col">
          <h3 class="sim-headline">Choose a Scenario to Test:</h3>
          <p class="sim-subtext">
            Imagine your car is parked at a crowded Delhi metro or mall parking lot. Select what the person scanning your tag wants to say:
          </p>

          <div class="sim-mobile-hint">
            <span>👉 Swipe to choose alert scenario</span>
            <span class="sim-hint-dots">••••</span>
          </div>

          <div class="sim-scenarios-track">
            <button onclick="runSimulator('Car Double Parked', '🚗 Moving Request: Please move your car, parking blocked.')" class="sim-scenario-btn active">
              <span class="scen-icon">🚗</span>
              <div class="scen-info">
                <strong>Car Double Parked</strong>
                <small>Move Request</small>
              </div>
            </button>
            <button onclick="runSimulator('Headlights Left On', '💡 Car Alert: Your headlamps are switched ON in parking.')" class="sim-scenario-btn">
              <span class="scen-icon">💡</span>
              <div class="scen-info">
                <strong>Headlights Switched ON</strong>
                <small>Battery Drain Alert</small>
              </div>
            </button>
            <button onclick="runSimulator('Tow Truck Warning', '🚨 Urgent Alert: Traffic police tow van is approaching your car.')" class="sim-scenario-btn">
              <span class="scen-icon">🚨</span>
              <div class="scen-info">
                <strong>Tow Truck Approaching</strong>
                <small>Police Tow Warning</small>
              </div>
            </button>
            <button onclick="runSimulator('Accident SOS', '⚠️ Emergency: Vehicle involved in minor collision.')" class="sim-scenario-btn">
              <span class="scen-icon">⚠️</span>
              <div class="scen-info">
                <strong>Emergency Collision</strong>
                <small>Immediate SOS Alert</small>
              </div>
            </button>
          </div>

          <div class="sim-result-box">
            🔒 <strong>The Result:</strong> The scanner clicks "Call Owner". Sampark's cloud proxy dials your phone. Neither party can view the other's real phone number!
          </div>
        </div>

        <!-- Simulated Phone Screen Column -->
        <div class="sim-phone-col">
          <div class="sim-phone-screen">
            <div class="sim-phone-notch"></div>
            <div style="font-size:0.7rem; color:#94A3B8; margin-bottom:8px;">SAMPARK CLOUD TELEPHONY</div>

            <div style="width:54px; height:54px; border-radius:50%; background:rgba(255,204,0,0.2); border:2px solid var(--primary); display:flex; align-items:center; justify-content:center; margin:0 auto 12px auto; font-size:1.6rem;">
              🛡️
            </div>

            <h4 style="color:#FFFFFF; font-size:1.1rem; margin-bottom:4px;" id="sim-status-title">Ready to Connect</h4>
            <div style="font-size:0.8rem; color:#10B981; font-weight:700;" id="sim-status-sub">Zero Number Exposure</div>

            <div style="background:rgba(255,255,255,0.06); border-radius:10px; padding:12px; margin:16px 0; text-align:left; font-size:0.8rem; color:#CBD5E1;" id="sim-scenario-box">
              Click any scenario on the left to simulate instant masked routing!
            </div>

            <div style="display:flex; justify-content:space-around; margin-top:16px;">
              <div style="width:42px; height:42px; border-radius:50%; background:#EF4444; display:flex; align-items:center; justify-content:center; font-size:1.1rem;">
                ✕
              </div>
              <div style="width:42px; height:42px; border-radius:50%; background:#10B981; display:flex; align-items:center; justify-content:center; font-size:1.1rem;">
                📞
              </div>
            </div>
          </div>
        </div>
      </div>"""

idx_content = re.sub(
    r'<div class="simulator-box">[\s\S]*?</div>\s*</div>\s*</div>\s*</section>',
    simulator_clean_markup + '\n    </div>\n  </section>',
    idx_content
)
print("Updated simulator box markup in index.html")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(idx_content)
print("Saved index.html successfully!")

print("=== Phase 1 Complete ===")
