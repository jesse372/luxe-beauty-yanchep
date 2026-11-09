# -*- coding: utf-8 -*-
"""
Ready-to-post Instagram tiles for Luxe Beauty Yanchep (1080 x 1350, the 4:5 feed size).

Every price comes from marketing/seo/prices.py and every claim is one the website
already makes, so a price change is: edit prices.py, run this, re-render.
Text-only on purpose: they sit between real client photos, they do not replace them.
Sizes are set for a phone: the smallest text is 32px, about 12px once shown in the feed.

Run:  python3 make_posts.py      -> build/*.html
      node render.mjs            -> posts/*.png   (needs headless Chrome, see render.mjs)
Captions and a posting order are in captions.txt (written by this script too).
"""
import os, sys, html
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "seo"))
import prices

P = dict(prices.FULL_SETS); R = prices.REFILLS
BOOK = "luxebeautyyanchep.com/book"
FONTS = "../../../assets/fonts"

CSS = """
@font-face{font-family:'Cormorant Garamond';font-style:normal;font-weight:300 400;src:url(%(f)s/cormorant-garamond-300-400-latin.woff2) format('woff2')}
@font-face{font-family:'Cormorant Garamond';font-style:italic;font-weight:300 400;src:url(%(f)s/cormorant-garamond-300-400-italic-latin.woff2) format('woff2')}
@font-face{font-family:'Jost';font-style:normal;font-weight:200 400;src:url(%(f)s/jost-200-400-latin.woff2) format('woff2')}
*{box-sizing:border-box} html,body{margin:0}
body{width:1080px;height:1350px;font-family:'Jost',sans-serif;font-weight:300;display:flex;flex-direction:column;
  align-items:center;text-align:center;padding:84px 86px 70px;position:relative;overflow:hidden}
body.dark{background:#0C0B0A;color:#F7F2EB;--accent:#C4A47C;--dim:#CBC1B4;--hair:rgba(247,242,235,.14)}
body.light{background:#F3EDE4;color:#1A1613;--accent:#9B7B4E;--dim:#5F554B;--hair:rgba(26,22,19,.16)}
body::before{content:"";position:absolute;inset:30px;border:1.5px solid var(--accent);opacity:.4;pointer-events:none}
.mark{width:104px;height:104px;border-radius:50%%;display:grid;place-items:center;font-family:'Cormorant Garamond',serif;
  font-size:48px;letter-spacing:.04em;border:2px solid var(--accent);color:var(--accent);flex:none}
.eyebrow{font-size:24px;letter-spacing:.42em;text-transform:uppercase;color:var(--accent);margin:34px 0 0;font-weight:400}
.mid{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;width:100%%}
h1{font-family:'Cormorant Garamond',serif;font-weight:300;font-size:104px;line-height:1.04;margin:0;letter-spacing:-.005em}
h1.sm{font-size:82px} h1 i{color:var(--accent)}
.rule{width:110px;height:2px;background:var(--accent);opacity:.7;margin:44px 0}
.sub{font-size:41px;line-height:1.45;color:var(--dim);margin:0;max-width:860px;text-wrap:balance} .sub b{font-weight:400;color:inherit;color:var(--accent)}
.rows{width:100%%;margin-top:6px}
.row{display:flex;align-items:baseline;justify-content:space-between;gap:24px;padding:25px 0;border-bottom:1.5px solid var(--hair);text-align:left}
.row:last-child{border-bottom:0}
.row .n{font-family:'Cormorant Garamond',serif;font-size:56px;line-height:1.1}
.row .d{display:block;font-family:'Jost',sans-serif;font-size:32px;color:var(--dim);margin-top:8px;line-height:1.35}
.row .p{font-family:'Cormorant Garamond',serif;font-size:56px;color:var(--accent);white-space:nowrap}
.pts{width:100%%;text-align:left;margin-top:4px}
.pt{display:flex;gap:30px;padding:24px 0;border-bottom:1.5px solid var(--hair);align-items:baseline}
.pt:last-child{border-bottom:0}
.pt .k{font-family:'Cormorant Garamond',serif;font-size:38px;color:var(--accent);min-width:58px}
.pt .t{font-family:'Cormorant Garamond',serif;font-size:52px;line-height:1.15}
.pt .t span{display:block;font-family:'Jost',sans-serif;font-size:32px;text-wrap:balance;color:var(--dim);margin-top:8px;line-height:1.4}
.foot{font-size:25px;letter-spacing:.3em;text-transform:uppercase;color:var(--accent);margin:0;flex:none;font-weight:400}
.foot b{font-weight:400;color:inherit}
.swipe{position:absolute;right:74px;bottom:66px;font-size:20px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim)}
""" % {"f": FONTS}

