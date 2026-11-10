# -*- coding: utf-8 -*-
"""
Build check. Exits 1 (and prints why) if the built site would ship something broken.
Run by build_all.sh; safe to run on its own.

Checks every indexable page for: one <h1>, title, description <= 160 chars, canonical,
parsing JSON-LD, FAQ markup that matches the questions actually visible on the page,
internal links and images that exist, sized images, an LCP preload that matches the hero,
no third-party font request; plus sitemap coverage, price consistency with prices.py,
and that the suburb pages are still different enough from each other.
"""
import glob, html as H, json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import prices, hours

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SITE = "https://luxebeautyyanchep.com"
errors, warns = [], []
E = lambda page, msg: errors.append("%s: %s" % (page, msg))
W = lambda page, msg: warns.append("%s: %s" % (page, msg))

def text_of(s):
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S)
    return re.sub(r"\s+", " ", H.unescape(re.sub(r"<[^>]+>", " ", s))).strip()

pages = {}
for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
    s = open(path, encoding="utf-8").read()
    if re.search(r'<meta name="robots" content="[^"]*noindex', s):
        continue
    pages[os.path.basename(path)] = s

for slug, s in pages.items():
    url = SITE + "/" + ("" if slug == "index.html" else slug)
    h1 = re.findall(r"<h1\b", s)
    if len(h1) != 1: E(slug, "%d <h1> tags" % len(h1))
    t = re.search(r"<title>(.*?)</title>", s, re.S)
    if not t: E(slug, "no title")
    elif len(H.unescape(t.group(1))) > 70: W(slug, "title %d chars" % len(H.unescape(t.group(1))))
    d = re.search(r'<meta name="description" content="([^"]*)"', s)
    if not d: E(slug, "no meta description")
    elif not 70 <= len(H.unescape(d.group(1))) <= 160: E(slug, "description %d chars" % len(H.unescape(d.group(1))))
    c = re.search(r'<link rel="canonical" href="([^"]*)"', s)
    if not c or c.group(1) != url: E(slug, "canonical is %s" % (c.group(1) if c else None))
    if "fonts.googleapis.com" in s or "fonts.gstatic.com" in s: E(slug, "still requests Google Fonts")
    if not re.search(r'href="assets/style\.css\?v=\w+"', s): E(slug, "stylesheet link has no cache-busting version")
    if s.count('rel="preload" as="font"') != 2: E(slug, "expected 2 font preloads, found %d" % s.count('rel="preload" as="font"'))

    # JSON-LD parses; FAQ markup only for questions the page really shows
    visible = set(text_of(q) for q in re.findall(r"<summary>(.*?)</summary>", s, re.S))
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try:
            j = json.loads(block)
        except ValueError as e:
            E(slug, "JSON-LD does not parse: %s" % e); continue
        nodes = j.get("@graph", [j]) if isinstance(j, dict) else j
        for n in nodes:
            if n.get("@type") == "FAQPage":
                for q in n["mainEntity"]:
                    if text_of(q["name"]) not in visible:
                        E(slug, "FAQ schema question not visible on page: %s" % q["name"][:60])
            if "aggregateRating" in json.dumps(n) or "AggregateRating" in json.dumps(n):
                E(slug, "review/rating markup present - not allowed without real third-party reviews")

    # links + images exist
    for href in re.findall(r'href="([^"#?]+)(?:[#?][^"]*)?"', s):
        if re.match(r"(https?:|mailto:|tel:|/llms)", href) or href in ("./", "/"): continue
        if not os.path.exists(os.path.join(ROOT, href.lstrip("/"))): E(slug, "broken link %s" % href)
    if 'href="index.html' in s: E(slug, "links to index.html instead of ./")
    for img in re.findall(r"<img\b[^>]*>", s):
        src = re.search(r'src="([^"]+)"', img).group(1)
        if not os.path.exists(os.path.join(ROOT, src)): E(slug, "missing image %s" % src)
        if not src.endswith(".webp"): E(slug, "image not WebP: %s" % src)
        if 'width="' not in img or 'height="' not in img: E(slug, "image without width/height: %s" % src)
        for f in re.findall(r"(photos/[\w-]+\.webp) \d+w", img):
            if not os.path.exists(os.path.join(ROOT, f)): E(slug, "missing srcset image %s" % f)
    hero = re.search(r'<img class="hero-bg"[^>]*src="([^"]+)"', s)
    pre = re.findall(r'<link rel="preload" as="image" href="([^"]+)"', s)
    if hero:
        if hero.group(1) not in pre: E(slug, "LCP preload %s does not match hero %s" % (pre, hero.group(1)))
        if 'loading="lazy"' in re.search(r'<img class="hero-bg"[^>]*>', s).group(0): E(slug, "hero image is lazy")

