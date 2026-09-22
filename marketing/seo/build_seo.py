# -*- coding: utf-8 -*-
"""
Generates the suburb landing pages + the "Areas We Serve" hub for
Luxe Beauty Yanchep, then rewrites sitemap.xml.

Run:  python3 marketing/seo/build_seo.py
It is idempotent - safe to re-run after editing suburbs.py.
"""
import json, os, sys, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from suburbs import TIER_A, TIER_B
_a = {s['name'] for s in TIER_A}
TIER_B = [b for b in TIER_B if b[0] not in _a]   # promoted suburbs get a page, not a row

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SITE = "https://luxebeautyyanchep.com"
TODAY = "2026-09-20"

NAV = """<header class="site-head">
  <div class="head-in">
    <a class="brand" href="index.html">
      <span class="mark" aria-hidden="true">LB</span>
      <span><b>Luxe Beauty</b><small>Lashes &amp; Brows</small></span>
    </a>
    <button class="nav-toggle" aria-expanded="false" aria-label="Menu">&#9776;</button>
    <nav class="nav">
      <a href="index.html">Home</a>
      <a href="services.html">Services</a>
      <a href="gallery.html">Gallery</a>
      <a href="areas-we-serve.html">Areas</a>
      <a href="aftercare.html">Aftercare</a>
      <a href="about.html">About</a>
      <a href="contact.html">Contact</a>
      <a class="btn" data-book href="https://www.instagram.com/luxebeautyyanchep/">Book now</a>
    </nav>
  </div>
</header>"""

def footer(area_line):
    return """<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div><h4>Luxe Beauty Yanchep</h4>
        <p>Luxury lashes &amp; brows in a private home studio.<br>Enhancing your natural beauty.</p></div>
      <div><h4>Treatments</h4>
        <a href="lash-extensions-yanchep.html">Lash extension prices</a>
        <a href="lash-lift-yanchep.html">Lash lift &amp; tint Yanchep</a>
        <a href="brow-lamination-yanchep.html">Brow lamination Yanchep</a>
        <a href="services.html">All services &amp; pricing</a></div>
      <div><h4>Guides</h4>
        <a href="lash-extensions-cost-perth.html">What lashes cost</a>
        <a href="lash-lift-vs-extensions.html">Lift vs extensions</a>
        <a href="classic-vs-hybrid-vs-volume-lashes.html">Classic, hybrid or volume</a>
        <a href="brow-lamination-vs-microblading.html">Lamination vs microblading</a></div>
      <div><h4>Areas served</h4>
        <a href="areas-we-serve.html">All areas we serve</a>
        <a href="lash-extensions-butler.html">Lashes Butler</a>
        <a href="lash-extensions-alkimos.html">Lashes Alkimos</a>
        <a href="lash-extensions-clarkson.html">Lashes Clarkson</a></div>
      <div><h4>Visit</h4>
        <p>Yanchep, WA 6035<br>Private home studio &mdash; exact address<br>sent with your booking confirmation.</p></div>
      <div><h4>Get in touch</h4>
        <a data-contact="instagram" href="https://www.instagram.com/luxebeautyyanchep/" target="_blank" rel="noopener">&#64;luxebeautyyanchep</a>
        <a data-contact="email" href="#">Email</a>
        <a data-contact="phone" href="#">Phone</a>
        <a class="btn ghost" data-book href="https://www.instagram.com/luxebeautyyanchep/" style="margin-top:16px">Book now</a></div>
    </div>
    <div class="foot-bot">
      <span>&copy; <span id="yr">2026</span> Luxe Beauty Yanchep</span>
      <span>%s</span>
    </div>
  </div>
</footer>
<script src="assets/site.js"></script>
</body>
</html>""" % area_line

PRICING = """    <div class="menu rv">
      <h3>Lash &amp; brow pricing</h3>
      <p class="note">Every appointment includes a consultation. Prices are the same wherever you travel from.</p>
      <div class="row"><span class="name">Classic Full Set</span><span class="desc">One extension per natural lash &mdash; defined and natural.</span><span class="price">$120</span></div>
      <div class="row"><span class="name">Hybrid Full Set</span><span class="desc">Classic and volume mixed for texture.</span><span class="price">$140</span></div>
      <div class="row"><span class="name">Volume Full Set</span><span class="desc">Lightweight fans for density and softness.</span><span class="price">$160</span></div>
      <div class="row"><span class="name">Mega Volume Full Set</span><span class="desc">Maximum density, still weightless.</span><span class="price">$180</span></div>
      <div class="row"><span class="name">Two / Three Week Refill</span><span class="desc">Keeps a set going indefinitely.</span><span class="price">$60 / $75</span></div>
      <div class="row"><span class="name">Lash Lift &amp; Tint</span><span class="desc">Your own lashes, lifted for six to eight weeks.</span><span class="price">$90</span></div>
      <div class="row"><span class="name">Brow Lamination &amp; Tint</span><span class="desc">Brows reset to sit full and brushed-up.</span><span class="price">$85</span></div>
      <div class="row"><span class="name">Lash Lift &amp; Tint + Brow Lamination &amp; Tint</span><span class="desc">The full eye reset. Save $15.</span><span class="price">$160</span></div>
    </div>"""

