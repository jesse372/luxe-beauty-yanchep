# -*- coding: utf-8 -*-
"""Builds the informational guide pages. Run after build_seo.py."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guides import GUIDES, TABLES
import build_seo as B

ROOT, SITE = B.ROOT, B.SITE

def table_html(slug):
    if slug not in TABLES: return ""
    heads, rows = TABLES[slug]
    th = "".join("<th>%s</th>" % h for h in heads)
    tr = "".join("<tr><th>%s</th>%s</tr>" % (r[0], "".join("<td>%s</td>" % c for c in r[1:]))
                 for r in rows)
    # three columns fit a phone without sideways scrolling; wider tables keep the scroll
    cls = "ctable ctable--fit rv" if len(heads) <= 3 else "ctable rv"
    return ('<div class="%s"><table><thead><tr>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>' % (cls, th, tr))

def build(g):
    slug = g["slug"] + ".html"
    url = "%s/%s" % (SITE, slug)
    strip = lambda x: (x.replace("&mdash;","-").replace("&ndash;","-").replace("&amp;","&")
                        .replace("&middot;","-").replace("&quot;",'"'))

    article = {"@context":"https://schema.org","@type":"Article",
      "headline":strip(g["title"]),"description":strip(g["desc"]),
      "mainEntityOfPage":{"@type":"WebPage","@id":url},
      "image":SITE+"/"+g["hero"],"datePublished":g.get("published","2026-09-21"),
      "dateModified":g.get("modified", g.get("published","2026-11-05")),"inLanguage":"en-AU",
      "author":{"@type":"Organization","name":"Luxe Beauty Yanchep","url":SITE+"/"},
      "publisher":{"@type":"BeautySalon","name":"Luxe Beauty Yanchep","@id":SITE+"/#business",
        "url":SITE+"/","logo":{"@type":"ImageObject","url":SITE+"/icons/icon-512.png"}}}
    faq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
      {"@type":"Question","name":strip(q),"acceptedAnswer":{"@type":"Answer","text":strip(a)}}
      for q,a in g["faqs"]]}
    crumb = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
      {"@type":"ListItem","position":2,"name":"Lash guides","item":SITE+"/lash-guides.html"},
      {"@type":"ListItem","position":3,"name":strip(g["title"]),"item":url}]}

    secs = ""
    for i,(heading, body) in enumerate(g["sections"]):
        secs += ('\n    <div class="sec-head center rv" style="margin-top:clamp(56px,7vw,92px)">'
                 '<h2>%s</h2></div>\n' % heading)
        secs += ('    <div class="prose rv">\n%s\n    </div>\n' % body) if body else \
                ("    %s\n" % table_html(g["slug"]))
        if heading == "The honest numbers":
            secs += "\n" + B.PRICING + "\n"

    faq_html = "".join('      <details class="faq"><summary>%s</summary><p>%s</p></details>\n'%(q,a)
                       for q,a in g["faqs"])
    others = "".join('<a class="btn ghost" href="%s.html" style="margin:0 8px 8px 0">%s</a>'
                     % (o["slug"], o["short"])
                     for o in GUIDES if o["slug"] != g["slug"])

    head = B.head(g["title"], strip(g["desc"]), slug, g["hero"],
                  "\n".join([B.ld(article), B.ld(faq), B.ld(crumb)]))
    body = """
{nav}

<section class="hero hero--sm">
  <img class="hero-bg" src="{hero}" alt="" aria-hidden="true">
  <div><p class="eyebrow">{eyebrow}</p><h1>{h1}</h1></div>
</section>

<section class="light">
  <div class="wrap">
    <div class="sec-head center rv">
      <p class="lede" style="margin:0 auto">{lede}</p>
    </div>
{secs}
    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">Questions</p><h2>Commonly asked</h2>
    </div>
    <div style="max-width:800px;margin:0 auto">
{faq_html}    </div>

    <div class="sec-head center rv" style="margin-top:clamp(66px,9vw,110px)">
      <p class="eyebrow">Keep reading</p><h2>Other guides</h2>
    </div>
    <div class="center" style="max-width:760px;margin:0 auto">{others}
      <p class="note" style="margin-top:18px"><a href="lash-guides.html">All lash guides &rarr;</a> &nbsp;&middot;&nbsp;
        <a href="lash-extensions-yanchep.html">Lash extension prices in Yanchep &rarr;</a></p></div>
  </div>
</section>

<section>
  <div class="wrap"><div class="callout rv">
    <img src="photos/feature.jpg" alt="" aria-hidden="true" loading="lazy">
    <p class="eyebrow">Yanchep &middot; new clients welcome</p>
    <h2>Book your appointment</h2>
    <p class="lede" style="margin:20px auto 0">{cta}</p>
    <div class="btn-row"><a class="btn" data-book href="https://www.instagram.com/luxebeautyyanchep/">Book now</a>
      <a class="btn ghost" href="services.html">All services</a></div>
  </div></div>
