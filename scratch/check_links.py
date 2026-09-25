import glob
import re

for filename in glob.glob("*.html"):
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
    
    div_img_wrappers = len(re.findall(r'<div[^>]*class=["\'][^"\']*product-img-wrapper', content))
    a_img_wrappers = len(re.findall(r'<a[^>]*class=["\'][^"\']*product-img-wrapper', content))
    product_single_links = len(re.findall(r'href=["\']product-single\.html[^"\']*["\']', content))
    
    if div_img_wrappers > 0 or a_img_wrappers > 0 or product_single_links > 0:
        print(f"{filename}: div_wrappers={div_img_wrappers}, a_wrappers={a_img_wrappers}, product_single_links={product_single_links}")
