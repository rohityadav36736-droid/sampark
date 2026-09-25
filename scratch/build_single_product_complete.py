import re

print("=== Building Complete Single Product Page & Mobile Hero CSS ===")

# =========================================================================
# 1. READ product-single.html
# =========================================================================
with open("product-single.html", "r", encoding="utf-8") as f:
    ps = f.read()

# Detailed Info Section HTML (How it Works, Tech Specs, What's in Box)
detailed_info_html = """
  <!-- Detailed Product Information Tabs / Section -->
  <section class="product-info-details-section">
    <div class="container">
      <div class="section-header" style="text-align:left; margin-bottom:28px;">
        <div class="section-tag">Complete Details</div>
        <h2>Product Information & Privacy Architecture</h2>
        <p>Everything you need to know about the hardware, laser encoding, and telecom relay setup.</p>
      </div>

      <div class="product-info-tabs-wrapper">
        <div class="info-tabs-nav">
          <button class="info-tab-btn active" onclick="switchInfoTab('how-it-works', this)">🛡️ How It Works</button>
          <button class="info-tab-btn" onclick="switchInfoTab('tech-specs', this)">📐 Technical Specs</button>
          <button class="info-tab-btn" onclick="switchInfoTab('whats-included', this)">📦 Box Contents</button>
          <button class="info-tab-btn" onclick="switchInfoTab('faqs', this)">❓ Tag FAQs</button>
        </div>

        <div class="info-tab-content-area">
          <!-- Tab 1: How It Works -->
          <div id="tab-how-it-works" class="info-tab-panel active">
            <div class="how-it-works-steps-grid">
              <div class="hw-step-box">
                <div class="hw-step-num">01</div>
                <h4>Peel & Stick in 30 Seconds</h4>
                <p>Peel the 3M weather-resistant adhesive strip and apply the acrylic tag on the inside corner of your windshield or bike visor.</p>
              </div>
              <div class="hw-step-box">
                <div class="hw-step-num">02</div>
                <h4>Instant Cloud Activation</h4>
                <p>Scan your unique registration QR with your own phone to link your vehicle number and mobile in under 60 seconds.</p>
              </div>
              <div class="hw-step-box">
                <div class="hw-step-num">03</div>
                <h4>100% Masked Relayed Calls</h4>
                <p>Anyone scanning your tag connects via Sampark's virtual cloud PBX (+91 11-4084-XXXX). Your number is NEVER revealed!</p>
              </div>
            </div>
          </div>

          <!-- Tab 2: Technical Specs -->
          <div id="tab-tech-specs" class="info-tab-panel">
            <div class="tech-specs-table-box">
              <table class="specs-full-table">
                <tbody>
                  <tr>
                    <th>Tag Material</th>
                    <td>UV-Treated Polycarbonate Acrylic with scratch-resistant top coat</td>
                  </tr>
                  <tr>
                    <th>Dimensions</th>
                    <td>85 mm x 54 mm (Standard ISO CR-80 credit card form factor)</td>
                  </tr>
                  <tr>
                    <th>Adhesive Type</th>
                    <td>Automotive-grade 3M VHB thermal adhesive (Leaves zero residue upon removal)</td>
                  </tr>
                  <tr>
                    <th>Operating Temperature</th>
                    <td>-10°C to +65°C (Engineered specifically for peak Delhi heatwaves & monsoons)</td>
                  </tr>
                  <tr>
                    <th>QR Longevity</th>
                    <td>Laser-etched high-density QR code rated for 5+ years without fading</td>
                  </tr>
                  <tr>
                    <th>Scanner Requirement</th>
                    <td>Zero App Needed! Scannable with native iOS Camera, Android Camera, Google Lens, or UPI apps</td>
                  </tr>
                  <tr>
                    <th>Telephony Network</th>
                    <td>Bank-grade encrypted dual-leg cloud telecom proxy with Delhi NCR routing</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- Tab 3: Box Contents -->
          <div id="tab-whats-included" class="info-tab-panel">
            <div class="box-contents-grid">
              <div class="content-item-card">
                <span class="content-item-icon">🏷️</span>
                <div>
                  <strong>1x Sampark Smart QR Tag</strong>
                  <p>Pre-printed with high-contrast durable automotive QR code</p>
                </div>
              </div>
              <div class="content-item-card">
                <span class="content-item-icon">🧽</span>
                <div>
                  <strong>1x Surface Prep Alcohol Wipe</strong>
                  <p>Ensures glass windshield is oil-free for maximum 3M bonding</p>
                </div>
              </div>
              <div class="content-item-card">
                <span class="content-item-icon">📖</span>
                <div>
                  <strong>Quick Start Activation Guide</strong>
                  <p>Simple 3-step pictorial instruction manual in English and Hindi</p>
                </div>
              </div>
              <div class="content-item-card">
                <span class="content-item-icon">🛡️</span>
                <div>
                  <strong>1 Year Replacement Warranty Card</strong>
                  <p>Free tag replacement if peeled or damaged under normal usage</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Tab 4: FAQs -->
          <div id="tab-faqs" class="info-tab-panel">
            <div class="tab-faq-list">
              <div class="tab-faq-item">
                <strong>Q: Can the person calling me see my true phone number?</strong>
                <p>Never. Sampark's cloud proxy connects both phones via an encrypted virtual relay (+91 11-4084-XXXX). Neither party sees the other's real phone number.</p>
              </div>
              <div class="tab-faq-item">
                <strong>Q: What happens if my vehicle is parked in a low network basement?</strong>
                <p>Sampark simultaneously triggers an instant SMS and WhatsApp alert with the scanner's message so you are notified the moment your phone catches network.</p>
              </div>
              <div class="tab-faq-item">
                <strong>Q: Is there any monthly fee or annual recharge?</strong>
                <p>No. Your one-time purchase includes lifetime cloud QR redirection and unlimited masked phone call routing with no hidden charges.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

# Customer Reviews Section HTML
reviews_section_html = """
  <!-- Verified Customer Reviews Section -->
  <section class="product-reviews-section" id="customer-reviews">
    <div class="container">
      <div class="reviews-header-block">
        <div>
          <div class="section-tag">Delhi NCR Community</div>
          <h2>Verified Customer Reviews</h2>
          <p>Real feedback from car and motorcycle owners across Delhi, Gurgaon, Noida, and Faridabad.</p>
        </div>
        <button class="btn btn-outline" onclick="openReviewModal()">✍️ Write a Review</button>
      </div>

      <!-- Rating Summary Overview Card -->
      <div class="rating-overview-card">
        <div class="rating-score-box">
          <div class="rating-big-num">4.9</div>
          <div class="rating-big-stars">★★★★★</div>
          <div class="rating-total-reviews">Based on 8,420+ Verified Purchases</div>
        </div>

        <div class="rating-bars-box">
          <div class="rating-bar-row">
            <span class="bar-star-label">5 Stars</span>
            <div class="bar-track"><div class="bar-fill" style="width: 92%;"></div></div>
            <span class="bar-pct">92%</span>
          </div>
          <div class="rating-bar-row">
            <span class="bar-star-label">4 Stars</span>
            <div class="bar-track"><div class="bar-fill" style="width: 6%;"></div></div>
            <span class="bar-pct">6%</span>
          </div>
          <div class="rating-bar-row">
            <span class="bar-star-label">3 Stars</span>
            <div class="bar-track"><div class="bar-fill" style="width: 1%;"></div></div>
            <span class="bar-pct">1%</span>
          </div>
          <div class="rating-bar-row">
            <span class="bar-star-label">2 Stars</span>
            <div class="bar-track"><div class="bar-fill" style="width: 0.5%;"></div></div>
            <span class="bar-pct">&lt;1%</span>
          </div>
          <div class="rating-bar-row">
            <span class="bar-star-label">1 Star</span>
            <div class="bar-track"><div class="bar-fill" style="width: 0.5%;"></div></div>
            <span class="bar-pct">&lt;1%</span>
          </div>
        </div>
      </div>

      <!-- Reviews Grid Cards -->
      <div class="reviews-cards-grid">
        <!-- Review 1 -->
        <div class="review-comment-card">
          <div class="review-card-top">
            <div class="reviewer-avatar">RK</div>
            <div class="reviewer-meta">
              <strong>Rahul Kapoor</strong>
              <span>Verified Buyer • DL 01 AB 1234 • South Delhi</span>
            </div>
            <span class="review-verified-badge">✓ Verified</span>
          </div>
          <div class="review-stars-row">★★★★★ <span class="review-date">Yesterday</span></div>
          <h4 class="review-title">Best ₹199 investment for Delhi car owners!</h4>
          <p class="review-text">
            I used to leave a paper slip on my windshield in Khan Market parking. Received unsolicited marketing calls every week. Switched to Sampark tag after seeing Shark Tank — now people can contact me anytime my car is double parked and my mobile number stays 100% confidential.
          </p>
        </div>

        <!-- Review 2 -->
        <div class="review-comment-card">
          <div class="review-card-top">
            <div class="reviewer-avatar" style="background:#0D9488;">PM</div>
            <div class="reviewer-meta">
              <strong>Dr. Pooja Malhotra</strong>
              <span>Verified Buyer • HR 26 DQ 5678 • Gurgaon</span>
            </div>
            <span class="review-verified-badge">✓ Verified</span>
          </div>
          <div class="review-stars-row">★★★★★ <span class="review-date">3 days ago</span></div>
          <h4 class="review-title">A lifesaver for working women drivers</h4>
          <p class="review-text">
            As a healthcare professional parking at hospitals and metro stations, privacy is non-negotiable. Someone double-parked behind me needed my car moved; they scanned the tag and dialed me through the virtual proxy within seconds. Zero awkwardness or number sharing.
          </p>
        </div>

        <!-- Review 3 -->
        <div class="review-comment-card">
          <div class="review-card-top">
            <div class="reviewer-avatar" style="background:#7C3AED;">VS</div>
            <div class="reviewer-meta">
              <strong>Vikramaditya Sharma</strong>
              <span>Verified Buyer • UP 16 CZ 9921 • Noida Sector 62</span>
            </div>
            <span class="review-verified-badge">✓ Verified</span>
          </div>
          <div class="review-stars-row">★★★★★ <span class="review-date">1 week ago</span></div>
          <h4 class="review-title">Survived 48°C Delhi heatwave with zero peeling</h4>
          <p class="review-text">
            Was skeptical about the adhesive in extreme summer. It has been 4 months through torrential rains and direct sun, and the tag looks brand new. The instant WhatsApp notifications give immense peace of mind whenever someone scans it.
          </p>
        </div>

        <!-- Review 4 -->
        <div class="review-comment-card">
          <div class="review-card-top">
            <div class="reviewer-avatar" style="background:#CA8A04;">AS</div>
            <div class="reviewer-meta">
              <strong>Ananya Sen</strong>
              <span>Verified Buyer • DL 3C CE 4410 • Rohini</span>
            </div>
            <span class="review-verified-badge">✓ Verified</span>
          </div>
          <div class="review-stars-row">★★★★★ <span class="review-date">2 weeks ago</span></div>
          <h4 class="review-title">Fast 24hr delivery & seamless activation</h4>
          <p class="review-text">
            Ordered Cash on Delivery and it arrived the very next afternoon in Delhi. Scanned the QR with my iPhone camera and activated it in 30 seconds. Already ordered the 3-tag family pack for my parents' cars!
          </p>
        </div>
      </div>
    </div>
  </section>