def page(theme, eyebrow, body, foot=BOOK, swipe=False):
    return ("""<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=1080">
<style>%s</style></head><body class="%s"><div class="mark">LB</div><p class="eyebrow">%s</p>
<div class="mid">%s</div><p class="foot">%s</p>%s</body></html>"""
            % (CSS, theme, eyebrow, body, foot, '<span class="swipe">Swipe &rarr;</span>' if swipe else ""))

def title(h, sub="", small=False):
    return ('<h1%s>%s</h1>' % (' class="sm"' if small else "", h)) + ('<div class="rule"></div><p class="sub">%s</p>' % sub if sub else "")

def rows(items, heading=None):
    out = ('<h1 class="sm" style="margin-bottom:34px">%s</h1>' % heading) if heading else ""
    return out + '<div class="rows">' + "".join(
        '<div class="row"><span class="n">%s%s</span><span class="p">%s</span></div>'
        % (n, ('<span class="d">%s</span>' % d) if d else "", p) for n, d, p in items) + "</div>"

def points(items, heading=None):
    out = ('<h1 class="sm" style="margin-bottom:30px">%s</h1>' % heading) if heading else ""
    return out + '<div class="pts">' + "".join(
        '<div class="pt"><span class="k">%02d</span><span class="t">%s%s</span></div>'
        % (i + 1, t, ('<span>%s</span>' % d) if d else "") for i, (t, d) in enumerate(items)) + "</div>"

