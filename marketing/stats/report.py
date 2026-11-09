#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Prints the visitor report for luxebeautyyanchep.com from the luxe-stats Worker.
First line is a one-sentence summary (the weekly job puts it in the phone message);
the rest is detail for the report file.

  python3 marketing/stats/report.py [--days 7]

Needs the report key at ~/.authframework/secrets/luxe-stats.token (set when the
Worker was created; rotate with `wrangler secret put REPORT_KEY` in marketing/stats/worker).
"""
import json, os, sys, urllib.request

URL = "https://luxe-stats.madlad-taps.workers.dev/report"
KEY_FILE = os.path.expanduser("~/.authframework/secrets/luxe-stats.token")

def main():
    days = int(sys.argv[sys.argv.index("--days") + 1]) if "--days" in sys.argv else 7
    try:
        key = open(KEY_FILE).read().strip()
    except OSError:
        sys.exit("no report key at %s" % KEY_FILE)
    req = urllib.request.Request("%s?days=%d" % (URL, days), headers={"Authorization": "Bearer " + key,
                                 # Cloudflare's edge rejects Python's default user agent with a 403
                                 "User-Agent": "luxe-stats-report/1 (Mac mini weekly job)"})
    d = json.load(urllib.request.urlopen(req, timeout=30))
    now = {r["event"]: r for r in d["now"]}
    prev = {r["event"]: r for r in d["prev"]}
    g = lambda t, e, k="n": (t.get(e) or {}).get(k) or 0
    visits, views, book = g(now, "view", "sessions"), g(now, "view"), g(now, "book")
    pv, pb = g(prev, "view", "sessions"), g(prev, "book")
    contact = sum(g(now, e) for e in ("call", "email", "instagram"))
    top = d["refs"][0]["ref"] if d["refs"] else "none"
    print("Site, last %d days: %d visits (prev %d), %d page views, %d booking clicks (prev %d), %d call/message clicks, %d review clicks. Top source: %s."
          % (days, visits, pv, views, book, pb, contact, g(now, "review"), top))
    print()
    print("By day (visits / views / booking clicks):")
    for r in d["byDay"]:
        print("  %s  %3d / %3d / %d" % (r["day"], r["visits"], r["views"], r["book"]))
    print("\nWhere visits came from:")
    for r in d["refs"]:
        print("  %-22s %d" % (r["ref"], r["visits"]))
    print("\nMost viewed pages:")
    for r in d["pages"]:
        print("  %-45s %d" % (r["path"], r["views"]))
    if d["bookPages"]:
        print("\nBooking clicks by page:")
        for r in d["bookPages"]:
            print("  %-45s %d" % (r["path"], r["clicks"]))
    if d["bookRefs"]:
        print("\nBooking clicks by source:")
        for r in d["bookRefs"]:
            print("  %-22s %d" % (r["ref"], r["clicks"]))
    if d["devs"]:
        print("\nPhone vs desktop: " + ", ".join("%s %d" % (r["dev"], r["visits"]) for r in d["devs"]))

if __name__ == "__main__":
    main()
