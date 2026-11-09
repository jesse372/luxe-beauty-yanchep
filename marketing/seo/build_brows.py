# -*- coding: utf-8 -*-
"""
eyebrows-yanchep.html - the brow page.

Why it exists: Search Console (Aug-Nov 2026) shows "eyebrows yanchep" as the
most-seen search the site appears for (position ~6), and until now the only
page answering it was the homepage, which barely mentions brows.

Facts come from services.html (the price source of truth), contact.html and
aftercare.html. Brow shape and brow shape & tint are ADD-ONS to a lash
appointment; the $60 package is the one brow appointment bookable alone.
The studio does not offer lamination, henna or cosmetic tattooing - say so
plainly rather than imply otherwise.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_seo as B

ROOT, SITE = B.ROOT, B.SITE
SLUG = "eyebrows-yanchep.html"
URL = SITE + "/" + SLUG

TITLE = "Eyebrows Yanchep | Brow Shape, Wax &amp; Tint | Luxe Beauty Yanchep"
DESC = ("Eyebrow shaping, waxing and tinting in Yanchep, WA. Brow shape $25 or shape and tint $40 with "
        "a lash appointment, or $60 with a lash tint booked on its own.")
assert len(DESC) <= 160, len(DESC)

OFFERS = [
    ("Brow Shape", "25", "Wax and tweeze, mapped to your features. Add-on to a lash set or refill."),
    ("Brow Shape and Tint", "40", "Shaped and tinted for depth and definition. Add-on to a lash set or refill."),
    ("Lash Tint", "25", "Darkens fair lash tips. Add-on to a lash set or refill."),
    ("Brow Shape and Tint with Lash Tint", "60", "Brows shaped and tinted with a lash tint. Can be booked on its own."),
]

FAQS = [
 ("How much is an eyebrow shape and tint in Yanchep?",
  "At Luxe Beauty Yanchep a brow shape is $25 and a brow shape and tint is $40, added to a lash full set "
  "or refill. A brow shape and tint with a lash tint is $60 and can be booked on its own."),
 ("Can I book eyebrows without lash extensions?",
  "Yes. The brow shape and tint with lash tint package ($60) is booked as its own appointment. The $25 "
  "brow shape and the $40 brow shape and tint are add-ons to a lash full set or refill."),
 ("Is the brow shape done by waxing or threading?",
  "Waxing and tweezing. Wax takes care of the fine hair above and below the brow, and tweezing finishes "
  "the line and deals with anything the wax should not go near."),
 ("How long does a brow tint last?",
  "A tint softens gradually over a few weeks. How long it holds depends on your hair, your skincare and "
  "how much sun and salt water your brows see. Oil-based cleansers and exfoliants fade it faster."),
 ("Do I need a patch test for a brow tint?",
  "Yes, if you have not had a tint at the studio before. It takes two minutes, it is free, and it needs "
  "to be done at least 24 hours before your appointment, preferably 48."),
 ("How long does a brow appointment take?",
  "The brow shape and tint with lash tint package takes about 45 minutes. Added to a lash appointment, "
  "brows take 20 to 30 minutes on top."),
 ("How often should I have my brows done?",
  "Most people are ready for a tidy-up every four to six weeks. If you wear lash extensions, adding "
  "brows to every second refill keeps both on the same schedule."),
 ("Do you offer brow lamination, henna brows or microblading?",
  "No. The brow menu is deliberately short: shaping by wax and tweeze, and tinting. If one of those other "
  "treatments would suit you better, you will be told so."),
 ("Should I let my brows grow out before the appointment?",
  "If you can, leave them alone for two to three weeks beforehand. More hair to work with means more "
  "choice about the shape."),
]


def build():
    strip = lambda x: (x.replace("&mdash;", "-").replace("&ndash;", "-").replace("&amp;", "&")
                        .replace("&middot;", "-").replace("&rsquo;", "'"))
    service = {"@context": "https://schema.org", "@type": "Service",
      "serviceType": "Eyebrow shaping and tinting", "name": "Eyebrow Shaping, Waxing and Tinting in Yanchep",
      "description": strip(DESC), "url": URL,
      "provider": {"@type": "BeautySalon", "name": "Luxe Beauty Yanchep", "@id": SITE + "/#business",
        "telephone": "+61411487177", "priceRange": "$$", "url": SITE + "/",
        "address": {"@type": "PostalAddress", "addressLocality": "Yanchep", "addressRegion": "WA",
                    "postalCode": "6035", "addressCountry": "AU"}},
      "areaServed": [{"@type": "City", "name": n} for n in
                     ["Yanchep", "Two Rocks", "Eglinton", "Alkimos", "Jindalee", "Butler"]],
      "hasOfferCatalog": {"@type": "OfferCatalog", "name": "Brow and tint services", "itemListElement": [
        {"@type": "Offer", "itemOffered": {"@type": "Service", "name": n, "description": d},
         "price": p, "priceCurrency": "AUD", "availability": "https://schema.org/InStock"}
        for n, p, d in OFFERS]}}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
      {"@type": "Question", "name": strip(q), "acceptedAnswer": {"@type": "Answer", "text": strip(a)}}
      for q, a in FAQS]}
    crumb = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
      {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
      {"@type": "ListItem", "position": 2, "name": "Services", "item": SITE + "/services.html"},
      {"@type": "ListItem", "position": 3, "name": "Eyebrows Yanchep", "item": URL}]}
    faq_html = "".join('      <details class="faq"><summary>%s</summary><p>%s</p></details>\n' % (q, a)
                       for q, a in FAQS)

    head = B.head(TITLE, strip(DESC), SLUG, "photos/brow-1.jpg",
                  "\n".join([B.ld(service), B.ld(faq), B.ld(crumb)]))
    body = """
{nav}

