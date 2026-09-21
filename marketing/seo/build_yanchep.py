# -*- coding: utf-8 -*-
"""
THE money page: lash-extensions-yanchep.html

This is the single most commercially important URL on the site. It is built
separately from the suburb generator on purpose - it should always be the
DEEPEST page here, not one of a set. If you shorten it, you are undoing the
whole point.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_seo as B

ROOT, SITE = B.ROOT, B.SITE
SLUG = "lash-extensions-yanchep.html"
URL  = SITE + "/" + SLUG

TITLE = "Eyelash Extension Prices Yanchep | Classic, Hybrid, Volume &amp; Mega"
DESC  = ("Eyelash extensions in Yanchep, WA from $120. Classic, hybrid, volume and mega volume, "
         "applied one lash at a time in a private studio - one client at a time, prices published, "
         "patch tests available.")

FAQS = [
 ("How much are lash extensions in Yanchep?",
  "A classic full set is $120, hybrid $140, volume $160 and mega volume $180. Refills are $60 at two "
  "weeks or $75 at three weeks. Every price is published on this page - you will never be quoted a "
  "different number on the day."),
 ("How long do eyelash extensions last?",
  "Individual extensions last the life of the natural lash they are attached to, which is six to eight "
  "weeks. Because your lashes are all at different stages, a set thins gradually rather than falling "
  "out at once. A refill every two to three weeks keeps it looking full indefinitely."),
 ("How long does a full set take?",
  "Allow about two hours for a classic set and up to two and a half for volume or mega volume. Refills "
  "are under an hour. Only one client is booked at a time, so the appointment starts when it says it does."),
 ("Do lash extensions damage your natural lashes?",
  "Not when applied correctly. Damage comes from two things: extensions that are too heavy for the "
  "natural lash, and poor isolation that glues several lashes together so they pull on each other as "
  "they shed. Both are application faults. A set mapped to what your lashes can actually carry will "
  "grow out cleanly."),
 ("Do I need a patch test?",
  "Yes, before your first appointment. It takes two minutes and should be done at least 24 hours "
  "ahead - 48 is better. It is free, and it is not worth skipping."),
 ("What is the difference between classic, hybrid and volume?",
  "Classic is one extension per natural lash for definition. Hybrid mixes classic extensions and fans "
  "for texture, and is the most forgiving on sparse lashes. Volume uses fans of much finer extensions "
  "for density. Mega volume goes further again and needs strong natural lashes to carry it."),
 ("Which set should I get for my first time?",
  "Classic or hybrid. Both are natural enough to live with while you work out what you like, and you "
  "can always go heavier next time. Starting with mega volume is the most common first-set regret."),
 ("Can I wear mascara with extensions?",
  "You should not need to, and oil-based or waterproof mascara will break down the adhesive. If you "
  "want more drama, a denser set is a better answer than mascara over a lighter one."),
 ("What if I have sensitive eyes?",
  "Say so at the consultation. Sensitivity is usually to the adhesive fumes rather than the extensions "
  "themselves, and there are gentler adhesives and application methods that help. This is exactly what "
  "the patch test is for."),
 ("How do I make them last longer?",
  "Keep them dry for the first 24 hours, avoid oil-based products around the eyes, brush them through "
  "daily with a clean spoolie, and do not pick or rub. In Yanchep the two biggest retention killers "
  "are salt water and sunscreen migrating into the lash line - rinse with fresh water after the beach."),
 ("Where exactly is the studio?",
  "In Yanchep, WA 6035. It is a private home studio, so the address is not published - it is sent to "
  "you when your appointment is confirmed. There is free off-street parking."),
 ("Can you fill a set done by someone else?",
  "Yes. A foreign lash refill is from $85, priced higher because it takes longer to assess, tidy and "
  "rebalance existing work. Send a photo before booking so the quote and the time set aside are accurate."),
]

TABLE = (["","Classic","Hybrid","Volume","Mega volume"],
 [["Per natural lash","1 extension","Mix of 1 and fans","Fan of 2&ndash;5","Fan of 6&ndash;15"],
  ["The look","Defined, natural","Textured, full","Dense, soft","Dark, dramatic"],
  ["Full set","$120","$140","$160","$180"],
  ["Appointment","~2 hours","~2 hours","~2.5 hours","~2.5 hours"],
  ["Best for","Dense natural lashes","Sparse or uneven","Most lash types","Strong, healthy lashes"],
  ["Good first set?","Yes","Yes","Maybe","Rarely"]])

def build():
    strip = lambda x:(x.replace("&mdash;","-").replace("&ndash;","-").replace("&amp;","&")
                       .replace("&middot;","-").replace("&rsquo;","'"))
    service = {"@context":"https://schema.org","@type":"Service",
      "serviceType":"Eyelash Extensions","name":"Eyelash Extension Prices in Yanchep",
      "description":strip(DESC),"url":URL,
      "provider":{"@type":"BeautySalon","name":"Luxe Beauty Yanchep","@id":SITE+"/#business",
        "telephone":"+61411487177","priceRange":"$$","currenciesAccepted":"AUD",
        "address":{"@type":"PostalAddress","addressLocality":"Yanchep","addressRegion":"WA",
                   "postalCode":"6035","addressCountry":"AU"},
        "geo":{"@type":"GeoCoordinates","latitude":-31.5464,"longitude":115.6353},
        "openingHoursSpecification":[{"@type":"OpeningHoursSpecification",
          "dayOfWeek":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
          "opens":"09:00","closes":"17:00"}]},
      "areaServed":[{"@type":"City","name":n} for n in
        ["Yanchep","Eglinton","Two Rocks","Alkimos","Jindalee","Butler","Nowergup"]],
      "hasOfferCatalog":{"@type":"OfferCatalog","name":"Lash extension services","itemListElement":[
        {"@type":"Offer","itemOffered":{"@type":"Service","name":n},"price":p,"priceCurrency":"AUD",
         "availability":"https://schema.org/InStock"} for n,p in
        [("Classic Full Set","120"),("Hybrid Full Set","140"),("Volume Full Set","160"),
         ("Mega Volume Full Set","180"),("Two Week Refill","60"),("Three Week Refill","75"),
         ("Foreign Lash Refill","85"),("Lash Removal","25")]]}}
    faq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
      {"@type":"Question","name":strip(q),"acceptedAnswer":{"@type":"Answer","text":strip(a)}}
      for q,a in FAQS]}
    crumb = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
      {"@type":"ListItem","position":2,"name":"Services","item":SITE+"/services.html"},
      {"@type":"ListItem","position":3,"name":"Eyelash Extension Prices Yanchep","item":URL}]}

    heads, rows = TABLE
    tbl = ('<div class="ctable rv"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
           % ("".join("<th>%s</th>"%h for h in heads),
              "".join("<tr><th>%s</th>%s</tr>"%(r[0],"".join("<td>%s</td>"%c for c in r[1:]))
                      for r in rows)))
    faq_html="".join('      <details class="faq"><summary>%s</summary><p>%s</p></details>\n'%(q,a)
                     for q,a in FAQS)

    head = B.head(TITLE, strip(DESC), SLUG, "photos/lash-1.jpg",
                  "\n".join([B.ld(service), B.ld(faq), B.ld(crumb)]))
    body = """
{nav}

