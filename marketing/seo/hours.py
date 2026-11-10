# -*- coding: utf-8 -*-
"""
THE opening hours. Source of truth = Bec's Square account (Jesse, 2026-11-10: "Square is the
real times"). Every place the site states hours reads from here: contact page, homepage FAQ,
structured data on every page, llms.txt. Change them here, rebuild, and update Google
Business Profile by hand to match (it still said "opens 8am" on 2026-11-09).
"""
# (day, opens, closes) in 24h; a day missing from the list is closed
HOURS = [
    ("Monday",    "09:00", "21:00"),
    ("Tuesday",   "09:00", "21:00"),
    ("Wednesday", "09:00", "18:00"),
    ("Thursday",  "10:30", "19:30"),
    ("Friday",    "09:00", "17:00"),
    ("Saturday",  "09:00", "13:00"),
]
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def ampm(t):
    h, m = int(t[:2]), t[3:]
    suffix = "am" if h < 12 else "pm"
    h = h % 12 or 12
    return "%d%s%s" % (h, "" if m == "00" else ":" + m, suffix)

def schema():
    """openingHoursSpecification: consecutive days with the same times are grouped."""
    out = []
    for day, o, c in HOURS:
        if out and out[-1]["opens"] == o and out[-1]["closes"] == c and DAYS.index(day) == DAYS.index(out[-1]["dayOfWeek"][-1]) + 1:
            out[-1]["dayOfWeek"].append(day)
        else:
            out.append({"@type": "OpeningHoursSpecification", "dayOfWeek": [day], "opens": o, "closes": c})
    return out

def rows():
    """[(label, '9am - 9pm')] for a table, grouping consecutive identical days; closed days last."""
    out = []
    for spec in schema():
        d = spec["dayOfWeek"]
        label = d[0] if len(d) == 1 else "%s to %s" % (d[0], d[-1]) if len(d) > 2 else "%s and %s" % (d[0], d[1])
        out.append((label, "%s to %s" % (ampm(spec["opens"]), ampm(spec["closes"]))))
    closed = [d for d in DAYS if d not in [h[0] for h in HOURS]]
    if closed:
        out.append((" and ".join(closed), "Closed"))
    return out

def sentence():
    """e.g. 'Monday and Tuesday 9am to 9pm, Wednesday 9am to 6pm, ... Closed Sunday.'"""
    open_days = ", ".join("%s %s" % (l, t) for l, t in rows() if t != "Closed")
    closed = [l for l, t in rows() if t == "Closed"]
    return open_days + "." + (" Closed %s." % closed[0] if closed else "")

def latest_close():
    return max(ampm(c) for _, _, c in HOURS)

if __name__ == "__main__":
    print(sentence()); print(rows()); print(schema())
