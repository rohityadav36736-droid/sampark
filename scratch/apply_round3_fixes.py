import re

print("=== Starting Round 3 Fixes ===")

# =========================================================================
# 1. EXTRACT MARQUEE REVIEWS HTML FROM index.html
# =========================================================================
with open("index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

# Find the exact marquee container from index.html
marquee_start = idx_content.find('<div class="marquee-container">')
marquee_end = idx_content.find('</section>', marquee_start)

if marquee_start != -1 and marquee_end != -1:
    marquee_container_html = idx_content[marquee_start:marquee_end].strip()
    print(f"Extracted marquee container from index.html (length {len(marquee_container_html)})")
else:
    print("ERROR: Could not find marquee container in index.html")
    marquee_container_html = ""

# =========================================================================
# 2. UPDATE product-single.html
# Replace static reviews cards with the dual moving marquee container!
# And ensure headings are left-aligned (start side).
# =========================================================================
with open("product-single.html", "r", encoding="utf-8") as f:
    ps_content = f.read()

# Replace <div class="reviews-cards-grid">...</div> with marquee_container_html
new_reviews_section = f"""  <!-- Verified Customer Reviews Section (Dual-Direction Infinite Moving Marquee from Home) -->
  <section class="marquee-reviews-section product-marquee-reviews" id="customer-reviews" style="padding: 60px 0;">
    <div class="container">
      <div class="section-header" style="max-width: 100% !important; margin: 0 0 24px 0 !important; text-align: left !important;">
        <div class="section-tag" style="margin-left: 0 !important; display: inline-flex !important;">50,000+ Happy Drivers</div>
        <h2 style="text-align: left !important; margin-left: 0 !important;">Delhi NCR Drivers Trust Sampark</h2>
        <p style="text-align: left !important; margin-left: 0 !important;">Continuous feedback from verified vehicle owners across Delhi, Gurgaon, Noida, Faridabad, and Ghaziabad.</p>
      </div>

      <!-- Rating Summary Overview Card -->
      <div class="rating-overview-card" style="margin-bottom: 30px;">
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
    </div>

    <!-- Dual Infinite Moving Marquee from Home Page -->
    {marquee_container_html}
  </section>"""

# Replace the existing product-reviews-section with new_reviews_section
ps_content = re.sub(
    r'<!-- Verified Customer Reviews Section -->[\s\S]*?</section>\s*(?=\s*<!-- Related Products)',
    new_reviews_section + '\n\n',
    ps_content
)

# Also ensure product-info-details-section header and related-products-section header start from left
ps_content = ps_content.replace(
    '<div class="section-header" style="text-align:left; margin-bottom:28px;">',
    '<div class="section-header" style="max-width: 100% !important; margin: 0 0 24px 0 !important; text-align: left !important;">'
)

with open("product-single.html", "w", encoding="utf-8") as f:
    f.write(ps_content)

print("Saved product-single.html with Home Page Dual Marquee Reviews & Left Aligned Headers!")


# =========================================================================
# 3. UPDATE assets/css/style.css
# 1. Desktop Start-Side Alignment for single product headers (Fixes Image 1)
# 2. Hero mobile sticker image size increase (Fixes Image 2)
# =========================================================================
with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

round3_css = """
/* ==========================================================================
   ROUND 3 ENHANCEMENTS: START-SIDE HEADERS & LARGE MOBILE HERO STICKER
   ========================================================================== */

/* 1. Desktop Start-Side Alignment for Single Product Page (Fixes Image 1) */
.product-info-details-section .section-header,
.product-marquee-reviews .section-header,
.product-reviews-section .section-header,
.related-products-section .section-header {
  max-width: 100% !important;
  margin: 0 0 24px 0 !important;
  text-align: left !important;
  padding: 0 !important;
}

.product-info-details-section .section-header .section-tag,
.product-marquee-reviews .section-header .section-tag,
.product-reviews-section .section-header .section-tag,
.related-products-section .section-header .section-tag {
  margin-left: 0 !important;
  margin-right: auto !important;
  display: inline-flex !important;
}

.product-info-details-section .section-header h2,
.product-marquee-reviews .section-header h2,
.product-reviews-section .section-header h2,
.related-products-section .section-header h2 {
  margin-left: 0 !important;
  text-align: left !important;
}

.product-info-details-section .section-header p,
.product-marquee-reviews .section-header p,
.product-reviews-section .section-header p,
.related-products-section .section-header p {
  margin-left: 0 !important;
  text-align: left !important;
}

/* 2. Much Larger & Bolder Mobile Hero Sticker Image (Fixes Image 2) */
@media (max-width: 768px) {
  .hero-slider-section .slide-visual-card {
    width: 100% !important;
    max-width: 360px !important;
    margin: 8px auto 0 auto !important;
    padding: 16px 14px 14px 14px !important;
  }

  .hero-slider-section .slide-visual-card .visual-mockup-wrapper {
    height: 245px !important;
    padding: 4px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    background: #F8FAFC !important;
    border-radius: 18px !important;
    margin-bottom: 12px !important;
    overflow: hidden !important;
  }

  .hero-slider-section .slide-visual-card .visual-mockup-wrapper img {
    max-height: 235px !important;
    max-width: 100% !important;
    width: auto !important;
    height: auto !important;
    object-fit: contain !important;
    transform: scale(1.3) !important;
    display: block !important;
    margin: 0 auto !important;
    filter: drop-shadow(0 12px 24px rgba(0, 0, 0, 0.22)) !important;
  }
}
"""

css += "\n" + round3_css

with open("assets/css/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Saved assets/css/style.css with start-side alignment and large hero mobile image!")
print("=== Round 3 Fixes Complete ===")
