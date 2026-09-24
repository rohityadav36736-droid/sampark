import glob
import re

html_files = sorted(glob.glob('*.html'))

desktop_nav_template = '''      <!-- Desktop Navigation Menu -->
      <nav class="nav-menu">
        <a href="index.html" class="nav-link {INDEX_ACT}">Home</a>
        <a href="shop.html" class="nav-link {SHOP_ACT}">Shop <span class="nav-tag-badge">TAGS</span></a>
        <a href="shark-tank.html" class="nav-link {SHARK_ACT}">Shark Tank</a>
        <a href="distributorship.html" class="nav-link {DIST_ACT}">Distributorship</a>
        <a href="contact.html" class="nav-link {CONTACT_ACT}">Contact & Hub</a>
        <a href="account.html" class="nav-link {ACCOUNT_ACT}">My Account</a>
      </nav>'''

drawer_nav_template = '''      <nav class="drawer-nav">
        <a href="index.html" class="{INDEX_ACT}">🏠 Home</a>
        <a href="shop.html" class="{SHOP_ACT}">🏷️ Shop Smart Tags</a>
        <a href="shark-tank.html" class="{SHARK_ACT}">🦈 Shark Tank Pitch</a>
        <a href="distributorship.html" class="{DIST_ACT}">🤝 Distributorship (B2B)</a>
        <a href="contact.html" class="{CONTACT_ACT}">📍 Contact & Hub</a>
        <a href="track-order.html" class="{TRACK_ACT}">📦 Track Your Order</a>
        <a href="account.html" class="{ACCOUNT_ACT}">👤 My Account & Tags</a>
      </nav>'''

for f in html_files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()

    # Determine active flags
    index_act = "active" if f == "index.html" else ""
    shop_act = "active" if f in ["shop.html", "products.html", "product-single.html"] else ""
    shark_act = "active" if f == "shark-tank.html" else ""
    dist_act = "active" if f == "distributorship.html" else ""
    contact_act = "active" if f == "contact.html" else ""
    account_act = "active" if f in ["account.html", "login.html", "signup.html"] else ""
    track_act = "active" if f == "track-order.html" else ""

    desktop_nav = desktop_nav_template.format(
        INDEX_ACT=index_act,
        SHOP_ACT=shop_act,
        SHARK_ACT=shark_act,
        DIST_ACT=dist_act,
        CONTACT_ACT=contact_act,
        ACCOUNT_ACT=account_act
    ).replace('  "', '"').replace('class="nav-link "', 'class="nav-link"')

    drawer_nav = drawer_nav_template.format(
        INDEX_ACT=index_act,
        SHOP_ACT=shop_act,
        SHARK_ACT=shark_act,
        DIST_ACT=dist_act,
        CONTACT_ACT=contact_act,
        ACCOUNT_ACT=account_act,
        TRACK_ACT=track_act
    )

    # Clean up empty classes or whitespace
    # Replace desktop nav
    content = re.sub(r'<!--\s*(?:Desktop\s+)?Navigation\s+Menu\s*-->\s*<nav class="nav-menu">.*?</nav>', desktop_nav, content, flags=re.DOTALL)
    content = re.sub(r'<nav class="nav-menu">.*?</nav>', desktop_nav, content, flags=re.DOTALL)

    # Replace drawer nav
    content = re.sub(r'<nav class="drawer-nav">.*?</nav>', drawer_nav, content, flags=re.DOTALL)

    # Replace header CTA to shop.html if it was products.html
    content = re.sub(r'href="products\.html"([^>]*class="[^"]*header-cta-btn[^"]*")', r'href="shop.html"\1', content)
    content = re.sub(r'href="products\.html"([^>]*id="header-cta-buy")', r'href="shop.html"\1', content)

    # Replace drawer bottom CTA
    content = re.sub(r'href="products\.html"([^>]*class="btn btn-primary btn-block")', r'href="shop.html"\1', content)

    # Clean any lingering `active>` typo
    content = content.replace('class="nav-link active>', 'class="nav-link active">')
    content = content.replace('active>', 'active">')

    # Remove double spaces in class names
    content = content.replace('class="nav-link "', 'class="nav-link"')
    content = content.replace('class=""', '')

    with open(f, 'w', encoding='utf-8') as fp:
        fp.write(content)

    print(f"Updated {f}")
