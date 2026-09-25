import glob
import re

print("=== Starting Round 2 Comprehensive Fixes ===")

# =========================================================================
# 1. FAVICON SYNC ACROSS ALL HTML FILES
# =========================================================================
canonical_favicon = '<link rel="icon" href="data:image/svg+xml,<svg xmlns=\'http://www.w3.org/2000/svg\' viewBox=\'0 0 24 24\' fill=\'%23FFCC00\'><path d=\'M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5\'/></svg>">'

for html_file in sorted(glob.glob("*.html")):
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Remove any existing favicon tags
    content = re.sub(r'<link[^>]*rel=["\'](?:shortcut )?icon["\'][^>]*>\n?', '', content)
    
    # Insert canonical favicon right before </head>
    content = content.replace("</head>", f"  {canonical_favicon}\n</head>")
    
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Updated favicon in {html_file}")


# =========================================================================
# 2. ACCOUNT.HTML: TAG BUTTONS GAP (IMAGE 5)
# =========================================================================
with open("account.html", "r", encoding="utf-8") as f:
    acc_content = f.read()

# Replace the tight style="display:flex; gap:6px;" with class="tag-card-actions"
acc_content = acc_content.replace(
    '<div style="display:flex; gap:6px;">',
    '<div class="tag-card-actions">'
)

with open("account.html", "w", encoding="utf-8") as f:
    f.write(acc_content)
print("Updated tag buttons container in account.html")


# =========================================================================
# 3. PRODUCT-SINGLE.HTML: REAL SVG ICONS & DESKTOP 2-COLUMN BOTTOM GRID (IMAGE 1)
# =========================================================================
with open("product-single.html", "r", encoding="utf-8") as f:
    ps_content = f.read()

# Construct the 9 Real SVG Feature Icons matching Image 1 exactly
svg_features_grid_html = """          <!-- 9 Feature Icons Grid Card Matching Image 1 -->
          <div class="product-features-grid-card">
            <div class="feature-grid-item">
              <div class="feature-grid-icon icon-blue">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#2563EB" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                </svg>
              </div>
              <div class="feature-grid-label">Masked Audio Calls</div>
            </div>

            <div class="feature-grid-item">
              <div class="feature-grid-icon icon-green">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="#25D366">
                  <path d="M17.472 14.382c-.301-.15-1.78-.879-2.056-.98-.275-.1-.475-.15-.675.15-.199.3-.774.98-.949 1.18-.175.2-.349.225-.65.075-.301-.15-1.272-.469-2.423-1.496-.895-.798-1.5-1.784-1.675-2.084-.175-.3-.019-.462.131-.611.136-.134.301-.35.451-.525.15-.175.2-.3.3-.5.1-.2.05-.375-.025-.525-.075-.15-.675-1.628-.925-2.228-.243-.585-.49-.505-.675-.515-.175-.01-.375-.01-.575-.01s-.525.075-.8.375c-.275.3-1.05 1.025-1.05 2.5s1.075 2.899 1.225 3.1c.15.2 2.115 3.23 5.124 4.53.716.31 1.275.495 1.71.634.719.229 1.373.197 1.89.12.576-.086 1.78-.727 2.03-1.428.25-.7.25-1.302.175-1.428-.075-.126-.275-.201-.576-.351zM12.04 2C6.516 2 2.028 6.488 2.028 12.012c0 1.954.56 3.784 1.536 5.334L2 22l4.81-1.523c1.488.887 3.226 1.385 5.23 1.385 5.524 0 10.012-4.488 10.012-10.012S17.564 2 12.04 2z"/>
                </svg>
              </div>
              <div class="feature-grid-label">WhatsApp Notifications</div>
            </div>

            <div class="feature-grid-item">
              <div class="feature-grid-icon icon-red">
                <svg width="26" height="26" viewBox="0 0 24 24" fill="none">
                  <rect x="3" y="2" width="18" height="20" rx="3" fill="#E11D48"/>
                  <text x="12" y="15" fill="#FFFFFF" font-size="7.5" font-weight="900" text-anchor="middle" font-family="sans-serif">PDF</text>
                </svg>
              </div>
              <div class="feature-grid-label">PDF Tag (Offline)</div>
            </div>

            <div class="feature-grid-item">
              <div class="feature-grid-icon icon-purple">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="#9333EA">
                  <path d="M17 10.5V7a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-3.5l4 4v-11l-4 4z"></path>
                </svg>
              </div>
              <div class="feature-grid-label">Masked Video Calls</div>
            </div>

            <div class="feature-grid-item">
              <div class="feature-grid-icon icon-teal">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#0D9488" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                  <polyline points="14 4 10 8 14 12"></polyline>
                  <path d="M20 10A6 6 0 0 0 10 8"></path>
                </svg>
              </div>
              <div class="feature-grid-label">Call Back Caller</div>
            </div>

            <div class="feature-grid-item">
              <div class="feature-grid-icon icon-green2">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="#16A34A">
                  <path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7zm0 9.5a2.5 2.5 0 0 1 0-5 2.5 2.5 0 0 1 0 5z"></path>
                </svg>
              </div>
              <div class="feature-grid-label">Check Location</div>
            </div>

            <div class="feature-grid-item">
              <div class="feature-grid-icon icon-orange">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="#EA580C">
                  <path d="M20 2H4c-1.1 0-2 .9-2 2v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2zM9 11H7V9h2v2zm4 0h-2V9h2v2zm4 0h-2V9h2v2z"/>
                </svg>
              </div>
              <div class="feature-grid-label">Offline SMS Available</div>
            </div>

            <div class="feature-grid-item">
              <div class="feature-grid-icon icon-red2">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#E11D48" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M3 18v-6a9 9 0 0 1 18 0v6"></path>
                  <path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3zM3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3z"></path>
                </svg>
              </div>
              <div class="feature-grid-label">Live Support Always</div>
            </div>

            <div class="feature-grid-item">
              <div class="feature-grid-icon icon-orange2">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="#CA8A04">
                  <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
                  <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
                </svg>
              </div>
              <div class="feature-grid-label">Emergency Alerts</div>
            </div>
          </div>"""

