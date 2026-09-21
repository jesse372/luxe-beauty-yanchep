# Local SEO playbook — Luxe Beauty Yanchep

Companion to `GOOGLE-BUSINESS-PROFILE.md`. That file is the one-time setup;
this is the ongoing work and the reasoning behind the on-site suburb pages.

---

## 1. The honest hierarchy

For "lash extensions near me" in the northern corridor, ranking works like this:

| Lever | Impact | Status |
|---|---|---|
| **Google Business Profile + reviews** | Owns the map pack, which sits above every organic result | **NOT CREATED YET — do this first** (see `YANCHEP-NUMBER-ONE.md`) |
| Suburb landing pages | Wins organic for "lash extensions <suburb>" | Done — 12 pages + hub |
| Citations (NAP consistency) | Supporting trust signal | Not started |
| Backlinks | Slow, compounding | Not started |

**The suburb pages cannot rank you in the map pack.** Map-pack position is
proximity + category + review signals, and nothing on the website changes it.
If only one thing gets done this month, it is the profile and ten reviews.

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
| `lash-lift-vs-extensions.html` | "lash lift vs extensions" |
| `classic-vs-hybrid-vs-volume-lashes.html` | "classic vs hybrid vs volume" |
| `brow-lamination-vs-microblading.html` | "brow lamination vs microblading" |

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
python3 marketing/seo/build_seo.py      # suburb pages + hub + sitemap.xml
python3 marketing/seo/build_guides.py   # guide pages   (run second)
python3 marketing/seo/build_yanchep.py  # the money page (run last)
```

Content lives in `marketing/seo/suburbs.py` and `marketing/seo/guides.py`. All three
generators are idempotent. `build_guides.py` imports helpers from `build_seo.py`, so
nav/footer changes only need making once, in `build_seo.py`.

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

1. **Now booking the northern corridor** — "Lash extensions, lifts and brow lamination from a private studio in Yanchep. Classic sets from $120, and I only ever book one client at a time." → Book
2. **Lash lift vs extensions** — "Not sure which you want? A lift curls your own lashes for 6–8 weeks with zero upkeep ($75). Extensions add length and density a lift can't ($120+). Send a photo of your natural lashes for an honest rec." → Book
3. **Brow lamination** — "The treatment that fixes the one thing makeup can't: brow hairs that won't sit where you want them. 6–8 weeks, $70, or $85 with a tint." → Book
4. **Refill reminder** — "Refills every 2–3 weeks keep a set going indefinitely. Two-week $60, three-week $75. Past four weeks it's usually a new full set — book before you leave." → Book
5. **Coming from further out** — "Clients travel from Butler, Clarkson, Mindarie and Joondalup. Combine a lash lift and brow lamination for $160 and make one trip do the work of two." → Learn more → /areas-we-serve.html
6. **Event lashes** — "Wedding or event coming up? Book 3–5 days before, not the morning of — it gives shedding time to settle and leaves room to adjust." → Book
7. **Patch tests** — "First time with tint or adhesive? A patch test 48 hours ahead is free and takes two minutes. Worth tying to another trip if you're driving in." → Book
8. **Lash health** — "If your natural lashes need a break, I'll tell you. Sometimes the right answer is a lift, or a few weeks off — a set applied over damaged lashes helps nobody." → Book

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
