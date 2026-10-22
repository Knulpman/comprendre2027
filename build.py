"""Génère le site (index.html + photos/) à partir de source/guide.html.
Usage : python3 build.py   (depuis la racine du dépôt)
source/guide.html est la même page que l'artifact Claude (photos intégrées en base64)."""
import re, base64, os
ROOT = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(ROOT, "source", "guide.html"), encoding="utf8").read()
URL = "https://comprendre2027.lucaschatel.me/"
i = s.index("</style>") + len("</style>")
head_part, body_part = s[:i], s[i:]
head_part = head_part.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
DESC = "Guide citoyen indépendant sur la présidentielle 2027 : candidats, programmes, votes, chiffrage, idées reçues et mode d'emploi du vote. Même grille pour tous, une source pour chaque information."
meta = f'''<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="{DESC}">
<meta name="theme-color" content="#FFD23F">
<link rel="canonical" href="{URL}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="Comprendre 2027">
<meta property="og:title" content="Comprendre la présidentielle 2027">
<meta property="og:description" content="Candidats, programmes, votes, idées reçues et mode d'emploi du vote. Guide indépendant et sourcé, sans consigne de vote.">
<meta property="og:url" content="{URL}">
<meta property="og:image" content="{URL}og.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
'''
ANALYTICS = """<script>window.va=window.va||function(){(window.vaq=window.vaq||[]).push(arguments);};
window.va("beforeSend",function(e){try{var u=new URL(e.url);if(u.hash){var h=decodeURIComponent(u.hash.slice(1));u.pathname=(h&&h!=="accueil")?"/"+h:"/";u.hash="";}return Object.assign({},e,{url:u.toString()});}catch(x){return e;}});</script>
<script defer src="/_vercel/insights/script.js"></script>"""
out = '<!doctype html>\n<html lang="fr">\n<head>\n' + meta + head_part + '\n' + ANALYTICS + '\n</head>\n<body>' + body_part + '\n</body>\n</html>\n'
os.makedirs(os.path.join(ROOT, "photos"), exist_ok=True)
def _ph(m):
    k, ext, b = m.group(1), m.group(2), m.group(3)
    ext = "jpg" if ext in ("jpeg", "jpg") else ext
    open(os.path.join(ROOT, "photos", f"{k}.{ext}"), "wb").write(base64.b64decode(b))
    return f'"{k}": "photos/{k}.{ext}"'
out = re.sub(r'"(\w+)": "data:image/(\w+);base64,([^"]+)"', _ph, out)
open(os.path.join(ROOT, "index.html"), "w", encoding="utf8").write(out)
print("index.html :", len(out), "octets")
