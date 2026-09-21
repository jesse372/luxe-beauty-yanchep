# Getting to #1 for "lash extensions Yanchep"

Focused plan for the home-suburb query. Companion to `LOCAL-SEO-PLAYBOOK.md`.

**Status (full SERP confirmed 2026-09-21):** ranking with the **homepage**
(`luxebeautyyanchep.com`) at **#6 organic**, below a map pack.
**Target:** #1.

> **Correction:** an earlier version of this file said #2. That came from a partial
> screenshot that began mid-page. The full result list shows **#6**. Everything below
> is from the complete SERP.

---

## 1. The actual SERP

Below the map pack ("More businesses"), the organic order is:

| # | Result | Type | Note |
|---|---|---|---|
| 1 | The Mooi Collective — "Eyelash Services" | Website | |
| 2 | **Instagram — @coastalbeautybymarissa** | **Social** | Name field = "Yanchep Lash Extensions" |
| 3 | The Mooi Collective — homepage | Website | **2nd slot, same business** |
| 4 | Facebook — Ocean Beauty Yanchep | Social | 5.0 ★ (22 reviews) |
| 5 | MK Wellness — "Lash and Brow \| Yanchep" | Website | Prices pulled into snippet |
| 6 | **Luxe Beauty** | Website | ← you |

Three things to take from this:

1. **Mooi Collective holds two of the top three slots.** They are the dominant entity
   here, despite a thin page (section 4).
2. **Half the first page is not websites.** Instagram and Facebook profiles outrank real
   sites, on domain authority yours can never match.
3. **Two results carry star ratings. Yours carries none.**

---

## 2. THE highest-leverage action: the Instagram Name field

Free, takes under a minute, and it is the clearest finding in this audit.

| Profile | Instagram **Name** field | Rank |
|---|---|---|
| `@coastalbeautybymarissa` | **"Yanchep Lash Extensions"** | **#2** |
| `@luxebeautyyanchep` | "LUXE BEAUTY YANCHEP" | not ranking |

Instagram's **Name** field (the bold line, *not* the @username) is indexed by Google and
is exactly what produces that #2 result titled "Yanchep Lash Extensions". Marissa put the
keyword in the Name field and moved her brand into the first line of her bio:

> **Name:** Yanchep Lash Extensions
> **Bio:** COASTAL BEAUTY BY MARISSA / Located in Yanchep WA 6035 since 2020. /
> Lashes, Brows, BBGlow. / DM to book.

Luxe has the brand in the Name field and no keyword anywhere:

> **Name:** LUXE BEAUTY YANCHEP
> **Bio:** ✨ Luxury Lashes & Brows / 🤍 Enhancing your natural beauty / 📍 Yanchep, WA …

### The change

Instagram → Edit Profile → **Name** (not Username):

```
Yanchep Lash Extensions & Brows
```

Then let the bio carry the brand, so nothing is lost:

```
LUXE BEAUTY YANCHEP
Luxury lashes & brows, private studio
Classic sets from $120 · Yanchep WA 6035
New clients welcome — book below
```

**Why first:** you cannot beat instagram.com on domain authority with your own site. But
you already own an Instagram profile — it is simply not targeting the keyword. This makes
an asset you already have eligible for a slot it currently cannot reach.

**Notes:** the @username stays `luxebeautyyanchep`, so no links break. Instagram limits
Name changes to twice per 14 days — set it once, deliberately. Allow a few weeks to settle.

---

## 3. The other two entity gaps

### Google Business Profile — still not created
There **is** a map pack on this query, above all six organic results, and you are absent
from it. Setup in section 5 and `GOOGLE-BUSINESS-PROFILE.md`.

### No Facebook page at all
The site's `sameAs` lists Instagram only, while a competitor's Facebook page ranks #4 with
5.0 ★ (22). A Facebook page is free, can take its own slot, and collects reviews that
display as stars.

### On stars — what not to do
Do **not** add `AggregateRating` schema to manufacture them. Google does not render
self-serving review markup for `LocalBusiness`, so it would not display, and there are no
real reviews to mark up. Fabricating one is a manual-action risk. Those competitors' stars
are real and hosted on third-party platforms — that is the only route.

