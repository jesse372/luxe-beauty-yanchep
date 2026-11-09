# -*- coding: utf-8 -*-
"""
Last build step. Runs over EVERY indexable .html page (generated or hand-written)
and makes the things that must be uniform, uniform. Idempotent.

  1. Images  -> WebP with srcset + width/height (photos/*.jpg stay as sources).
               Wide heroes also get a portrait crop for phones via <picture>.
  2. Fonts   -> no Google Fonts request; self-hosted woff2, two faces preloaded.
  3. Links   -> the home link is "./" not "index.html" (one URL for the homepage).
  4. Sitemap -> lastmod only moves when a page's content actually changes
               (hash state in marketing/seo/.lastmod.json).
  5. IndexNow key file + the URL list for a ping (marketing/seo/indexnow.py sends it).

Run:  python3 marketing/seo/finalize.py        (build_all.sh runs it last)
"""
import datetime, glob, hashlib, json, os, re, sys
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SITE = "https://luxebeautyyanchep.com"
STATE = os.path.join(ROOT, "marketing", "seo", ".lastmod.json")
INDEXNOW_KEY = "08c01bd8e2daf37158d5686d6a569eb4"

# sitemap priority; anything indexable but unlisted gets 0.6
PRIORITY = {"": "1.0", "services.html": "0.9", "lash-extensions-yanchep.html": "0.9",
            "eyebrows-yanchep.html": "0.9", "areas-we-serve.html": "0.8", "contact.html": "0.7",
            "aftercare.html": "0.7", "gallery.html": "0.6", "about.html": "0.6"}
INNER = ("eglinton", "two-rocks", "alkimos", "jindalee", "butler")   # the real catchment

FONT_PRELOADS = ["assets/fonts/cormorant-garamond-300-400-latin.woff2",
                 "assets/fonts/jost-200-400-latin.woff2"]
WIDE = {"hero", "bleed"}          # full-bleed landscape images -> portrait crop for phones
SIZES = "(max-width:700px) 100vw, (max-width:1100px) 50vw, 600px"


# ---------------------------------------------------------------- images
def build_images():
    """photos/X.jpg -> X.webp (+ X-800.webp, + X-m.webp for wide heroes). Returns {name: (w, h, has800)}."""
    meta = {}
    for src in sorted(glob.glob(os.path.join(ROOT, "photos", "*.jpg"))):
        name = os.path.splitext(os.path.basename(src))[0]
        im = Image.open(src).convert("RGB")
        w, h = im.size
        full = os.path.join(ROOT, "photos", name + ".webp")
        if not os.path.exists(full) or os.path.getmtime(full) < os.path.getmtime(src):
            im.save(full, "WEBP", quality=80, method=6)
        has800 = False
        if w >= 1000 and name not in WIDE:
            small = os.path.join(ROOT, "photos", name + "-800.webp")
            if not os.path.exists(small) or os.path.getmtime(small) < os.path.getmtime(src):
                im.resize((800, round(h * 800 / w)), Image.LANCZOS).save(small, "WEBP", quality=78, method=6)
            has800 = True
        if name in WIDE:
            # centre crop to 2:3 - what object-fit:cover shows on a phone anyway
            m = os.path.join(ROOT, "photos", name + "-m.webp")
            if not os.path.exists(m) or os.path.getmtime(m) < os.path.getmtime(src):
                cw = round(h * 2 / 3)
                left = (w - cw) // 2
                im.crop((left, 0, left + cw, h)).save(m, "WEBP", quality=76, method=6)
        meta[name] = (w, h, has800)
    return meta


def img_tag(m, meta):
    tag = m.group(0)
    name = re.search(r'src="photos/([\w-]+?)(?:-800|-m)?\.(?:jpg|webp)"', tag)
    if not name or name.group(1) not in meta:
        return tag
    n = name.group(1)
    w, h, has800 = meta[n]
    # strip anything we manage, then re-add
    tag = re.sub(r'\s(?:srcset|sizes|width|height|decoding)="[^"]*"', "", tag)
    tag = re.sub(r'src="photos/[^"]+"', 'src="photos/%s.webp"' % n, tag)
    extra = ' width="%d" height="%d"' % (w, h)
    if has800:
        extra += ' srcset="photos/%s-800.webp 800w, photos/%s.webp %dw" sizes="%s"' % (n, n, w, SIZES)
    if 'loading="lazy"' in tag:
        extra += ' decoding="async"'
    return tag[:-1].rstrip("/").rstrip() + extra + ">"


