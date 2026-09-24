import urllib.request
import os

urls = [
    ("sharktank_or_hero_1", "https://i.ibb.co/6RC8P8gf/image.png"),
    ("sharktank_or_hero_2", "https://i.ibb.co/7dKMmXRw/image.png"),
    ("sharktank_or_hero_3", "https://i.ibb.co/Qy1T0DT/image.png"),
    ("sharktank_or_hero_4", "https://i.ibb.co/Z9rWkjR/image.png"),
    ("sharktank_or_hero_5", "https://i.ibb.co/ZpchMWHp/image.png"),
    ("car_tag_pack_2", "https://samparkmedelhi.com/images/car-sampark-tag-pack-2.png")
]

os.makedirs("scratch/downloaded", exist_ok=True)

for name, url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as resp, open(f"scratch/downloaded/{name}.png", "wb") as f:
            f.write(resp.read())
        print(f"Downloaded {name}: size {os.path.getsize(f'scratch/downloaded/{name}.png')} bytes")
    except Exception as e:
        print(f"Failed {name} ({url}): {e}")
