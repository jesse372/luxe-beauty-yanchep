# -*- coding: utf-8 -*-
"""
Per-suburb source data for Luxe Beauty Yanchep local SEO pages.

EVERY field here must be genuinely specific to the suburb. This data is the
only thing standing between "a useful local page" and "a doorway page Google
demotes the whole domain for". If you add a suburb, write real copy for it.
Do not copy another suburb's block and swap the name.
"""

# Tier A = individual page. km = straight-line from the studio.
TIER_A = [
{
 "slug":"eglinton","name":"Eglinton","postcode":"6034","km":5.3,"mins":"7",
 "route":"straight down Marmion Avenue",
 "anchor":"the Allara and Amberton estates",
 "hero":"photos/lash-1.jpg",
 "intro":"Eglinton is the closest suburb to the studio &mdash; close enough that most Eglinton "
   "clients are home again before their coffee has gone cold. It is a single run down Marmion "
   "Avenue, about seven minutes from the Allara and Amberton estates, with no freeway and no "
   "hunting for parking at a shopping centre.",
 "angle":"Eglinton has grown fast, but its beauty options have not kept pace. Most residents "
   "still drive to Clarkson or Joondalup for lashes &mdash; a thirty to forty minute round trip "
   "past a dozen salons, for something you can have done properly seven minutes up the road.",
 "local":"If you catch the train, Eglinton Station opened on the Yanchep line in 2024 and Yanchep "
   "Station is one stop north &mdash; though for a lash appointment the drive is almost always quicker.",
 "faqs":[
  ("How far is the studio from Eglinton?",
   "About 5 kilometres, or roughly seven minutes up Marmion Avenue. It is the shortest trip of any "
   "suburb the studio serves."),
  ("Do you take clients from the new Eglinton estates?",
   "Yes &mdash; Allara, Amberton and the surrounding Eglinton estates make up a good share of the "
   "regular client list, largely because of how short the drive is."),
  ("Can I get a full set done in a school run window?",
   "A classic full set takes around two hours, so it fits comfortably between drop-off and pick-up "
   "with the Eglinton drive included. Mention it when you book and the appointment can be timed to suit."),
 ],
},
{
 "slug":"two-rocks","name":"Two Rocks","postcode":"6037","km":7.4,"mins":"9",
 "route":"south along Two Rocks Road onto Marmion Avenue",
 "anchor":"the marina and Atlantis Beach",
 "hero":"photos/lash-3.jpg",
 "intro":"Two Rocks sits at the very top of the coast, and that has always meant a long drive for "
   "anything beauty-related. The studio is about nine minutes south &mdash; down Two Rocks Road and "
   "onto Marmion Avenue &mdash; which makes it comfortably the closest lash and brow studio to the marina.",
 "angle":"Living in Two Rocks usually means accepting that everything is a drive. Lashes do not have "
   "to be one of them. Instead of forty minutes each way to Clarkson or Joondalup, it is under ten "
   "minutes to a private studio where you are the only client booked in.",
 "local":"Two Rocks clients often book the last appointment of the day so the drive home is an easy "
   "run north on an empty road rather than a crawl through afternoon traffic.",
 "faqs":[
  ("Is the studio the closest lash salon to Two Rocks?",
   "For lash extensions, lash lifts and brow lamination, yes &mdash; the studio in Yanchep is about "
   "nine minutes south, where the next nearest options are in Clarkson or Joondalup, thirty-plus minutes away."),
  ("How long is the drive from Two Rocks?",
   "Roughly 7 kilometres, about nine minutes via Two Rocks Road and Marmion Avenue. There is no "
   "freeway section and no traffic to speak of outside school hours."),
  ("Is it worth coming this far for a refill?",
   "Refills run every two to three weeks and take under an hour, so the appointment is often shorter "
   "than the round trip to anywhere else. Several Two Rocks clients book their refills as a standing "
   "fortnightly slot so it never has to be thought about."),
 ],
},
{
 "slug":"alkimos","name":"Alkimos","postcode":"6038","km":7.5,"mins":"9",
 "route":"north up Marmion Avenue",
 "anchor":"the Shorehaven and Trinity estates",
 "hero":"photos/lash-5.jpg",
 "intro":"Alkimos is about nine minutes from the studio, straight up Marmion Avenue from Shorehaven, "
   "Trinity and the older beachside pockets. It is close enough that a lash refill is a genuine errand "
   "rather than an afternoon out.",
 "angle":"Alkimos has a lot of young families and a lot of shift workers, and both tend to want the "
   "same thing from a lash appointment: an exact time, one client at a time, and no waiting room. A "
   "private home studio nine minutes away does that better than a salon floor with four beds running at once.",
 "local":"Alkimos Station opened on the Yanchep rail extension in 2024, so a car is not essential &mdash; "
   "but for most Alkimos clients the drive up Marmion Avenue is still the fastest way to get here.",
 "faqs":[
  ("How far is Yanchep from Alkimos?",
   "About 7.5 kilometres, or nine minutes up Marmion Avenue. No freeway, no shopping-centre car park."),
  ("Do you have evening appointments for shift workers?",
   "The last appointment usually starts mid-afternoon, but the schedule is flexible for regulars. If "
   "you are on shift work, ask when you book and something can usually be arranged."),
  ("Which set suits someone at the beach a lot?",
   "Alkimos clients are in and out of the water constantly, and that shortens the life of a set. A "
   "classic or hybrid set with a slightly stronger adhesive holds up better than mega volume, and a "
   "lash lift is worth considering if you swim most days &mdash; there is nothing to fall out."),
 ],
},
{
 "slug":"jindalee","name":"Jindalee","postcode":"6036","km":10.0,"mins":"11",
 "route":"north on Marmion Avenue",
 "anchor":"the Jindalee foreshore",
 "hero":"photos/lash-2.jpg",
 "intro":"Jindalee is a small, quiet coastal suburb about eleven minutes south of the studio on "
   "Marmion Avenue &mdash; one of those places with a beautiful beach and almost no local services. "
   "For lashes and brows, the studio in Yanchep is the nearest option worth the drive.",
 "angle":"Small suburbs get overlooked by salons because the numbers do not stack up on a shopfront. "
   "A home studio has no shopfront to justify, which is exactly why Jindalee clients can be looked "
   "after properly eleven minutes from home instead of half an hour down the coast.",
 "local":"Jindalee sits between Alkimos and Eglinton on Marmion Avenue, so the run north is short and "
   "uncomplicated at any time of day.",
 "faqs":[
  ("Is there a lash technician in Jindalee?",
   "Jindalee itself is almost entirely residential with no beauty strip. The closest studio is in "
   "Yanchep, about ten kilometres and eleven minutes north on Marmion Avenue."),
  ("Do you do brows as well as lashes for Jindalee clients?",
   "Yes &mdash; brow lamination, henna, tinting and shaping are all available, and combining brows "
   "with a lash appointment saves a second trip. There are combination prices for exactly that reason."),
  ("Can I book lashes and brows in the same visit?",
   "Yes, and it is the most common request from further-out suburbs. A lash lift with brow lamination "
   "and tint runs about two hours together and is priced as a combination rather than two separate services."),
 ],
},
{
 "slug":"butler","name":"Butler","postcode":"6036","km":12.1,"mins":"13",
 "route":"north on Marmion Avenue or Connolly Drive",
 "anchor":"Brighton Village and Butler Station",
 "hero":"photos/lash-4.jpg",
 "intro":"Butler is about thirteen minutes from the studio, whether you come up Marmion Avenue from "
   "the Brighton side or Connolly Drive from the east. It is one of the biggest suburbs in the northern "
   "corridor, and a large share of the regular client list lives there.",
 "angle":"Butler is well served for most things &mdash; but a busy salon floor at a shopping centre is "
   "a different experience to a private studio where one client is booked at a time. No walk-ins "
   "interrupting, no music you did not choose, and the same technician doing your set every time.",
 "local":"Butler Station was the end of the northern line for years before the Yanchep extension opened "
   "in 2024, and Brighton Village is the usual meeting point locally. Either way the drive north is a "
   "straight run.",
 "faqs":[
  ("How far is the studio from Butler?",
   "About 12 kilometres, or thirteen minutes north via Marmion Avenue or Connolly Drive."),
  ("Why come to Yanchep when there are salons in Butler?",
   "Mostly for the format. The studio takes one client at a time in a private room, the same technician "
   "does every set, and appointments run to time because there is nobody double-booked. For a two-hour "
   "full set that difference matters more than thirteen minutes of driving."),
  ("Do you do refills for sets done somewhere else?",
   "Yes &mdash; a foreign lash refill is available for work done elsewhere, priced slightly higher because "
   "it takes longer to tidy and rebalance an existing set. Send a photo before you book so you get an "
   "accurate quote and time."),
 ],
},
{
 "slug":"merriwa","name":"Merriwa","postcode":"6030","km":14.4,"mins":"16",
 "route":"north on Connolly Drive then Marmion Avenue",
 "anchor":"Merriwa Plaza",
 "hero":"photos/brow-1.jpg",
 "intro":"Merriwa is around sixteen minutes from the studio, north on Connolly Drive and across to "
   "Marmion Avenue. It is an established suburb with a settled community, and a good number of the "
   "studio's longest-standing clients have come from there.",
 "angle":"Merriwa clients tend to book for the long haul &mdash; a set maintained with regular refills "
   "rather than a one-off before an event. That suits the studio's approach, which is built around lash "
   "health over time rather than the heaviest set that will fit on the day.",
 "local":"Merriwa Plaza is the local hub, and the run north from there to Yanchep avoids the freeway entirely.",
 "faqs":[
  ("How long does it take to get to the studio from Merriwa?",
   "About 14 kilometres, roughly sixteen minutes via Connolly Drive and Marmion Avenue."),
  ("How often do I need refills?",
   "Every two to three weeks for most people. A two-week refill is $60 and a three-week refill is $75. "
   "Leaving it past four weeks usually means paying for a new full set, so Merriwa regulars tend to book "
   "the next one before they leave."),
  ("What happens if my lashes are damaged from a previous salon?",
   "It gets assessed honestly at the consultation. If the natural lashes need a break, that will be said "
   "plainly rather than applying a set over the top &mdash; sometimes the right answer is a lash lift or a "
   "few weeks of recovery first."),
 ],
},
{
 "slug":"quinns-rocks","name":"Quinns Rocks","postcode":"6030","km":15.0,"mins":"17",
 "route":"north on Marmion Avenue from Ocean Drive",
 "anchor":"Quinns Beach",
 "hero":"photos/lash-1.jpg",
 "intro":"Quinns Rocks is about seventeen minutes down the coast from the studio, an easy run from "
   "Ocean Drive onto Marmion Avenue. It is an older, established beachside suburb, and its clients tend "
   "to know exactly what they want from a set.",
 "angle":"Quinns Rocks is a beach suburb through and through, and that shapes the advice given. Salt "
   "water, sunscreen and sand are all hard on extensions, so sets for Quinns clients are mapped with "
   "retention in mind rather than maximum drama on day one.",
 "local":"The stretch of coast from Quinns Beach north is one of the most-used dog and swimming beaches "
   "in the area &mdash; if you are in the water most days, that is worth mentioning at your consultation.",
 "faqs":[
  ("How far is Quinns Rocks from the Yanchep studio?",
   "About 15 kilometres, roughly seventeen minutes north on Marmion Avenue."),
  ("Will swimming ruin my lash extensions?",
   "It will shorten their life, but it does not ruin them. Keep them dry for the first 24 hours, rinse "
   "with fresh water after the ocean, and brush them through once dry. Regular swimmers usually go to a "
   "two-week refill cycle instead of three."),
  ("Is a lash lift better than extensions if I swim daily?",
   "Often, yes. A lift changes your own lashes rather than attaching anything, so there is nothing for "
   "salt water to loosen. It lasts six to eight weeks with no refills, which suits a lot of Quinns Rocks clients."),
 ],
},
{
 "slug":"ridgewood","name":"Ridgewood","postcode":"6030","km":15.3,"mins":"17",
 "route":"north on Connolly Drive onto Marmion Avenue",
 "anchor":"Ridgewood Park",
 "hero":"photos/brow-2.jpg",
 "intro":"Ridgewood is roughly seventeen minutes from the studio via Connolly Drive and Marmion Avenue. "
   "It sits just inland of the coast between Merriwa and Clarkson, and the drive north is one of the "
   "simpler ones in the corridor &mdash; two roads, no freeway.",
 "angle":"A lot of Ridgewood enquiries start with brows rather than lashes. Brow lamination has quietly "
   "become the most requested single treatment in the studio, largely because it fixes the one thing "
   "makeup cannot: brow hair that will not sit where you want it.",
 "local":"Ridgewood Park is the usual local landmark, and from there it is a straight run north to Yanchep.",
 "faqs":[
  ("How far is the studio from Ridgewood?",
   "About 15 kilometres, or seventeen minutes via Connolly Drive and Marmion Avenue."),
  ("What is brow lamination and how long does it last?",
   "It is a treatment that relaxes and resets the direction your brow hairs grow, so they sit fuller and "
   "brushed-up. It lasts six to eight weeks. Lamination is $70, or $85 with a tint, or $95 with tint and shape."),
  ("Do I need a patch test first?",
   "For anything involving tint or lash adhesive, a patch test is recommended before your first "
   "appointment &mdash; ideally 48 hours ahead. For Ridgewood clients it is usually worth combining the "
   "patch test with another errand rather than making a separate trip."),
 ],
},
{
 "slug":"clarkson","name":"Clarkson","postcode":"6030","km":17.3,"mins":"19",
 "route":"north on Marmion Avenue from Ocean Keys",
 "anchor":"Ocean Keys Shopping Centre",
 "hero":"photos/lash-5.jpg",
 "intro":"Clarkson is about nineteen minutes south of the studio, a straight run up Marmion Avenue from "
   "Ocean Keys. It is the commercial centre of the northern corridor, which means plenty of beauty "
   "options &mdash; and a very different experience to a private studio.",
 "angle":"Clarkson has no shortage of salons. What it does not have much of is one-client-at-a-time. In a "
   "busy centre a two-hour full set often means a technician moving between beds, a rushed consultation, "
   "and a different person next visit. The trade here is nineteen minutes of driving for an appointment "
   "that is genuinely yours.",
 "local":"Ocean Keys is the obvious local landmark and the drive north from there is uncomplicated outside "
   "of school pick-up.",
 "faqs":[
  ("Why drive to Yanchep when Clarkson has salons?",
   "Because of how the appointment runs rather than what is used. One client at a time, the same "
   "technician every visit, a full consultation before anything is applied, and a finish time that is "
   "real. For a two-hour appointment that is usually worth nineteen minutes each way."),
  ("How far is Yanchep from Clarkson?",
   "About 17 kilometres, roughly nineteen minutes north on Marmion Avenue."),
  ("Can I see examples of your work before booking?",
   "Yes &mdash; the gallery on this site and the Instagram page both show real client sets rather than "
   "stock imagery. If you want to see a specific style on a similar eye shape, ask and a relevant "
   "example can be sent through."),
 ],
},
{
 "slug":"mindarie","name":"Mindarie","postcode":"6030","km":17.3,"mins":"19",
 "route":"north on Marmion Avenue from Ocean Drive",
 "anchor":"Mindarie Marina",
 "hero":"photos/lash-2.jpg",
 "intro":"Mindarie is around nineteen minutes from the studio, north along Marmion Avenue from the marina "
   "end of Ocean Drive. It is one of the more established coastal suburbs in the corridor and its clients "
   "generally book with a clear idea of the look they are after.",
 "angle":"Mindarie brings a lot of event bookings &mdash; the marina end of the suburb runs on weddings, "
   "birthdays and long lunches. Event sets need different planning to everyday sets: applied a few days "
   "ahead rather than the morning of, and mapped to photograph well rather than just look good in a mirror.",
 "local":"Mindarie Marina is the landmark most people navigate by, and Marmion Avenue north from there is "
   "a clean run to Yanchep.",
 "faqs":[
  ("How far is the studio from Mindarie?",
   "About 17 kilometres, or nineteen minutes north on Marmion Avenue."),
  ("When should I book lashes before a wedding or event?",
   "Three to five days beforehand is the sweet spot. It gives any shedding time to settle and lets you "
   "get used to them, while still looking freshly done. Booking the morning of an event is the most "
   "common mistake &mdash; there is no room to adjust anything."),
  ("What set photographs best?",
   "Hybrid or volume, usually. Classic sets can read as thin under camera flash, while mega volume can "
   "look heavy in close-up. A hybrid set gives definition that holds up in photos without looking "
   "obviously applied."),
 ],
},
{
 "slug":"banksia-grove","name":"Banksia Grove","postcode":"6031","km":22.0,"mins":"23",
 "route":"north on Wanneroo Road then west via Flynn Drive to Marmion Avenue",
 "anchor":"Banksia Grove Village",
 "hero":"photos/brow-3.jpg",
 "intro":"Banksia Grove is about twenty-three minutes from the studio, running north on Wanneroo Road and "
   "cutting west on Flynn Drive to Marmion Avenue. It is one of the few inland suburbs on this list, and "
   "the drive is a genuinely pleasant one outside peak hour.",
 "angle":"Because the trip is a little longer, Banksia Grove clients usually make it count &mdash; lashes "
   "and brows in the same visit, or a lift and lamination together. The combination pricing exists for "
   "exactly this, and the appointment is planned as one block rather than two.",
 "local":"Banksia Grove Village and Joseph Banks Secondary College are the usual local reference points. "
   "Flynn Drive is the quickest way across to the coast road.",
 "faqs":[
  ("How far is Banksia Grove from the Yanchep studio?",
   "About 22 kilometres, roughly twenty-three minutes via Wanneroo Road and Flynn Drive."),
  ("Is it worth the drive from an inland suburb?",
   "It depends on what you book. For a single brow tint, probably not. For a full set, a lift and "
   "lamination combination, or a standing refill with a technician you trust, Banksia Grove clients "
   "generally say yes &mdash; and tend to book combinations to make one trip do the work of two."),
  ("Can I combine lashes and brows to save a trip?",
   "Yes, and it is recommended for anyone coming from inland. A lash lift and tint with brow lamination "
   "and tint is $160 together rather than $175 separately, and runs about two hours in one sitting."),
 ],
},
{
 "slug":"carramar","name":"Carramar","postcode":"6031","km":22.5,"mins":"24",
 "route":"north on Wanneroo Road then Flynn Drive to Marmion Avenue",
 "anchor":"Carramar Golf Course",
 "hero":"photos/brow-1.jpg",
 "intro":"Carramar is roughly twenty-four minutes from the studio, north on Wanneroo Road and west along "
   "Flynn Drive. It sits at the inland edge of the area the studio serves, and the clients who come from "
   "there generally do so because they want a specific technician rather than the closest chair.",
 "angle":"At this distance nobody drives past three salons by accident. Carramar bookings are almost "
   "entirely word of mouth or returning clients, which means they tend to be longer appointments &mdash; "
   "full sets, combinations, and work that needs someone who already knows the natural lashes they are building on.",
 "local":"Carramar Golf Course and Carramar Village are the local landmarks; Flynn Drive is the fastest "
   "link across to Marmion Avenue and north.",
 "faqs":[
  ("How far is the studio from Carramar?",
   "About 22 kilometres, or twenty-four minutes via Wanneroo Road and Flynn Drive. Carramar is at the "
   "outer edge of the regular catchment."),
  ("Do you take new clients from further out?",
   "Yes. A patch test is recommended 48 hours before a first appointment involving tint or adhesive, so "
   "for clients coming from Carramar it is worth planning that around another trip if possible."),
  ("What is the difference between classic, hybrid and volume?",
   "Classic is one extension per natural lash for a defined, natural finish ($120). Hybrid mixes classic "
   "and volume fans for texture ($140). Volume uses lightweight fans for density and softness ($160). "
   "Which one suits you depends on how many natural lashes you have to work with, which is what the "
   "consultation is for."),
 ],
},
]

