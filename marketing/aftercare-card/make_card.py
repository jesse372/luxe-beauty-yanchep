# -*- coding: utf-8 -*-
"""
The card a client takes home: aftercare on the front, next appointment on the back.

  aftercare-cards-a4.html -> 2-page A4: page 1 = four fronts, page 2 = four backs.
  Print double-sided (flip on the long edge), cut into quarters.

The QR code on the back points at https://luxebeautyyanchep.com/book (the short link
to online booking). The six rules are the ones on aftercare.html - keep them in step.

Run:  python3 make_card.py   (needs: pip install segno)   then   node render.mjs
"""
import io, os
import segno

HERE = os.path.dirname(os.path.abspath(__file__))
URL = "https://luxebeautyyanchep.com/book"
FONTS = "../../assets/fonts"

def qr_svg():
    buf = io.BytesIO()
    # make_qr + omitsize: see marketing/review-card/make_card.py for why
    segno.make_qr(URL, error="q").save(buf, kind="svg", border=2, dark="#1A1613", light="#ffffff",
                                       xmldecl=False, svgns=True, nl=False, omitsize=True)
    return buf.getvalue().decode()

RULES = [("Dry for 24 hours", "No water, steam or heavy sweat while the adhesive cures."),
         ("Cleanse every day", "Lash-safe foaming cleanser and a soft brush."),
         ("Keep oil away", "Check cleanser, moisturiser, sunscreen, makeup remover."),
         ("No curlers or waterproof mascara", "Extensions already hold their curl."),
         ("Sleep on your back if you can", "Or use a silk pillowcase."),
         ("Infill every 2 to 3 weeks", "It costs less than starting again.")]

FRONT = """<div class="card">
  <div class="mark">LB</div>
  <p class="eyebrow">Lash aftercare</p>
  <h1>Make them <i>last</i></h1>
  <div class="rules">%s</div>
</div>""" % "".join('<div class="r"><b>%02d</b><span>%s<small>%s</small></span></div>' % (i + 1, t, d)
                    for i, (t, d) in enumerate(RULES))

BACK = """<div class="card">
  <p class="eyebrow">Your next appointment</p>
  <div class="slot"><span>Date</span><i></i></div>
  <div class="slot"><span>Time</span><i></i></div>
  <p class="ask">Infills are due in two to three weeks.<br>Book inside three and it is a refill, not a full set.</p>
  <div class="qr">%s</div>
  <p class="how">Book or change online</p>
  <p class="url"><b>luxebeautyyanchep.com/book</b></p>
  <p class="fine">Something not sitting right? Message within 48 hours: 0411 487 177<br>
    Happy with them? luxebeautyyanchep.com/review</p>
</div>""" % qr_svg()

CSS = """
@font-face{font-family:'Cormorant Garamond';font-style:normal;font-weight:300 400;src:url(%(f)s/cormorant-garamond-300-400-latin.woff2) format('woff2')}
@font-face{font-family:'Cormorant Garamond';font-style:italic;font-weight:300 400;src:url(%(f)s/cormorant-garamond-300-400-italic-latin.woff2) format('woff2')}
@font-face{font-family:'Jost';font-style:normal;font-weight:200 400;src:url(%(f)s/jost-200-400-latin.woff2) format('woff2')}
@page{size:A4;margin:0} *{box-sizing:border-box} html,body{margin:0}
.sheet{width:210mm;height:297mm;display:grid;grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr;break-after:page}
.card{background:#F3EDE4;outline:.2mm dashed #b9ad9d;outline-offset:-.1mm;display:flex;flex-direction:column;align-items:center;
  justify-content:center;text-align:center;font-family:'Jost',sans-serif;font-weight:300;color:#1A1613;padding:9mm 11mm}
.mark{width:12mm;height:12mm;border-radius:50%%;display:grid;place-items:center;font-family:'Cormorant Garamond',serif;font-size:5.6mm;
  border:.3mm solid #9B7B4E;color:#9B7B4E}
.eyebrow{font-size:2.3mm;letter-spacing:.42em;text-transform:uppercase;color:#9B7B4E;margin:3mm 0 0}
h1{font-family:'Cormorant Garamond',serif;font-weight:300;font-size:9mm;line-height:1.05;margin:2.5mm 0 3mm} h1 i{color:#9B7B4E}
.rules{width:100%%;text-align:left}
.r{display:flex;gap:3.2mm;align-items:baseline;padding:2.1mm 0;border-bottom:.2mm solid rgba(26,22,19,.14)} .r:last-child{border-bottom:0}
.r b{font-family:'Cormorant Garamond',serif;font-weight:400;font-size:3.6mm;color:#9B7B4E;min-width:5mm}
.r span{font-family:'Cormorant Garamond',serif;font-size:4.5mm;line-height:1.15}
.r small{display:block;font-family:'Jost',sans-serif;font-size:2.75mm;color:#5F554B;margin-top:.7mm;line-height:1.35}
.slot{width:100%%;display:flex;align-items:flex-end;gap:4mm;margin-top:7mm}
.slot span{font-size:2.5mm;letter-spacing:.3em;text-transform:uppercase;color:#5F554B;min-width:12mm;text-align:left}
.slot i{flex:1;border-bottom:.3mm solid #1A1613;height:6mm}
.ask{font-size:3.1mm;line-height:1.5;color:#5F554B;margin:7mm 0 0}
.qr{margin:5mm 0 3mm;padding:1.6mm;background:#fff;line-height:0} .qr svg{width:28mm;height:28mm;display:block}
.how{font-size:2.4mm;letter-spacing:.3em;text-transform:uppercase;margin:0}
.url{font-size:3.6mm;margin:1.6mm 0 0} .url b{font-weight:400}
.fine{font-size:2.5mm;line-height:1.6;color:#5F554B;margin:5mm 0 0}
""" % {"f": FONTS}

html = ("""<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=794">
<title>Luxe Beauty Yanchep - aftercare and next appointment cards (A4, double-sided, cut into four)</title>
<style>%s</style></head><body><div class="sheet">%s</div><div class="sheet">%s</div></body></html>"""
        % (CSS, FRONT * 4, BACK * 4))
open(os.path.join(HERE, "aftercare-cards-a4.html"), "w", encoding="utf-8").write(html)
print("  wrote aftercare-cards-a4.html")
