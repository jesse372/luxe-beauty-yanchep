# -*- coding: utf-8 -*-
"""
Tell Bing (and the other IndexNow engines: Yandex, Seznam, Naver) which pages changed.
Bing feeds ChatGPT search, Copilot and DuckDuckGo, and as of 2026-11-09 had none of this
site indexed. Google does not use IndexNow - for Google, resubmit the sitemap instead.

Run AFTER the change is live:
    python3 marketing/seo/indexnow.py            # every URL in sitemap.xml
    python3 marketing/seo/indexnow.py --today    # only pages whose lastmod is today
"""
import datetime, json, os, re, sys, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from finalize import INDEXNOW_KEY, ROOT, SITE

HOST = SITE.split("//")[1]

def main():
    sm = open(os.path.join(ROOT, "sitemap.xml")).read()
    rows = re.findall(r"<loc>(.*?)</loc><lastmod>(.*?)</lastmod>", sm)
    today = datetime.date.today().isoformat()
    urls = [u for u, d in rows if "--today" not in sys.argv or d == today]
    if not urls:
        print("  indexnow: nothing changed today"); return
    # the key file has to be live first, or the engines reject the ping
    key_url = "%s/%s.txt" % (SITE, INDEXNOW_KEY)
    try:
        live = urllib.request.urlopen(key_url, timeout=20).read().decode().strip()
    except Exception as e:
        sys.exit("  indexnow: key file not live yet (%s) - deploy first" % e)
    if live != INDEXNOW_KEY:
        sys.exit("  indexnow: key file content does not match")
    body = json.dumps({"host": HOST, "key": INDEXNOW_KEY, "keyLocation": key_url, "urlList": urls}).encode()
    req = urllib.request.Request("https://api.indexnow.org/indexnow", data=body,
                                 headers={"Content-Type": "application/json; charset=utf-8"})
    try:
        code = urllib.request.urlopen(req, timeout=30).getcode()
    except urllib.error.HTTPError as e:
        sys.exit("  indexnow: rejected with HTTP %s %s" % (e.code, e.read()[:200]))
    print("  indexnow: %d urls submitted, HTTP %s" % (len(urls), code))

if __name__ == "__main__":
    main()