"""

# Related Products Section HTML
related_products_html = """
  <!-- Related Products / Frequently Bought Together -->
  <section class="related-products-section">
    <div class="container">
      <div class="section-header" style="text-align:left; margin-bottom:28px;">
        <div class="section-tag">Explore More Tags</div>
        <h2>Frequently Bought Together</h2>
        <p>Complete privacy coverage for your other household vehicles and commercial fleets.</p>
      </div>

      <div class="related-products-grid">
        <!-- Related 1: Pro Tag -->
        <div class="related-prod-card">
          <span class="related-badge">Dual QR Pro</span>
          <a href="product-single.html?id=pro-tag" class="related-img-link">
            <img src="assets/images/car-tag-hd.jpg" alt="Pro Windshield Acrylic Tag">
          </a>
          <div class="related-info">
            <div class="related-rating">★★★★★ <span>(4.9)</span></div>
            <h4 class="related-title">
              <a href="product-single.html?id=pro-tag">Pro Windshield Tag (Dual QR)</a>
            </h4>
            <div class="related-price-row">
              <span class="rel-price-now">₹249</span>
              <span class="rel-price-old">₹599</span>
            </div>
            <a href="product-single.html?id=pro-tag" class="btn btn-outline btn-block btn-sm">View Tag Details</a>
          </div>
        </div>

        <!-- Related 2: Bike Tag -->
        <div class="related-prod-card">
          <span class="related-badge">Helmet & Moto</span>
          <a href="product-single.html?id=bike-tag" class="related-img-link">
            <img src="assets/images/bike-tag-hd.jpg" alt="Moto & Helmet Emergency Tag">
          </a>
          <div class="related-info">
            <div class="related-rating">★★★★★ <span>(4.9)</span></div>
            <h4 class="related-title">
              <a href="product-single.html?id=bike-tag">Moto & Helmet Emergency Tag</a>
            </h4>
            <div class="related-price-row">
              <span class="rel-price-now">₹249</span>
              <span class="rel-price-old">₹549</span>
            </div>
            <a href="product-single.html?id=bike-tag" class="btn btn-outline btn-block btn-sm">View Tag Details</a>
          </div>
        </div>

        <!-- Related 3: Fleet Tag -->
        <div class="related-prod-card">
          <span class="related-badge">Fleet / Commercial</span>
          <a href="product-single.html?id=fleet-tag" class="related-img-link">
            <img src="assets/images/product-fleet.jpg" alt="Commercial Fleet Vehicle Tag">
          </a>
          <div class="related-info">
            <div class="related-rating">★★★★★ <span>(4.8)</span></div>
            <h4 class="related-title">
              <a href="product-single.html?id=fleet-tag">Commercial & Fleet Vehicle Tag</a>
            </h4>
            <div class="related-price-row">
              <span class="rel-price-now">₹299</span>
              <span class="rel-price-old">₹699</span>
            </div>
            <a href="product-single.html?id=fleet-tag" class="btn btn-outline btn-block btn-sm">View Tag Details</a>
          </div>
        </div>

        <!-- Related 4: Family Combo -->
        <div class="related-prod-card">
          <span class="related-badge" style="background:#FFCC00; color:#000;">Best Value</span>
          <a href="product-single.html?id=combo-pack" class="related-img-link">
            <img src="assets/images/ref-product-gallery.png" alt="Delhi Family Combo Pack">
          </a>
          <div class="related-info">
            <div class="related-rating">★★★★★ <span>(5.0)</span></div>
            <h4 class="related-title">
              <a href="product-single.html?id=combo-pack">Delhi Family Combo (3 Tags)</a>
            </h4>
            <div class="related-price-row">
              <span class="rel-price-now">₹449</span>
              <span class="rel-price-old">₹1,199</span>
            </div>
            <a href="product-single.html?id=combo-pack" class="btn btn-outline btn-block btn-sm">View Tag Details</a>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

