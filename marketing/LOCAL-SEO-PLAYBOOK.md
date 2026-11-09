# Local SEO playbook — Luxe Beauty Yanchep

Companion to `GOOGLE-BUSINESS-PROFILE.md`. That file is the one-time setup;
this is the ongoing work and the reasoning behind the on-site suburb pages.

---

## 1. The honest hierarchy

For "lash extensions near me" in the northern corridor, ranking works like this:

| Lever | Impact | Status |
|---|---|---|
| **Google Business Profile + reviews** | Owns the map pack, which sits above every organic result | Profile is LIVE (138 views in Oct 2026). **Zero reviews** and the category shows "Beauty salon", not "Eyelash salon" — see section 0 |
| Homepage + lash prices + eyebrows pages | The three pages that can rank for Yanchep searches | Done (2026-11-09 pass) |
| Suburb landing pages | Wins organic for "lash extensions <suburb>" | Built (22 + hub), but Google has crawled almost none of them — see section 0 |
| Guides | Questions people ask before they pick a salon | 6 guides + hub |
| Citations (NAP consistency) | Supporting trust signal | Not started |
| Backlinks | Slow, compounding. The reason Google is not crawling the site | Not started |

**The suburb pages cannot rank you in the map pack.** Map-pack position is
proximity + category + review signals, and nothing on the website changes it.
If only one thing gets done this month, it is the profile and ten reviews.

---

## 0. Where things stand (measured 2026-11-09)

Numbers from Search Console (`GSC_SITE=sc-domain:luxebeautyyanchep.com python3 ~/JesseOS/workspace/gsc/gsc.py ...`):

- **About 80 impressions and 2-4 clicks a week**, average position 7. Yanchep is a small market.
- **Only 6 of 32 pages were indexed** seven weeks after launch. 26 had never been crawled, including
  every suburb page bar none and both guides. Google knows the URLs exist and has not bothered to
  fetch them. That is a trust problem (new domain, no links, no reviews), not a content problem,
  and more pages do not fix it.
- The searches the site actually shows for: "eyebrows yanchep" (position 6, the most-seen query),
  "yanchep beauty", "yanchep beauty salon", "lash extensions near me". Nothing suburb-specific.
- **Bing has indexed nothing.** Bing feeds ChatGPT search, Copilot and DuckDuckGo.
- Mobile Lighthouse on the homepage before this pass: performance 82, largest paint 4.0s.

What was done about it on 2026-11-09:

1. Homepage: the `<h1>` is now "Lash extensions & brows · Yanchep, WA" (the brand line keeps its
   look as a styled paragraph). Added a price list, an eyebrows section, nine FAQs, guide links and
   links to the six nearest suburbs. Title tag untouched.
2. New `eyebrows-yanchep.html`, for the query the site is already seen for.
3. Four new guides (how long lashes last, swimming, first appointment, weddings) plus a guides hub.
4. Aftercare page rebuilt into a proper guide with FAQs. Services, about, contact and gallery got
   real titles and structured data.
5. Speed: fonts are self-hosted, every photo is WebP with phone-sized versions.
6. Sitemap priorities now favour the pages that can win: Yanchep pages first, the five nearest
   suburbs next, the outer ring last. `lastmod` only moves when a page really changes.
7. IndexNow set up for Bing (`marketing/seo/indexnow.py`).
8. The Google Maps listing is linked from the site's structured data, the contact page and aftercare.

Second pass, same day:

9. `lash-infills-yanchep.html`. Australians search "lash infills"; the word was nowhere on the site
   (the menu says refills). The page also speaks to people whose lash technician has moved on.
10. Two more guides: do extensions damage natural lashes, and lash styles by eye shape. 41 pages in all.
11. **Review link: `luxebeautyyanchep.com/review`** forwards to the Google review form. Printable
    cards are in `marketing/review-card/` (`review-cards-a4.pdf`, four to a page; `review-card.png`
    for sending). The QR code points at the short link, so if Google's link ever changes, edit
    `review.html` and the printed cards keep working.
12. Weekly index report: `com.jesse.gsc-weekly-luxe` (Thursdays 07:10) writes
    `~/JesseOS/workspace/gsc/reports/luxe-<date>.md` and sends the count to Jesse's phone.
    Baseline 2026-11-09: 6 of 41 indexed.
13. Fixed the homepage ticker (items after the third were invisible).

**Decision still open: the outer-ring suburb pages.** Kinross, Currambine, Joondalup, Burns Beach,
Iluka, Connolly, Ocean Reef, Mullaloo, Tapping and Wanneroo are 23-30 minutes away with their own
lash salons. They were left in place because Google has not judged them yet. If Search Console still
shows them as "Discovered - currently not indexed" in mid-January 2027, fold them into the hub page
and keep only the pages earning impressions.

