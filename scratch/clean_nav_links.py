import glob

for p in glob.glob('*.html'):
    with open(p, 'r', encoding='utf-8') as f:
        c = f.read()

    filename = p.replace('\\', '/').split('/')[-1]

    # Clean any malformed nav links
    c = c.replace('class="nav-link >', 'class="nav-link">')
    c = c.replace('class="nav-link  >', 'class="nav-link">')
    c = c.replace('class="nav-link active">', 'class="nav-link active">')

    # Double check title "Sampark Delhi Delhi"
    c = c.replace('Sampark Delhi Delhi', 'Sampark Delhi')

    with open(p, 'w', encoding='utf-8') as f:
        f.write(c)

print("Nav classes cleaned and title fixed!")