# Insert detailed_info_html, reviews_section_html, and related_products_html before the footer
insert_sections = f"""
{detailed_info_html}
{reviews_section_html}
{related_products_html}
"""

# Check if already present, if not add
if "product-info-details-section" not in ps:
    ps = ps.replace("  <!-- Footer -->", insert_sections + "\n  <!-- Footer -->")

# Add Tab switching function to script in product-single.html
tab_script = """
    function switchInfoTab(tabId, btn) {
      document.querySelectorAll('.info-tab-btn').forEach(b => b.classList.remove('active'));
      document.querySelectorAll('.info-tab-panel').forEach(p => p.classList.remove('active'));
      btn.classList.add('active');
      const target = document.getElementById('tab-' + tabId);
      if (target) target.classList.add('active');
    }

    function openReviewModal() {
      window.SamparkApp.showToastMessage('✍️ Review submission form opened! (Requires verified purchase login)');
    }
"""

if "function switchInfoTab" not in ps:
    ps = ps.replace("  </script>", tab_script + "\n  </script>")

with open("product-single.html", "w", encoding="utf-8") as f:
    f.write(ps)

print("Saved product-single.html with Detailed Info, Reviews, and Related Products!")


# =========================================================================
# 2. ADD CSS FOR SINGLE PRODUCT COMPLETE SECTIONS AND HERO SLIDER PHONE FIX
# =========================================================================
with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