# a <picture>-wrapped hero needs the CSS that stops the wrapper becoming a positioned box
css = open(os.path.join(ROOT, "assets", "style.css"), encoding="utf-8").read()
if any("<picture>" in v for v in pages.values()) and ".hero > picture" not in css:
    E("assets/style.css", "missing '.hero > picture{display:contents}' - the hero photo would be invisible")

# sitemap covers exactly the indexable pages
sm = open(os.path.join(ROOT, "sitemap.xml")).read()
locs = set(re.findall(r"<loc>(.*?)</loc>", sm))
want = set(SITE + "/" + ("" if s == "index.html" else s) for s in pages)
for u in sorted(want - locs): E("sitemap.xml", "missing %s" % u)
for u in sorted(locs - want): E("sitemap.xml", "lists a page that is not indexable: %s" % u)

# prices: services.html is what Square is synced from; it must agree with prices.py
rows = dict((H.unescape(n), int(p)) for n, p in re.findall(
    r'<span class="name">(.*?)</span>.*?<span class="price">\$(\d+)</span>', pages["services.html"]))
for n, p in [(n + " Full Set", p) for n, p in prices.FULL_SETS] + [(n, p) for n, p, _ in prices.refill_services()]:
    if rows.get(n) != p: E("services.html", "%s is %s on the page but %s in prices.py" % (n, rows.get(n), p))

# opening hours: one source (hours.py). Old wordings must not come back anywhere.
for slug, s in pages.items():
    t = text_of(s)
    for old in ("Monday to Saturday, 9am to 5pm", "9:00am - 5:00pm", "Mon - Sat 9:00am", "Saturdays run 9am to 5pm", "by arrangement"):
        if old.lower() in t.lower(): E(slug, "stale opening-hours wording: %r" % old)
for l, t in hours.rows():
    if ("<b>%s</b><span>%s</span>" % (l.replace(" and ", "&amp;".join((" ", " "))), t)) not in pages["contact.html"]:
        E("contact.html", "hours table missing %s %s" % (l, t))
if hours.sentence() not in open(os.path.join(ROOT, "llms.txt"), encoding="utf-8").read():
    E("llms.txt", "hours sentence differs from hours.py")

# one booking link everywhere: site.js is the source, /book and the schema must match it
js = open(os.path.join(ROOT, "assets", "site.js"), encoding="utf-8").read()
booking = re.search(r'const BOOKING_URL = "([^"]+)"', js).group(1)
book_page = open(os.path.join(ROOT, "book.html"), encoding="utf-8").read()
if book_page.count(booking) < 3: E("book.html", "does not forward to the BOOKING_URL in site.js (%s)" % booking)
if booking not in pages["index.html"]: E("index.html", "schema booking link differs from site.js")
stats_url = re.search(r'const STATS_URL = "([^"]*)"', js).group(1)
for stub in ("book.html", "review.html"):
    if stats_url and stats_url not in open(os.path.join(ROOT, stub), encoding="utf-8").read():
        E(stub, "visitor counter address differs from STATS_URL in site.js")
low = min(p for _, p in prices.FULL_SETS)
if "from $%d" % low not in js: E("assets/site.js", "phone booking bar should say 'from $%d' (prices.py)" % low)
for claim in ("at Luxe Beauty Yanchep\"", "studio in Yanchep\""):
    for slug, s in pages.items():
        if re.search(r'alt="[^"]*' + claim, s): E(slug, "an image description claims a stock photo is the studio's own work")

# suburb pages must stay different from each other (doorway-page guard)
def grams(s, n=8):
    w = re.findall(r"[a-z0-9$']+", text_of(s[s.find("</header>"):s.find("<footer")]).lower())
    return set(tuple(w[i:i + n]) for i in range(len(w) - n + 1))
subs = dict((k, grams(v)) for k, v in pages.items()
            if k.startswith("lash-extensions-") and k not in ("lash-extensions-yanchep.html", "lash-extensions-cost-perth.html"))
worst = (0, "", "")
keys = sorted(subs)
for i, a in enumerate(keys):
    for b in keys[i + 1:]:
        j = len(subs[a] & subs[b]) / float(len(subs[a] | subs[b]))
        if j > worst[0]: worst = (j, a, b)
if worst[0] > 0.45: E("suburb pages", "too similar (%.2f): %s vs %s" % worst)

for w in warns: print("  warn  " + w)
if errors:
    for e in errors: print("  FAIL  " + e)
    print("  check: %d problem(s) in %d pages" % (len(errors), len(pages)))
    sys.exit(1)
print("  check: %d pages OK, sitemap %d urls, suburb overlap max %.2f, %d warning(s)"
      % (len(pages), len(locs), worst[0], len(warns)))
