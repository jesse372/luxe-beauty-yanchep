# -*- coding: utf-8 -*-
"""
Entity schema + AI-crawler surface for Luxe Beauty Yanchep.

Regenerates three things:
  index.html   -> a consolidated schema.org @graph (WebSite + LocalBusiness + WebPage)
  llms.txt     -> curated plain-text brief for LLM crawlers (ChatGPT, Perplexity, Claude)
  robots.txt   -> explicit allow-list for AI crawlers

Only verified facts go in here. Do not invent credentials, staff names,
review counts or ratings.
"""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from suburbs import TIER_A, TIER_B

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
SITE = "https://luxebeautyyanchep.com"
PHONE = "+61411487177"

SERVICES = [
    ("Classic Lash Extensions", "120", "One extension per natural lash for defined, everyday length."),
    ("Hybrid Lash Extensions", "140", "Classic extensions and volume fans mixed for texture and fullness."),
    ("Volume Lash Extensions", "160", "Lightweight handmade fans for density and softness."),
    ("Mega Volume Lash Extensions", "180", "Maximum density, still lightweight on the natural lash."),
    ("Two Week Lash Refill", "60", "Maintains an existing set of extensions."),
    ("Three Week Lash Refill", "75", "Maintains an existing set of extensions."),
    ("Foreign Lash Refill", "85", "Refilling another technician's work, including tidy-up."),
    ("Lash Removal", "25", "Safe, gentle removal with no damage to natural lashes."),
    ("Lash Lift", "75", "Keratin lift that curls your own lashes for six to eight weeks."),
    ("Lash Lift and Tint", "90", "Lifted and darkened, the most popular low-maintenance option."),
    ("Lash Tint", "25", "Darkens fair lash tips."),
    ("Brow Lamination", "70", "Resets the direction brow hair grows so it sits fuller."),
    ("Brow Lamination and Tint", "85", "Laminated and tinted brows, six to eight weeks."),
    ("Brow Lamination, Tint and Shape", "95", "The full brow treatment."),
    ("Brow Henna and Shape", "60", "Henna tint with shaping."),
    ("Brow Shape", "25", "Shaping only."),
    ("Brow Shape and Tint", "40", "Shaped and tinted."),
]

AREAS = ["Yanchep"] + [s["name"] for s in TIER_A] + [b[0] for b in TIER_B]
AREAS = list(dict.fromkeys(AREAS))

KNOWS_ABOUT = [
    "Eyelash extensions", "Classic lash extensions", "Hybrid lash extensions",
    "Volume lash extensions", "Mega volume lash extensions", "Lash lift",
    "Keratin lash lift", "Lash tinting", "Lash refills", "Brow lamination",
    "Brow henna", "Brow tinting", "Brow shaping", "Lash aftercare", "Lash mapping",
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
                        "volume and mega volume eyelash extensions, keratin lash lifts, lash tinting, "
                        "brow lamination, henna, tinting and shaping. One client at a time."),
        "telephone": PHONE,
        "priceRange": "$$",
        "currenciesAccepted": "AUD",
        "paymentAccepted": "Cash, EFTPOS, Credit Card",
        "address": {"@type": "PostalAddress", "addressLocality": "Yanchep",
                    "addressRegion": "WA", "postalCode": "6035", "addressCountry": "AU"},
        "geo": {"@type": "GeoCoordinates", "latitude": -31.5464, "longitude": 115.6353},
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
            "opens": "09:00", "closes": "17:00"}],
        "areaServed": [{"@type": "City", "name": n, "containedInPlace":
                        {"@type": "State", "name": "Western Australia"}} for n in AREAS],
        "knowsAbout": KNOWS_ABOUT,
        "availableLanguage": {"@type": "Language", "name": "English"},
        "sameAs": ["https://www.instagram.com/luxebeautyyanchep/",
                   "https://www.facebook.com/luxebeautyyanchep"],
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
    ]}

