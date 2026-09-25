import re

print("=== Starting CSS Polish Script ===")

with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# 1. Ensure product image wrapper img has pointer-events: none;
if ".product-img-wrapper img {" in css:
    css = css.replace(
        ".product-img-wrapper img {",
        ".product-img-wrapper img {\n  pointer-events: none;\n  user-select: none;"
    )
    print("Added pointer-events: none to .product-img-wrapper img")

# 2. Add / Refine Simulator & Hero Styles at the end of style.css
simulator_and_hero_css = """
/* ==========================================================================
   SIMULATOR ENHANCED RESPONSIVE SYSTEM (DESKTOP CLEAN & MOBILE HORIZONTAL SWIPE)
   ========================================================================== */
.sim-controls-col {
  min-width: 0;
  width: 100%;
}

.sim-headline {
  font-size: 1.3rem;
  font-weight: 800;
  color: var(--dark-900);
  margin-bottom: 10px;
}

.sim-subtext {
  color: var(--text-muted);
  font-size: 0.88rem;
  line-height: 1.5;
  margin-bottom: 18px;
}

.sim-mobile-hint {
  display: none;
}

.sim-scenarios-track {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-bottom: 20px;
  width: 100%;
}

.sim-scenario-btn {
  display: flex;
  align-items: center;
  gap: 12px;
  background: #FFFFFF;
  border: 1.5px solid #E2E8F0;
  border-radius: 14px;
  padding: 12px 16px;
  font-family: inherit;
  cursor: pointer;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  text-align: left;
  width: 100%;
  color: var(--dark-900);
}

.sim-scenario-btn:hover,
.sim-scenario-btn.active {
  border-color: #FFCC00;
  background: #FFFDF0;
  box-shadow: 0 4px 14px rgba(255, 204, 0, 0.25);
  transform: translateY(-1px);
}

.sim-scenario-btn .scen-icon {
  font-size: 1.35rem;
  flex-shrink: 0;
  line-height: 1;
}

.sim-scenario-btn .scen-info {
  display: flex;
  flex-direction: column;
  min-width: 0;
}

.sim-scenario-btn .scen-info strong {
  font-size: 0.9rem;
  color: #0F172A;
  line-height: 1.25;
}

.sim-scenario-btn .scen-info small {
  font-size: 0.74rem;
  color: #64748B;
  font-weight: 600;
  margin-top: 2px;
}

.sim-result-box {
  background: #ECFDF5;
  border: 1px solid #10B981;
  border-radius: 12px;
  padding: 13px 16px;
  font-size: 0.84rem;
  color: #065F46;
  line-height: 1.5;
  box-sizing: border-box;
  width: 100%;
}

@media (max-width: 768px) {
  .simulator-box {
    grid-template-columns: 1fr !important;
    padding: 20px 16px !important;
    gap: 22px !important;
    overflow: hidden !important;
    width: 100% !important;
    box-sizing: border-box !important;
    border-radius: 20px !important;
  }

  .sim-controls-col {
    min-width: 0 !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }

  .sim-headline {
    font-size: 1.15rem !important;
    margin-bottom: 6px !important;
  }

  .sim-subtext {
    font-size: 0.82rem !important;
    line-height: 1.4 !important;
    margin-bottom: 12px !important;
  }

  .sim-mobile-hint {
    display: flex !important;
    align-items: center;
    justify-content: space-between;
    font-size: 0.74rem;
    font-weight: 700;
    color: #475569;
    background: #F8FAFC;
    border: 1px solid #E2E8F0;
    border-radius: 8px;
    padding: 5px 10px;
    margin-bottom: 10px;
  }

  .sim-hint-dots {
    color: #FFCC00;
    letter-spacing: 2px;
    font-size: 0.95rem;
  }

  .sim-scenarios-track {
    flex-direction: row !important;
    overflow-x: auto !important;
    overflow-y: hidden !important;
    scroll-snap-type: x mandatory !important;
    -webkit-overflow-scrolling: touch !important;
    padding: 4px 2px 10px 2px !important;
    gap: 10px !important;
    scrollbar-width: none !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }

  .sim-scenarios-track::-webkit-scrollbar {
    display: none !important;
  }

  .sim-scenario-btn {
    flex: 0 0 220px !important;
    min-width: 220px !important;
    max-width: 220px !important;
    scroll-snap-align: start !important;
    padding: 10px 12px !important;
    box-sizing: border-box !important;
  }

  .sim-result-box {
    padding: 10px 12px !important;
    font-size: 0.78rem !important;
    line-height: 1.4 !important;
    border-radius: 10px !important;
  }

  .sim-phone-screen {
    max-width: 290px !important;
    padding: 18px 14px !important;
    border-radius: 24px !important;
  }
}

/* ==========================================================================
   STYLISH MOBILE HERO SECTION (ULTRA POLISHED & GOOD LOOKING)
   ========================================================================== */
@media (max-width: 768px) {
  .hero-slider-section {
    padding: 0 0 16px 0 !important;
    background: #0B0E17 !important;
  }

  .slide {
    padding: 16px 0 24px 0 !important;
  }

  .slide-content-wrapper {
    padding: 0 14px !important;
  }

  .slide-content {
    margin-bottom: 14px !important;
  }

  .slide-content .section-tag {
    background: rgba(255, 204, 0, 0.15) !important;
    border: 1px solid rgba(255, 204, 0, 0.45) !important;
    color: #FFCC00 !important;
    font-size: 0.72rem !important;
    font-weight: 800 !important;
    padding: 4px 12px !important;
    border-radius: 9999px !important;
    margin-bottom: 10px !important;
    display: inline-flex !important;
    align-items: center !important;
    gap: 6px !important;
  }

  .slide-content h1 {
    font-size: 1.35rem !important;
    font-weight: 900 !important;
    line-height: 1.25 !important;
    color: #FFFFFF !important;
    margin-bottom: 8px !important;
    letter-spacing: -0.02em !important;
  }

  .slide-content h1 .highlight {
    color: #FFCC00 !important;
    text-shadow: 0 0 20px rgba(255, 204, 0, 0.4);
  }

  .slide-visual-card {
    background: linear-gradient(180deg, #FFFFFF 0%, #F8FAFC 100%) !important;
    border-radius: 20px !important;
    padding: 16px 14px !important;
    box-shadow: 0 14px 36px rgba(0, 0, 0, 0.4) !important;
    border: 1.5px solid rgba(255, 204, 0, 0.3) !important;
    max-width: 340px !important;
    width: 100% !important;
    margin: 0 auto !important;
  }

  .visual-card-badge {
    background: #ECFDF5 !important;
    border: 1px solid #10B981 !important;
    color: #065F46 !important;
    font-size: 0.74rem !important;
    font-weight: 800 !important;
    padding: 4px 12px !important;
    margin-bottom: 10px !important;
  }

  .visual-mockup-wrapper img {
    max-height: 140px !important;
    object-fit: contain !important;
  }

  .visual-card-stats {
    display: grid !important;
    grid-template-columns: repeat(3, 1fr) !important;
    gap: 6px !important;
    margin-top: 12px !important;
    padding-top: 10px !important;
    border-top: 1px solid #E2E8F0 !important;
  }

  .visual-stat-number {
    font-size: 0.95rem !important;
    font-weight: 900 !important;
    color: var(--dark-900) !important;
  }

  .visual-stat-label {
    font-size: 0.65rem !important;
    color: #64748B !important;
    font-weight: 700 !important;
  }

  .slide-cta-row {
    flex-direction: column !important;
    gap: 8px !important;
    margin-top: 14px !important;
    max-width: 340px !important;
    width: 100% !important;
  }

  .slide-cta-row .btn {
    width: 100% !important;
    padding: 12px 18px !important;
    font-size: 0.92rem !important;
    border-radius: 9999px !important;
    font-weight: 900 !important;
  }

  .slide-cta-row .btn-primary {
    background: #FFCC00 !important;
    color: #000000 !important;
    box-shadow: 0 4px 16px rgba(255, 204, 0, 0.45) !important;
  }
}
"""

css += "\n" + simulator_and_hero_css

with open("assets/css/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Saved updated style.css with enhanced simulator & stylish mobile hero CSS!")