def head(title, desc, slug, hero_img, extra_ld):
    url = "%s/%s" % (SITE, slug)
    return """<!doctype html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{u}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Luxe Beauty Yanchep">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:image" content="{s}/icons/og-image.jpg">
<meta property="og:url" content="{u}">
<meta name="twitter:card" content="summary_large_image">
<meta name="geo.region" content="AU-WA">
<meta name="geo.placename" content="Yanchep, Western Australia">
<meta name="geo.position" content="-31.5464;115.6353">
<meta name="ICBM" content="-31.5464, 115.6353">
<link rel="icon" href="icons/favicon-64.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="Luxe Beauty">
<meta name="theme-color" content="#0C0B0A">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;1,300;1,400&family=Jost:wght@200;300;400&display=swap">
<link rel="stylesheet" href="assets/style.css">
<link rel="preload" as="image" href="{hero}" fetchpriority="high">
{ld}
</head>
<body>""".format(t=title, d=desc, u=url, s=SITE, ld=extra_ld, hero=hero_img)

def ld(obj):
    return '<script type="application/ld+json">\n%s\n</script>' % json.dumps(obj, ensure_ascii=False)

ALL_NAMES = [s["name"] for s in TIER_A] + [b[0] for b in TIER_B]

def build_suburb(s, idx):
    n, slug = s["name"], "lash-extensions-%s.html" % s["slug"]
    title = "Lash Extensions %s | Lashes &amp; Brows | Luxe Beauty Yanchep" % n
    desc = ("Lash extensions, lash lifts and brow lamination for %s, WA. A private studio in Yanchep, "
            "about %s minutes from %s via %s. Classic sets from $120." % (n, s["mins"], n, s["route"]))
    desc_plain = desc.replace("&mdash;", "-")

    breadcrumb = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
      {"@type":"ListItem","position":2,"name":"Areas We Serve","item":SITE+"/areas-we-serve.html"},
      {"@type":"ListItem","position":3,"name":"Lash Extensions "+n,"item":"%s/%s"%(SITE,slug)}]}

    service = {"@context":"https://schema.org","@type":"Service",
      "serviceType":"Eyelash Extensions","name":"Lash Extensions in %s"%n,
      "description":desc_plain,"url":"%s/%s"%(SITE,slug),
      "provider":{"@type":"BeautySalon","name":"Luxe Beauty Yanchep","@id":SITE+"/#business",
        "telephone":"+61411487177","priceRange":"$$",
        "address":{"@type":"PostalAddress","addressLocality":"Yanchep","addressRegion":"WA",
                   "postalCode":"6035","addressCountry":"AU"},
        "geo":{"@type":"GeoCoordinates","latitude":-31.5464,"longitude":115.6353}},
      "areaServed":{"@type":"City","name":n,"containedInPlace":{"@type":"State","name":"Western Australia"},
                    "postalCode":s["postcode"]},
      "hasOfferCatalog":{"@type":"OfferCatalog","name":"Lash and brow services","itemListElement":[
        {"@type":"Offer","itemOffered":{"@type":"Service","name":"Classic Full Set"},"price":"120","priceCurrency":"AUD"},
        {"@type":"Offer","itemOffered":{"@type":"Service","name":"Hybrid Full Set"},"price":"140","priceCurrency":"AUD"},
        {"@type":"Offer","itemOffered":{"@type":"Service","name":"Volume Full Set"},"price":"160","priceCurrency":"AUD"},
        {"@type":"Offer","itemOffered":{"@type":"Service","name":"Lash Lift and Tint"},"price":"90","priceCurrency":"AUD"},
        {"@type":"Offer","itemOffered":{"@type":"Service","name":"Brow Lamination and Tint"},"price":"85","priceCurrency":"AUD"}]}}

    def strip(x): return x.replace("&mdash;","-").replace("&nbsp;"," ").replace("&amp;","&")
    faq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
      {"@type":"Question","name":strip(q),"acceptedAnswer":{"@type":"Answer","text":strip(a)}}
      for q,a in s["faqs"]]}

    # neighbouring Tier A suburbs for internal linking (by distance proximity)
    others = sorted([o for o in TIER_A if o["slug"]!=s["slug"]], key=lambda o: abs(o["km"]-s["km"]))[:4]
    near = "".join(
      '<a class="btn ghost" href="lash-extensions-%s.html" style="margin:0 8px 8px 0">%s</a>'
      % (o["slug"], o["name"]) for o in others)

    faq_html = "".join(
      '      <details class="faq"><summary>%s</summary><p>%s</p></details>\n' % (q,a)
      for q,a in s["faqs"])

    h = head(title, desc_plain, slug, s["hero"], "\n".join([ld(service), ld(faq), ld(breadcrumb)]))

    body = """
{nav}

<section class="hero hero--sm">
  <img class="hero-bg" src="{hero}" alt="" aria-hidden="true">
  <div><p class="eyebrow">{n} &middot; {km} km from the studio</p>
  <h1>Lash Extensions<br>in {n}</h1></div>
</section>

<section class="light">
  <div class="wrap">
    <div class="sec-head center rv">
      <h2>Lashes &amp; brows for {n}</h2>
      <p class="lede" style="margin:0 auto">{intro}</p>
    </div>

    <div class="info rv" style="max-width:720px;margin:clamp(40px,5vw,64px) auto 0">
      <div><b>Distance</b><span>About {km} km from {n} to the studio in Yanchep.</span></div>
      <div><b>Drive time</b><span>Roughly {mins} minutes, {route}.</span></div>
      <div><b>Landmark</b><span>Around {anchor}.</span></div>
      <div><b>Parking</b><span>Free off-street parking at the studio &mdash; no shopping-centre car park.</span></div>
      <div><b>Privacy</b><span>One client at a time. The exact address is sent with your booking confirmation.</span></div>
    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">Why {n} clients come here</p><h2>Worth the {mins} minutes</h2>
      <p class="lede" style="margin:0 auto">{angle}</p>
    </div>
    <p class="note" style="max-width:700px;margin:26px auto 0;text-align:center">{local}</p>

    <div style="margin-top:clamp(66px,9vw,110px)">
{pricing}
    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">Treatments</p><h2>What you can book</h2>
    </div>
    <div class="grid g3 rv">
      <div class="card"><span class="num">01</span><h3>Lash extensions</h3>
        <p>Classic, hybrid, volume and mega volume, mapped to your eye shape and natural lash health.
        <a href="lash-extensions-yanchep.html">Full details &amp; pricing</a>.</p></div>
      <div class="card"><span class="num">02</span><h3>Lash lift &amp; tint</h3>
        <p>A keratin lift on your own lashes, six to eight weeks, no refills.
        <a href="lash-lift-yanchep.html">Full details &amp; pricing</a>.</p></div>
      <div class="card"><span class="num">03</span><h3>Brow lamination</h3>
        <p>Brows reset to sit full and brushed-up, with optional tint and shape.
        <a href="brow-lamination-yanchep.html">Full details &amp; pricing</a>.</p></div>
    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">Questions from {n}</p><h2>Good to know</h2>
    </div>
    <div style="max-width:800px;margin:0 auto">
{faq_html}    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">Nearby</p><h2>Also serving</h2>
    </div>
    <div class="center" style="max-width:760px;margin:0 auto">
      {near}
      <p class="note" style="margin-top:18px"><a href="areas-we-serve.html">See every suburb the studio serves &rarr;</a></p>
    </div>
  </div>
</section>

<section>
  <div class="wrap"><div class="callout rv">
    <img src="photos/lash-2.jpg" alt="" aria-hidden="true" loading="lazy">
    <p class="eyebrow">Now booking &middot; {n} &amp; surrounds</p>
    <h2>Book your appointment</h2>
    <p class="lede" style="margin:20px auto 0">A private studio in Yanchep, about {mins} minutes
      from {n} &mdash; no freeway, no waiting room.</p>
    <div class="btn-row"><a class="btn" data-book href="https://www.instagram.com/luxebeautyyanchep/">Book now</a>
      <a class="btn ghost" href="services.html">All services</a></div>
  </div></div>
</section>

{foot}""".format(nav=NAV, hero=s["hero"], n=n, km=s["km"], mins=s["mins"], route=s["route"],
                 anchor=s["anchor"], intro=s["intro"], angle=s["angle"], local=s["local"],
                 pricing=PRICING, faq_html=faq_html, near=near,
                 foot=footer("Yanchep &middot; %s &middot; Butler &middot; Clarkson &middot; Joondalup" % n))
    return slug, h + body

