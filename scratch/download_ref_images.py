import urllib.request
import os

images = {
    'assets/images/ref-car-tag-1.png': 'https://i.ibb.co/Z9rWkjR/image.png',
    'assets/images/ref-bike-tag-2.png': 'https://i.ibb.co/6RC8P8gf/image.png',
    'assets/images/ref-car-pack-1.png': 'https://i.ibb.co/ZpchMWHp/image.png',
    'assets/images/ref-product-gallery.png': 'https://i.ibb.co/7dKMmXRw/image.png',
    'assets/images/ref-brochure-preview.png': 'https://i.ibb.co/Qy1T0DT/image.png',
}

for local_path, url in images.items():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(req, timeout=15).read()
        with open(local_path, 'wb') as f:
            f.write(data)
        print(f"Downloaded {local_path} ({len(data)} bytes)")
    except Exception as e:
        print(f"Failed {local_path}: {e}")