# Tier B = covered properly on the hub page, no individual page.
TIER_B = [
 ("Nowergup","6032",10.8,"12"),("Neerabup","6031",19.6,"21"),("Tamala Park","6030",19.7,"21"),
 ("Burns Beach","6028",20.9,"23"),("Kinross","6028",21.0,"23"),("Iluka","6028",21.9,"24"),
 ("Currambine","6028",22.8,"25"),("Connolly","6027",23.3,"25"),("Tapping","6065",23.8,"26"),
 ("Ocean Reef","6027",25.2,"27"),("Joondalup","6027",25.3,"27"),("Ashby","6065",25.9,"28"),
 ("Heathridge","6027",26.8,"29"),("Edgewater","6027",27.0,"29"),("Sinagra","6065",27.1,"29"),
 ("Mullaloo","6027",27.6,"30"),("Wanneroo","6065",27.7,"30"),("Beldon","6027",27.8,"30"),
 ("Craigie","6025",29.0,"31"),("Kallaroo","6025",29.1,"31"),("Hocking","6065",29.4,"32"),
 ("Pearsall","6065",29.5,"32"),("Padbury","6025",30.1,"33"),("Hillarys","6025",30.7,"33"),
 ("Woodvale","6026",31.0,"33"),("Wangara","6065",32.5,"35"),("Kingsley","6026",32.6,"35"),
 ("Sorrento","6020",32.8,"35"),("Duncraig","6023",34.0,"36"),("Greenwood","6024",34.5,"37"),
 ("Marmion","6020",34.6,"37"),("Madeley","6065",35.1,"37"),("Darch","6065",35.3,"38"),
 ("Landsdale","6065",35.4,"38"),("Watermans Bay","6020",35.5,"38"),("Hamersley","6022",35.8,"38"),
 ("Warwick","6024",36.5,"39"),("North Beach","6020",36.5,"39"),("Carine","6020",36.8,"39"),
 ("Alexander Heights","6064",37.4,"40"),("Marangaroo","6064",37.5,"40"),("Girrawheen","6064",37.7,"40"),
 ("Trigg","6029",37.7,"40"),("Karrinyup","6018",38.3,"41"),("Koondoola","6064",39.4,"42"),
 ("Pinjar","6078",20.9,"25"),("Gnangara","6077",32.7,"36"),("Muchea","6501",31.9,"34"),
 ("Bullsbrook","6084",38.1,"41"),
]
