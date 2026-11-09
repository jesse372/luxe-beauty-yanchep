# -*- coding: utf-8 -*-
"""More guide pages (added 2026-11-09). Same shape as guides.py, which imports these.

Every factual claim here matches what the rest of the site already says
(aftercare.html, contact.html, services.html, prices.py). Keep it that way:
if a policy changes, change it there first, then here.
"""
import prices

_P = dict(prices.FULL_SETS)
_R = prices.REFILLS

MORE_GUIDES = [
{
 "slug":"how-long-do-lash-extensions-last",
 "short":"How long lashes last",
 "published":"2026-11-09",
 "title":"How Long Do Lash Extensions Last? Refills Explained",
 "h1":"How long lashes<br>actually last",
 "eyebrow":"Refill guide &middot; Timing &amp; cost",
 "desc":"How long lash extensions really last, why a set thins gradually, when to book a two or three "
        "week refill, what a foreign refill is and what it all costs.",
 "hero":"photos/lash-1.jpg",
 "lede":"Two different questions hide inside this one. How long does a single extension stay on, and "
        "how long does a set keep looking like a set? The answers are about six weeks and about two to "
        "three, and the gap between them is the whole reason refills exist.",
 "sections":[
  ("The short answer","""<p>An extension is bonded to one natural lash, and it stays until that lash
   sheds. Natural lashes live for roughly six to eight weeks, so that is the outer limit for any single
   extension.</p>
   <p>A <b>set</b> is a different thing. Your lashes are all at different points in their cycle, so a few
   are shed every day, each taking its extension along. After two to three weeks enough have gone that the
   set starts to look gappy rather than deliberate. That is the point a refill is for.</p>"""),
  ("Why a set thins instead of falling out","""<p>If extensions came off because the adhesive failed,
   you would lose them in patches in the first few days. When they are applied properly that is not
   what happens. They leave one at a time, attached to the natural lash that was always going to shed.</p>
   <p>This is also why finding an extension on your pillow is not a fault. Look closely and there is
   usually a natural lash attached to it. A handful a day is the normal cycle doing its job.</p>
   <p>What is <b>not</b> normal is losing a lot in the first 48 hours, or extensions sliding off with no
   natural lash attached. If that happens, send a message within 48 hours of the appointment and it
   gets sorted.</p>"""),
  ("Two week, three week and foreign refills",""),
  ("Which refill you actually need","""<p><b>Two week refill.</b> You are back within two weeks of your
   last appointment. Most of the set is still there, so it is a lighter top-up and the cheapest of the
   three.</p>
   <p><b>Three week refill.</b> Within three weeks. More has grown out, so there is more to rebuild and
   it costs a little more.</p>
   <p><b>The line between a refill and a full set</b> is roughly 40% of the extensions still in place.
   Under that, and usually anywhere past three weeks, there is not enough left to refill and a new full
   set is the honest answer.</p>
   <p><b>Foreign refill.</b> A refill of a set applied by another technician. It costs more because it
   includes a tidy-up, and because working over someone else&rsquo;s mapping and adhesive takes longer.
   If the existing set has lashes glued together, it gets removed rather than built on. Lash removal is
   $25 as an add-on, and a clean start protects your natural lashes.</p>"""),
  ("What shortens the life of a set","""<p>In rough order of how often they are the cause:</p>
   <p><b>Oil.</b> Oil-based cleansers, makeup removers, moisturisers and sunscreens break down the
   adhesive. This is the big one, and it is usually a product nobody thought to check.</p>
   <p><b>Rubbing and picking.</b> Towelling your face dry, rubbing tired eyes, pulling at a lash that
   feels loose.</p>
   <p><b>Getting them wet too early.</b> The adhesive needs 24 hours to cure fully. Water, steam and heavy
   sweat inside that window weaken the bond for the whole life of the set.</p>
   <p><b>Not cleansing.</b> It sounds backwards, but dirty lashes shed faster. Skin oil and makeup build
   up at the base and work on the adhesive all day.</p>
   <p><b>Sleeping on them.</b> Side sleepers see one eye thin out first. A silk pillowcase helps.</p>
   <p>The full routine is on the <a href="aftercare.html">aftercare page</a>.</p>"""),
  ("What it costs to keep a set going","""<p>The full set is the entry fee. The refills are the running
   cost, and they are the number worth budgeting for.</p>
   <p>A classic set on two week refills works out at about <b>$130 a month</b>. Stretch to three week
   refills and it is closer to <b>$110 a month</b>, with a set that looks a little thinner in the last
   few days before each appointment. Hybrid, volume and mega volume scale up in proportion.</p>
   <p>Skipping refills to save money rarely works. Leave it past three weeks and you are paying for a
   full set again, which costs more than the refill you skipped. There is a fuller breakdown in
   <a href="lash-extensions-cost-perth.html">what lash extensions cost</a>.</p>"""),
 ],
 "faqs":[
  ("How often should I get a lash refill?",
   "Every two to three weeks. Two weeks keeps a set looking full the whole time. Three weeks is fine if "
   "you do not mind it looking a little lighter in the last few days."),
  ("Can I go four weeks between refills?",
   "Usually not as a refill. By four weeks most sets are under the roughly 40% needed to build on, so the "
   "appointment becomes a new full set. If you know you will be away, book a refill just before you go."),
  ("Is it normal to lose extensions in the first few days?",
   "A few, yes, because natural lashes are shed every day and take their extension along. Losing a lot in "
   "the first 48 hours is not normal. Message within 48 hours of your appointment and it will be sorted."),
  ("Why do my lashes fall out faster on one side?",
   "Almost always sleep. Whichever side you sleep on gets pressed into the pillow for hours. Sleeping on "
   "your back or using a silk pillowcase evens it out."),
  ("Do lash extensions fall out faster in summer?",
   "They can. Sweat, sunscreen and swimming all work on the adhesive. Oil-free sunscreen around the eyes "
   "and a rinse with fresh water after the beach make most of the difference."),
  ("Do I need to take a break from lash extensions?",
   "Not on a schedule. If your natural lashes are healthy and the set is the right weight for them, you "
   "can wear extensions continuously. If your lashes do need a rest, you will be told so at the appointment."),
 ],
 "cta":"Due for a refill, or not sure whether you need a refill or a full set? Book in, or send a photo first.",
},
{
 "slug":"swimming-with-lash-extensions",
 "short":"Swimming with lashes",
 "published":"2026-11-09",
 "title":"Can You Swim With Lash Extensions? Beach, Pool &amp; Sunscreen",
 "h1":"Swimming with<br>lash extensions",
 "eyebrow":"Summer guide &middot; Beach &amp; pool",
 "desc":"Yes, you can swim with lash extensions after the first 24 hours. What salt water, chlorine "
        "and sunscreen really do to a set, and how to protect it.",
 "hero":"photos/lash-5.jpg",
 "lede":"The studio is in Yanchep, where summer means the lagoon, so this one is worth answering "
        "properly. The short answer is yes. The longer answer is that the water is rarely what does "
        "the damage.",
 "sections":[
  ("Yes, after the first 24 hours","""<p>Lash adhesive cures over about 24 hours. Until it has, water,
   steam and sweat weaken the bond, and a bond that cured badly stays weak for the life of the set.</p>
   <p>So the one hard rule is the first day: no swimming, no long steamy shower, no sauna and no hard
   training session. After that, extensions are made to get wet. Showers, pools and the ocean are all
   fine.</p>"""),
  ("Salt water","""<p>Sea water does not dissolve cured adhesive. What it does is dry on your lashes.
   Salt crystals sit at the base of each extension, hold grit there and make the bond more brittle, and
   that is before you rub your eyes because they sting.</p>
   <p>The fix is simple. Rinse your lashes with fresh water when you get out. The beach shower or a
   water bottle is enough. Then cleanse properly that evening.</p>"""),
  ("Chlorine","""<p>An occasional swim in a pool does very little. Regular lap swimming is a different
   matter, because chlorinated water several times a week shortens retention. If you swim
   laps, expect to be on two week refills rather than three.</p>
   <p>Goggles matter more than the water. Small racing goggles press the cup straight onto your lashes
   and bend them. A mask-style pair with a larger socket sits on the bone around the eye and leaves the
   extensions alone.</p>"""),
  ("Sunscreen is the real culprit","""<p>If a set does not survive a beach holiday, it is nearly always
   the sunscreen and not the sea. Most sunscreens are oil-based, oil breaks down lash adhesive, and it
   migrates into the lash line as you sweat.</p>
   <p>You do not have to choose between your skin and your lashes. Use an <b>oil-free</b> sunscreen on
   your face, put it on with a fingertip and stop short of the lash line, and let sunglasses and a hat
   do the work right around the eyes. The same goes for after-sun and any oily makeup remover that
   evening.</p>"""),
  ("The two-minute routine after a swim","""<p><b>Rinse</b> with fresh water as soon as you are out.</p>
   <p><b>Pat, do not rub.</b> Press a towel gently around the eyes. Dragging a towel across wet lashes
   pulls extensions sideways.</p>
   <p><b>Cleanse that night</b> with a lash-safe foaming cleanser and a soft brush, to lift salt,
   chlorine and sunscreen from the lash line.</p>
   <p><b>Brush once dry.</b> A clean spoolie through dry lashes puts everything back in line.</p>"""),
  ("Timing a set around a holiday","""<p>Book the full set or refill two or three days before you leave,
   not the morning you fly. That covers the 24 hour cure and leaves time to fix anything that is not
   sitting right.</p>
   <p>Expect to need a refill when you get back. A week of sun, salt and sunscreen is harder on a set
   than a week at a desk, which is completely fine. That is what they are for.</p>"""),
 ],
 "faqs":[
  ("How soon after a full set can I swim?",
   "Wait at least 24 hours so the adhesive can cure fully. If you can leave it 48 hours, better still."),
  ("Does salt water ruin lash extensions?",
   "No. Salt water does not dissolve cured adhesive. Dried salt left at the lash line is what causes "
   "trouble, so rinse with fresh water after a swim and cleanse that evening."),
  ("Can I wear goggles with lash extensions?",
   "Yes. Choose a mask-style pair with a larger socket that sits on the bone around the eye. Small racing "
   "goggles press on the lashes and bend them."),
  ("Can I shower with lash extensions?",
   "Yes, after the first 24 hours. Avoid pointing a strong shower jet straight at your face, and pat your "
   "lashes dry afterwards."),
  ("Can I use a sauna or steam room?",
   "After the first 24 hours, occasionally. Heat and steam soften adhesive, so regular sauna use shortens "
   "how long a set lasts."),
  ("Can I wear waterproof mascara at the beach instead?",
   "Not over extensions. Waterproof mascara is close to impossible to remove without oil or rubbing, and "
   "both take the extensions off with it."),
 ],
 "cta":"Heading away, or just want lashes that survive a Yanchep summer? Book two or three days before you go.",
},
{
 "slug":"first-lash-extension-appointment",
 "short":"Your first appointment",
 "published":"2026-11-09",
 "title":"Your First Lash Extension Appointment: What to Expect",
 "h1":"Your first<br>lash appointment",
 "eyebrow":"First-timer guide",
 "desc":"What happens at a first lash extension appointment: the patch test, how to arrive, what it "
        "feels like, how long it takes, and the first 24 hours afterwards.",
 "hero":"photos/lash-2.jpg",
 "lede":"Lying still with your eyes shut for two hours while someone works a few millimetres from them "
        "is an odd thing to sign up for if nobody has told you what happens. Here is the whole "
        "appointment, start to finish.",
 "sections":[
  ("Before you book: the patch test","""<p>If you have never had lash extensions or a tint, you need a
   patch test first. A small amount of product goes on the skin to check you do not react to it.</p>
   <p>It takes two minutes, it is free, and it has to be done at least 24 hours before your appointment.
   48 hours is better. If you are driving in from further out, tie it to another trip so you are not
   coming up twice.</p>"""),
  ("Choosing your first set","""<p>For a first set, <b>classic</b> or <b>hybrid</b>. Both are natural
   enough to live with while you work out what you like, and you can always go fuller next time. Starting
   with mega volume is the most common first-set regret.</p>
   <p>You do not need to decide alone. The appointment starts with a look at your eye shape and your
   natural lashes, and what they can comfortably carry narrows the choice quickly. If you want to read
   up first, the differences are laid out in
   <a href="classic-vs-hybrid-vs-volume-lashes.html">classic, hybrid or volume</a>.</p>"""),
  ("How to arrive","""<p><b>Clean lashes, no eye makeup.</b> No mascara, no liner, no oily skincare
   around the eyes. Adhesive bonds to a clean lash and slides off an oily one, so this makes a real
   difference to how long the set holds.</p>
   <p><b>Contact lenses.</b> If you wear them, it is more comfortable to take them out for the
   appointment. Bring your case and glasses.</p>
   <p><b>Comfortable clothes.</b> You will be lying down for about two hours.</p>
   <p><b>Come alone.</b> It is a home studio with sharp tools and adhesive fumes, so it is not a place
   for children, and the two hours are yours.</p>"""),
  ("What happens in the room","""<p><b>Consultation.</b> Your eye shape, your natural lashes, your
   routine and how bold you want to go. The length, curl and thickness of the extensions are mapped
   across the eye from that.</p>
   <p><b>Preparation.</b> Your lower lashes are covered with soft pads so nothing bonds to them, and your
   lashes are cleansed. Your eyes stay closed from here until the end.</p>
   <p><b>Application.</b> One natural lash is separated from its neighbours, and one extension is
   attached to it, a millimetre or so from the skin. Then the next one. That separation step is
   called isolation, and it is what stops lashes being glued together.</p>
   <p><b>What it feels like.</b> Very little. A light touch on the lids, and tweezers you can hear but
   not feel. It should never sting. If it does, say so straight away.</p>
   <p>Most clients fall asleep, which is the highest compliment the studio gets.</p>"""),
  ("How long it takes","""<p>Allow about two hours for a classic full set and up to two and a half for
   volume or mega volume. Only one client is booked at a time, so your appointment starts when it says it
   does and nobody is waiting on you to finish.</p>
   <p>Refills afterwards are much shorter, at around an hour.</p>"""),
  ("The first 24 hours","""<p>Keep them completely dry for 24 hours while the adhesive cures. No shower
   on the face, no steam, no swimming and no heavy sweating.</p>
   <p>After that, cleanse them daily with a lash-safe foaming cleanser, keep oil-based products away from
   your eyes, and do not use a lash curler or waterproof mascara. The full list is on the
   <a href="aftercare.html">aftercare page</a>.</p>
   <p>Then book your first refill for two to three weeks later. It is easiest to do that before you
   leave.</p>"""),
  ("Booking and cost","""<p>A classic full set is $120, hybrid $140, volume $160 and mega volume $180.
   Every price is on the <a href="services.html">services page</a>, and it is the price you pay.</p>
   <p>Bookings are made online and confirmed with a $50 deposit, which comes straight off your total on
   the day. Give at least 24 hours&rsquo; notice and the deposit moves with you to a new time.</p>"""),
 ],
 "faqs":[
  ("Do lash extensions hurt?",
   "No. You feel a light touch on your eyelids and that is about it. Nothing should sting or pull. If "
   "anything does, say so during the appointment and it is adjusted on the spot."),
  ("Can I open my eyes during the appointment?",
   "No, they stay closed the whole time. That keeps adhesive fumes out of your eyes, and it is why most "
   "people end up asleep."),
  ("Do I need a patch test before my first lash appointment?",
   "Yes. It takes two minutes, it is free, and it needs to be done at least 24 hours beforehand, "
   "preferably 48."),
  ("Can I get lash extensions if my natural lashes are short or sparse?",
   "Usually, yes. A hybrid set is the most forgiving on sparse or uneven lashes because the fans fill "
   "gaps. What your lashes can carry is assessed at the consultation, and you will get an honest answer."),
  ("How long before an event should I book my first set?",
   "Three to five days before. That gives the set time to settle and leaves room to adjust anything. "
   "Do not book a first-ever set for the morning of an event."),
  ("What if I have a reaction afterwards?",
   "Reactions are uncommon, and the patch test exists to catch them first. If your eyes are red, swollen "
   "or itchy after an appointment, get in touch straight away so the set can be removed safely, and see "
   "a pharmacist or doctor if it is severe."),
 ],
 "cta":"First set? Start with the patch test and a classic or hybrid. New clients are always welcome.",
},
{
 "slug":"wedding-lash-extensions",
 "short":"Wedding lashes",
 "published":"2026-11-09",
 "title":"Wedding Lash Extensions: When to Book &amp; Which Set to Choose",
 "h1":"Lashes for<br>your wedding",
 "eyebrow":"Bridal guide &middot; Timing",
 "desc":"Lash extensions for your wedding: the timeline that works, why you need a trial set, which "
        "style suits photos, and how they cope with tears and a long day.",
 "hero":"photos/lash-3.jpg",
 "lede":"Lash extensions are one of the few parts of wedding-day beauty you can finish days in advance "
        "and then forget about. They only work that way if the timing is right, and the most common "
        "mistake is leaving the first set until the week of the wedding.",
 "sections":[
  ("The timeline that works","""<p><b>Six to eight weeks out: patch test and a trial set.</b> Never wear
   a style for the first time on your wedding day. A trial set tells you whether you like the look, how
   your eyes take to the adhesive and how the set wears over a fortnight, with time to change your mind.</p>
   <p><b>From then on: refills every two to three weeks.</b> This keeps the set going and lets the shape
   be adjusted. A little longer at the outer corner, a little lighter overall, whatever the trial showed.</p>
   <p><b>Three to five days before: the final refill.</b> Not the day before and never the morning of.
   Three to five days lets the set settle, covers the 24 hours it has to stay dry, and leaves room to fix
   anything that is not sitting right.</p>"""),
  ("If you are short on time","""<p>If the wedding is under three weeks away and you have never had
   extensions, it can still be done. Book the patch test now and a full set three to five days before
   the day.</p>
   <p>Choose a classic or hybrid set. This is not the week to find out how mega volume feels.</p>"""),
  ("Which set to choose","""<p><b>Classic</b> gives definition and reads as your own lashes, only
   better. It suits a natural or minimal makeup look and is the safest choice if you do not usually wear
   much.</p>
   <p><b>Hybrid</b> adds texture and fullness without looking heavy. It is a good middle ground if you are torn between the other two.</p>
   <p><b>Volume</b> is denser and darker at the lash line, which holds up well alongside a full
   evening makeup.</p>
   <p>Whatever you choose, do not go heavier than you have worn before. You want to recognise yourself in
   the photos. The styles are compared side by side in
   <a href="classic-vs-hybrid-vs-volume-lashes.html">classic, hybrid or volume</a>.</p>"""),
  ("Tears, heat and a very long day","""<p>This is where extensions earn their place. There is no mascara
   to run and no strip lash to lift at the corner halfway through the speeches.</p>
   <p>If you cry, and most people do, <b>dab under the eye with a tissue and do not wipe across</b>.
   Cured extensions are not bothered by tears.</p>
   <p>Tell your makeup artist you are wearing them. That means oil-free products around the eyes, no lash
   curler, no strip lashes glued on top and no waterproof mascara. A good artist will know all of this
   already.</p>"""),
  ("The honeymoon","""<p>The final refill before the wedding normally carries you through the first week
   or so away. Sun, salt water and sunscreen are harder on a set than ordinary life, so rinse with fresh
   water after swimming and keep oily sunscreen away from your lash line. There is more in
   <a href="swimming-with-lash-extensions.html">swimming with lash extensions</a>.</p>"""),
  ("Bridal parties","""<p>The studio books one client at a time, so a bridal party is a run of separate
   appointments rather than a group session. That is easy to arrange with notice and hard to arrange
   without it. If bridesmaids or mums want lashes too, ask early so the appointments can be lined up
   across the same few days.</p>"""),
  ("What it costs","""<p>A trial full set is the normal price: $%(c)d classic, $%(h)d hybrid, $%(v)d
   volume. Refills between the trial and the wedding are from $%(r)d each.</p>
   <p>If you would rather not wear extensions at all, a brow shape and tint with a lash tint is $60. It
   can be booked on its own and makes a quick, low-commitment refresh a few days before the day.
   Everything is listed on the <a href="services.html">services page</a>.</p>"""
   % {"c":_P["Classic"], "h":_P["Hybrid"], "v":_P["Volume"], "r":_R["Classic"][0]}),
 ],
 "faqs":[
  ("How far before my wedding should I get lash extensions?",
   "Have a trial set six to eight weeks before, keep it going with refills, and book the final refill "
   "three to five days before the wedding. Avoid the day before and the morning of."),
  ("Should I get lash extensions or strip lashes for my wedding?",
   "Strip lashes are applied on the day and can lift with tears or heat. Extensions are done days ahead, "
   "do not lift and need nothing on the morning. Extensions suit you if you want one less thing to think "
   "about. Strips suit you if you want a look for one day only."),
  ("Can I cry with lash extensions?",
   "Yes. Once the adhesive has cured, tears do not affect it. Dab under the eye with a tissue rather than "
   "wiping across the lashes."),
  ("Can my makeup artist work with lash extensions?",
   "Yes, and most prefer it. Let them know beforehand so they use oil-free products around the eyes and "
   "skip the lash curler, strip lashes and waterproof mascara."),
  ("Is there an option if I do not want extensions?",
   "A lash tint darkens your own lashes so you can go without mascara. It is available as an add-on, or "
   "on its own as part of the $60 brow shape and tint with lash tint package."),
 ],
 "cta":"Getting married? Start with a patch test and a trial set six to eight weeks out.",
},
]


def _refill_table():
    heads = [""] + [n for n, _ in prices.FULL_SETS]
    rows = [["Full set"] + ["$%d" % p for _, p in prices.FULL_SETS]]
    for i, label in enumerate(["Two week refill", "Three week refill", "Foreign refill"]):
        rows.append([label] + ["$%d" % _R[n][i] for n, _ in prices.FULL_SETS])
    return heads, rows

MORE_TABLES = {"how-long-do-lash-extensions-last": _refill_table()}