def build_hub():
    slug = "areas-we-serve.html"
    title = "Areas We Serve | Lash &amp; Brow Studio Near You | Luxe Beauty Yanchep"
    desc = ("Luxe Beauty is a private lash and brow studio in Yanchep, WA, serving 60+ suburbs across "
            "Perth's northern corridor - Two Rocks, Alkimos, Butler, Clarkson, Joondalup and beyond.")

    area_served = ([{"@type":"City","name":s["name"],"postalCode":s["postcode"]} for s in TIER_A]
                   + [{"@type":"City","name":b[0],"postalCode":b[1]} for b in TIER_B]
                   + [{"@type":"City","name":"Yanchep","postalCode":"6035"}])
    biz = {"@context":"https://schema.org","@type":"BeautySalon","@id":SITE+"/#business",
      "name":"Luxe Beauty Yanchep","url":SITE+"/","image":SITE+"/icons/og-image.jpg",
      "telephone":"+61411487177","priceRange":"$$","currenciesAccepted":"AUD",
      "description":"Private lash and brow studio in Yanchep, Western Australia, serving Perth's northern corridor.",
      "address":{"@type":"PostalAddress","addressLocality":"Yanchep","addressRegion":"WA",
                 "postalCode":"6035","addressCountry":"AU"},
      "geo":{"@type":"GeoCoordinates","latitude":-31.5464,"longitude":115.6353},
      "areaServed":area_served,
      "openingHoursSpecification":[{"@type":"OpeningHoursSpecification",
        "dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
        "opens":"09:00","closes":"17:00"}],
      "sameAs":["https://www.instagram.com/luxebeautyyanchep/","https://www.facebook.com/luxebeautyyanchep"]}
    crumb = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
      {"@type":"ListItem","position":2,"name":"Areas We Serve","item":"%s/%s"%(SITE,slug)}]}

    cards = "".join(
      '      <a class="card" href="lash-extensions-{sl}.html" style="text-decoration:none;display:block">'
      '<span class="num">{km} KM</span><h3>{n}</h3>'
      '<p>{mins} minutes {route}. {anchor_s}.</p></a>\n'.format(
        sl=s["slug"], n=s["name"], km=s["km"], mins=s["mins"], route=s["route"],
        anchor_s="Near "+s["anchor"]) for s in TIER_A)

    rows = "".join(
      '      <div class="row"><span class="name">{n}</span>'
      '<span class="desc">WA {pc} &middot; about {mins} minutes from the studio</span>'
      '<span class="price">{km} km</span></div>\n'.format(n=b[0], pc=b[1], km=b[2], mins=b[3])
      for b in sorted(TIER_B, key=lambda x: x[2]))

    h = head(title, desc, slug, "photos/bleed.jpg", "\n".join([ld(biz), ld(crumb)]))
    body = """
{nav}

<section class="hero hero--sm">
  <img class="hero-bg" src="photos/bleed.jpg" alt="" aria-hidden="true">
  <div><p class="eyebrow">Perth's northern corridor</p><h1>Areas<br>We Serve</h1></div>
</section>

<section class="light">
  <div class="wrap">
    <div class="sec-head center rv">
      <h2>A private studio in Yanchep</h2>
      <p class="lede" style="margin:0 auto">Luxe Beauty is a home studio, not a shopfront &mdash; which
        means clients travel to it rather than stumbling past it. That is worth being honest about, so
        below is every suburb the studio serves, how far away it actually is, and roughly how long the
        drive takes. Prices are the same wherever you come from.</p>
    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">The close corridor</p><h2>Suburbs within 25 minutes</h2>
      <p class="lede" style="margin:0 auto">These are the suburbs most clients come from. Each has its
        own page with drive times, local detail and the questions people from that area actually ask.</p>
    </div>
    <div class="grid g3 rv" style="margin-top:clamp(30px,4vw,50px)">
{cards}    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">The wider ring</p><h2>Also within 40 km</h2>
      <p class="lede" style="margin:0 auto">Clients do travel from these suburbs, usually for a full set
        or a combination appointment rather than a quick tint &mdash; at this distance it is worth making
        one trip do the work of two. Straight-line distances from the studio.</p>
    </div>
    <div class="menu rv" style="margin-top:clamp(30px,4vw,50px)">
      <h3>Northern corridor &amp; beyond</h3>
      <p class="note">Distances are straight-line from Yanchep; drive times are indicative and assume
        off-peak traffic.</p>
{rows}    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">Coming from further out</p><h2>Making the trip worth it</h2>
    </div>
    <div class="grid g3 rv">
      <div class="card"><span class="num">01</span><h3>Combine treatments</h3>
        <p>A lash lift and tint with brow lamination and tint is $160 together rather than $175
        separately, and runs about two hours in one sitting. Most clients travelling more than
        twenty-five minutes book a combination.</p></div>
      <div class="card"><span class="num">02</span><h3>Plan the patch test</h3>
        <p>Anything involving tint or lash adhesive needs a patch test about 48 hours before your first
        appointment. If you are coming a distance, tie it to another trip rather than driving twice.</p></div>
      <div class="card"><span class="num">03</span><h3>Book a standing slot</h3>
        <p>Refills run every two to three weeks. Regulars from further out book the next appointment
        before they leave, which locks in a time that suits the drive.</p></div>
    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">Questions</p><h2>Good to know</h2>
    </div>
    <div style="max-width:800px;margin:0 auto">
      <details class="faq"><summary>Do you travel to clients?</summary><p>No &mdash; all appointments are
        at the private studio in Yanchep. Lash work needs controlled lighting, a proper bed and a still,
        dust-free room, none of which travel well. The exact address is sent with your booking confirmation.</p></details>
      <details class="faq"><summary>Is there a travel fee or a different price for outer suburbs?</summary>
        <p>No. Prices are identical wherever you come from &mdash; a classic full set is $120 whether you
        live in Eglinton or Karrinyup.</p></details>
      <details class="faq"><summary>What if my suburb is not listed?</summary><p>The list covers roughly a
        40 km radius, but nobody is turned away for living outside it. Send a message and it can be sorted out.</p></details>
      <details class="faq"><summary>Where exactly is the studio?</summary><p>In Yanchep, WA 6035. It is a
        private home studio, so the address is not published &mdash; it is sent to you once your appointment
        is confirmed. There is free off-street parking.</p></details>
      <details class="faq"><summary>How long should I allow for an appointment?</summary><p>A classic full set
        is about two hours, volume closer to two and a half. Refills are under an hour, and a lash lift is
        45 minutes to an hour. Add your drive time to that when planning the day.</p></details>
    </div>
  </div>
</section>

<section>
  <div class="wrap"><div class="callout rv">
    <img src="photos/feature.jpg" alt="" aria-hidden="true" loading="lazy">
    <p class="eyebrow">60+ suburbs &middot; one studio</p>
    <h2>Book your appointment</h2>
    <p class="lede" style="margin:20px auto 0">Wherever you are driving from, you get the same thing:
      one client at a time, in a private studio, with the time your set actually needs.</p>
    <div class="btn-row"><a class="btn" data-book href="https://www.instagram.com/luxebeautyyanchep/">Book now</a>
      <a class="btn ghost" href="services.html">All services</a></div>
  </div></div>
</section>

{foot}""".format(nav=NAV, cards=cards, rows=rows,
                 foot=footer("Yanchep &middot; Two Rocks &middot; Alkimos &middot; Butler &middot; Clarkson &middot; Joondalup"))
    return slug, h + body