D, L = "dark", "light"
POSTS = [
 # (file, theme, eyebrow, body html, swipe)
 ("01-prices-lashes", D, "Lash extensions &middot; Yanchep", rows([
    ("Classic", "One extension per natural lash", "$%d" % P["Classic"]),
    ("Hybrid", "Classic and volume mixed", "$%d" % P["Hybrid"]),
    ("Volume", "Lightweight fans, soft and full", "$%d" % P["Volume"]),
    ("Mega Volume", "Maximum density", "$%d" % P["Mega Volume"])], "Full set <i>prices</i>"), False),
 ("02-prices-infills", L, "Lash infills &middot; Yanchep", rows([
    ("Classic", "Two weeks / three weeks", "$%d / $%d" % R["Classic"][:2]),
    ("Hybrid", "Two weeks / three weeks", "$%d / $%d" % R["Hybrid"][:2]),
    ("Volume", "Two weeks / three weeks", "$%d / $%d" % R["Volume"][:2]),
    ("Mega Volume", "Two weeks / three weeks", "$%d / $%d" % R["Mega Volume"][:2])], "Infill <i>prices</i>"), False),
 ("03-prices-brows", D, "Brows &amp; tinting &middot; Yanchep", rows([
    ("Brow Shape", "Wax and tweeze. With your lashes", "$25"),
    ("Brow Shape &amp; Tint", "With your lashes", "$40"),
    ("Lash Tint", "With your lashes", "$25"),
    ("Brows + Lash Tint", "Book it on its own. 45 minutes", "$60")], "Brows, <i>shaped</i>"), False),
 ("04-book-online", L, "Now booking online", title("Book in<br><i>a minute</i>",
    "Pick your treatment and time online.<br>A <b>$50 deposit</b> confirms it and comes off your total."), False),
 ("05-one-client", D, "Private studio &middot; Yanchep", title("One client<br><i>at a time</i>",
    "No busy salon floor. No overlapping appointments.<br>Just the time your set needs."), False),

 ("06-aftercare-1", D, "Lash aftercare", title("Make them<br><i>last</i>", "Six rules that add days to every set."), True),
 ("06-aftercare-2", L, "Lash aftercare &middot; 1 to 3", points([
    ("Keep them dry for 24 hours", "No water, steam or heavy sweat while the adhesive cures."),
    ("Cleanse every day", "Lash-safe foaming cleanser and a soft brush. Clean lashes last."),
    ("Keep oil away", "Check your cleanser, moisturiser, sunscreen and makeup remover.")]), True),
 ("06-aftercare-3", D, "Lash aftercare &middot; 4 to 6", points([
    ("No curlers, no waterproof mascara", "Extensions already hold their curl."),
    ("Sleep on your back if you can", "Or use a silk pillowcase. Side sleepers thin one side first."),
    ("Infill every two to three weeks", "It costs less than starting again.")]), False),

 ("07-styles-1", L, "Which set is which", title("Classic, hybrid<br>or <i>volume?</i>", "The names are about how many extensions go on each natural lash."), True),
 ("07-styles-2", D, "Classic &middot; $%d" % P["Classic"], title("<i>Classic</i>", "One extension on one natural lash.<br>Length and definition, like your own lashes on a very good day.<br><b>A good first set.</b>"), True),
 ("07-styles-3", L, "Hybrid &middot; $%d" % P["Hybrid"], title("<i>Hybrid</i>", "Classic extensions mixed with soft fans.<br>Texture and fullness, and the most forgiving on sparse lashes.<br><b>Also a good first set.</b>"), True),
 ("07-styles-4", D, "Volume &middot; $%d" % P["Volume"], title("<i>Volume</i>", "Fans of very fine extensions on each lash.<br>Dense and soft. Fuller, not heavier."), True),
 ("07-styles-5", L, "Mega volume &middot; $%d" % P["Mega Volume"], title("<i>Mega</i><br>volume", "The fullest, darkest lash line.<br>It needs strong natural lashes to carry it, so ask first."), False),

 ("08-infill-or-full-set", D, "Good to know", points([
    ("Within two weeks", "A two week infill. The lightest top-up and the lowest price."),
    ("Within three weeks", "A three week infill. A little more to rebuild."),
    ("Beyond three weeks", "Usually a new full set. An infill needs about 40% of the set left.")], "Infill or<br><i>full set?</i>"), False),
 ("09-patch-test", L, "First time?", title("Patch test<br><i>first</i>", "New to lash extensions or tinting?<br>A patch test takes two minutes, it is free, and it is done <b>48 hours before</b> your appointment."), False),
 ("10-swimming", D, "Yanchep summer", points([
    ("Wait 24 hours after your set", "Then showers, the pool and the ocean are all fine."),
    ("Rinse with fresh water", "Dried salt at the lash line is what does the damage."),
    ("Oil-free sunscreen near your eyes", "Sunscreen undoes more sets than the sea does."),
    ("Pat dry, never rub", "Then brush through once they are dry.")], "Lashes at<br><i>the beach</i>"), False),
 ("11-wedding", L, "Getting married?", points([
    ("Six to eight weeks before", "Patch test and a trial set. Never try a new look on the day."),
    ("Every two to three weeks", "Infills keep it full and let the shape be adjusted."),
    ("Three to five days before", "Your final infill. Not the day before, never the morning of.")], "Wedding lash<br><i>timeline</i>"), False),
 ("12-new-tech", D, "Moving from another lash tech?", title("You do not have to<br><i>start again</i>",
    "Sets from other salons are welcome.<br>Book a <b>foreign lash refill</b> and your set is tidied, then filled.", small=True), False),
 ("13-december", L, "December &amp; January", title("Holiday<br><i>bookings</i>",
    "Appointments around weekends and holidays book out first.<br>Book your pre-Christmas set or infill <b>now</b>."), False),
 ("14-review", D, "A small favour", title("Loved your<br><i>lashes?</i>",
    "A Google review helps other locals find the studio.<br><b>luxebeautyyanchep.com/review</b>"), False),
]

