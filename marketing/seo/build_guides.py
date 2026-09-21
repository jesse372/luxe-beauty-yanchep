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
    return ('<div class="ctable rv"><table><thead><tr>%s</tr></thead>'
            '<tbody>%s</tbody></table></div>' % (th, tr))

def build(g):
    slug = g["slug"] + ".html"
    url = "%s/%s" % (SITE, slug)
    strip = lambda x: (x.replace("&mdash;","-").replace("&ndash;","-").replace("&amp;","&")
                        .replace("&middot;","-").replace("&quot;",'"'))

    article = {"@context":"https://schema.org","@type":"Article",
      "headline":strip(g["title"]),"description":strip(g["desc"]),
      "mainEntityOfPage":{"@type":"WebPage","@id":url},
      "image":SITE+"/icons/og-image.jpg","datePublished":"2026-09-21","dateModified":"2026-09-21",
      "author":{"@type":"Organization","name":"Luxe Beauty Yanchep","url":SITE+"/"},
      "publisher":{"@type":"BeautySalon","name":"Luxe Beauty Yanchep","@id":SITE+"/#business",
        "url":SITE+"/","logo":{"@type":"ImageObject","url":SITE+"/icons/icon-512.png"}}}
    faq = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
      {"@type":"Question","name":strip(q),"acceptedAnswer":{"@type":"Answer","text":strip(a)}}
      for q,a in g["faqs"]]}
    crumb = {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Home","item":SITE+"/"},
      {"@type":"ListItem","position":2,"name":"Guides","item":SITE+"/services.html"},
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
                     % (o["slug"], o["eyebrow"].split("&middot;")[0].strip())
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
    <div class="center" style="max-width:760px;margin:0 auto">{others}</div>
  </div>
</section>

<section>
  <div class="wrap"><div class="callout rv">
    <img src="photos/feature.jpg" alt="" aria-hidden="true" loading="lazy">
    <p class="eyebrow">Yanchep &middot; serving 62 suburbs</p>
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

def main():
    for g in GUIDES:
        slug, html = build(g)
        open(os.path.join(ROOT, slug), "w", encoding="utf-8").write(html)
        print("  wrote", slug)

if __name__ == "__main__":
    main()
