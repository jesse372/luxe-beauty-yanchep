# -*- coding: utf-8 -*-
"""
Single source for lash set + refill prices (AUD, whole dollars).

Refills exist for every lash style. Each refill is priced at the same share of
its full set as the classic refills are of the classic set ($60 / $75 / $85 on
$120), rounded to the nearest $5. Change a number here, then re-run
build_seo.py, build_yanchep.py, build_guides.py and build_schema.py, and update
the matching rows in services.html and square-services-import.csv.
"""
FULL_SETS = [("Classic", 120), ("Hybrid", 140), ("Volume", 160), ("Mega Volume", 180)]

# (two week, three week, foreign)
REFILLS = {
    "Classic":     (60, 75, 85),
    "Hybrid":      (70, 90, 100),
    "Volume":      (80, 100, 115),
    "Mega Volume": (90, 115, 130),
}

REFILL_KINDS = [
    ("Two Week Refill",     "Within two weeks of your last appointment."),
    ("Three Week Refill",   "Within three weeks. A little more to rebuild."),
    ("Foreign Lash Refill", "Filling another artist&rsquo;s work, including tidy-up."),
]

def refill_services():
    """[(name, price, html_desc)] e.g. ('Hybrid Two Week Refill', 70, '...')."""
    out = []
    for style, _ in FULL_SETS:
        for (kind, desc), price in zip(REFILL_KINDS, REFILLS[style]):
            out.append(("%s %s" % (style, kind), price, desc))
    return out

def refill_rows(indent="      "):
    return "\n".join(
        '%s<div class="row"><span class="name">%s</span><span class="desc">%s</span>'
        '<span class="price">$%d</span></div>' % (indent, n, d, p)
        for n, p, d in refill_services())
