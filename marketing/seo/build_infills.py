# -*- coding: utf-8 -*-
"""
lash-infills-yanchep.html - lash infills (refills) page.

Why it exists: in Australia people search "lash infills", and until 2026-11-09 the
word did not appear anywhere on the site (the menu calls them refills). It also
answers a real local need: someone whose lash technician has moved or stopped,
looking for somewhere to keep an existing set going ("foreign" infills).

Prices come from prices.py. Rules (two weeks / three weeks / roughly 40% left /
beyond three weeks is a full set) are the ones on services.html.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_seo as B
import prices

ROOT, SITE = B.ROOT, B.SITE
SLUG = "lash-infills-yanchep.html"
URL = SITE + "/" + SLUG
R = prices.REFILLS
LOW = min(v[0] for v in R.values())

TITLE = "Lash Infills Yanchep | Lash Refills From $%d | Luxe Beauty Yanchep" % LOW
DESC = ("Lash infills in Yanchep, WA from $%d. Two and three week refills for classic, hybrid, volume and "
        "mega volume sets, including sets applied at another salon." % LOW)
assert len(DESC) <= 160, len(DESC)

FAQS = [
 ("How much are lash infills in Yanchep?",
  "At Luxe Beauty Yanchep a classic infill is $%d within two weeks and $%d within three. Hybrid infills are "
  "$%d and $%d, volume $%d and $%d, and mega volume $%d and $%d."
  % (R["Classic"][0], R["Classic"][1], R["Hybrid"][0], R["Hybrid"][1],
     R["Volume"][0], R["Volume"][1], R["Mega Volume"][0], R["Mega Volume"][1])),
 ("What is the difference between an infill and a refill?",
  "Nothing. Infill, refill and fill all mean the same appointment: the grown-out and missing extensions are "
  "replaced so the set looks full again. The studio's menu calls them refills."),
 ("Do you infill lashes done at another salon?",
  "Yes. It is booked as a foreign lash refill, which costs a little more because it includes a tidy-up of "
  "the existing work. If the set has lashes glued together it is removed and started fresh instead."),
 ("How long does a lash infill take?",
  "Around an hour. A foreign infill can take a little longer because the existing set is tidied first."),
 ("How often do I need lash infills?",
  "Every two to three weeks. Two weeks keeps the set looking full the whole time; three weeks is fine if "
  "you do not mind it looking lighter towards the end."),
 ("Can I get an infill after four weeks?",
  "Usually not. An infill needs roughly 40% of the extensions still in place, and beyond three weeks there "
  "is rarely enough left, so it is booked as a new full set."),
 ("How should I prepare for an infill?",
  "Arrive with clean lashes and no eye makeup, and wash your lashes that morning. Clean lashes hold the new "
  "extensions better and the appointment goes faster."),
]


def build():
    strip = lambda x: (x.replace("&mdash;", "-").replace("&ndash;", "-").replace("&amp;", "&")
                        .replace("&middot;", "-").replace("&rsquo;", "'"))
    esc = lambda x: x.replace("&", "&amp;")
    service = {"@context": "https://schema.org", "@type": "Service",
      "serviceType": "Eyelash extension infills", "name": "Lash Infills in Yanchep",
      "alternateName": "Lash refills", "description": strip(DESC), "url": URL,
      "provider": {"@type": "BeautySalon", "name": "Luxe Beauty Yanchep", "@id": SITE + "/#business",
        "telephone": "+61411487177", "priceRange": "$$", "url": SITE + "/",
        "address": {"@type": "PostalAddress", "addressLocality": "Yanchep", "addressRegion": "WA",
                    "postalCode": "6035", "addressCountry": "AU"}},
      "areaServed": [{"@type": "City", "name": n} for n in
                     ["Yanchep", "Two Rocks", "Eglinton", "Alkimos", "Jindalee", "Butler"]],
      "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Lash infills", "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n},
         "price": str(p), "priceCurrency": "AUD", "availability": "https://schema.org/InStock"}
        for n, p, _ in prices.refill_services()]}}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
      {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQS]}
    crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
      {"@type": "ListItem", "position": 2, "name": "Services", "item": SITE + "/services.html"},
      {"@type": "ListItem", "position": 3, "name": "Lash Infills Yanchep", "item": URL}]}

    heads = [""] + [n for n, _ in prices.FULL_SETS]
    rows = [[label] + ["$%d" % R[n][i] for n, _ in prices.FULL_SETS]
            for i, label in enumerate(["Two week infill", "Three week infill", "Foreign infill"])]
    tbl = ('<div class="ctable rv"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
           % ("".join("<th>%s</th>" % h for h in heads),
              "".join("<tr><th>%s</th>%s</tr>" % (r[0], "".join("<td>%s</td>" % c for c in r[1:]))
                      for r in rows)))
    faq_html = "".join('      <details class="faq"><summary>%s</summary><p>%s</p></details>\n' % (esc(q), esc(a))
                       for q, a in FAQS)

    head = B.head(TITLE, strip(DESC), SLUG, "photos/lash-5.jpg",
                  "\n".join([B.ld(service), B.ld(faq), B.ld(crumb)]))
    body = """
{nav}

<section class="hero hero--sm">
  <img class="hero-bg" src="photos/lash-5.jpg" alt="" aria-hidden="true">
  <div><p class="eyebrow">Lash refills &middot; Yanchep WA</p>
  <h1>Lash Infills<br>in Yanchep</h1></div>
</section>