def write_index():
    p = os.path.join(ROOT, "index.html")
    s = open(p, encoding="utf-8").read()
    block = ('<script type="application/ld+json">\n'
             + json.dumps(graph(), ensure_ascii=False, indent=1) + '\n</script>')
    new, n = re.subn(r'<script type="application/ld\+json">.*?</script>', block, s, count=1, flags=re.S)
    assert n == 1, "homepage JSON-LD block not found"
    open(p, "w", encoding="utf-8").write(new)
    json.loads(re.search(r'<script type="application/ld\+json">(.*?)</script>',
                         open(p, encoding="utf-8").read(), re.S).group(1))
    print("  index.html  @graph written (%d nodes)" % len(graph()["@graph"]))

def write_llms():
    lines = []
    A = lines.append
    A("# Luxe Beauty Yanchep")
    A("")
    A("> Private lash and brow studio in Yanchep, Western Australia (WA 6035). Eyelash")
    A("> extensions, keratin lash lifts and brow lamination, by appointment, one client")
    A("> at a time. Serving Yanchep and the northern Perth corridor.")
    A("")
    A("## Facts")
    A("")
    A("- Business name: Luxe Beauty Yanchep")
    A("- Type: private home studio (service-area business, by appointment only)")
    A("- Location: Yanchep, Western Australia 6035, Australia")
    A("- Phone: 0411 487 177")
    A("- Website: %s" % SITE)
    A("- Hours: Monday to Saturday, 9:00am-5:00pm. Closed Sunday.")
    A("- Booking: by appointment; patch test required 48 hours before a first appointment")
    A("- Instagram: https://www.instagram.com/luxebeautyyanchep/")
    A("- Facebook: https://www.facebook.com/luxebeautyyanchep")
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
    A("- [Lash lift and tint Yanchep](%s/lash-lift-yanchep.html): keratin lash lift, six to eight weeks" % SITE)
    A("- [Brow lamination Yanchep](%s/brow-lamination-yanchep.html): lamination, tint, henna and shaping" % SITE)
    A("- [Areas we serve](%s/areas-we-serve.html): every suburb served, with distances and drive times" % SITE)
    A("- [Services and pricing](%s/services.html): the full menu" % SITE)
    A("- [Aftercare](%s/aftercare.html): how to make a set last" % SITE)
    A("")
    A("## Guides")
    A("")
    A("- [What lash extensions cost in Perth](%s/lash-extensions-cost-perth.html): full set and refill costs, what changes the price" % SITE)
    A("- [Lash lift vs extensions](%s/lash-lift-vs-extensions.html): cost, upkeep and which suits which lashes" % SITE)
    A("- [Classic vs hybrid vs volume lashes](%s/classic-vs-hybrid-vs-volume-lashes.html): what the names mean and how to choose" % SITE)
    A("- [Brow lamination vs microblading](%s/brow-lamination-vs-microblading.html): temporary styling vs cosmetic tattooing" % SITE)
    A("")
    A("## Common questions")
    A("")
    A("- How much are lash extensions in Yanchep? A classic full set is $120, hybrid $140, volume $160, mega volume $180. Refills are $60 at two weeks or $75 at three weeks.")
    A("- How long do lash extensions last? Individual extensions last the life of the natural lash they are attached to, six to eight weeks. A refill every two to three weeks keeps a set looking full.")
    A("- How long does a full set take? About two hours for classic, up to two and a half for volume or mega volume.")
    A("- Is a patch test needed? Yes, before a first appointment, at least 24 hours ahead and preferably 48.")
    A("- How much is a lash lift? $75, or $90 with a tint. It lasts six to eight weeks with no refills.")
    A("- How much is brow lamination? $70, $85 with a tint, or $95 with tint and shape.")
    A("- Where is the studio? Yanchep, WA 6035. It is a private home studio; the exact address is sent on booking confirmation. Free off-street parking.")
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
    write_index(); write_llms(); write_robots()