<section class="hero hero--sm">
  <img class="hero-bg" src="photos/brow-1.jpg" alt="" aria-hidden="true">
  <div><p class="eyebrow">Brow shape, wax &amp; tint &middot; Yanchep WA</p>
  <h1>Eyebrows<br>in Yanchep</h1></div>
</section>

<section class="light">
  <div class="wrap">
    <div class="sec-head center rv">
      <h2>Shaped to your face, not a stencil</h2>
      <p class="lede" style="margin:0 auto">Eyebrow shaping and tinting in a private Yanchep studio.
        Brows are waxed and tweezed to a shape that follows your own bone structure, then tinted for
        depth if you want it. A brow shape is $25, a shape and tint is $40, and every price is on
        this page.</p>
    </div>

    <div class="grid g3 rv" style="margin-top:clamp(44px,5vw,70px)">
      <div class="card"><span class="num">01</span><h3>Mapped first</h3>
        <p>Where a brow should start, arch and finish is set by your face, not by a template. The shape
        is agreed with you before any wax goes on.</p></div>
      <div class="card"><span class="num">02</span><h3>Wax and tweeze</h3>
        <p>Wax for the fine hair above and below, tweezers for the line itself. Tidy and defined, without
        taking more than was agreed.</p></div>
      <div class="card"><span class="num">03</span><h3>Tint, if you want it</h3>
        <p>A tint picks up the fine, fair hairs that are already there, so brows look fuller with nothing
        drawn on. Chosen to suit your colouring.</p></div>
    </div>

    <div class="menu rv" style="margin-top:clamp(66px,9vw,110px)">
      <h3>Brow &amp; tint pricing</h3>
      <p class="note">Yanchep, WA. Prices are the same ones on the <a href="services.html">full menu</a>.</p>
      <div class="row"><span class="name">Brow Shape</span><span class="desc">Wax and tweeze, tidied and mapped to your features. Added to a lash set or refill.</span><span class="price">$25</span></div>
      <div class="row"><span class="name">Brow Shape &amp; Tint</span><span class="desc">Shaped and tinted for depth and definition. Added to a lash set or refill.</span><span class="price">$40</span></div>
      <div class="row"><span class="name">Lash Tint</span><span class="desc">Darkens fair lash tips so you can skip the mascara. Added to a lash set or refill.</span><span class="price">$25</span></div>
      <div class="row"><span class="name">Brow Shape &amp; Tint + Lash Tint</span><span class="desc">The brow appointment you can book on its own. About 45 minutes. Save $5.</span><span class="price">$60</span></div>
    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">How to book</p><h2>Two ways to have your brows done</h2>
    </div>
    <div class="prose rv">
      <p><b>With your lashes.</b> A brow shape ($25) or a brow shape and tint ($40) is added to a lash
      full set or refill and done in the same visit. It adds 20 to 30 minutes, and it is how most clients
      have their brows done, because one trip covers both.</p>
      <p><b>On their own.</b> The brow shape and tint with lash tint ($60) is a stand-alone appointment
      of about 45 minutes. Brows shaped, brows tinted and lashes tinted in one sitting. It is the one to
      choose before an event, or if you do not wear extensions.</p>
      <p>Either way you book online, and a $50 deposit confirms the appointment and comes off the total.
      If you already wear extensions, <a href="lash-extensions-yanchep.html">lash prices are here</a>.</p>
    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">What happens</p><h2>Your brow appointment</h2>
    </div>
    <div class="steps rv">
      <div class="step"><div><h3>Patch test, if it is your first tint</h3>
        <p>Two minutes, free, and done at least 24 hours before, preferably 48. Tint is the one part of a
        brow appointment that can cause a reaction, and this is how it is checked safely.</p></div></div>
      <div class="step"><div><h3>Mapping</h3>
        <p>A look at your natural brows, your face shape and how you usually wear them. If one brow sits
        higher or fuller than the other, which is normal, the plan allows for it.</p></div></div>
      <div class="step"><div><h3>Shape</h3>
        <p>Wax and tweeze to the agreed line. If your brows would look better left a little fuller, that
        is what you will be told, even if you asked for thinner.</p></div></div>
      <div class="step"><div><h3>Tint</h3>
        <p>Colour is matched to your hair and skin, applied to the brow, and removed once it has taken.
        A lash tint, if you are having one, is done in the same sitting.</p></div></div>
      <div class="step"><div><h3>Aftercare</h3>
        <p>Keep the area dry for 24 hours and go easy on oil-based cleansers and exfoliants afterwards.
        <a href="aftercare.html">Full aftercare</a>.</p></div></div>
    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">Timing</p><h2>How long it lasts</h2>
    </div>
    <div class="prose rv">
      <p>A shape lasts until the hair grows back, which for most people means a tidy-up every four to six
      weeks. A tint softens gradually over a few weeks. It does not stop suddenly, it just loses depth.</p>
      <p>In Yanchep, sun and salt water speed that up a little. Oil-based sunscreen and cleansers do the
      same, so cleanse around tinted brows gently and they will hold their colour longer.</p>
      <p>If you wear lash extensions you are in every two to three weeks for a refill anyway. Adding brows
      to every second refill keeps both on one schedule, and saves a separate trip.</p>
    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">Questions</p><h2>Good to know</h2>
    </div>
    <div style="max-width:800px;margin:0 auto">
{faq_html}    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">Nearby</p><h2>Brows for Yanchep and surrounds</h2>
    </div>
    <div class="prose rv">
      <p>The studio is a private home studio in Yanchep, WA 6035, with one client booked at a time. The
      exact address is sent with your booking confirmation. Clients come from Yanchep and from
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
    <img src="photos/brow-3.jpg" alt="" aria-hidden="true" loading="lazy">
    <p class="eyebrow">Yanchep &middot; new clients welcome</p>
    <h2>Book your brows</h2>
    <p class="lede" style="margin:20px auto 0">Add brows to a lash appointment, or book the $60 brow
      shape and tint with lash tint on its own.</p>
    <div class="btn-row"><a class="btn" data-book href="https://www.instagram.com/luxebeautyyanchep/">Book now</a>
      <a class="btn ghost" href="services.html">All services</a></div>
  </div></div>
</section>

{foot}""".format(nav=B.NAV, faq_html=faq_html,
                 foot=B.footer("Yanchep &middot; Two Rocks &middot; Alkimos &middot; Eglinton &middot; Butler"))
    return head + body


if __name__ == "__main__":
    open(os.path.join(ROOT, SLUG), "w", encoding="utf-8").write(build())
    print("  wrote", SLUG)