single_prod_and_hero_css = """
/* ==========================================================================
   COMPLETE SINGLE PRODUCT SECTIONS (TABS, TECH SPECS, REVIEWS, RELATED PRODUCTS)
   ========================================================================== */

/* 1. Detailed Info Tabs Section */
.product-info-details-section {
  padding: 60px 0;
  background: #F8FAFC;
  border-top: 1px solid var(--border-light);
  border-bottom: 1px solid var(--border-light);
}

.product-info-tabs-wrapper {
  background: #FFFFFF;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-sm);
  overflow: hidden;
}

.info-tabs-nav {
  display: flex;
  background: #F1F5F9;
  border-bottom: 1px solid var(--border-light);
  overflow-x: auto;
  scrollbar-width: none;
}

.info-tabs-nav::-webkit-scrollbar {
  display: none;
}

.info-tab-btn {
  padding: 16px 24px;
  background: transparent;
  border: none;
  font-family: var(--font-heading);
  font-weight: 700;
  font-size: 0.95rem;
  color: #64748B;
  cursor: pointer;
  white-space: nowrap;
  transition: all 0.2s ease;
  border-bottom: 3px solid transparent;
}

.info-tab-btn:hover {
  color: var(--dark-900);
}

.info-tab-btn.active {
  background: #FFFFFF;
  color: var(--dark-900);
  border-bottom-color: #FFCC00;
}

.info-tab-content-area {
  padding: 32px;
}

.info-tab-panel {
  display: none;
}

.info-tab-panel.active {
  display: block;
}

/* How It Works Steps Grid */
.how-it-works-steps-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.hw-step-box {
  background: #F8FAFC;
  border: 1px solid #E2E8F0;
  border-radius: 16px;
  padding: 24px 20px;
  position: relative;
}

.hw-step-num {
  font-size: 1.8rem;
  font-weight: 900;
  font-family: var(--font-heading);
  color: #FFCC00;
  margin-bottom: 8px;
}

.hw-step-box h4 {
  font-size: 1.05rem;
  font-weight: 800;
  color: var(--dark-900);
  margin-bottom: 8px;
}

.hw-step-box p {
  font-size: 0.86rem;
  color: #64748B;
  line-height: 1.5;
  margin: 0;
}

/* Tech Specs Table */
.specs-full-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.9rem;
}

.specs-full-table tr {
  border-bottom: 1px solid #F1F5F9;
}

.specs-full-table tr:last-child {
  border-bottom: none;
}

.specs-full-table th {
  padding: 14px 16px;
  color: #64748B;
  font-weight: 700;
  width: 32%;
  background: #F8FAFC;
  text-align: left;
}

.specs-full-table td {
  padding: 14px 16px;
  color: var(--dark-900);
  font-weight: 600;
}

/* Box Contents Grid */
.box-contents-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 18px;
}

.content-item-card {
  display: flex;
  align-items: center;
  gap: 16px;
  background: #F8FAFC;
  border: 1px solid #E2E8F0;
  border-radius: 14px;
  padding: 16px;
}

.content-item-icon {
  font-size: 1.8rem;
  flex-shrink: 0;
}

.content-item-card strong {
  display: block;
  font-size: 0.95rem;
  color: var(--dark-900);
  margin-bottom: 2px;
}

.content-item-card p {
  font-size: 0.8rem;
  color: #64748B;
  margin: 0;
  line-height: 1.35;
}

/* Tab FAQs */
.tab-faq-list {
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.tab-faq-item {
  background: #F8FAFC;
  border: 1px solid #E2E8F0;
  border-radius: 12px;
  padding: 18px 20px;
}

.tab-faq-item strong {
  display: block;
  font-size: 0.95rem;
  color: var(--dark-900);
  margin-bottom: 6px;
}

.tab-faq-item p {
  font-size: 0.86rem;
  color: #64748B;
  line-height: 1.5;
  margin: 0;
}

/* 2. Reviews Section */
.product-reviews-section {
  padding: 70px 0;
  background: #FFFFFF;
}

.reviews-header-block {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
  margin-bottom: 32px;
}

.rating-overview-card {
  background: #F8FAFC;
  border: 1.5px solid #E2E8F0;
  border-radius: 20px;
  padding: 28px 36px;
  display: grid;
  grid-template-columns: 260px 1fr;
  gap: 36px;
  align-items: center;
  margin-bottom: 36px;
}

.rating-score-box {
  text-align: center;
  border-right: 1px solid #E2E8F0;
  padding-right: 28px;
}

.rating-big-num {
  font-size: 3.5rem;
  font-weight: 900;
  font-family: var(--font-heading);
  color: var(--dark-900);
  line-height: 1;
}

.rating-big-stars {
  color: #FFCC00;
  font-size: 1.4rem;
  margin: 6px 0;
  letter-spacing: 2px;
}

.rating-total-reviews {
  font-size: 0.8rem;
  font-weight: 700;
  color: #64748B;
}

.rating-bars-box {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.rating-bar-row {
  display: flex;
  align-items: center;
  gap: 14px;
  font-size: 0.82rem;
  font-weight: 700;
  color: #475569;
}

.bar-star-label {
  width: 55px;
}

.bar-track {
  flex: 1;
  height: 8px;
  background: #E2E8F0;
  border-radius: 9999px;
  overflow: hidden;
}

.bar-fill {
  height: 100%;
  background: #FFCC00;
  border-radius: 9999px;
}

.bar-pct {
  width: 38px;
  text-align: right;
  color: #64748B;
}

.reviews-cards-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.review-comment-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 16px;
  padding: 22px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
}

.review-card-top {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 12px;
}

.reviewer-avatar {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  background: #2563EB;
  color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 900;
  font-size: 0.95rem;
  flex-shrink: 0;
}

.reviewer-meta {
  flex: 1;
  min-width: 0;
}

.reviewer-meta strong {
  display: block;
  font-size: 0.92rem;
  color: var(--dark-900);
  line-height: 1.2;
}

.reviewer-meta span {
  font-size: 0.74rem;
  color: #64748B;
}

.review-verified-badge {
  background: #ECFDF5;
  color: #065F46;
  border: 1px solid #A7F3D0;
  font-size: 0.72rem;
  font-weight: 800;
  padding: 3px 8px;
  border-radius: 9999px;
}

.review-stars-row {
  color: #FFCC00;
  font-size: 0.9rem;
  margin-bottom: 8px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.review-date {
  color: #94A3B8;
  font-size: 0.74rem;
}

.review-title {
  font-size: 1rem;
  font-weight: 800;
  color: var(--dark-900);
  margin-bottom: 6px;
  line-height: 1.3;
}

.review-text {
  font-size: 0.86rem;
  color: #475569;
  line-height: 1.5;
  margin: 0;
}

/* 3. Related Products Section */
.related-products-section {
  padding: 60px 0 80px 0;
  background: #F8FAFC;
  border-top: 1px solid var(--border-light);
}

.related-products-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}

.related-prod-card {
  background: #FFFFFF;
  border: 1.5px solid #E2E8F0;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.03);
  position: relative;
  display: flex;
  flex-direction: column;
  transition: transform 0.25s ease, border-color 0.25s ease, box-shadow 0.25s ease;
}

.related-prod-card:hover {
  transform: translateY(-4px);
  border-color: #FFCC00;
  box-shadow: 0 8px 24px rgba(255, 204, 0, 0.22);
}

.related-badge {
  position: absolute;
  top: 10px;
  left: 10px;
  background: #0B0E17;
  color: #FFFFFF;
  font-size: 0.68rem;
  font-weight: 800;
  padding: 3px 8px;
  border-radius: 6px;
  z-index: 2;
}

.related-img-link {
  display: flex;
  align-items: center;
  justify-content: center;
  height: 180px;
  background: #F8FAFC;
  padding: 14px;
  border-bottom: 1px solid #F1F5F9;
}

.related-img-link img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

.related-info {
  padding: 16px;
  display: flex;
  flex-direction: column;
  flex: 1;
}

.related-rating {
  color: #FFCC00;
  font-size: 0.8rem;
  margin-bottom: 4px;
}

.related-rating span {
  color: #64748B;
  font-weight: 700;
  font-size: 0.75rem;
}

.related-title {
  font-size: 0.94rem;
  font-weight: 800;
  color: var(--dark-900);
  margin-bottom: 10px;
  line-height: 1.3;
  flex: 1;
}

.related-title a {
  text-decoration: none;
  color: inherit;
}

.related-price-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 14px;
}

.rel-price-now {
  font-size: 1.15rem;
  font-weight: 900;
  color: var(--dark-900);
}

.rel-price-old {
  font-size: 0.84rem;
  color: #94A3B8;
  text-decoration: line-through;
}

/* ==========================================================================
   MOBILE RESPONSIVENESS FOR NEW SECTIONS & HERO SLIDER CLEANUP
   ========================================================================== */
@media (max-width: 768px) {
  /* HIDE ALL BULKY TEXT & BUTTONS IN HERO SLIDER ON MOBILE SO THE BANNERS SHINE UNCLUTTERED */
  .hero-slider-section .slide-content {
    display: none !important;
  }

  .hero-slider-section .slide-visual-card {
    display: block !important;
    width: 100% !important;
    max-width: 350px !important;
    margin: 8px auto 0 auto !important;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45) !important;
  }

  .hero-slider-section .slide {
    padding: 10px 0 20px 0 !important;
  }

  /* Single Product Info Tabs on Mobile */
  .info-tab-content-area {
    padding: 20px 16px !important;
  }

  .how-it-works-steps-grid {
    grid-template-columns: 1fr !important;
    gap: 14px !important;
  }

  .hw-step-box {
    padding: 16px !important;
  }

  .specs-full-table th {
    width: 40% !important;
    font-size: 0.8rem !important;
    padding: 10px 8px !important;
  }

  .specs-full-table td {
    font-size: 0.8rem !important;
    padding: 10px 8px !important;
  }

  .box-contents-grid {
    grid-template-columns: 1fr !important;
    gap: 12px !important;
  }

  /* Reviews on Mobile */
  .rating-overview-card {
    grid-template-columns: 1fr !important;
    padding: 20px 16px !important;
    gap: 20px !important;
  }

  .rating-score-box {
    border-right: none !important;
    border-bottom: 1px solid #E2E8F0 !important;
    padding-right: 0 !important;
    padding-bottom: 18px !important;
  }

  .rating-big-num {
    font-size: 2.8rem !important;
  }

  .reviews-cards-grid {
    grid-template-columns: 1fr !important;
    gap: 14px !important;
  }

  .review-comment-card {
    padding: 16px 14px !important;
  }

  /* Related Products on Mobile (2 columns) */
  .related-products-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 12px !important;
  }

  .related-img-link {
    height: 125px !important;
    padding: 8px !important;
  }

  .related-info {
    padding: 10px !important;
  }

  .related-title {
    font-size: 0.8rem !important;
    margin-bottom: 6px !important;
  }

  .rel-price-now {
    font-size: 0.95rem !important;
  }

  .rel-price-old {
    font-size: 0.72rem !important;
  }

  .related-info .btn {
    padding: 6px 8px !important;
    font-size: 0.72rem !important;
  }
}
"""

css += "\n" + single_prod_and_hero_css

with open("assets/css/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Saved updated style.css with complete Single Product sections & Mobile Hero Slider Cleanup!")
