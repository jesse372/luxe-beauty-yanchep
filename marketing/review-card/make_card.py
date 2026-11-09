# -*- coding: utf-8 -*-
"""
Builds the Google review cards for Luxe Beauty Yanchep.

  review-cards-a4.html  -> print-friendly A4 sheet, four cards, cut into quarters
  review-card.html      -> one dark card for sending on a phone / posting

The QR code points at https://luxebeautyyanchep.com/review, a short link on the site
that forwards to the Google review form. If Google's link ever changes, edit
review.html in the repo root - the printed cards keep working.

Run:  python3 make_card.py     (needs: pip install segno)
Then render.mjs turns the two HTML files into review-cards-a4.pdf and review-card.png,
and verify.py scans both to prove the QR code reads as the right address.
"""
import io, os
import segno

HERE = os.path.dirname(os.path.abspath(__file__))
URL = "https://luxebeautyyanchep.com/review"
FONTS = "../../assets/fonts"

def qr_svg(dark, light):
    buf = io.BytesIO()
    # make_qr, NOT make: make() silently picks a "Micro QR" for short text, which most phone
    # cameras cannot read. verify.py scans the finished files to prove they decode.
    segno.make_qr(URL, error="q").save(buf, kind="svg", border=2, dark=dark, light=light,
                                    xmldecl=False, svgns=True, nl=False, omitsize=True)   # omitsize -> viewBox, so CSS can size it
    return buf.getvalue().decode()

FACE = """
@font-face{font-family:'Cormorant Garamond';font-style:normal;font-weight:300 400;src:url(%(f)s/cormorant-garamond-300-400-latin.woff2) format('woff2')}
@font-face{font-family:'Cormorant Garamond';font-style:italic;font-weight:300 400;src:url(%(f)s/cormorant-garamond-300-400-italic-latin.woff2) format('woff2')}
@font-face{font-family:'Jost';font-style:normal;font-weight:200 400;src:url(%(f)s/jost-200-400-latin.woff2) format('woff2')}
""" % {"f": FONTS}

CARD = """<div class="card">
  <div class="mark">LB</div>
  <p class="eyebrow">Luxe Beauty Yanchep</p>
  <h1>Loved your <i>lashes?</i></h1>
  <div class="rule"></div>
  <p class="ask">A Google review helps other locals<br>find the studio.</p>
  <div class="qr">%s</div>
  <p class="how">Scan with your phone camera</p>
  <p class="url">or visit <b>luxebeautyyanchep.com/review</b></p>
  <p class="thanks">Thank you</p>
</div>"""

BASE = FACE + """
*{box-sizing:border-box} html,body{margin:0}
.card{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;
  font-family:'Jost',sans-serif;font-weight:300}
.mark{width:15mm;height:15mm;border-radius:50%%;display:grid;place-items:center;font-family:'Cormorant Garamond',serif;
  font-size:7mm;letter-spacing:.04em;border:.3mm solid %(accent)s;color:%(accent)s}
.eyebrow{font-size:2.3mm;letter-spacing:.42em;text-transform:uppercase;color:%(accent)s;margin:4mm 0 0}
h1{font-family:'Cormorant Garamond',serif;font-weight:300;font-size:10.5mm;line-height:1.05;margin:4mm 0 0;color:%(fg)s}
h1 i{color:%(accent)s}
.rule{width:12mm;height:.25mm;background:%(accent)s;margin:4.5mm 0}
.ask{font-size:3.6mm;line-height:1.5;margin:0;color:%(dim)s}
.qr{margin:5.5mm 0 3.5mm;padding:2mm;background:#fff;line-height:0}
.qr svg{width:36mm;height:36mm;display:block}
.how{font-size:2.5mm;letter-spacing:.3em;text-transform:uppercase;margin:0;color:%(fg)s}
.url{font-size:3.2mm;margin:2mm 0 0;color:%(dim)s} .url b{font-weight:400;color:%(fg)s}
.thanks{font-family:'Cormorant Garamond',serif;font-style:italic;font-size:5mm;margin:5mm 0 0;color:%(accent)s}
"""

def write(name, html):
    open(os.path.join(HERE, name), "w", encoding="utf-8").write(html)
    print("  wrote", name)

# A4, four cream cards with hairline cut guides (light background = cheap to print at home)
light = BASE % {"accent": "#9B7B4E", "fg": "#1A1613", "dim": "#5F554B"}
write("review-cards-a4.html", """<!doctype html><html lang="en-AU"><head><meta charset="utf-8">
<meta name="viewport" content="width=794">
<title>Luxe Beauty Yanchep - Google review cards (A4, cut into four)</title>
<style>@page{size:A4;margin:0}%s
body{width:210mm;height:297mm;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;background:#fff}
.card{background:#F3EDE4;outline:.2mm dashed #b9ad9d;outline-offset:-.1mm}
</style></head><body>%s</body></html>""" % (light, (CARD % qr_svg("#1A1613", "#ffffff")) * 4))

# one dark card, 1080 x 1350, for texting or posting
dark = BASE % {"accent": "#C4A47C", "fg": "#F7F2EB", "dim": "#CBC1B4"}
write("review-card.html", """<!doctype html><html lang="en-AU"><head><meta charset="utf-8">
<meta name="viewport" content="width=408">
<title>Luxe Beauty Yanchep - Google review card</title>
<style>%s
body{width:108mm;height:135mm;background:#0C0B0A}
.card{width:108mm;height:135mm;background:#0C0B0A;border:.3mm solid rgba(196,164,124,.45);outline:3mm solid #0C0B0A;outline-offset:-3.3mm}
</style></head><body>%s</body></html>""" % (dark, CARD % qr_svg("#0C0B0A", "#ffffff")))
