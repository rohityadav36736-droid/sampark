import re
import glob

print("=== Starting Comprehensive Execution of All 6 Fixes ===")

# =========================================================================
# FIX 5: Remove stray `">` and path fragment from index.html (and any other file)
# =========================================================================
for fpath in glob.glob("*.html"):
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Look for stray <path or </svg>">
    modified = False
    lines = content.splitlines()
    new_lines = []
    for line in lines:
        if "<path d='M12" in line and not line.strip().startswith("<link") and not line.strip().startswith("<svg"):
            print(f"Removed stray line in {fpath}: {line.strip()[:60]}")
            modified = True
            continue
        if line.strip() in ['">', '">', '">']:
            print(f"Removed stray `\">` in {fpath}")
            modified = True
            continue
        new_lines.append(line)

    if modified:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write("\n".join(new_lines) + "\n")
        print(f"Saved cleaned {fpath}")

# Specifically check index.html head
with open("index.html", "r", encoding="utf-8") as f:
    idx_content = f.read()

# Remove the exact stray snippet if present
stray_pattern = r"\s*<path d='M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5'/></svg>\">"
if re.search(stray_pattern, idx_content):
    idx_content = re.sub(stray_pattern, "", idx_content)
    print("Cleaned stray snippet from index.html")

# =========================================================================
# FIX 1 (HERO SLIDER): Add class `shark-tank-slide` to Slide 2 in index.html
# =========================================================================
idx_content = idx_content.replace(
    '      <!-- Slide 2: Real Shark Tank India Featured -->\n      <div class="slide">',
    '      <!-- Slide 2: Real Shark Tank India Featured -->\n      <div class="slide shark-tank-slide">'
)

# =========================================================================
# FIX 3 (TAG STUDIO): Prevent title wrapping clipping & improve tag studio markup in index.html
# =========================================================================
old_studio_title = """          <h2 style="font-size:clamp(1.75rem, 2.8vw, 2.3rem); font-weight:800; margin-bottom:12px;">
            Preview Your Custom Tag <span style="color:var(--primary); background:var(--dark-900); padding:2px 10px; border-radius:6px;">In Real-Time</span>
          </h2>"""

new_studio_title = """          <h2 class="tag-studio-heading">
            Preview Your Custom Tag <span class="tag-studio-badge">In Real-Time</span>
          </h2>"""

if old_studio_title in idx_content:
    idx_content = idx_content.replace(old_studio_title, new_studio_title)
    print("Updated tag studio title in index.html")

# Change tag studio form container style attribute to class="customizer-form-card"
idx_content = idx_content.replace(
    '<div style="background:#FFFFFF; border:1px solid #E2E8F0; border-radius:var(--radius-lg); padding:24px; box-shadow:var(--shadow-sm); display:flex; flex-direction:column; gap:16px;">',
    '<div class="customizer-form-card">'
)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(idx_content)
print("Saved index.html successfully!")


# =========================================================================
# FIX 2 (ACCOUNT.HTML BUTTONS GAP - IMAGE 2):
# =========================================================================
with open("account.html", "r", encoding="utf-8") as f:
    acc_content = f.read()

# Replace the text-align:right wrapper with tag-actions-wrapper
acc_content = re.sub(
    r'<div style="text-align:right;">\s*<div style="font-size:0.8rem; color:#64748B; margin-bottom:6px;">Total Scans: <strong>(\d+)</strong></div>\s*<div class="tag-card-actions">',
    r'<div class="tag-actions-wrapper">\n                <div class="tag-scans-count">Total Scans: <strong>\1</strong></div>\n                <div class="tag-card-actions">',
    acc_content
)

with open("account.html", "w", encoding="utf-8") as f:
    f.write(acc_content)
print("Saved account.html successfully with tag-actions-wrapper!")


# =========================================================================
# CSS FIXES in assets/css/style.css:
# 1. Product single gallery styling (.gallery-main-view, .gallery-thumbnails, .gallery-thumb)
# 2. Account tag-card-actions grid & gap (Image 2)
# 3. Interactive tag studio responsive blowout fix (Image 3)
# 4. Marquee reviews white shadow fix (Image 4)
# 5. Shark Tank slide 2 hide text & buttons on mobile (Image 2 Hero)
# =========================================================================
with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css_content = f.read()

