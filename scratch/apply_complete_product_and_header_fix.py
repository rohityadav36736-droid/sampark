import re

print("=== Starting Complete Product Single & Header Fix ===")

# =========================================================================
# 1. UPDATE product-single.html PURCHASE CONTROLS
# =========================================================================
with open("product-single.html", "r", encoding="utf-8") as f:
    ps_content = f.read()

# Replace the unstyled vehicle input, pincode checker, quantity stepper, and action buttons
old_purchase_controls = """          <!-- Vehicle Plate Linking Preview Card -->
          <div class="vehicle-input-preview-card">
            <label for="vehicle-plate-input">
              🚗 Link Vehicle Registration (Optional, or activate after delivery):
            </label>
            <input type="text" id="vehicle-plate-input" class="vehicle-plate-input" placeholder="e.g. DL 01 AB 1234" maxlength="15">
            <small style="color:#64748B; display:block; margin-top:4px; font-size:0.75rem;">
              💡 Pre-linked to your vehicle in our secure cloud so it works right out of the box!
            </small>
          </div>

          <!-- Pincode Checker -->
          <div style="background:#FFFFFF; border:1px solid var(--border-light); border-radius:var(--radius-md); padding:14px; margin: 16px 0;">
            <strong style="font-size:0.84rem; color:var(--dark-900);">Check Delivery Speed in Your City:</strong>
            <div class="pincode-checker-box" style="margin-top:8px; margin-bottom:4px;">
              <input type="text" id="pincode-input" placeholder="6-digit Pincode (e.g. 110001)" maxlength="6">
              <button class="btn btn-dark btn-sm" id="check-pincode-btn">Check</button>
            </div>
            <div id="pincode-result"></div>
          </div>

          <!-- Quantity & Action Buttons -->
          <div style="display:flex; align-items:center; gap:14px; margin-bottom: 20px;">
            <div class="qty-stepper">
              <button class="qty-btn" id="prod-qty-minus">-</button>
              <span class="qty-val" id="prod-qty-val">1</span>
              <button class="qty-btn" id="prod-qty-plus">+</button>
            </div>
            <span style="font-size:0.82rem; color:#10B981; font-weight:700;">✓ In Stock — Ready to Dispatch</span>
          </div>

          <div style="display:grid; grid-template-columns: 1fr 1fr; gap:12px; margin-bottom: 24px;">
            <button class="btn btn-outline btn-lg" id="add-to-cart-page-btn">
              🛒 Add To Cart
            </button>
            <button class="btn btn-primary btn-lg" id="buy-now-page-btn">
              ⚡ Buy Now
            </button>
          </div>

          <!-- Guarantee Highlights -->
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
          </div>"""

new_purchase_controls = """          <!-- Vehicle Plate Linking Preview Card -->
          <div class="product-config-card">
            <label for="vehicle-plate-input" class="config-label">
              🚗 Link Vehicle Registration <span class="config-optional">(Optional — can activate later)</span>
            </label>
            <div class="config-input-wrapper">
              <input type="text" id="vehicle-plate-input" class="config-plate-input" placeholder="e.g. DL 01 AB 1234" maxlength="15">
            </div>
            <small class="config-hint">
              💡 Pre-linked to your vehicle in our secure cloud so it works right out of the box!
            </small>
          </div>

          <!-- Pincode Checker Card -->
          <div class="product-pincode-card">
            <div class="pincode-card-header">
              <span class="pincode-icon">📍</span>
              <strong>Check Delivery Speed in Your City:</strong>
            </div>
            <div class="pincode-input-row">
              <input type="text" id="pincode-input" class="pincode-text-input" placeholder="Enter 6-digit Pincode" maxlength="6">
              <button type="button" class="pincode-check-btn" id="check-pincode-btn">Check</button>
            </div>
            <div id="pincode-result" class="pincode-result-msg"></div>
          </div>

          <!-- Quantity Stepper & Stock Status Row -->
          <div class="product-quantity-row">
            <div class="product-stepper-box">
              <button type="button" class="stepper-btn" id="prod-qty-minus">−</button>
              <span class="stepper-count" id="prod-qty-val">1</span>
              <button type="button" class="stepper-btn" id="prod-qty-plus">+</button>
            </div>
            <div class="product-stock-badge">
              <span class="stock-dot"></span> In Stock — Ready to Dispatch
            </div>
          </div>

          <!-- Primary Action Buttons (Pill & High Contrast) -->
          <div class="product-main-actions-grid">
            <button type="button" class="btn-product-cart" id="add-to-cart-page-btn">
              🛒 Add To Cart
            </button>
            <button type="button" class="btn-product-buy" id="buy-now-page-btn">
              ⚡ Buy Now
            </button>
          </div>

          <!-- Guarantee Highlights Grid -->
          <div class="product-trust-badges-grid">
            <div class="trust-badge-item">
              <span class="trust-badge-icon">🛡️</span>
              <span>100% Privacy Calling Proxy</span>
            </div>
            <div class="trust-badge-item">
              <span class="trust-badge-icon">🌦️</span>
              <span>All-Weather Heat & Rainproof</span>
            </div>
            <div class="trust-badge-item">
              <span class="trust-badge-icon">📱</span>
              <span>Zero App Needed for Scanners</span>
            </div>
            <div class="trust-badge-item">
              <span class="trust-badge-icon">♾️</span>
              <span>Lifetime Cloud Connectivity</span>
            </div>
          </div>"""