</section>

{foot}""".format(nav=B.NAV, hero=g["hero"], eyebrow=g["eyebrow"], h1=g["h1"], lede=g["lede"],
                 secs=secs, faq_html=faq_html, others=others, cta=g["cta"],
                 foot=B.footer("Yanchep &middot; Two Rocks &middot; Alkimos &middot; Butler &middot; Clarkson"))
    return slug, head + body

def build_hub():
    slug = "lash-guides.html"
    url = "%s/%s" % (SITE, slug)
    title = "Lash Extension Guides | Costs, Styles, Refills &amp; Aftercare"
    desc = ("Plain-English lash extension guides from a Yanchep studio: cost, styles, how long they "
            "last, swimming, weddings and your first appointment.")
    assert len(desc) <= 160, len(desc)
    strip = lambda x: x.replace("&amp;","&").replace("&mdash;","-").replace("&middot;","-")
    items = [(g["slug"]+".html", strip(g["title"]), g["desc"], g["eyebrow"].split("&middot;")[0].strip())
             for g in GUIDES]
    items.append(("aftercare.html", "Lash extension aftercare",
                  "The daily routine that keeps a set full between refills, and what to do after a tint.",
                  "Aftercare"))
    coll = {"@context":"https://schema.org","@type":"CollectionPage","name":strip(title),"url":url,
      "description":desc,"inLanguage":"en-AU","isPartOf":{"@id":SITE+"/#website"},
      "about":{"@id":SITE+"/#business"},
      "mainEntity":{"@type":"ItemList","itemListElement":[
        {"@type":"ListItem","position":i+1,"url":"%s/%s"%(SITE,s_),"name":t}
        for i,(s_,t,_,_) in enumerate(items)]}}
    crumb = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
      {"@type":"ListItem","position":2,"name":"Lash guides","item":url}]}
    cards = "".join(
      '      <a class="card" href="%s" style="text-decoration:none;display:block">'
      '<span class="num">%s</span><h3>%s</h3><p>%s</p></a>\n'
      % (s_, e.upper(), t.split(":")[0].split("|")[0].split("(")[0].strip().replace("&","&amp;"), d)
      for s_,t,d,e in items)
    head = B.head(title, desc, slug, "photos/lash-4.jpg", "\n".join([B.ld(coll), B.ld(crumb)]))
    body = """
{nav}

<section class="hero hero--sm">
  <img class="hero-bg" src="photos/lash-4.jpg" alt="" aria-hidden="true">
  <div><p class="eyebrow">Straight answers</p><h1>Lash extension<br>guides</h1></div>
</section>

<section class="light">
  <div class="wrap">
    <div class="sec-head center rv">
      <h2>What people ask before they book</h2>
      <p class="lede" style="margin:0 auto">Most of what is written about lash extensions is trying to
        sell you a set. These are the answers given in the studio every week, written down: what things
        cost, what the names mean, how long a set lasts and how to look after it. Prices quoted are the
        studio&rsquo;s own and are the same ones on the <a href="services.html">services page</a>.</p>
    </div>
    <div class="grid g3 rv" style="margin-top:clamp(30px,4vw,50px)">
{cards}    </div>
  </div>
</section>

<section>
  <div class="wrap"><div class="callout rv">
    <img src="photos/feature.jpg" alt="" aria-hidden="true" loading="lazy">
    <p class="eyebrow">Yanchep &middot; new clients welcome</p>
    <h2>Still not sure?</h2>
    <p class="lede" style="margin:20px auto 0">Send a photo of your natural lashes and you will get an
      honest recommendation, including if the answer is a lighter set.</p>
    <div class="btn-row"><a class="btn" data-book href="https://www.instagram.com/luxebeautyyanchep/">Book now</a>
      <a class="btn ghost" href="lash-extensions-yanchep.html">Lash extension prices</a></div>
  </div></div>
</section>

{foot}""".format(nav=B.NAV, cards=cards,
                 foot=B.footer("Yanchep &middot; Two Rocks &middot; Alkimos &middot; Eglinton &middot; Butler"))
    return slug, head + body

def main():
    for g in GUIDES:
        slug, html = build(g)
        open(os.path.join(ROOT, slug), "w", encoding="utf-8").write(html)
        print("  wrote", slug)
    slug, html = build_hub()
    open(os.path.join(ROOT, slug), "w", encoding="utf-8").write(html)
    print("  wrote", slug)

if __name__ == "__main__":
    main()
