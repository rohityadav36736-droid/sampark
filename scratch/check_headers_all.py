import glob

for f in sorted(glob.glob("*.html")):
    with open(f, "r", encoding="utf-8") as file:
        c = file.read()
    has_header = '<header class="site-header">' in c
    has_drawer = 'id="mobile-drawer"' in c
    has_announcement = 'top-announcement' in c
    first_tag = c.split("<body>")[1].strip()[:80] if "<body>" in c else "NO BODY"
    print(f"{f:22} | header:{str(has_header):5} | drawer:{str(has_drawer):5} | top:{first_tag.replace(chr(10), ' ')}")