<section class="hero hero--sm">
  <img class="hero-bg" src="photos/lash-1.jpg" alt="" aria-hidden="true">
  <div><p class="eyebrow">Prices &amp; set types &middot; Yanchep WA</p>
  <h1>Eyelash Extension<br>Prices in Yanchep</h1></div>
</section>

<section class="light">
  <div class="wrap">
    <div class="sec-head center rv">
      <h2>Classic, hybrid, volume and mega volume</h2>
      <p class="lede" style="margin:0 auto">Eyelash extensions applied one lash at a time in a private
        Yanchep studio. Every set is mapped to your eye shape and to the health of your natural lashes,
        so it flatters your face and grows out cleanly. Classic sets from $120, and every price is on
        this page.</p>
    </div>

    <div class="grid g3 rv" style="margin-top:clamp(44px,5vw,70px)">
      <div class="card"><span class="num">01</span><h3>One client at a time</h3>
        <p>No salon floor, no second client on another bed, no walk-ins interrupting. Your appointment
        is the only one booked, which is why it starts on time and runs for as long as the set needs.</p></div>
      <div class="card"><span class="num">02</span><h3>The same technician, every visit</h3>
        <p>It is a one-person studio. Whoever maps your first set does every refill after it, so nothing
        is handed over and nothing has to be re-explained.</p></div>
      <div class="card"><span class="num">03</span><h3>Published prices</h3>
        <p>Every price is listed below, including refills and removals. You will not be quoted a
        different number on the day, and there are no packages to decline.</p></div>
    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">Choosing a set</p><h2>Which one suits your lashes</h2>
      <p class="lede" style="margin:0 auto">The names describe how many extensions go onto each natural
        lash, not how dramatic the result is. What you can actually wear depends more on your own lashes
        than on the photo you brought in &mdash; which is what the consultation is for.</p>
    </div>
    {tbl}
    <div class="prose rv" style="margin-top:clamp(34px,4vw,54px)">
      <p><b>Classic</b> is one extension on one natural lash. It adds length and definition without
      density &mdash; your lash line, on a good day. If you want to look well rather than to have people
      notice your lashes, start here.</p>
      <p><b>Hybrid</b> mixes classic extensions with lightweight fans. The mix fills gaps that classic
      alone would leave visible, which makes it the most forgiving option for sparse or uneven lash lines
      and the most commonly recommended first set.</p>
      <p><b>Volume</b> uses fans of several ultra-fine extensions per natural lash. Because each filament
      is far thinner, a fan of five can weigh less than one thick classic extension &mdash; volume is
      denser, not heavier. <b>Mega volume</b> pushes that further and needs healthy natural lashes to carry it.</p>
      <p>Not sure? <a href="classic-vs-hybrid-vs-volume-lashes.html">The full comparison guide</a> goes
      deeper, and <a href="lash-lift-vs-extensions.html">lash lift vs extensions</a> is worth reading if
      you are still deciding whether extensions are the right treatment at all.</p>
    </div>