**What moves the needle from here is off the website:** Google reviews, the profile's primary
category, real client photos, and a handful of genuine links. See sections 3 and 5.

---

## 2. What was built on-site, and why it is shaped this way

**22 individual suburb pages** (`lash-extensions-<suburb>.html`) covering the genuine
catchment out to ~30 minutes:

*Inner (≤25 min):* Eglinton · Two Rocks · Alkimos · Jindalee · Butler · Merriwa ·
Quinns Rocks · Ridgewood · Clarkson · Mindarie · Banksia Grove · Carramar
*Outer (20–30 min):* Kinross · Currambine · Joondalup · Burns Beach · Iluka ·
Connolly · Ocean Reef · Mullaloo · Tapping · Wanneroo

**One hub page** (`areas-we-serve.html`) — 22 linked suburb cards plus 39 wider-ring
rows, covering all **62 suburbs** inside 40 km with real distances and drive times.

**4 guide pages** — the higher-volume play. These target what people search *before*
they look for a salon, and carry no doorway risk because they are not geo-targeted:

| Page | Targets |
|---|---|
| `lash-extensions-cost-perth.html` | "how much do lash extensions cost perth" |
| `classic-vs-hybrid-vs-volume-lashes.html` | "classic vs hybrid vs volume" |

**Expect the guides to out-earn the suburb pages.** "How much do lash extensions cost"
has more monthly volume than every suburb query on this site combined. They also earn
links, which suburb pages never do.

### Why not a page per suburb for all 62

Because that is a doorway-page pattern, and Google's scaled-content-abuse policy targets
it directly. The risk is not that the extra pages fail to rank — it is that they drag the
**whole domain** down, including pages that already work. A new, low-authority domain is
exactly the profile that classifier is tuned for.

The tiering is the hedge: deep unique pages where there is genuine commercial intent, one
strong hub for the long tail.

### The uniqueness bar these pages must clear

Every page carries its own drive time, route, landmark, local angle and three
suburb-specific FAQs, at ~660 words each. Measured 8-gram overlap:

| Comparison | Max | Mean |
|---|---|---|
| suburb vs suburb | **0.336** | 0.276 |
| guide vs guide | 0.069 | 0.068 |
| suburb vs guide | 0.072 | 0.068 |

Above ~0.70 is doorway territory. Roughly half of every suburb page is text found
nowhere else on the site; the shared remainder is the pricing table, nav and footer,
which is legitimate.

> **If you add a suburb, write real copy for it.** Do not duplicate another suburb's
> block and swap the name — that is precisely what the tiering exists to avoid.
> Re-run the uniqueness check after any change and keep max overlap under 0.45.

### Rebuilding

```bash
marketing/seo/build_all.sh              # every generator in the right order, then the checks
python3 marketing/seo/indexnow.py       # after the change is LIVE: tells Bing what changed
GSC_SITE=sc-domain:luxebeautyyanchep.com python3 ~/JesseOS/workspace/gsc/gsc.py submit-sitemap
```

`build_all.sh` ends with `check.py`, which fails the build on a broken link, a missing image,
FAQ markup that does not match the page, a description over 160 characters, prices that disagree
with `prices.py`, or suburb pages that have drifted too close to each other.

Content lives in `suburbs.py`, `guides.py` + `guides_more.py`, `build_yanchep.py` (lash prices
page), `build_brows.py` (eyebrows page) and `build_schema.py` (homepage FAQ, structured data,
`llms.txt`). Nav and footer are in `build_seo.py` and are copied onto the hand-written pages
(index, services, about, aftercare, gallery, contact) by `build_schema.py`. `finalize.py` runs last:
WebP images, fonts, sitemap. To add a photo, drop the `.jpg` in `photos/` and rebuild.

### Technical

- Every page preloads its own hero image (`fetchpriority="high"`) — the hero is the LCP
  element sitewide, and it was previously unprioritised.
- 36 pages, 88 JSON-LD blocks, all parsing. Service + FAQPage + BreadcrumbList on suburb
  pages; Article + FAQPage + BreadcrumbList on guides; full 62-locality `areaServed` on
  the homepage `BeautySalon` node.

## 3. Review engine — the actual ranking lever

Review **count, recency and velocity** is the biggest movable factor in the map
pack. A new profile with 10 genuine reviews beats a five-year-old one with 2.

