import re

for filename in ['shop.html', 'products.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    product_image_links = [
        ('id="card-car-tag"', 'assets/images/car-tag-hd.jpg', 'car-tag'),
        ('id="card-pro-tag"', 'assets/images/product-pro-tag.jpg', 'pro-tag'),
        ('id="card-fleet-tag"', 'assets/images/product-fleet.jpg', 'fleet-tag'),
        ('id="card-bike-tag"', 'assets/images/bike-tag-hd.jpg', 'bike-tag'),
        ('id="card-combo-tag"', 'assets/images/ref-product-gallery.png', 'combo-pack'),
        ('id="card-society-tag"', 'assets/images/ref-car-pack-1.png', 'society-tag'),
    ]

    for card_id, img_src, prod_param in product_image_links:
        old_div = f'<div class="product-img-wrapper">\n            <img src="{img_src}"'
        new_a = f'<a href="product-single.html?id={prod_param}" class="product-img-wrapper" title="View Product Details">\n            <img src="{img_src}"'
        if old_div in content:
            content = content.replace(old_div, new_a)

    content = re.sub(
        r'(<a href="product-single\.html\?id=[^"]*" class="product-img-wrapper"[^>]*>\s*<img [^>]*>)\s*</div>',
        r'\1\n          </a>',
        content
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Product images made clickable in {filename}")