---

## 4. Done (2026-09-21)

`lash-extensions-yanchep.html` rebuilt from **499 → 1,676 words**. It was the thinnest
page on the site — thinner than the Ridgewood page — while being the single most
commercially important URL. Now the deepest.

Added: a classic/hybrid/volume/mega comparison table, a five-step "your appointment"
section, a Yanchep-specific section on salt, sunscreen and retention, FAQs expanded
5 → 12, and 19 internal links out to the guides and nearby suburbs.

Schema: Service (8 priced offers) + FAQPage (12 questions) + BreadcrumbList.

Rebuild with `python3 marketing/seo/build_yanchep.py`.

---

## 5. THE lever: Google Business Profile — 20 minutes

Not created. Until it is, the map pack is unwinnable and three competitors sit above
every organic result you earn. Nothing else on this list comes close in value.

**Do this in one sitting** (full detail in `GOOGLE-BUSINESS-PROFILE.md`):

1. `business.google.com` → use the **business** Google account, not a personal one
2. Name: exactly `Luxe Beauty Yanchep` — **no keywords in the name**, that is the most
   common cause of suspension and competitors can report it in two clicks
3. "Add a location customers can visit?" → **NO**. This makes it a Service Area
   Business and keeps the home address private
4. Service areas: Yanchep, Eglinton, Two Rocks, Alkimos, Jindalee, Butler (+14 more,
   capped at 20 — list is in the GBP doc)
5. Primary category: **Eyelash salon** ← the single most important ranking field
   Secondary: Beauty salon, Eyebrow bar
6. Hours Mon–Sat 9–5, phone `0411 487 177`, website `https://luxebeautyyanchep.com`
7. Add all 19 services with prices (they are in the GBP doc, ready to paste)
8. Photos: logo `icons/icon-512.png` + **real** client work only — never the site's
   stock photos, which can get a profile flagged

Then verify. Postcard verification takes 1–2 weeks, so **start it today** — the clock
runs regardless of anything else on this list.

---

## 6. Then: reviews, which decide the map pack

After proximity and category, **review count and recency** is the biggest factor.
A new profile with 10 genuine reviews beats a five-year-old one with 2.

- Ask **at the appointment**, while she is there and happy — not by text later
- Send the link the same evening
- Reply to every one, including bad ones

**Target: 10 in the first month.** That alone is usually enough to enter the map pack
in a suburb the size of Yanchep. Never buy reviews or offer a discount for one.

---

## 7. Cannibalisation — FIXED 2026-09-21

The screenshot confirmed the **homepage** is the ranking URL, which unblocked this.

- **Homepage: untouched.** It ranks, so its title still owns
  "Lash Extensions & Brows Yanchep". Never rewrite the page that is working.
- **`lash-extensions-yanchep.html`: retargeted** to
  *"Eyelash Extension Prices Yanchep | Classic, Hybrid, Volume & Mega"*, H1
  *"Eyelash Extension Prices in Yanchep"* — it now owns the price / set-type long tail
  instead of competing with its own parent.
- **36 internal anchors** changed from "Lash extensions Yanchep" to "Lash extension
  prices". Those anchors had been telling Google the child page owned the homepage's
  head term.

### One open item on the homepage

Its `<h1>` is *"Enhancing your natural beauty"* — no keyword, no location. For the page
that actually ranks, that is a missed relevance signal.

**Not changed unilaterally**, because it is the brand statement on the hero of the one
page that is working, and that is an aesthetic call rather than a purely technical one.
Worth testing a variant that keeps the brand line as the visual hero while adding a
keyword-bearing heading lower on the page. Ask before changing the hero itself.

## 8. What to measure

- [ ] **Google Search Console** — verify by DNS, submit `sitemap.xml`. Without this you
      are guessing at positions, which is where this plan is currently stuck.
- [ ] Track position weekly for `lash extensions yanchep`, `eyelash extensions yanchep`,
      `lashes yanchep`, `lash technician yanchep`
- [ ] Track map-pack position separately from organic — they move independently

Expect the rebuilt page to take **2–6 weeks** to settle. Do not judge it before then,
and do not keep editing it in the meantime — that resets the clock.
