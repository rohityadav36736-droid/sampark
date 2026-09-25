import re

shop_products_grid = '''      <!-- Category Filter Tabs -->
      <div class="shop-filter-bar">
        <div class="filter-tabs">
          <button class="filter-tab active" data-category="all">All Tags <span class="filter-count-badge">6</span></button>
          <button class="filter-tab" data-category="car">🚗 Car & Pro <span class="filter-count-badge">3</span></button>
          <button class="filter-tab" data-category="bike">🏍️ Bike & Helmet <span class="filter-count-badge">1</span></button>
          <button class="filter-tab" data-category="fleet">🚛 Fleet & Commercial <span class="filter-count-badge">2</span></button>
        </div>

        <div style="font-size:0.85rem; color:#64748B; font-weight:600;">
          Showing <span id="visible-count" style="color:var(--dark-900); font-weight:800;">6</span> Verified Smart Tags
        </div>
      </div>

      <!-- Products Grid (Landing Page Style Cards) -->
      <div class="products-grid" id="products-grid">

        <!-- Product 1: Car Sampark Tag -->
        <div class="product-card" data-category="car" id="card-car-tag">
          <span class="product-badge-float">🔥 Delhi Bestseller</span>
          <span class="product-badge-discount">60% OFF</span>
          <div class="product-img-wrapper">
            <img src="assets/images/car-tag-hd.jpg" alt="Sampark Car Tag">
          </div>
          <div class="product-details">
            <div class="product-rating">
              <span class="rating-stars">★★★★★</span>
              <span class="rating-count">4.9 (8,420+ Reviews)</span>
            </div>
            <h3 class="product-title">
              <a href="product-single.html?id=car-tag">Sampark Smart Car Tag</a>
            </h3>
            <p class="product-snippet">
              Let people contact you for car parking blocks, vehicle emergencies, or towing warnings with complete privacy.
            </p>
            <div class="product-pricing-row">
              <span class="price-current">₹199</span>
              <span class="price-original">₹499</span>
              <span class="price-save">Save ₹300</span>
            </div>
            <div class="product-action-row">
              <button class="btn btn-outline btn-sm" data-add-cart
                data-id="car-tag"
                data-name="Sampark Smart Car Tag"
                data-price="199"
                data-original="499"
                data-image="assets/images/product-car.jpg">
                Add to Cart
              </button>
              <button class="btn btn-primary btn-sm" data-buy-now
                data-id="car-tag"
                data-name="Sampark Smart Car Tag"
                data-price="199"
                data-original="499"
                data-image="assets/images/product-car.jpg">
                Buy Now
              </button>
            </div>
          </div>
        </div>

        <!-- Product 2: NEW Sampark Pro Elite Tag (NFC + QR) -->
        <div class="product-card" data-category="car" id="card-pro-tag">
          <span class="product-badge-float">⚡ NEW PRO EDITION</span>
          <span class="product-badge-discount">56% OFF</span>
          <div class="product-img-wrapper">
            <img src="assets/images/product-pro-tag.jpg" alt="Sampark Pro Smart Tag">
          </div>
          <div class="product-details">
            <div class="product-rating">
              <span class="rating-stars">★★★★★</span>
              <span class="rating-count">5.0 (1,180+ Reviews)</span>
            </div>
            <h3 class="product-title">
              <a href="product-single.html?id=pro-tag">Sampark Pro Elite Metallic Tag (NFC + QR)</a>
            </h3>
            <p class="product-snippet">
              Flagship smart privacy badge with dual NFC tap + laser QR code. Premium automotive tempered acrylic gloss.
            </p>
            <div class="product-pricing-row">
              <span class="price-current">₹349</span>
              <span class="price-original">₹799</span>
              <span class="price-save">Save ₹450</span>
            </div>
            <div class="product-action-row">
              <button class="btn btn-outline btn-sm" data-add-cart
                data-id="pro-tag"
                data-name="Sampark Pro Elite Metallic Tag"
                data-price="349"
                data-original="799"
                data-image="assets/images/product-pro-tag.jpg">
                Add to Cart
              </button>
              <button class="btn btn-primary btn-sm" data-buy-now
                data-id="pro-tag"
                data-name="Sampark Pro Elite Metallic Tag"
                data-price="349"
                data-original="799"
                data-image="assets/images/product-pro-tag.jpg">
                Buy Now
              </button>
            </div>
          </div>
        </div>

        <!-- Product 3: Commercial & Fleet Tag -->
        <div class="product-card" data-category="fleet" id="card-fleet-tag">
          <span class="product-badge-float">🚛 Fleet / Commercial</span>
          <span class="product-badge-discount">57% OFF</span>
          <div class="product-img-wrapper">
            <img src="assets/images/product-fleet.jpg" alt="Sampark Fleet Tag">
          </div>
          <div class="product-details">
            <div class="product-rating">
              <span class="rating-stars">★★★★★</span>
              <span class="rating-count">4.8 (2,910+ Reviews)</span>
            </div>
            <h3 class="product-title">
              <a href="product-single.html?id=fleet-tag">Commercial & Fleet Vehicle Tag</a>
            </h3>
            <p class="product-snippet">
              Built for commercial cabs, delivery trucks, school vans, and buses. Dual-manager forwarding and 24/7 routing.
            </p>
            <div class="product-pricing-row">
              <span class="price-current">₹299</span>
              <span class="price-original">₹699</span>
              <span class="price-save">Save ₹400</span>
            </div>
            <div class="product-action-row">
              <button class="btn btn-outline btn-sm" data-add-cart
                data-id="fleet-tag"
                data-name="Commercial & Fleet Vehicle Tag"
                data-price="299"
                data-original="699"
                data-image="assets/images/product-fleet.jpg">
                Add to Cart
              </button>
              <button class="btn btn-primary btn-sm" data-buy-now
                data-id="fleet-tag"
                data-name="Commercial & Fleet Vehicle Tag"
                data-price="299"
                data-original="699"
                data-image="assets/images/product-fleet.jpg">
                Buy Now
              </button>
            </div>
          </div>
        </div>

        <!-- Product 4: Moto & Helmet Tag -->
        <div class="product-card" data-category="bike" id="card-bike-tag">
          <span class="product-badge-float">🏍️ Bike & Helmet</span>
          <span class="product-badge-discount">55% OFF</span>
          <div class="product-img-wrapper">
            <img src="assets/images/bike-tag-hd.jpg" alt="Sampark Moto Tag">
          </div>
          <div class="product-details">
            <div class="product-rating">
              <span class="rating-stars">★★★★★</span>
              <span class="rating-count">4.9 (4,180+ Reviews)</span>
            </div>
            <h3 class="product-title">
              <a href="product-single.html?id=bike-tag">Moto & Helmet Emergency Tag</a>
            </h3>
            <p class="product-snippet">
              Compact curved resin badge engineered for two-wheelers, scooter visors, and helmets with crash SOS trigger.
            </p>
            <div class="product-pricing-row">
              <span class="price-current">₹249</span>
              <span class="price-original">₹549</span>
              <span class="price-save">Save ₹300</span>
            </div>
            <div class="product-action-row">
              <button class="btn btn-outline btn-sm" data-add-cart
                data-id="bike-tag"
                data-name="Moto & Helmet Emergency Tag"
                data-price="249"
                data-original="549"
                data-image="assets/images/product-bike.jpg">
                Add to Cart
              </button>
              <button class="btn btn-primary btn-sm" data-buy-now
                data-id="bike-tag"
                data-name="Moto & Helmet Emergency Tag"
                data-price="249"
                data-original="549"
                data-image="assets/images/product-bike.jpg">
                Buy Now
              </button>
            </div>
          </div>
        </div>

        <!-- Product 5: Delhi Family Value Pack -->
        <div class="product-card" data-category="car" id="card-combo-tag">
          <span class="product-badge-float">📦 Family Pack</span>
          <span class="product-badge-discount">63% OFF</span>
          <div class="product-img-wrapper">
            <img src="assets/images/ref-product-gallery.png" alt="Sampark Family Pack">
          </div>
          <div class="product-details">
            <div class="product-rating">
              <span class="rating-stars">★★★★★</span>
              <span class="rating-count">5.0 (1,540+ Reviews)</span>
            </div>
            <h3 class="product-title">
              <a href="product-single.html?id=combo-pack">Delhi Family Combo (2 Cars + 1 Bike)</a>
            </h3>
            <p class="product-snippet">
              Complete vehicle security for the entire family. Manage all 3 tags under a single master mobile dashboard.
            </p>
            <div class="product-pricing-row">
              <span class="price-current">₹449</span>
              <span class="price-original">₹1,199</span>
              <span class="price-save">Save ₹750</span>
            </div>
            <div class="product-action-row">
              <button class="btn btn-outline btn-sm" data-add-cart
                data-id="combo-pack"
                data-name="Delhi Family Combo Pack (2 Cars + 1 Bike)"
                data-price="449"
                data-original="1199"
                data-image="assets/images/ref-product-gallery.png">
                Add to Cart
              </button>
              <button class="btn btn-primary btn-sm" data-buy-now
                data-id="combo-pack"
                data-name="Delhi Family Combo Pack (2 Cars + 1 Bike)"
                data-price="449"
                data-original="1199"
                data-image="assets/images/ref-product-gallery.png">
                Buy Now
              </button>
            </div>
          </div>
        </div>

        <!-- Product 6: Society & Residential Gate Tag -->
        <div class="product-card" data-category="fleet" id="card-society-tag">
          <span class="product-badge-float">🏢 Society & Gate Pass</span>
          <span class="product-badge-discount">58% OFF</span>
          <div class="product-img-wrapper">
            <img src="assets/images/ref-car-pack-1.png" alt="Sampark Society Tag">
          </div>
          <div class="product-details">
            <div class="product-rating">
              <span class="rating-stars">★★★★★</span>
              <span class="rating-count">4.8 (980+ Reviews)</span>
            </div>
            <h3 class="product-title">
              <a href="product-single.html?id=society-tag">Society & RWA Gate Privacy Tag</a>
            </h3>
            <p class="product-snippet">
              Ideal for gated apartments and corporate parking. Direct guard alert with zero personal phone exposure.
            </p>
            <div class="product-pricing-row">
              <span class="price-current">₹229</span>
              <span class="price-original">₹549</span>
              <span class="price-save">Save ₹320</span>
            </div>
            <div class="product-action-row">
              <button class="btn btn-outline btn-sm" data-add-cart
                data-id="society-tag"
                data-name="Society & RWA Gate Privacy Tag"
                data-price="229"
                data-original="549"
                data-image="assets/images/ref-car-pack-1.png">
                Add to Cart
              </button>
              <button class="btn btn-primary btn-sm" data-buy-now
                data-id="society-tag"
                data-name="Society & RWA Gate Privacy Tag"
                data-price="229"
                data-original="549"
                data-image="assets/images/ref-car-pack-1.png">
                Buy Now
              </button>
            </div>
          </div>
        </div>

      </div>'''

for target_file in ['shop.html', 'products.html']:
    with open(target_file, 'r', encoding='utf-8') as f:
        html = f.read()

    pattern = r'<!-- Category Filter Tabs -->[\s\S]*?<!-- Products Grid[\s\S]*?</div>\s*</div>\s*<!-- Delhi NCR Fast Dispatch Banner -->'
    replacement = shop_products_grid + '\n\n      <!-- Delhi NCR Fast Dispatch Banner -->'
    
    if re.search(pattern, html):
        html = re.sub(pattern, replacement, html)
        print(f'Updated product cards in {target_file}')
    else:
        print(f'Regex did not match in {target_file}, trying alternate')
        alt_pattern = r'<div class="shop-filter-bar">[\s\S]*?<div class="products-grid"[^>]*>[\s\S]*?</div>\s*</div>'
        html = re.sub(alt_pattern, shop_products_grid, html)
        print(f'Updated with alternate regex in {target_file}')

    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(html)