new_styles_block = """
/* ==========================================================================
   GALLERY STYLING FOR SINGLE PRODUCT PAGE (FIXES 3 GIANT STACKED IMAGES - IMAGE 1)
   ========================================================================== */
.gallery-main-view {
  width: 100%;
  height: 380px;
  background: #F8FAFC;
  border: 1.5px solid var(--border-light);
  border-radius: 20px;
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 14px;
}

.gallery-main-view img {
  max-width: 90%;
  max-height: 90%;
  object-fit: contain;
  transition: transform 0.3s ease;
}

.gallery-thumbnails {
  display: flex;
  gap: 12px;
  overflow-x: auto;
  padding: 4px 2px 8px 2px;
  scrollbar-width: none;
}

.gallery-thumbnails::-webkit-scrollbar {
  display: none;
}

.gallery-thumb {
  width: 76px;
  height: 76px;
  min-width: 76px;
  border-radius: 14px;
  border: 2px solid #E2E8F0;
  background: #FFFFFF;
  padding: 4px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
}

.gallery-thumb.active,
.gallery-thumb:hover {
  border-color: #FFCC00;
  box-shadow: 0 4px 14px rgba(255, 204, 0, 0.3);
  transform: translateY(-2px);
}

.gallery-thumb img {
  max-width: 100%;
  max-height: 100%;
  object-fit: contain;
}

@media (max-width: 768px) {
  .gallery-main-view {
    height: 250px;
    border-radius: 16px;
    margin-bottom: 10px;
  }
  .gallery-thumb {
    width: 60px;
    height: 60px;
    min-width: 60px;
    border-radius: 10px;
  }
}

/* ==========================================================================
   ACCOUNT TAG BUTTONS GRID & GAP (FIXES IMAGE 2 - ZERO GAP ISSUE)
   ========================================================================== */
.tag-actions-wrapper {
  text-align: right;
}

.tag-scans-count {
  font-size: 0.82rem;
  color: #64748B;
  margin-bottom: 8px;
}

.tag-card-actions {
  display: flex !important;
  gap: 14px !important;
  align-items: center !important;
  justify-content: flex-end !important;
}

.tag-card-actions .btn {
  margin: 0 !important;
  padding: 8px 16px !important;
  font-weight: 700 !important;
}

@media (max-width: 768px) {
  .tag-actions-wrapper {
    width: 100% !important;
    text-align: left !important;
    margin-top: 12px !important;
    display: flex !important;
    flex-direction: column !important;
    gap: 8px !important;
  }

  .tag-scans-count {
    margin-bottom: 0 !important;
    font-size: 0.8rem !important;
  }

  .tag-card-actions {
    width: 100% !important;
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
    gap: 14px !important;
    justify-content: stretch !important;
  }

  .tag-card-actions .btn {
    width: 100% !important;
    min-height: 42px !important;
    font-size: 0.86rem !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    border-radius: 12px !important;
  }
}

/* ==========================================================================
   TAG STUDIO RESPONSIVE FIT (FIXES IMAGE 3 - RIGHT MARGIN CLIPPING)
   ========================================================================== */
.tag-studio-heading {
  font-size: clamp(1.5rem, 2.5vw, 2.2rem);
  font-weight: 800;
  margin-bottom: 12px;
  line-height: 1.3;
}

.tag-studio-badge {
  color: var(--primary);
  background: var(--dark-900);
  padding: 2px 10px;
  border-radius: 6px;
  display: inline-block;
  white-space: nowrap;
}

.customizer-form-card {
  background: #FFFFFF;
  border: 1px solid #E2E8F0;
  border-radius: var(--radius-lg);
  padding: 24px;
  box-shadow: var(--shadow-sm);
  display: flex;
  flex-direction: column;
  gap: 16px;
  width: 100%;
  box-sizing: border-box;
}

@media (max-width: 768px) {
  .customizer-grid {
    grid-template-columns: 1fr !important;
    gap: 20px !important;
    width: 100% !important;
    overflow: hidden !important;
  }

  .customizer-form-side {
    min-width: 0 !important;
    width: 100% !important;
    box-sizing: border-box !important;
  }

  .customizer-form-card {
    padding: 16px 14px !important;
    border-radius: 16px !important;
    gap: 14px !important;
  }

  .tag-studio-heading {
    font-size: 1.35rem !important;
    line-height: 1.25 !important;
  }

  .tag-studio-badge {
    margin-top: 4px;
    font-size: 0.9em;
  }

  .customizer-preview-box {
    padding: 22px 12px !important;
    width: 100% !important;
    box-sizing: border-box !important;
    border-radius: 20px !important;
    overflow: hidden !important;
  }

  .custom-tag-preview {
    max-width: 290px !important;
    width: 100% !important;
    padding: 16px 12px !important;
    margin-top: 14px !important;
    box-sizing: border-box !important;
  }

  .customizer-form-card select,
  .customizer-form-card input {
    font-size: 0.88rem !important;
    padding: 10px 12px !important;
  }
}

/* ==========================================================================
   MARQUEE REVIEWS WHITE SHADOW FIX (FIXES IMAGE 4 - ALL TEXT HIDDEN)
   ========================================================================== */
@media (max-width: 768px) {
  .marquee-reviews-section::before,
  .marquee-reviews-section::after {
    display: none !important;
  }
}

@media (min-width: 769px) {
  /* On desktop, only fade the card track, not the header text */
  .marquee-reviews-section::before,
  .marquee-reviews-section::after {
    top: 170px !important;
    bottom: 30px !important;
    width: 120px !important;
  }
}

/* ==========================================================================
   HERO SLIDE 2 PHONE VIEW CLEANUP (FIXES IMAGE 2 HERO - HIDE TEXT & BUTTONS)
   ========================================================================== */
@media (max-width: 768px) {
  .hero-slider-section .slide.shark-tank-slide .slide-content {
    display: none !important;
  }

  .hero-slider-section .slide.shark-tank-slide .slide-visual-card {
    display: block !important;
    width: 100% !important;
    max-width: 350px !important;
    margin: 8px auto 0 auto !important;
    box-shadow: 0 16px 40px rgba(0, 0, 0, 0.45) !important;
  }

  .hero-slider-section .slide.shark-tank-slide .visual-mockup-wrapper img {
    max-height: 200px !important;
    width: 100% !important;
    object-fit: cover !important;
    border-radius: 14px !important;
  }
}
"""

css_content += "\n" + new_styles_block

with open("assets/css/style.css", "w", encoding="utf-8") as f:
    f.write(css_content)

print("Saved updated style.css with all fixes!")
print("=== All 6 Fixes Applied Successfully ===")
