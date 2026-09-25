import re, os

# ==========================================
# 1. UPDATE ASSETS/CSS/STYLE.CSS
# ==========================================
with open('assets/css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make sure product-img-wrapper is styled as clickable link
if '.product-img-wrapper {' in css:
    css = css.replace('.product-img-wrapper {\n  background: #F8FAFC;', '.product-img-wrapper {\n  display: flex;\n  text-decoration: none;\n  cursor: pointer;\n  background: #F8FAFC;')

# Add Feature Cards Marquee CSS and Single Product Page CSS and Comparison Table CSS
additional_css = '''
/* ==========================================================================
   FEATURE CARDS MARQUEE (REPLACES 4 STATIC CARDS & PILL TICKER)
   ========================================================================== */
.feature-cards-marquee-section {
  background: #FFFFFF;
  border-top: 1px solid rgba(255, 204, 0, 0.35);
  border-bottom: 1px solid var(--border-light);
  overflow: hidden;
  user-select: none;
  position: relative;
  width: 100%;
  padding: 14px 0;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.03);
  z-index: 10;
}

.feature-marquee-container {
  display: flex;
  overflow: hidden;
  width: 100%;
}

.feature-marquee-track {
  display: flex;
  width: max-content;
  gap: 16px;
  animation: featureCardLoop 24s linear infinite;
  will-change: transform;
}

.feature-cards-marquee-section:hover .feature-marquee-track {
  animation-play-state: paused;
}

.feature-marquee-card {
  display: flex;
  align-items: center;
  gap: 14px;
  background: #FFFFFF;
  border: 1.5px solid #E2E8F0;
  border-radius: 16px;
  padding: 12px 18px;
  width: 320px;
  min-width: 320px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
  flex-shrink: 0;
  transition: transform 0.2s ease, border-color 0.2s ease, box-shadow 0.2s ease;
}

.feature-marquee-card:hover {
  transform: translateY(-2px);
  border-color: #FFCC00;
  box-shadow: 0 6px 18px rgba(255, 204, 0, 0.2);
}

.feature-card-icon {
  width: 44px;
  height: 44px;
  min-width: 44px;
  border-radius: 12px;
  background: #FFFDF0;
  border: 1px solid rgba(255, 204, 0, 0.4);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.35rem;
  flex-shrink: 0;
}

.feature-card-info h4 {
  font-size: 0.92rem;
  font-weight: 800;
  color: var(--dark-900);
  margin-bottom: 2px;
  line-height: 1.25;
}

.feature-card-info p {
  font-size: 0.76rem;
  color: var(--text-muted);
  line-height: 1.35;
  margin: 0;
}

@keyframes featureCardLoop {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}

/* ==========================================================================
   SINGLE PRODUCT PAGE STYLES (MATCHING USER IMAGE 2)
   ========================================================================== */
.product-features-grid-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 20px;
  padding: 22px 16px;
  margin: 20px 0;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px 10px;
  text-align: center;
}

.feature-grid-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 6px;
}

.feature-grid-icon {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
}

.feature-grid-icon.icon-blue { background: #EFF6FF; color: #2563EB; }
.feature-grid-icon.icon-green { background: #ECFDF5; color: #10B981; }
.feature-grid-icon.icon-red { background: #FEF2F2; color: #EF4444; }
.feature-grid-icon.icon-purple { background: #FAF5FF; color: #9333EA; }
.feature-grid-icon.icon-teal { background: #F0FDFA; color: #0D9488; }
.feature-grid-icon.icon-green2 { background: #F0FDF4; color: #16A34A; }
.feature-grid-icon.icon-orange { background: #FFF7ED; color: #EA580C; }
.feature-grid-icon.icon-red2 { background: #FFF1F2; color: #E11D48; }
.feature-grid-icon.icon-orange2 { background: #FEFCE8; color: #CA8A04; }

.feature-grid-label {
  font-size: 0.74rem;
  font-weight: 700;
  color: #1E293B;
  line-height: 1.2;
}

.product-specs-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: 20px;
  padding: 22px;
  margin: 20px 0;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
}

.product-specs-card h3 {
  font-size: 1.15rem;
  font-weight: 800;
  color: var(--dark-900);
  margin-bottom: 14px;
}

.specs-table {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 16px;
}

.specs-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 0.88rem;
  border-bottom: 1px solid #F1F5F9;
  padding-bottom: 8px;
}

.specs-row:last-child {
  border-bottom: none;
}

.specs-label {
  color: #64748B;
  font-weight: 600;
}

.specs-value {
  color: #0F172A;
  font-weight: 800;
}

.specs-highlight-bullet {
  display: flex;
  align-items: flex-start;
  gap: 8px;
  font-size: 0.86rem;
  font-weight: 600;
  color: #1E293B;
  line-height: 1.45;
  background: #FFFDF0;
  border-left: 3px solid #FFCC00;
  padding: 10px 12px;
  border-radius: 0 8px 8px 0;
  margin-bottom: 16px;
}

.specs-checklist {
  display: flex;
  flex-direction: column;
  gap: 8px;
  margin-bottom: 18px;
  font-size: 0.84rem;
  font-weight: 600;
  color: #334155;
}

.checklist-item {
  display: flex;
  align-items: center;
  gap: 8px;
}

.specs-community-note {
  border-top: 1px dashed #CBD5E1;
  padding-top: 14px;
  font-size: 0.84rem;
  color: #475569;
  line-height: 1.5;
}

.specs-community-note p {
  margin-bottom: 6px;
}

/* Sticky Bottom Buy Bar on Mobile (Image 2) */
.mobile-sticky-buy-bar {
  display: none;
}

@media (max-width: 768px) {
  .mobile-sticky-buy-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: #FFFFFF;
    border-top: 1px solid #E2E8F0;
    padding: 12px 18px calc(12px + env(safe-area-inset-bottom, 0px)) 18px;
    box-shadow: 0 -4px 18px rgba(0, 0, 0, 0.08);
    z-index: 999;
  }

  .buy-bar-price .price-val {
    font-size: 1.35rem;
    font-weight: 900;
    color: var(--dark-900);
    line-height: 1;
  }

  .buy-bar-price .price-sub {
    font-size: 0.72rem;
    color: #64748B;
    font-weight: 600;
    margin-top: 2px;
  }

  .buy-bar-btn {
    background: #FFE600 !important;
    color: #000000 !important;
    font-weight: 900 !important;
    font-size: 0.95rem !important;
    border-radius: 9999px !important;
    padding: 12px 32px !important;
    box-shadow: 0 4px 14px rgba(255, 204, 0, 0.4) !important;
    border: none !important;
    cursor: pointer;
  }

  /* Padding at bottom of page to prevent sticky buy bar from covering content */
  .product-single-section {
    padding-bottom: 80px;
  }
}

/* ==========================================================================
   RESPONSIVE COMPARISON TABLE (FIXES IMAGE 1 HORIZONTAL OVERFLOW)
   ========================================================================== */
.comparison-table-wrapper {
  background: #FFFFFF;
  border: 1px solid var(--border-light);
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-sm);
  overflow: hidden;
  width: 100%;
}

.comparison-table {
  width: 100%;
  border-collapse: collapse;
  text-align: left;
  font-size: 0.9rem;
}

@media (max-width: 768px) {
  .comparison-table {
    font-size: 0.76rem;
  }
  .comparison-table th,
  .comparison-table td {
    padding: 10px 6px !important;
    vertical-align: middle;
  }
  .comparison-table th:nth-child(1),
  .comparison-table td:nth-child(1) {
    width: 34%;
  }
  .comparison-table th:nth-child(2),
  .comparison-table td:nth-child(2) {
    width: 33%;
  }
  .comparison-table th:nth-child(3),
  .comparison-table td:nth-child(3) {
    width: 33%;
  }
}

/* ==========================================================================
   RESPONSIVE SCAN HISTORY TABLE (FIXES IMAGE 5 CHOPPED OFF TABLE)
   ========================================================================== */
@media (max-width: 768px) {
  .scan-history-table thead {
    display: none;
  }
  .scan-history-table,
  .scan-history-table tbody {
    display: block;
    width: 100%;
  }
  .scan-history-table tr {
    display: flex;
    flex-direction: column;
    background: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
    padding: 12px 14px;
    margin-bottom: 12px;
    box-shadow: 0 1px 4px rgba(0, 0, 0, 0.03);
    gap: 6px;
  }
  .scan-history-table td {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 2px 0 !important;
    border: none !important;
    font-size: 0.84rem;
  }
  .scan-history-table td::before {
    content: attr(data-label);
    font-weight: 700;
    color: #64748B;
    font-size: 0.76rem;
    text-transform: uppercase;
  }
}
'''

# Now let's adjust mobile hero section in style.css so it looks STYLISH & GOOD LOOKING (Point 6)
old_mobile_hero = '''.slide-content {
    display: none !important;
  }'''

new_mobile_hero = '''.slide-content {
    display: flex !important;
    flex-direction: column;
    align-items: center;
    text-align: center;
    max-width: 100%;
    margin: 0 auto 16px auto;
  }

  .slide-content h1 {
    font-size: 1.45rem !important;
    line-height: 1.25 !important;
    margin-bottom: 8px !important;
    color: #FFFFFF !important;
  }

  .slide-desc {
    display: none !important;
  }

  .slide-trust-row {
    display: none !important;
  }

  .slide-cta-row {
    display: flex !important;
    width: 100%;
    max-width: 340px;
    margin-top: 14px;
    margin-bottom: 0;
  }

  .slide-cta-row .btn {
    width: 100% !important;
  }'''

if old_mobile_hero in css:
    css = css.replace(old_mobile_hero, new_mobile_hero)
    print("Mobile hero updated to stylish layout")

# Append additional css
css += '\n' + additional_css

with open('assets/css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("assets/css/style.css updated successfully!")