<section class="light">
  <div class="wrap">
    <div class="sec-head center rv">
      <h2>Keep your set full</h2>
      <p class="lede" style="margin:0 auto">Lash infills in a private Yanchep studio, for classic, hybrid,
        volume and mega volume sets. Infills are from ${low} and take around an hour. Sets applied at
        another salon are welcome.</p>
    </div>

    <div class="sec-head center rv" style="margin-top:clamp(56px,7vw,92px)">
      <p class="eyebrow">Prices</p><h2>Lash infill prices</h2>
      <p class="lede" style="margin:0 auto">Infill, refill and fill all mean the same appointment. The
        price depends on your lash style and how long it has been since your last visit.</p>
    </div>
    {tbl}
    <p class="note center" style="max-width:700px;margin:22px auto 0">The same prices are on the
      <a href="services.html">full menu</a>. A $50 deposit confirms your booking and comes off the total.</p>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">Which one to book</p><h2>Two weeks, three weeks or foreign</h2>
    </div>
    <div class="grid g3 rv">
      <div class="card"><span class="num">01</span><h3>Two week infill</h3>
        <p>You were last in within the past two weeks. Most of the set is still there, so it is a light
        top-up and the lowest price.</p></div>
      <div class="card"><span class="num">02</span><h3>Three week infill</h3>
        <p>Within three weeks. More has grown out and there is more to rebuild, so it costs a little
        more.</p></div>
      <div class="card"><span class="num">03</span><h3>Foreign infill</h3>
        <p>Your set was applied by another technician. Includes a tidy-up of the existing work before
        anything new goes on.</p></div>
    </div>
    <div class="prose rv" style="margin-top:clamp(34px,4vw,54px)">
      <p>An infill needs roughly <b>40% of the extensions still in place</b>. With less than that, and
      usually anywhere beyond three weeks, there is not enough of the set left to build on and a
      <a href="lash-extensions-yanchep.html">new full set</a> is the honest answer. Why sets thin the way
      they do is explained in <a href="how-long-do-lash-extensions-last.html">how long lash extensions last</a>.</p>
    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">New to the studio</p><h2>Moving from another lash technician</h2>
    </div>
    <div class="prose rv">
      <p>Technicians move, stop taking clients or go on leave, and a set does not wait. If you are
      wearing extensions from somewhere else, you do not have to start again.</p>
      <p>Book a <b>foreign lash refill</b> in the style you are wearing. At the appointment the existing
      set is checked first. If the extensions are properly separated and sitting well, they are tidied
      and filled, and you leave with a full set.</p>
      <p>If lashes have been glued together, or the extensions are too heavy for your natural lashes, you
      will be told that plainly. Building on top of a set like that damages the lashes underneath, so the
      right fix is to remove it and start a new one. Removal is $25 as an add-on.</p>
      <p>Not sure what style you are wearing? Send a photo before you book and you will be told which
      one to choose.</p>
    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">What happens</p><h2>Your infill appointment</h2>
    </div>
    <div class="steps rv">
      <div class="step"><div><h3>Arrive with clean lashes</h3>
        <p>No eye makeup and no oily skincare around the eyes. Wash your lashes that morning with a
        lash-safe cleanser.</p></div></div>
      <div class="step"><div><h3>Check and tidy</h3>
        <p>Grown-out extensions that have twisted or are hanging on to a lash about to shed are removed,
        so the new ones sit cleanly.</p></div></div>
      <div class="step"><div><h3>Fill</h3>
        <p>New extensions go on to the natural lashes that have grown in since last time, one lash at a
        time, matched to the rest of the set.</p></div></div>
      <div class="step"><div><h3>Book the next one</h3>
        <p>Two to three weeks later. Booking before you leave keeps you on a refill price rather than a
        full set. <a href="aftercare.html">Aftercare</a> does the rest.</p></div></div>
    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">Questions</p><h2>Good to know</h2>
    </div>
    <div style="max-width:800px;margin:0 auto">
{faq_html}    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">Nearby</p><h2>Infills for Yanchep and surrounds</h2>
    </div>
    <div class="prose rv">
      <p>The studio is a private home studio in Yanchep, WA 6035, with one client booked at a time, so
      an infill starts when it says it does. Clients come from Yanchep and from
      <a href="lash-extensions-two-rocks.html">Two Rocks</a>,
      <a href="lash-extensions-eglinton.html">Eglinton</a>,
      <a href="lash-extensions-alkimos.html">Alkimos</a> and
      <a href="lash-extensions-butler.html">Butler</a>.
      <a href="areas-we-serve.html">All areas served</a>.</p>
    </div>
  </div>
</section>

<section>
  <div class="wrap"><div class="callout rv">
    <img src="photos/lash-2.jpg" alt="" aria-hidden="true" loading="lazy">
    <p class="eyebrow">Yanchep &middot; new clients welcome</p>
    <h2>Book your infill</h2>
    <p class="lede" style="margin:20px auto 0">Choose your lash style and how long it has been. Sets
      from other salons are welcome.</p>
    <div class="btn-row"><a class="btn" data-book href="https://www.instagram.com/luxebeautyyanchep/">Book now</a>
      <a class="btn ghost" href="services.html">All services</a></div>
  </div></div>
</section>

{foot}""".format(nav=B.NAV, tbl=tbl, faq_html=faq_html, low=LOW,
                 foot=B.footer("Yanchep &middot; Two Rocks &middot; Alkimos &middot; Eglinton &middot; Butler"))
    return head + body


if __name__ == "__main__":
    open(os.path.join(ROOT, SLUG), "w", encoding="utf-8").write(build())
    print("  wrote", SLUG)
