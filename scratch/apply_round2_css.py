print("=== Starting Round 2 CSS Polish ===")

with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

round2_css = """
/* ==========================================================================
   ROUND 2 ENHANCEMENTS: FAQ 2-COLUMN, TAG ACTIONS GAP, SLIDE 2 BANNER, SIM PHONE
   ========================================================================== */

/* 1. Account Tag Card Actions Gap (Fixes Image 5) */
.tag-card-actions {
  display: flex;
  gap: 12px;
  align-items: center;
  justify-content: flex-end;
}

@media (max-width: 768px) {
  .tag-card-actions {
    width: 100% !important;
    display: flex !important;
    gap: 12px !important;
    margin-top: 10px !important;
    justify-content: stretch !important;
  }
  .tag-card-actions .btn {
    flex: 1 !important;
    min-height: 40px !important;
    font-weight: 700 !important;
    border-radius: 10px !important;
    text-align: center !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
  }
}

/* 2. FAQ Accordion 2-Column / 2-Row Layout (Fixes Image 4) */
.faq-list {
  max-width: 1100px !important;
  margin: 0 auto !important;
  display: grid !important;
  grid-template-columns: repeat(2, 1fr) !important;
  gap: 16px 24px !important;
  align-items: start !important;
}

@media (max-width: 820px) {
  .faq-list {
    grid-template-columns: 1fr !important;
    gap: 12px !important;
  }
}

/* 3. Hero Slide 2 Banner Phone View (Fixes Image 2) */
@media (max-width: 768px) {
  .slide:nth-child(2) .slide-content {
    display: none !important;
  }
  .slide:nth-child(2) .slide-visual-card {
    display: block !important;
    margin: 10px auto 0 auto !important;
    max-width: 360px !important;
    width: 100% !important;
  }
  .slide:nth-child(2) .slide-visual-card .visual-mockup-wrapper img {
    max-height: 190px !important;
    object-fit: cover !important;
    border-radius: 14px !important;
  }
}

/* 4. Pixel-Perfect Phone Simulator Screen (Fixes Image 3) */
.sim-phone-screen {
  background: #0B0E17 !important;
  border: 3.5px solid #1E293B !important;
  border-radius: 36px !important;
  padding: 24px 20px !important;
  color: #FFFFFF !important;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.55), 0 0 0 1px rgba(255, 255, 255, 0.08) !important;
  max-width: 330px !important;
  margin: 0 auto !important;
  text-align: center !important;
  position: relative !important;
  box-sizing: border-box !important;
}

.sim-phone-notch {
  width: 76px !important;
  height: 5.5px !important;
  background: #334155 !important;
  border-radius: 9999px !important;
  margin: 0 auto 16px auto !important;
}

.sim-screen-header {
  font-size: 0.72rem !important;
  color: #94A3B8 !important;
  letter-spacing: 0.08em !important;
  font-weight: 800 !important;
  text-transform: uppercase !important;
  margin-bottom: 16px !important;
}

.sim-shield-badge {
  width: 64px !important;
  height: 64px !important;
  border-radius: 50% !important;
  background: #171D2D !important;
  border: 2.5px solid #FFCC00 !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  margin: 0 auto 14px auto !important;
  box-shadow: 0 0 24px rgba(255, 204, 0, 0.28) !important;
}

.sim-screen-title {
  color: #FFFFFF !important;
  font-size: 1.25rem !important;
  font-weight: 900 !important;
  margin-bottom: 4px !important;
  letter-spacing: -0.01em !important;
}

.sim-screen-sub {
  font-size: 0.86rem !important;
  color: #10B981 !important;
  font-weight: 800 !important;
  margin-bottom: 16px !important;
}

.sim-scenario-bubble {
  background: #151A26 !important;
  border: 1px solid rgba(255, 255, 255, 0.09) !important;
  border-radius: 14px !important;
  padding: 14px 16px !important;
  margin: 0 0 20px 0 !important;
  text-align: left !important;
  font-size: 0.84rem !important;
  color: #E2E8F0 !important;
  line-height: 1.45 !important;
  min-height: 52px !important;
}

.sim-call-actions {
  display: flex !important;
  justify-content: space-around !important;
  align-items: center !important;
  padding: 0 10px !important;
}

.sim-call-btn {
  width: 52px !important;
  height: 52px !important;
  border-radius: 50% !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  border: none !important;
  cursor: pointer !important;
  transition: transform 0.15s ease, box-shadow 0.15s ease !important;
}

.sim-call-btn:hover {
  transform: scale(1.08) !important;
}

.sim-call-btn.btn-decline {
  background: #EF4444 !important;
  color: #FFFFFF !important;
  font-size: 1.25rem !important;
  box-shadow: 0 8px 20px rgba(239, 68, 68, 0.4) !important;
}

.sim-call-btn.btn-accept {
  background: #10B981 !important;
  box-shadow: 0 8px 20px rgba(16, 185, 129, 0.45) !important;
}

@media (max-width: 768px) {
  .sim-phone-screen {
    max-width: 295px !important;
    padding: 20px 16px !important;
    border-radius: 28px !important;
  }
}

/* 5. Single Product Page Bottom 2-Column Grid (Desktop & Mobile) */
.product-bottom-details-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 32px;
  margin-top: 44px;
  align-items: start;
}

.product-bottom-details-grid .product-features-grid-card,
.product-bottom-details-grid .product-specs-card {
  margin: 0 !important;
  height: 100%;
}

@media (max-width: 992px) {
  .product-bottom-details-grid {
    grid-template-columns: 1fr !important;
    gap: 20px !important;
    margin-top: 24px !important;
  }
}

/* Product features grid vector icon styling */
.feature-grid-icon svg {
  display: block;
}
"""

css += "\n" + round2_css

with open("assets/css/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Saved updated style.css with Round 2 enhancements!")