if old_purchase_controls in ps_content:
    ps_content = ps_content.replace(old_purchase_controls, new_purchase_controls)
    print("Replaced purchase controls in product-single.html")
else:
    # Use regex replacement if whitespace differences
    ps_content = re.sub(
        r'<!-- Vehicle Plate Linking Preview Card -->[\s\S]*?<!-- Guarantee Highlights -->[\s\S]*?</div>\s*</div>\s*(?=</div>\s*</div>\s*<!-- Bottom Full-Width)',
        new_purchase_controls + '\n',
        ps_content
    )
    print("Replaced purchase controls via regex in product-single.html")

with open("product-single.html", "w", encoding="utf-8") as f:
    f.write(ps_content)

print("Saved updated product-single.html!")


# =========================================================================
# 2. UPDATE assets/css/style.css:
# - Product Single purchase controls CSS
# - Desktop layout balance & sticky gallery
# - Universal mobile header sticky & styling fix across all pages
# =========================================================================
with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css_content = f.read()

round4_css = """
/* ==========================================================================
   ROUND 4 ENHANCEMENTS: PRODUCT SINGLE PURCHASE PANEL & MOBILE HEADER FIX
   ========================================================================== */

/* 1. Single Product Sticky Gallery on Desktop */
@media (min-width: 993px) {
  .product-single-grid {
    display: grid !important;
    grid-template-columns: 1fr 1.15fr !important;
    gap: 52px !important;
    align-items: start !important;
  }

  .product-single-grid > div:first-child {
    position: -webkit-sticky !important;
    position: sticky !important;
    top: 92px !important;
  }
}

/* 2. Product Single Purchase Panel Controls */
.product-config-card {
  background: #F8FAFC;
  border: 1.5px solid #E2E8F0;
  border-radius: 16px;
  padding: 16px 18px;
  margin: 16px 0;
}

.config-label {
  display: block;
  font-weight: 800;
  font-size: 0.88rem;
  color: #0F172A;
  margin-bottom: 8px;
}

.config-optional {
  font-weight: 600;
  color: #64748B;
  font-size: 0.78rem;
}

.config-input-wrapper {
  position: relative;
  width: 100%;
}

.config-plate-input {
  width: 100%;
  border: 1.5px solid #CBD5E1;
  border-radius: 10px;
  padding: 12px 14px;
  font-size: 1.05rem;
  font-weight: 800;
  letter-spacing: 1px;
  text-transform: uppercase;
  background: #FFFFFF;
  color: #0F172A;
  box-sizing: border-box;
  transition: all 0.2s ease;
}

.config-plate-input:focus {
  border-color: #FFCC00;
  outline: none;
  box-shadow: 0 0 0 3px rgba(255, 204, 0, 0.25);
  background: #FFFDF0;
}

.config-hint {
  color: #64748B;
  font-size: 0.75rem;
  margin-top: 6px;
  display: block;
  line-height: 1.4;
}

/* Pincode Card */
.product-pincode-card {
  background: #FFFFFF;
  border: 1.5px solid #E2E8F0;
  border-radius: 16px;
  padding: 16px 18px;
  margin: 16px 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
}

.pincode-card-header {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.86rem;
  color: #0F172A;
  margin-bottom: 10px;
}

.pincode-input-row {
  display: flex;
  gap: 8px;
  width: 100%;
}

.pincode-text-input {
  flex: 1;
  border: 1.5px solid #CBD5E1;
  border-radius: 10px;
  padding: 10px 14px;
  font-size: 0.9rem;
  font-weight: 600;
  color: #0F172A;
  box-sizing: border-box;
}

.pincode-text-input:focus {
  border-color: #FFCC00;
  outline: none;
  box-shadow: 0 0 0 2px rgba(255, 204, 0, 0.25);
}

.pincode-check-btn {
  background: #0B0E17;
  color: #FFFFFF;
  border: none;
  border-radius: 10px;
  padding: 10px 18px;
  font-weight: 800;
  font-size: 0.85rem;
  cursor: pointer;
  flex-shrink: 0;
  transition: all 0.2s ease;
}

.pincode-check-btn:hover {
  background: #1E293B;
}

.pincode-result-msg {
  margin-top: 8px;
  font-size: 0.8rem;
  font-weight: 700;
}

/* Quantity Stepper & Stock */
.product-quantity-row {
  display: flex;
  align-items: center;
  gap: 16px;
  margin: 18px 0;
  flex-wrap: wrap;
}

.product-stepper-box {
  display: inline-flex;
  align-items: center;
  border: 1.5px solid #CBD5E1;
  border-radius: 9999px;
  background: #FFFFFF;
  padding: 3px;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
}

.stepper-btn {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: none;
  background: #F1F5F9;
  font-size: 1.15rem;
  font-weight: 900;
  color: #0F172A;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.15s ease;
}

.stepper-btn:hover {
  background: #E2E8F0;
}

.stepper-count {
  min-width: 38px;
  text-align: center;
  font-weight: 900;
  font-size: 1.05rem;
  color: #0F172A;
}

.product-stock-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 0.84rem;
  font-weight: 700;
  color: #059669;
  background: #ECFDF5;
  border: 1px solid #A7F3D0;
  padding: 6px 14px;
  border-radius: 9999px;
}

.stock-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #10B981;
}

/* Primary Action Buttons */
.product-main-actions-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 14px;
  margin: 20px 0 24px 0;
  width: 100%;
}

.btn-product-cart {
  width: 100%;
  background: #FFFFFF;
  border: 2.5px solid #0B0E17;
  color: #0B0E17;
  font-weight: 900;
  font-size: 1rem;
  border-radius: 9999px;
  padding: 14px 20px;
  cursor: pointer;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  text-align: center;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.btn-product-cart:hover {
  background: #0B0E17;
  color: #FFFFFF;
  transform: translateY(-2px);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

.btn-product-buy {
  width: 100%;
  background: #FFE600 !important;
  border: 2.5px solid #FFE600 !important;
  color: #000000 !important;
  font-weight: 900 !important;
  font-size: 1.05rem !important;
  border-radius: 9999px !important;
  padding: 14px 24px !important;
  cursor: pointer !important;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
  box-shadow: 0 6px 20px rgba(255, 204, 0, 0.45) !important;
  text-align: center !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  gap: 8px !important;
}

.btn-product-buy:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 10px 25px rgba(255, 204, 0, 0.6) !important;
}

/* Trust Badges Grid */
.product-trust-badges-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 12px;
  border-top: 1px solid #E2E8F0;
  padding-top: 18px;
  margin-top: 16px;
}

.trust-badge-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 0.8rem;
  font-weight: 700;
  color: #475569;
}

/* 3. Universal Mobile Header Fix Across All Pages */
@media (max-width: 992px) {
  .top-announcement {
    display: none !important;
  }
}

@media (max-width: 768px) {
  .site-header {
    position: -webkit-sticky !important;
    position: sticky !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    width: 100% !important;
    z-index: 1000 !important;
    background: #FFFFFF !important;
    border-bottom: 1px solid #E2E8F0 !important;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05) !important;
  }

  .header-container {
    height: 58px !important;
    padding: 0 14px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: space-between !important;
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
  }

  .brand-logo {
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
    text-decoration: none !important;
    flex-shrink: 0 !important;
  }

  .brand-logo-icon {
    width: 36px !important;
    height: 36px !important;
    background: #FFE600 !important;
    color: #000000 !important;
    font-size: 1.05rem !important;
    font-weight: 900 !important;
    border-radius: 9px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    flex-shrink: 0 !important;
  }

  .brand-logo-name {
    font-size: 1.15rem !important;
    font-weight: 900 !important;
    color: #0F172A !important;
    letter-spacing: -0.02em !important;
  }

  .brand-logo-badge {
    display: none !important;
  }

  .header-actions {
    display: flex !important;
    align-items: center !important;
    gap: 8px !important;
    flex-shrink: 0 !important;
  }

  .cart-icon-btn {
    width: 38px !important;
    height: 38px !important;
    background: #F1F5F9 !important;
    border-radius: 50% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    position: relative !important;
    color: #0F172A !important;
    text-decoration: none !important;
  }

  .cart-counter {
    position: absolute !important;
    top: -2px !important;
    right: -2px !important;
    background: #000000 !important;
    color: #FFE600 !important;
    font-size: 0.68rem !important;
    font-weight: 900 !important;
    width: 18px !important;
    height: 18px !important;
    border-radius: 50% !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
  }

  .mobile-toggle {
    width: 38px !important;
    height: 38px !important;
    background: #F8FAFC !important;
    border: 1.5px solid #E2E8F0 !important;
    border-radius: 10px !important;
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
    align-items: center !important;
    gap: 4px !important;
    cursor: pointer !important;
    padding: 0 !important;
  }

  .mobile-toggle span {
    display: block !important;
    width: 18px !important;
    height: 2px !important;
    background: #0F172A !important;
    border-radius: 2px !important;
  }

  /* Mobile Single Product adjustments */
  .product-main-actions-grid {
    grid-template-columns: 1fr 1fr !important;
    gap: 10px !important;
    margin: 16px 0 !important;
  }

  .btn-product-cart,
  .btn-product-buy {
    padding: 12px 14px !important;
    font-size: 0.92rem !important;
  }

  .product-config-card {
    padding: 14px !important;
    border-radius: 14px !important;
  }

  .config-plate-input {
    padding: 10px 12px !important;
    font-size: 0.95rem !important;
  }
}
"""

css_content += "\n" + round4_css

with open("assets/css/style.css", "w", encoding="utf-8") as f:
    f.write(css_content)

print("Saved updated style.css with Round 4 purchase panel & mobile header fixes!")
print("=== Complete Execution Successful ===")
