import sys
sys.stdout.reconfigure(encoding='utf-8')
from PIL import Image
import glob

for img_path in sorted(glob.glob('assets/images/*.*')):
    try:
        with Image.open(img_path) as im:
            print(f"{img_path}: {im.size} (aspect {im.size[0]/im.size[1]:.2f}) - format {im.format}")
    except Exception as e:
        pass
