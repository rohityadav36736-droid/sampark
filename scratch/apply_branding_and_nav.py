import glob
import re

files = sorted(glob.glob('*.html'))

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = filepath.replace('\\', '/').split('/')[-1]

    # Active states
    idx_act = 'active' if filename == 'index.html' else ''
    prod_act = 'active' if filename in ['products.html', 'product-single.html'] else ''
    shark_act = 'active' if filename == 'shark-tank.html' else ''
    dist_act = 'active' if filename == 'distributorship.html' else ''
    cont_act = 'active' if filename == 'contact.html' else ''
    acc_act = 'active' if filename in ['account.html', 'login.html', 'signup.html'] else ''
    track_act = 'active' if filename == 'track-order.html' else ''

    # 1. Update Desktop Nav
    new_nav = f'''<nav class="nav-menu">
        <a href="index.html" class="nav-link {idx_act}".strip()>Home</a>
        <a href="products.html" class="nav-link {prod_act}".strip()>Buy Tag <span class="nav-tag-badge">₹199</span></a>
        <a href="shark-tank.html" class="nav-link {shark_act}".strip()>Shark Tank</a>
        <a href="distributorship.html" class="nav-link {dist_act}".strip()>Distributorship</a>
        <a href="contact.html" class="nav-link {cont_act}".strip()>Contact Us</a>
        <a href="account.html" class="nav-link {acc_act}".strip()>My Account</a>
      </nav>'''.replace('".strip()', '')

    content = re.sub(r'<nav class="nav-menu">.*?</nav>', new_nav, content, flags=re.DOTALL)

    # 2. Update Drawer Nav
    new_drawer = f'''<nav class="drawer-nav">
        <a href="index.html" class="{idx_act}">🏠 Home</a>
        <a href="products.html" class="{prod_act}">🏷️ Buy Smart Tag (₹199)</a>
        <a href="shark-tank.html" class="{shark_act}">🦈 Shark Tank Pitch</a>
        <a href="distributorship.html" class="{dist_act}">🤝 Distributorship (B2B)</a>
        <a href="contact.html" class="{cont_act}">📍 Contact Us</a>
        <a href="track-order.html" class="{track_act}">📦 Track Your Order</a>
        <a href="account.html" class="{acc_act}">👤 My Account & Tags</a>
      </nav>'''

    content = re.sub(r'<nav class="drawer-nav">.*?</nav>', new_drawer, content, flags=re.DOTALL)

    # 3. Update Logo to SAMPARK DELHI badge
    content = content.replace('<span class="logo-me-badge">ME</span>', '<span class="logo-me-badge">DELHI</span>')
    content = content.replace('SAMPARK ME', 'SAMPARK DELHI')
    content = content.replace('Sampark Me', 'Sampark Delhi')
    content = content.replace('Sampark ME', 'Sampark DELHI')

    # 4. Update Phone Numbers
    content = content.replace('+91 98765 43210', '+91 84477 77266')
    content = content.replace('+91 9876543210', '+91 84477 77266')
    content = content.replace('+91 99999 99999', '+91 84477 77266')
    content = content.replace('+91 98765 00000', '+91 84477 77266')
    content = content.replace('9876543210', '918447777266')
    content = content.replace('9999999999', '918447777266')

    # 5. Update Email Addresses
    content = content.replace('support@samparkmedelhi.com', 'samparkme.delhi@gmail.com')
    content = content.replace('support@samparkme.com', 'samparkme.delhi@gmail.com')
    content = content.replace('care@samparkme.com', 'samparkme.delhi@gmail.com')
    content = content.replace('dealers@samparkme.com', 'samparkme.delhi@gmail.com')

    # 6. Update Address
    content = content.replace('Tech Innovation Hub, Cyber Park, Gurugram, NCR, India', 'Sukar Bazar Road, Near Smriti Van Park, Pkt.-11, Sec A-6, Narela, Delhi - 110040')
    content = content.replace('Cyber City, Gurugram, Haryana - 122002', 'Sukar Bazar Road, Near Smriti Van Park, Pkt.-11, Sec A-6, Narela, Delhi - 110040')
    content = content.replace('Narela Industrial Area, Delhi - 110040', 'Sukar Bazar Road, Near Smriti Van Park, Pkt.-11, Sec A-6, Narela, Delhi - 110040')

    # 7. Update Social Media Links
    content = content.replace('https://instagram.com/samparkme', 'https://www.instagram.com/samparkme.delhi')
    content = content.replace('https://facebook.com/samparkme', 'https://www.facebook.com/samparkme.delhi')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Updated {filename}")

print("All HTML files updated successfully!")