**The workflow that works:**
1. Ask **at the appointment**, while she is there and happy — not by text later.
2. Send the short review link the same evening.
3. Reply to every review, including bad ones. Google weights owner responses.

**Target:** 10 in the first month, then 2–3 a week.

**Never** buy reviews, post them yourself, or offer a discount for one. Google
detects velocity anomalies, and review-gating breaches their policy. Suspensions
are very hard to reverse.

### The link and the card

- Link to text or say: **luxebeautyyanchep.com/review**
- Card to leave by the mirror or hand over: `marketing/review-card/review-cards-a4.pdf`
- Text for the same evening: "Hi [name], thanks for coming in today! If you're happy with your
  lashes, a quick Google review would mean a lot: luxebeautyyanchep.com/review"

Ask everyone, not only the clients you expect to be happy. Asking only happy clients is review
gating, which Google's rules forbid.

### Ask script (say it, don't send it)

> "If you're happy with these, would you mind leaving a quick Google review?
> It genuinely is the whole reason people find me. I'll text you the link tonight."

### Reply templates

**5★** — "Thank you so much, [name]! So glad you love them. See you at your refill."

**3★ or under** — "Thanks for the honest feedback, [name], and I'm sorry these
weren't what you hoped for. I'd like to put it right — could you message me so we
can sort it out?" *(Never argue. The reply is for the 200 people reading it, not
the reviewer.)*

---

## 4. Google Posts — 8 drafts, one a week

Post weekly from the profile. Posts signal an active business and show in the panel.

1. **Now booking the northern corridor** — "Lash extensions, refills and brow shaping from a private studio in Yanchep. Classic sets from $120, and I only ever book one client at a time." → Book
2. **Which set suits you** — "Not sure which you want? Classic is one extension per lash ($120), hybrid mixes in fans ($140), volume is all fans ($160). Send a photo of your natural lashes for an honest rec." → Book
3. **Brow shape & tint** — "Brows shaped to your face, not a stencil, and tinted for depth. Add it to any lash set or refill for $40, or $25 for the shape alone." → Book
4. **Refill reminder** — "Refills every 2–3 weeks keep a set going indefinitely. Classic refills are $60 at two weeks and $75 at three; hybrid, volume and mega volume refills are priced in proportion. Past four weeks it's usually a new full set — book before you leave." → Book
5. **Coming from further out** — "Clients travel from Butler, Clarkson, Mindarie and Joondalup. Add a brow shape and tint with a lash tint for $60 and make one trip do the work of two." → Learn more → /areas-we-serve.html
6. **Event lashes** — "Wedding or event coming up? Book 3–5 days before, not the morning of — it gives shedding time to settle and leaves room to adjust." → Book
7. **Patch tests** — "First time with tint or adhesive? A patch test 48 hours ahead is free and takes two minutes. Worth tying to another trip if you're driving in." → Book
8. **Lash health** — "If your natural lashes need a break, I'll tell you. Sometimes the right answer is a few weeks off — a set applied over damaged lashes helps nobody." → Book

---

## 5. Citations — NAP consistency

Same **name, area, phone** everywhere. Inconsistency is a live ranking drag.

**Canonical NAP:**
```
Luxe Beauty Yanchep
Yanchep WA 6035  (service-area business — do NOT publish the street address)
0411 487 177
https://luxebeautyyanchep.com
```

Priority order:
- [ ] **Bing Places** — can import directly from Google Business Profile
- [ ] **Apple Business Connect** — Apple Maps; every iPhone "near me" search
- [ ] Facebook Page (category: Beauty Salon)
- [ ] Instagram business profile — link to the site, not Linktree
- [ ] True Local · Yellow Pages AU · Hotfrog AU · StartLocal
- [ ] Yanchep / Two Rocks community Facebook groups (participate, don't spam)
- [ ] Local school fete and sports club sponsorships — cheap, genuine local links

---

## 6. Measuring it

Set up once:
- [ ] **Google Search Console** — verify via DNS, submit `sitemap.xml`
- [ ] **GBP Insights** — track calls, direction requests, booking clicks monthly

**Leading indicator:** map-pack position for "lash extensions yanchep" and
"eyelash extensions butler". **Lagging indicator that actually matters:** bookings.

Check Search Console at 30 days for the suburb pages. Expect nothing for 4–8
weeks — new pages on a new domain take that long to settle.

### Watch for this

If impressions across the whole site drop sharply after the suburb pages index,
that is the scaled-content signal firing. The fix is to consolidate: cut the
weakest suburb pages into the hub and keep only those earning impressions.
Unlikely at 12 well-differentiated pages, but worth knowing the failure mode.