def main():
    written = []
    for i, s in enumerate(TIER_A):
        slug, html = build_suburb(s, i)
        open(os.path.join(ROOT, slug), "w", encoding="utf-8").write(html)
        written.append((slug, "0.8"))
        print("  wrote", slug)
    slug, html = build_hub()
    open(os.path.join(ROOT, slug), "w", encoding="utf-8").write(html)
    written.append((slug, "0.9"))
    print("  wrote", slug)

    guides = [("lash-extensions-cost-perth.html","0.8"),("lash-lift-vs-extensions.html","0.8"),
              ("classic-vs-hybrid-vs-volume-lashes.html","0.7"),
              ("brow-lamination-vs-microblading.html","0.7")]
    core = [("", "1.0"), ("services.html","0.9"), ("lash-extensions-yanchep.html","0.9"),
            ("lash-lift-yanchep.html","0.9"), ("brow-lamination-yanchep.html","0.9"),
            ("gallery.html","0.7"), ("contact.html","0.8"), ("aftercare.html","0.6"),
            ("about.html","0.6")]
    urls = (core[:5] + [("areas-we-serve.html","0.9")] + guides
            + [w for w in written if w[0]!="areas-we-serve.html"] + core[5:])
    seen, out = set(), []
    for u,p in urls:
        if u in seen: continue
        seen.add(u)
        out.append('  <url><loc>%s/%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>' % (SITE,u,TODAY,p))
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' \
         + "\n".join(out) + "\n</urlset>\n"
    open(os.path.join(ROOT,"sitemap.xml"),"w",encoding="utf-8").write(sm)
    print("  wrote sitemap.xml (%d urls)" % len(out))

if __name__ == "__main__":
    main()