specs_card_html = """          <!-- Specifications Card Matching Image 1 -->
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
          </div>"""

# Remove existing features grid and specs card from product-info-panel
ps_content = re.sub(r'<!-- 9 Feature Icons Grid Card[\s\S]*?<!-- Specifications Card[\s\S]*?</div>\s*</div>\s*(?=</div>\s*</div>\s*</div>\s*</section>)', '', ps_content)

# We now structure the single product page:
# 1. Product Single Grid: Gallery (left) & Info Panel (right)
# 2. Product Bottom Details Grid: Features Grid (left) & Specs Card (right)
bottom_grid_html = f"""      <!-- Bottom Full-Width 2-Column Section (Desktop Side-by-Side, Mobile Stack) -->
      <div class="product-bottom-details-grid">
{svg_features_grid_html}
{specs_card_html}
      </div>"""

# Insert bottom_grid_html right before </section>
ps_content = ps_content.replace(
    '        </div>\n\n      </div>\n    </div>\n  </section>',
    '        </div>\n\n      </div>\n\n' + bottom_grid_html + '\n    </div>\n  </section>'
)

with open("product-single.html", "w", encoding="utf-8") as f:
    f.write(ps_content)
print("Updated product-single.html with vector SVG icons and 2-column bottom layout")


# =========================================================================
# 4. INDEX.HTML: SLIDE 2 MOBILE CLEANUP & SIMULATOR PHONE SCREEN PIXEL-PERFECT (IMAGES 2 & 3)
# =========================================================================
with open("index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

# For Simulator Phone Screen, make sure the HTML markup has clean classes and structure
sim_phone_screen_markup = """        <!-- Simulated Phone Screen Column (Pixel-Perfect Matching Image 3) -->
        <div class="sim-phone-col">
          <div class="sim-phone-screen">
            <div class="sim-phone-notch"></div>
            <div class="sim-screen-header">SAMPARK CLOUD TELEPHONY</div>

            <div class="sim-shield-badge">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none">
                <path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-9-5z" fill="#3B82F6"/>
                <path d="M12 4.18L5 8.07v4.93c0 4.33 2.99 8.38 7 9.42V4.18z" fill="#60A5FA"/>
              </svg>
            </div>

            <h4 class="sim-screen-title" id="sim-status-title">Ready to Connect</h4>
            <div class="sim-screen-sub" id="sim-status-sub">Zero Number Exposure</div>

            <div class="sim-scenario-bubble" id="sim-scenario-box">
              Click any scenario on the left to simulate instant masked routing!
            </div>

            <div class="sim-call-actions">
              <button type="button" class="sim-call-btn btn-decline" aria-label="End Simulation" onclick="resetSimulator()">
                ✕
              </button>
              <button type="button" class="sim-call-btn btn-accept" aria-label="Accept Masked Call" onclick="triggerMaskedVoice()">
                <svg width="22" height="22" viewBox="0 0 24 24" fill="#FF1493">
                  <path d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 0 0-1.01.24l-1.57 1.97c-2.83-1.35-5.48-3.9-6.89-6.83l1.95-1.66c.27-.28.35-.67.24-1.02-.37-1.11-.56-2.3-.56-3.53 0-.54-.45-.99-.99-.99H4.19C3.65 3 3 3.24 3 3.99 3 13.28 10.73 21 20.01 21c.71 0 .99-.63.99-1.18v-3.45c0-.54-.45-.99-.99-.99z"/>
                </svg>
              </button>
            </div>
          </div>
        </div>"""

idx_content = re.sub(
    r'<!-- Simulated Phone Screen Column[\s\S]*?</div>\s*</div>\s*(?=</div>\s*</div>\s*</section>)',
    sim_phone_screen_markup + '\n      </div>\n',
    idx_content
)

# Also ensure resetSimulator and triggerMaskedVoice functions exist in index.html script
if "function resetSimulator" not in idx_content:
    sim_helper_script = """    function resetSimulator() {
      document.getElementById('sim-status-title').textContent = 'Ready to Connect';
      document.getElementById('sim-status-sub').textContent = 'Zero Number Exposure';
      document.getElementById('sim-scenario-box').textContent = 'Click any scenario on the left to simulate instant masked routing!';
      document.querySelectorAll('.sim-scenario-btn').forEach(b => b.classList.remove('active'));
    }

    function triggerMaskedVoice() {
      window.SamparkApp.showToastMessage('📞 Connecting 100% Masked Cloud Relay... Your number is protected!');
    }"""
    idx_content = idx_content.replace(
        "    function runSimulator(title, message) {",
        sim_helper_script + "\n\n    function runSimulator(title, message) {"
    )

with open("index.html", "w", encoding="utf-8") as f:
    f.write(idx_content)
print("Updated simulator phone screen markup and helpers in index.html")

print("=== Phase 1 Script Completed Successfully ===")