CAPTIONS = """LUXE BEAUTY YANCHEP - INSTAGRAM TILES + CAPTIONS
================================================
Pictures are in the "posts" folder, numbered. Tiles that share a number (06, 07) are ONE
carousel post: add them all to the same post, in order.

These are text tiles. They work best BETWEEN photos of your real work, roughly one tile
for every two photos. Put the link luxebeautyyanchep.com/book in your bio.

Suggested order, two or three a week:
  Week 1: 04 book online  -  01 lash prices  -  a client photo
  Week 2: 06 aftercare (carousel)  -  a client photo  -  13 December bookings
  Week 3: 07 classic / hybrid / volume (carousel)  -  a client photo  -  02 infill prices
  Week 4: 12 moving from another tech  -  a client photo  -  10 lashes at the beach
  Week 5: 03 brows  -  a client photo  -  08 infill or full set
  Week 6: 09 patch test  -  a client photo  -  05 one client at a time
  Any time: 11 wedding timeline, 14 review (best as a Story, with a link sticker)

Hashtags to paste under any of them:
#yanchep #yancheplashes #yanchepbeauty #tworocks #alkimos #eglinton #jindalee #butlerwa
#perthlashes #lashextensionsperth #perthlashextensions #lashinfills #perthbrows

------------------------------------------------------------------------------------
01 LASH PRICES
Full set prices, all in one place. Classic $%(c)d, hybrid $%(h)d, volume $%(v)d, mega volume $%(m)d. Every appointment includes a consultation, and the price you see is the price you pay. Book online, link in bio.

02 INFILL PRICES
Infills keep your set full for a fraction of a new one. Come back within two weeks for the lowest price, or within three. Sets from other salons are welcome too. Book online, link in bio.

03 BROWS
Brows shaped to your face, not a stencil. Add a brow shape ($25) or a shape and tint ($40) to any lash appointment. Not wearing lashes? The brow shape and tint with a lash tint is $60 and you can book it on its own.

04 BOOK ONLINE
Online booking is open. Pick your treatment and your time, and a $50 deposit locks it in (it comes straight off your total). Need something in the next 24 hours? Call or message me instead. Link in bio.

05 ONE CLIENT AT A TIME
It is a private home studio in Yanchep, and I only book one client at a time. No waiting room, no being rushed. Just a quiet room and the time to get your set right.

06 AFTERCARE (carousel, 3 pictures)
Half of how long your lashes last is down to what happens after you leave. Save this one. Six rules, and the first 24 hours matter most. Full guide on the website.

07 CLASSIC, HYBRID OR VOLUME (carousel, 5 pictures)
Not sure which set to ask for? The names are about how many extensions go on each natural lash, not how dramatic it looks. Swipe through, and if you are still not sure, send me a photo of your natural lashes and I will tell you honestly what will suit.

08 INFILL OR FULL SET
The question I get asked most. It comes down to how much of your set is left. Stay inside three weeks and it is an infill. Leave it longer and it is usually a new full set, so book your next one before you leave.

09 PATCH TEST
First time having lash extensions or a tint? You need a patch test first. It is free, it takes two minutes, and it needs to be done 48 hours before your appointment. Message me to arrange it.

10 LASHES AT THE BEACH
Yes, you can swim with lash extensions. Give them 24 hours first, rinse with fresh water afterwards, and keep oily sunscreen away from your lash line. More on the website.

11 WEDDING TIMELINE
Getting married? Lashes are the one thing you can finish days ahead and forget about, as long as the timing is right. Start with a trial set six to eight weeks out. Full guide on the website.

12 MOVING FROM ANOTHER LASH TECH
If your lash tech has moved on, you do not have to take your set off and start again. Book a foreign lash refill in the style you are wearing. Not sure what style that is? Send me a photo.

13 DECEMBER
December and January fill up early, especially weekends. If you want lashes for Christmas, a party or a holiday, book now and choose your time. Link in bio.

14 REVIEW (post as a Story with a link sticker to luxebeautyyanchep.com/review)
If you have been in recently and you are happy with your lashes, a quick Google review would mean a lot. It is how other locals find me.

------------------------------------------------------------------------------------
MESSAGES TO SAVE IN YOUR PHONE

The evening after an appointment:
  Hi [name], thanks for coming in today! If you're happy with your lashes, a quick Google
  review would mean a lot: luxebeautyyanchep.com/review

Two weeks after a set, if they have not rebooked:
  Hi [name], your lashes are about due for an infill. Book inside three weeks and it's a
  refill, not a full set: luxebeautyyanchep.com/book

To a new enquiry:
  Thanks for getting in touch! You can see prices and book online here:
  luxebeautyyanchep.com/book  If it's your first time, you'll need a quick patch test
  48 hours before. When suits you to pop in for that?
""" % {"c": P["Classic"], "h": P["Hybrid"], "v": P["Volume"], "m": P["Mega Volume"]}

if __name__ == "__main__":
    os.makedirs(os.path.join(HERE, "build"), exist_ok=True)
    for name, theme, eyebrow, body, swipe in POSTS:
        open(os.path.join(HERE, "build", name + ".html"), "w", encoding="utf-8").write(page(theme, eyebrow, body, swipe=swipe))
    open(os.path.join(HERE, "captions.txt"), "w", encoding="utf-8").write(CAPTIONS)
    print("  wrote %d tiles to build/ and captions.txt" % len(POSTS))
