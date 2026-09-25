import glob
import re

favicon_tag = "<link rel=\"icon\" href=\"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23FFCC00'><path d='M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5'/></svg>\">"

for f in sorted(glob.glob("*.html")):
    content = open(f, encoding="utf-8").read()
    icons = re.findall(r'<link[^>]*rel=["\'](?:shortcut )?icon["\'][^>]*>', content)
    print(f, icons)
