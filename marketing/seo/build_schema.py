# -*- coding: utf-8 -*-
"""
Entity schema + AI-crawler surface for Luxe Beauty Yanchep.

Regenerates:
  index.html   -> a consolidated schema.org @graph (WebSite + LocalBusiness + WebPage + FAQPage)
                  and the visible homepage FAQ (HOME_FAQS is the single source for both)
  hand-written pages (services, about, aftercare, gallery, contact)
               -> JSON-LD between LD markers, and the shared footer from build_seo.py
  llms.txt     -> curated plain-text brief for LLM crawlers (ChatGPT, Perplexity, Claude)
  robots.txt   -> explicit allow-list for AI crawlers

Only verified facts go in here. Do not invent credentials, staff names,
review counts or ratings.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from suburbs import TIER_A, TIER_B
from guides import GUIDES
import build_seo as B
import hours
import prices

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SITE = "https://luxebeautyyanchep.com"
PHONE = "+61411487177"
# The Google Business Profile listing (Maps CID). Linking it from the site's schema ties the
# website and the Maps listing together as one business.
GOOGLE_MAPS = "https://www.google.com/maps?cid=5383694766537348091"
BOOKING_URL = "https://book.squareup.com/appointments/7f8c8bo8u2qnx0/location/L33Q7M0YA0VCJ"   # same as assets/site.js (check.py compares)

SERVICES = [
    ("Classic Lash Extensions", "120", "One extension per natural lash for defined, everyday length."),
    ("Hybrid Lash Extensions", "140", "Classic extensions and volume fans mixed for texture and fullness."),
    ("Volume Lash Extensions", "160", "Lightweight handmade fans for density and softness."),
    ("Mega Volume Lash Extensions", "180", "Maximum density, still lightweight on the natural lash."),
] + [
    (n, str(p), "Refilling another technician's work, including tidy-up." if "Foreign" in n
     else "Maintains an existing %s set of extensions." % n.split(" Two ")[0].split(" Three ")[0].lower())
    for n, p, _ in prices.refill_services()
] + [
    ("Lash Removal", "25", "Safe, gentle removal. Add-on to a lash set or refill."),
    ("Lash Tint", "25", "Darkens fair lash tips. Add-on to a lash set or refill."),
    ("Brow Shape", "25", "Shaping only. Add-on to a lash set or refill."),
    ("Brow Shape and Tint", "40", "Shaped and tinted. Add-on to a lash set or refill."),
    ("Brow Shape and Tint with Lash Tint", "60", "Brows shaped and tinted with a lash tint. Can be booked on its own."),
]

AREAS = ["Yanchep"] + [s["name"] for s in TIER_A] + [b[0] for b in TIER_B]
AREAS = list(dict.fromkeys(AREAS))

KNOWS_ABOUT = [
    "Eyelash extensions", "Classic lash extensions", "Hybrid lash extensions",
    "Volume lash extensions", "Mega volume lash extensions", "Lash tinting",
    "Lash refills", "Lash infills", "Brow tinting", "Brow shaping", "Eyebrow waxing", "Lash aftercare", "Lash mapping",
    "Wedding lash extensions",
]

# The homepage FAQ. One list drives BOTH the visible <details> on index.html and the
# FAQPage node in its JSON-LD, so the markup can never claim something the page does not show.
# Every answer restates a fact already published on services.html / contact.html.
HOME_FAQS = [
 ("Where is Luxe Beauty Yanchep?",
  "Luxe Beauty is a private home studio in Yanchep, WA 6035. Because it is a home studio the street "
  "address is not published. It is sent to you with your booking confirmation, and there is free parking."),
 ("How much are lash extensions in Yanchep?",
  "A classic full set is $120, hybrid $140, volume $160 and mega volume $180. Every price is published "
  "and is the price you pay on the day."),
 ("How much is a lash infill?",
  "Infills, also called refills, keep an existing set full. Classic infills are $60 within two weeks "
  "and $75 within three. Hybrid, volume and mega volume infills are priced in proportion to the full "
  "set, from $70 to $115. Infilling another technician's work costs a little more."),
 ("Do you do eyebrows?",
  "Yes. A brow shape (wax and tweeze) is $25 and a brow shape and tint is $40 when added to a lash "
  "appointment. A brow shape and tint with a lash tint is $60 and can be booked on its own."),
 ("How do I book?",
  "Online, in about a minute. A $50 deposit confirms your appointment and comes off the total. Online "
  "booking closes 24 hours ahead, so for anything sooner call or message the studio."),
 ("Do I need a patch test?",
  "Yes, if it is your first time having lash extensions or a tint. It takes two minutes, it is free, and "
  "it needs to be done at least 24 hours before your appointment."),
 ("How long does a full set of lash extensions take?",
  "About two hours for a classic set and up to two and a half for volume or mega volume. Refills are "
  "around an hour. Only one client is booked at a time."),
 ("What are your opening hours?",
  hours.sentence() + " Evening appointments run on Monday, Tuesday and Thursday."),
 ("Which areas do you serve?",
  "Yanchep, Two Rocks, Eglinton, Alkimos, Jindalee and Butler make up most of the studio's clients, and "
  "people travel from across Perth's northern corridor. Prices are the same wherever you come from."),
]

def business_node():
    return {
        "@type": ["BeautySalon", "LocalBusiness"],
        "@id": SITE + "/#business",
        "name": "Luxe Beauty Yanchep",
        "alternateName": "Luxe Beauty",
        "url": SITE + "/",
        "image": SITE + "/icons/og-image.jpg",
        "logo": {"@type": "ImageObject", "url": SITE + "/icons/icon-512.png"},
        "description": ("Private lash and brow studio in Yanchep, Western Australia. Classic, hybrid, "
                        "volume and mega volume eyelash extensions, lash refills, lash tinting, "
                        "brow tinting and shaping. One client at a time."),
        "telephone": PHONE,
        "email": "bec@luxebeautyyanchep.com",
        "priceRange": "$$",
        "currenciesAccepted": "AUD",
        "paymentAccepted": "Cash, EFTPOS, Credit Card",
        "address": {"@type": "PostalAddress", "addressLocality": "Yanchep",
                    "addressRegion": "WA", "postalCode": "6035", "addressCountry": "AU"},
        "geo": {"@type": "GeoCoordinates", "latitude": -31.5464, "longitude": 115.6353},
        "openingHoursSpecification": hours.schema(),
        "areaServed": [{"@type": "City", "name": n, "containedInPlace":
                        {"@type": "State", "name": "Western Australia"}} for n in AREAS],
        "knowsAbout": KNOWS_ABOUT,
        "availableLanguage": {"@type": "Language", "name": "English"},
        "hasMap": GOOGLE_MAPS,
        "potentialAction": {"@type": "ReserveAction", "name": "Book an appointment",
            "target": {"@type": "EntryPoint", "urlTemplate": BOOKING_URL, "inLanguage": "en-AU",
                       "actionPlatform": ["https://schema.org/DesktopWebPlatform",
                                          "https://schema.org/MobileWebPlatform"]},
            "result": {"@type": "Reservation", "name": "Lash or brow appointment"}},
        "sameAs": ["https://www.instagram.com/luxebeautyyanchep/",
                   "https://www.facebook.com/luxebeautyyanchep",
                   GOOGLE_MAPS],
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": "Lash and brow services",
            "itemListElement": [
                {"@type": "Offer",
                 "itemOffered": {"@type": "Service", "name": n, "description": d,
                                 "serviceType": "Beauty treatment",
                                 "provider": {"@id": SITE + "/#business"}},
                 "price": p, "priceCurrency": "AUD",
                 "availability": "https://schema.org/InStock"}
                for n, p, d in SERVICES]},
    }

def graph():
    return {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "@id": SITE + "/#website", "url": SITE + "/",
         "name": "Luxe Beauty Yanchep", "inLanguage": "en-AU",
         "publisher": {"@id": SITE + "/#business"}},
        business_node(),
        {"@type": "WebPage", "@id": SITE + "/#webpage", "url": SITE + "/",
         "name": "Lash Extensions & Brows Yanchep | Luxe Beauty Yanchep",
         "isPartOf": {"@id": SITE + "/#website"},
         "about": {"@id": SITE + "/#business"},
         "primaryImageOfPage": {"@type": "ImageObject", "url": SITE + "/icons/og-image.jpg"},
         "inLanguage": "en-AU"},
        {"@type": "FAQPage", "@id": SITE + "/#faq", "isPartOf": {"@id": SITE + "/#webpage"},
         "mainEntity": [{"@type": "Question", "name": q,
                         "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in HOME_FAQS]},
    ]}

def write_index():
    p = os.path.join(ROOT, "index.html")
    s = open(p, encoding="utf-8").read()
    block = ('<script type="application/ld+json">\n'
             + json.dumps(graph(), ensure_ascii=False, indent=1) + '\n</script>')
    new, n = re.subn(r'<script type="application/ld\+json">.*?</script>', lambda m: block, s, count=1, flags=re.S)
    assert n == 1, "homepage JSON-LD block not found"
    esc = lambda x: x.replace("&", "&amp;")
    faq_html = "".join('      <details class="faq"><summary>%s</summary><p>%s</p></details>\n'
                       % (esc(q), esc(a)) for q, a in HOME_FAQS)
    new, n = re.subn(r'(<!-- FAQ:START[^>]*-->\n).*?(<!-- FAQ:END -->)',
                     lambda m: m.group(1) + faq_html + m.group(2), new, count=1, flags=re.S)
    assert n == 1, "homepage FAQ markers not found"
    new = sync_footer(new)
    open(p, "w", encoding="utf-8").write(new)
    json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',
                         open(p, encoding="utf-8").read(), re.S).group(1))
    print("  index.html  @graph written (%d nodes)" % len(graph()["@graph"]))

def sync_footer(html):
    """Hand-written pages carry the same footer as generated ones (links live in build_seo.footer)."""
    m = re.search(r'<footer class="site-foot">.*</html>\s*$', html, re.S)
    assert m, "footer not found"
    line = re.search(r'<div class="foot-bot">\s*<span>.*?</span>\s*<span>(.*?)</span>', m.group(0), re.S).group(1)
    return html[:m.start()] + B.footer(line) + "\n"

def crumb(*trail):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + "/" + u}
        for i, (n, u) in enumerate(trail)]}

def static_schema():
    biz = {"@id": SITE + "/#business"}
    web = {"@id": SITE + "/#website"}
    page = lambda t, slug, name, desc: {"@context": "https://schema.org", "@type": t,
        "@id": "%s/%s#webpage" % (SITE, slug), "url": "%s/%s" % (SITE, slug), "name": name,
        "description": desc, "inLanguage": "en-AU", "isPartOf": web, "about": biz}
    catalog = {"@context": "https://schema.org", "@type": "OfferCatalog",
        "name": "Luxe Beauty Yanchep services and prices", "url": SITE + "/services.html",
        "itemListElement": [
            {"@type": "Offer", "price": p, "priceCurrency": "AUD",
             "availability": "https://schema.org/InStock", "offeredBy": biz,
             "itemOffered": {"@type": "Service", "name": n, "description": d,
                             "areaServed": {"@type": "City", "name": "Yanchep"}}}
            for n, p, d in SERVICES]}
    howto_steps = [
        ("Keep them dry for 24 hours", "Avoid water, steam, saunas and heavy sweating while the adhesive fully cures."),
        ("Cleanse daily", "Use a lash-safe foaming cleanser and a soft brush every day. Clean lashes last longer."),
        ("Avoid oil", "Oil breaks down lash adhesive. Check your cleanser, moisturiser, sunscreen and makeup remover."),
        ("Skip lash curlers and waterproof mascara", "Extensions already hold their curl, and waterproof mascara cannot be removed safely."),
        ("Sleep on your back where you can", "Side sleepers see one side thin first. A silk pillowcase helps."),
        ("Book a refill every two to three weeks", "Regular refills keep a set full and cost less than starting again."),
    ]
    return {
     "services.html": [
        page("WebPage", "services.html", "Lash Extension & Brow Prices | Luxe Beauty Yanchep",
             "The full Luxe Beauty Yanchep menu with prices: lash extension full sets, refills, lash tint, brow shape and tint."),
        catalog, crumb(("Home", ""), ("Services & prices", "services.html"))],
     "about.html": [
        page("AboutPage", "about.html", "About Luxe Beauty Yanchep",
             "A private lash and brow studio in Yanchep, WA. One client at a time."),
        crumb(("Home", ""), ("About", "about.html"))],
     "aftercare.html": [
        {"@context": "https://schema.org", "@type": "HowTo", "name": "How to look after lash extensions",
         "description": "The daily aftercare routine that keeps a set of lash extensions full between refills.",
         "url": SITE + "/aftercare.html", "inLanguage": "en-AU", "publisher": biz,
         "step": [{"@type": "HowToStep", "position": i + 1, "name": n, "text": t}
                  for i, (n, t) in enumerate(howto_steps)]},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in AFTERCARE_FAQS]},
        crumb(("Home", ""), ("Lash guides", "lash-guides.html"), ("Aftercare", "aftercare.html"))],
     "gallery.html": [
        page("WebPage", "gallery.html", "Lash & Brow Gallery | Luxe Beauty Yanchep",
             "The natural, mapped-to-you finish behind every lash and brow appointment at Luxe Beauty Yanchep."),
        crumb(("Home", ""), ("Gallery", "gallery.html"))],
     "contact.html": [
        page("ContactPage", "contact.html", "Book a Lash Appointment in Yanchep | Luxe Beauty Yanchep",
             "Book online, call or message Luxe Beauty Yanchep. Studio hours, location and booking policies."),
        crumb(("Home", ""), ("Contact & booking", "contact.html"))],
    }

AFTERCARE_FAQS = [
 ("How soon can I get lash extensions wet?",
  "After 24 hours. The adhesive needs a full day to cure, so keep water, steam and heavy sweat away from "
  "your lashes until then."),
 ("How do I wash lash extensions?",
  "Once a day with a lash-safe foaming cleanser. Work it gently through the lashes with a soft brush, "
  "rinse with cool water, pat dry and brush through with a clean spoolie."),
 ("Can I wear mascara or eyeliner with lash extensions?",
  "You should not need mascara, and waterproof or oil-based mascara will break down the adhesive. If you "
  "wear eyeliner, choose an oil-free one and remove it with an oil-free remover."),
 ("What should I avoid with lash extensions?",
  "Oil-based products around the eyes, rubbing or picking, lash curlers, waterproof mascara, and water or "
  "steam in the first 24 hours."),
 ("Can I swim with lash extensions?",
  "Yes, after the first 24 hours. Rinse with fresh water afterwards, pat dry and cleanse that evening."),
 ("How often do I need a refill?",
  "Every two to three weeks. Beyond three weeks there is usually too little of the set left to refill "
  "and a new full set is needed."),
 ("How do I look after a brow or lash tint?",
  "Keep the area dry for 24 hours, then go easy on oil-based cleansers and exfoliants, which fade a tint "
  "faster. A tint softens gradually over a few weeks."),
]

def write_static():
    esc = lambda x: x.replace("&", "&amp;")
    for slug, nodes in static_schema().items():
        p = os.path.join(ROOT, slug)
        s = open(p, encoding="utf-8").read()
        block = ("<!-- LD:START (generated by marketing/seo/build_schema.py) -->\n"
                 + "\n".join('<script type="application/ld+json">\n%s\n</script>'
                             % json.dumps(n, ensure_ascii=False) for n in nodes)
                 + "\n<!-- LD:END -->")
        if "<!-- LD:START" in s:
            s = re.sub(r"<!-- LD:START.*?<!-- LD:END -->", lambda m: block, s, flags=re.S)
        else:
            s = s.replace("</head>", block + "\n</head>", 1)
        if slug == "contact.html":
            rows_html = "".join("          <div><b>%s</b><span>%s</span></div>\n" % (l.replace(" and ", " &amp; "), t)
                                for l, t in hours.rows())
            s, n = re.subn(r'(<!-- HOURS:START[^>]*-->\n).*?(<!-- HOURS:END -->)',
                           lambda m: m.group(1) + rows_html + m.group(2), s, count=1, flags=re.S)
            assert n == 1, "contact hours markers not found"
        if slug == "aftercare.html":
            faq_html = "".join('      <details class="faq"><summary>%s</summary><p>%s</p></details>\n'
                               % (esc(q), esc(a)) for q, a in AFTERCARE_FAQS)
            s, n = re.subn(r'(<!-- FAQ:START[^>]*-->\n).*?(<!-- FAQ:END -->)',
                           lambda m: m.group(1) + faq_html + m.group(2), s, count=1, flags=re.S)
            assert n == 1, "aftercare FAQ markers not found"
        s = sync_footer(s)
        open(p, "w", encoding="utf-8").write(s)
        for b in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
            json.loads(b)
        print("  %-14s schema + footer written" % slug)

def write_llms():
    lines = []
    A = lines.append
    A("# Luxe Beauty Yanchep")
    A("")
    A("> Private lash and brow studio in Yanchep, Western Australia (WA 6035). Eyelash")
    A("> extensions, lash refills, tinting and brow shaping, by appointment, one client")
    A("> at a time. Serving Yanchep and the northern Perth corridor.")
    A("")
    A("## Facts")
    A("")
    A("- Business name: Luxe Beauty Yanchep")
    A("- Type: private home studio (service-area business, by appointment only)")
    A("- Location: Yanchep, Western Australia 6035, Australia")
    A("- Phone: 0411 487 177")
    A("- Email: bec@luxebeautyyanchep.com")
    A("- Website: %s" % SITE)
    A("- Hours: " + hours.sentence())
    A("- Booking: by appointment; patch test required 48 hours before a first appointment")
    A("- Instagram: https://www.instagram.com/luxebeautyyanchep/")
    A("- Facebook: https://www.facebook.com/luxebeautyyanchep")
    A("- Google Maps: %s" % GOOGLE_MAPS)
    A("- Book online: %s/book (forwards to %s)" % (SITE, BOOKING_URL))
    A("")
    A("## Services and prices (AUD)")
    A("")
    for n, p, d in SERVICES:
        A("- %s: $%s - %s" % (n, p, d))
    A("")
    A("## Areas served")
    A("")
    A("Yanchep and %d suburbs across Perth's northern corridor, including: %s."
      % (len(AREAS) - 1, ", ".join(AREAS[1:26])))
    A("Full list with distances and drive times: %s/areas-we-serve.html" % SITE)
    A("")
    A("## Key pages")
    A("")
    A("- [Lash extension prices Yanchep](%s/lash-extensions-yanchep.html): classic, hybrid, volume and mega volume sets, prices, FAQs" % SITE)
    A("- [Eyebrows Yanchep](%s/eyebrows-yanchep.html): brow shape (wax and tweeze), brow tint and lash tint, prices, how to book" % SITE)
    A("- [Lash infills Yanchep](%s/lash-infills-yanchep.html): two week, three week and foreign infills (refills) for every lash style, with prices" % SITE)
    A("- [Areas we serve](%s/areas-we-serve.html): every suburb served, with distances and drive times" % SITE)
    A("- [Services and pricing](%s/services.html): the full menu" % SITE)
    A("- [Aftercare](%s/aftercare.html): how to make a set last" % SITE)
    A("")
    A("## Guides")
    A("")
    for g in GUIDES:
        t = g["title"].replace("&amp;", "&")
        A("- [%s](%s/%s.html): %s" % (t, SITE, g["slug"], g["desc"]))
    A("- [All lash guides](%s/lash-guides.html)" % SITE)
    A("")
    A("## Common questions")
    A("")
    A("- How much are lash extensions in Yanchep? A classic full set is $120, hybrid $140, volume $160, mega volume $180. Classic refills are $60 at two weeks or $75 at three weeks; refills for hybrid, volume and mega volume sets are priced in the same proportion to the full set.")
    A("- How long do lash extensions last? Individual extensions last the life of the natural lash they are attached to, six to eight weeks. A refill every two to three weeks keeps a set looking full.")
    A("- How long does a full set take? About two hours for classic, up to two and a half for volume or mega volume.")
    A("- Is a patch test needed? Yes, before a first appointment, at least 24 hours ahead and preferably 48.")
    A("- How much are brows? A brow shape is $25, or $40 with a tint, as an add-on to a lash set or refill. Lash tint and lash removal ($25 each) are add-ons too. Booked without lashes, a brow shape and tint with a lash tint is $60.")
    A("- Where is the studio? Yanchep, WA 6035. It is a private home studio; the exact address is sent on booking confirmation. Free parking.")
    A("- Can I swim with lash extensions? Yes, after the first 24 hours. Rinse with fresh water afterwards and keep oil-based sunscreen away from the lash line.")
    A("- When should I get lash extensions before a wedding? A trial set six to eight weeks before, then a final refill three to five days before the day.")
    A("")
    open(os.path.join(ROOT, "llms.txt"), "w", encoding="utf-8").write("\n".join(lines))
    print("  llms.txt    written (%d lines)" % len(lines))

AI_BOTS = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "PerplexityBot", "Perplexity-User",
           "ClaudeBot", "Claude-User", "Claude-SearchBot", "Google-Extended",
           "Applebot", "Applebot-Extended", "CCBot", "Bingbot", "Amazonbot", "meta-externalagent"]

def write_robots():
    L = ["# Luxe Beauty Yanchep", "",
         "User-agent: *", "Allow: /", "",
         "# AI assistants and answer engines are explicitly allowed. Being cited by",
         "# ChatGPT, Perplexity, Claude and Google AI Overviews requires their crawlers",
         "# to be able to read the site - blocking them removes the business from those",
         "# answers entirely. Listed individually so a future edit cannot silently",
         "# disallow them via a wildcard.", ""]
    for b in AI_BOTS:
        L += ["User-agent: %s" % b, "Allow: /", ""]
    L += ["Sitemap: %s/sitemap.xml" % SITE, ""]
    open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8").write("\n".join(L))
    print("  robots.txt  written (%d AI crawlers allowed)" % len(AI_BOTS))

if __name__ == "__main__":
    write_index(); write_static(); write_llms(); write_robots()