{pricing}

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">What happens</p><h2>Your appointment</h2>
    </div>
    <div class="steps rv">
      <div class="step"><div><h3>Patch test, 48 hours before</h3>
        <p>Two minutes, free, and done before your first set. Sensitivity is usually to the adhesive
        rather than the extensions, and this is how it gets found out safely.</p></div></div>
      <div class="step"><div><h3>Consultation and mapping</h3>
        <p>Your eye shape, your natural lash density and what you actually want are worked out before
        anything is applied. Mapping is where a set stops being generic and starts suiting your face.</p></div></div>
      <div class="step"><div><h3>Application</h3>
        <p>Each natural lash is isolated and one extension &mdash; or one fan &mdash; is attached to it.
        Isolation is the slow part and the part cheap sets skip. You lie down with your eyes closed;
        most clients fall asleep.</p></div></div>
      <div class="step"><div><h3>Aftercare, honestly explained</h3>
        <p>Dry for 24 hours, no oil-based products near the eyes, brush daily. You will be told what
        actually matters rather than sold a product.
        <a href="aftercare.html">Full aftercare guide</a>.</p></div></div>
      <div class="step"><div><h3>Refills every two to three weeks</h3>
        <p>$60 at two weeks, $75 at three. Past about four weeks too little of the set remains and it is
        priced as a new full set, so most clients book the next one before they leave.</p></div></div>
    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">Yanchep</p><h2>Lashes on this stretch of coast</h2>
    </div>
    <div class="prose rv">
      <p>Yanchep is a beach suburb, and that genuinely changes what holds up. Salt water, sunscreen and
      wind are the three things that shorten the life of a set, and everyone here gets all three. It does
      not rule extensions out &mdash; it means a well-isolated set with the right adhesive will outlast a
      heavy one, and that regular beachgoers usually do better on a two-week refill cycle than a three-week one.</p>
      <p>Sunscreen is the quiet culprit. It migrates into the lash line through the day and breaks down
      adhesive faster than swimming does. Rinsing with fresh water after the beach and brushing the
      lashes through once they are dry makes a bigger difference than any product sold for the purpose.</p>
      <p>The studio is a private home studio in Yanchep, minutes from Yanchep Lagoon and the town centre,
      with free off-street parking and no shopping-centre car park to navigate. The exact address is sent
      with your booking confirmation. Clients also travel in from
      <a href="lash-extensions-two-rocks.html">Two Rocks</a>,
      <a href="lash-extensions-eglinton.html">Eglinton</a>,
      <a href="lash-extensions-alkimos.html">Alkimos</a> and
      <a href="lash-extensions-butler.html">Butler</a> &mdash;
      <a href="areas-we-serve.html">all 62 suburbs served</a>.</p>
    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">Questions</p><h2>Good to know</h2>
    </div>
    <div style="max-width:800px;margin:0 auto">
{faq_html}    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">Keep reading</p><h2>Before you book</h2>
    </div>
    <div class="center" style="max-width:760px;margin:0 auto">
      <a class="btn ghost" href="lash-extensions-cost-perth.html" style="margin:0 8px 8px 0">What lashes cost</a>
      <a class="btn ghost" href="classic-vs-hybrid-vs-volume-lashes.html" style="margin:0 8px 8px 0">Classic, hybrid or volume</a>
      <a class="btn ghost" href="lash-lift-vs-extensions.html" style="margin:0 8px 8px 0">Lift vs extensions</a>
      <a class="btn ghost" href="aftercare.html" style="margin:0 8px 8px 0">Aftercare</a>
    </div>
  </div>
