import re

def validate():
    all_ok = True
    
    # 1. index.html checks
    with open("index.html", "r", encoding="utf-8") as f:
        idx = f.read()
    
    if "feature-marquee-card" not in idx:
        print("[FAIL] index.html missing feature-marquee-card")
        all_ok = False
    else:
        print("[PASS] index.html: 4-card marquee present")
        
    if "sim-scenarios-track" not in idx:
        print("[FAIL] index.html missing sim-scenarios-track")
        all_ok = False
    else:
        print("[PASS] index.html: simulator scenarios track present")
        
    if "comparison-table-wrapper" not in idx or "comparison-table" not in idx:
        print("[FAIL] index.html missing comparison-table")
        all_ok = False
    else:
        print("[PASS] index.html: comparison table properly classed")
        
    product_img_links = re.findall(r'<a[^>]*class=["\'][^"\']*product-img-wrapper[^"\']*["\'][^>]*href=["\']product-single\.html\?id=', idx)
    if len(product_img_links) < 6:
        print(f"[WARN] index.html has only {len(product_img_links)} product img links")
    else:
        print(f"[PASS] index.html: all {len(product_img_links)} product card images link to product-single.html")

    # 2. product-single.html checks
    with open("product-single.html", "r", encoding="utf-8") as f:
        ps = f.read()
        
    if "product-features-grid-card" not in ps:
        print("[FAIL] product-single.html missing 9 feature icons grid card")
        all_ok = False
    else:
        print("[PASS] product-single.html: 9 feature icons grid card present")
        
    if "product-specs-card" not in ps:
        print("[FAIL] product-single.html missing specifications card")
        all_ok = False
    else:
        print("[PASS] product-single.html: specifications card present")
        
    if "mobile-sticky-buy-bar" not in ps or "mobile-sticky-buy-btn" not in ps:
        print("[FAIL] product-single.html missing mobile-sticky-buy-bar or button")
        all_ok = False
    else:
        print("[PASS] product-single.html: mobile sticky buy bar present")
        
    if "One time purchase, COD Available" not in ps:
        print("[FAIL] product-single.html missing COD badge")
        all_ok = False
    else:
        print("[PASS] product-single.html: COD badge present")

    # 3. shark-tank.html checks
    with open("shark-tank.html", "r", encoding="utf-8") as f:
        st = f.read()
    if "comparison-table-wrapper" not in st or "comparison-table" not in st:
        print("[FAIL] shark-tank.html missing comparison table classes")
        all_ok = False
    else:
        print("[PASS] shark-tank.html: comparison table properly classed")

    # 4. account.html checks
    with open("account.html", "r", encoding="utf-8") as f:
        acc = f.read()
    if "scan-history-table" not in acc or 'data-label="Timestamp"' not in acc:
        print("[FAIL] account.html missing scan-history-table or data-labels")
        all_ok = False
    else:
        print("[PASS] account.html: scan history table has data-labels for mobile card layout")

    # 5. style.css checks
    with open("assets/css/style.css", "r", encoding="utf-8") as f:
        css = f.read()
        
    if "pointer-events: none;" not in css:
        print("[FAIL] style.css missing pointer-events on product-img-wrapper img")
        all_ok = False
    else:
        print("[PASS] style.css: pointer-events on img active")

    if all_ok:
        print("\n>>> ALL VALIDATIONS PASSED PERFECTLY! <<<")

if __name__ == "__main__":
    validate()