def images_pass(html, meta):
    # unwrap any <picture> we added before, so the pass is idempotent
    html = re.sub(r'<picture><source media="[^"]*" srcset="photos/[\w-]+-m\.webp">(<img[^>]*>)</picture>',
                  r"\1", html)
    html = re.sub(r"<img\b[^>]*>", lambda m: img_tag(m, meta), html)

    def wrap(m):
        n = m.group(2)
        if n not in WIDE:
            return m.group(0)
        return ('<picture><source media="(max-width:700px) and (orientation:portrait)" '
                'srcset="photos/%s-m.webp">%s</picture>' % (n, m.group(1)))
    html = re.sub(r'(<img\b[^>]*src="photos/([\w-]+)\.webp"[^>]*>)', wrap, html)

    # the LCP preload must name the file the hero actually renders
    def preload(m):
        n = m.group(1)
        if n in WIDE:
            return ('<link rel="preload" as="image" href="photos/%s.webp" fetchpriority="high" '
                    'media="(min-width:701px), (orientation:landscape)">\n'
                    '<link rel="preload" as="image" href="photos/%s-m.webp" fetchpriority="high" '
                    'media="(max-width:700px) and (orientation:portrait)">' % (n, n))
        if n in meta and meta[n][2]:
            return ('<link rel="preload" as="image" href="photos/%s.webp" fetchpriority="high" '
                    'imagesrcset="photos/%s-800.webp 800w, photos/%s.webp %dw" imagesizes="100vw">'
                    % (n, n, n, meta[n][0]))
        return '<link rel="preload" as="image" href="photos/%s.webp" fetchpriority="high">' % n
    html = re.sub(r'<link rel="preload" as="image" href="photos/([\w-]+?)(?:-m)?\.(?:jpg|webp)"[^>]*>'
                  r'(?:\n<link rel="preload" as="image" href="photos/[\w-]+-m\.webp"[^>]*>)?',
                  preload, html)
    # the hero image is the LCP element: tell the browser, and it must not be lazy
    html = re.sub(r'(<img class="hero-bg"(?![^>]*fetchpriority)[^>]*?)>', r'\1 fetchpriority="high">', html)
    # hero images fill the viewport width
    html = re.sub(r'(<img class="hero-bg"[^>]*?) sizes="[^"]*"', r'\1 sizes="100vw"', html)
    return html


# ---------------------------------------------------------------- fonts / links
def fonts_pass(html):
    html = re.sub(r'<link rel="preconnect" href="https://fonts\.(?:googleapis|gstatic)\.com"[^>]*>\n?', "", html)
    html = re.sub(r'<link rel="stylesheet" href="https://fonts\.googleapis\.com/[^"]*">\n?', "", html)
    html = re.sub(r'<link rel="preload" as="font"[^>]*>\n?', "", html)
    pre = "".join('<link rel="preload" as="font" type="font/woff2" href="%s" crossorigin>\n' % f
                  for f in FONT_PRELOADS)
    return html.replace('<link rel="stylesheet" href="assets/style.css">',
                        pre + '<link rel="stylesheet" href="assets/style.css">', 1)


def links_pass(html):
    return re.sub(r'href="index\.html(#[\w-]+)?"', lambda m: 'href="./%s"' % (m.group(1) or ""), html)


# ---------------------------------------------------------------- sitemap
def indexable(html):
    return not re.search(r'<meta name="robots" content="[^"]*noindex', html)


def priority(slug):
    if slug in PRIORITY:
        return PRIORITY[slug]
    if slug.startswith("lash-extensions-"):
        return "0.7" if slug[len("lash-extensions-"):-5] in INNER else "0.4"
    return "0.6"                                  # guides


def write_sitemap(pages):
    try:
        state = json.load(open(STATE))
    except (OSError, ValueError):
        state = {}
    today = datetime.date.today().isoformat()
    rows = []
    for slug, html in pages:
        # hash the content only, so a cosmetic rebuild does not fake a "last modified"
        meta_bits = " ".join(re.findall(r'<title>.*?</title>|<meta name="description" content="[^"]*">', html, re.S))
        body = meta_bits + re.sub(r"\s+", " ", re.sub(r"<script[^>]*>.*?</script>|<[^>]+>", " ", html, flags=re.S))
        h = hashlib.sha256(body.encode()).hexdigest()[:16]
        old = state.get(slug)
        if not old:
            state[slug] = {"hash": h, "lastmod": today}
        elif old["hash"] != h:
            state[slug] = {"hash": h, "lastmod": today}
        rows.append((slug, state[slug]["lastmod"]))
    for gone in set(state) - {s for s, _ in pages}:
        del state[gone]
    order = sorted(rows, key=lambda r: (-float(priority(r[0])), r[0]))
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for slug, lastmod in order:
        xml.append("  <url><loc>%s/%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>"
                   % (SITE, slug, lastmod, priority(slug)))
    xml.append("</urlset>\n")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(xml))
    tmp = STATE + ".tmp"
    json.dump(state, open(tmp, "w"), indent=1, sort_keys=True)
    os.replace(tmp, STATE)
    changed = [s for s, d in rows if d == today]
    return len(rows), changed


def main():
    meta = build_images()
    pages = []
    for path in sorted(glob.glob(os.path.join(ROOT, "*.html"))):
        slug = os.path.basename(path)
        html = open(path, encoding="utf-8").read()
        if not indexable(html):
            continue                               # redirect stubs and 404.html: leave untouched
        new = links_pass(fonts_pass(images_pass(html, meta)))
        if new != html:
            open(path, "w", encoding="utf-8").write(new)
        if indexable(new):
            pages.append(("" if slug == "index.html" else slug, new))
    n, changed = write_sitemap(pages)
    open(os.path.join(ROOT, INDEXNOW_KEY + ".txt"), "w").write(INDEXNOW_KEY)
    print("  finalize: %d images, %d pages, sitemap %d urls (%d changed today)"
          % (len(meta), len(pages), n, len(changed)))


if __name__ == "__main__":
    main()