</section>

<section>
  <div class="wrap"><div class="callout rv">
    <img src="photos/lash-2.jpg" alt="" aria-hidden="true" loading="lazy">
    <p class="eyebrow">Yanchep &middot; Two Rocks &middot; Alkimos &middot; Eglinton &middot; Butler</p>
    <h2>Book your appointment</h2>
    <p class="lede" style="margin:20px auto 0">A private home studio in Yanchep, minutes from
      Two Rocks and Alkimos &mdash; no drive down the freeway required.</p>
    <div class="btn-row"><a class="btn" data-book href="https://www.instagram.com/luxebeautyyanchep/">Book now</a>
      <a class="btn ghost" href="services.html">All services</a></div>
  </div></div>
</section>

{foot}""".format(nav=B.NAV, tbl=tbl, pricing=PRICING_YANCHEP, faq_html=faq_html,
                 foot=B.footer("Yanchep &middot; Two Rocks &middot; Alkimos &middot; Eglinton &middot; Butler"))
    return head + body

PRICING_YANCHEP = """
    <div class="menu rv" style="margin-top:clamp(66px,9vw,110px)">
      <h3>Lash extension pricing</h3>
      <p class="note">Prices include your consultation and patch test advice. Yanchep, WA.</p>
      <div class="row"><span class="name">Classic Full Set</span><span class="desc">One extension per natural lash for soft, everyday definition.</span><span class="price">$120</span></div>
      <div class="row"><span class="name">Hybrid Full Set</span><span class="desc">Classic and volume mixed &mdash; texture and fullness without the weight.</span><span class="price">$140</span></div>
      <div class="row"><span class="name">Volume Full Set</span><span class="desc">Handmade fans for a fluffy, fuller, camera-ready look.</span><span class="price">$160</span></div>
      <div class="row"><span class="name">Mega Volume Full Set</span><span class="desc">Maximum density and drama, still lightweight on the lash.</span><span class="price">$180</span></div>
      <div class="row"><span class="name">Two Week Refill</span><span class="desc">The best-value way to maintain a set.</span><span class="price">from $60</span></div>
      <div class="row"><span class="name">Three Week Refill</span><span class="desc">A little more to rebuild. Still cheaper than starting again.</span><span class="price">from $75</span></div>
      <div class="row"><span class="name">Foreign Lash Refill</span><span class="desc">Filling another artist&rsquo;s work, including tidy-up.</span><span class="price">from $85</span></div>
      <div class="row"><span class="name">Lash Removal</span><span class="desc">Safe, gentle removal with no damage to your natural lashes.</span><span class="price">$25</span></div>
    </div>"""

if __name__ == "__main__":
    open(os.path.join(ROOT, SLUG), "w", encoding="utf-8").write(build())
    print("  wrote", SLUG)
