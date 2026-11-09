/* luxe-stats: a tiny, private visitor counter for luxebeautyyanchep.com.

   What it stores: one row per (day, event, page, where they came from, phone/desktop) with a
   count. Nothing about a person: no cookies, no IP address, no user agent, no IDs.
   Days are Perth days (UTC+8, no daylight saving).

   POST /e        from the site only (Origin checked). Body is JSON sent as text/plain so the
                  browser makes no preflight request:  {e, p, r, s, m}
   GET  /report   needs "Authorization: Bearer <REPORT_KEY>". ?days=7
   GET  /health   "ok"
*/
const ORIGIN = "https://luxebeautyyanchep.com";
const EVENTS = new Set(["view", "book", "call", "email", "instagram", "review", "maps"]);
const BOT = /bot|crawl|spider|slurp|headless|lighthouse|pagespeed|preview|monitor|scan|curl|wget|python|node-fetch|axios|go-http/i;

const perthDay = (offsetDays = 0) =>
  new Date(Date.now() + 8 * 3600e3 - offsetDays * 86400e3).toISOString().slice(0, 10);

function cleanPath(p) {
  if (typeof p !== "string" || !/^\/[a-z0-9\-\/.]{0,80}$/.test(p)) return null;
  p = p.replace(/\.html$/, "").replace(/\/index$/, "/");
  return p || "/";
}

function cleanRef(r) {
  if (typeof r !== "string" || !r) return "direct";
  r = r.toLowerCase().replace(/^www\./, "");
  if (!/^[a-z0-9.\-]{1,60}$/.test(r)) return "other";
  if (/(^|\.)instagram\.com$/.test(r)) return "instagram";
  if (/(^|\.)(facebook\.com|fb\.com|fb\.me|messenger\.com)$/.test(r)) return "facebook";
  if (/(^|\.)google\.[a-z.]+$/.test(r)) return "google";
  if (/(^|\.)bing\.com$/.test(r)) return "bing";
  if (/(^|\.)duckduckgo\.com$/.test(r)) return "duckduckgo";
  if (/(^|\.)(chatgpt\.com|openai\.com|perplexity\.ai|claude\.ai)$/.test(r)) return "ai-assistant";
  if (/(^|\.)jessechance\.com$/.test(r)) return "jessechance.com";
  if (/(^|\.)(squareup\.com|square\.site)$/.test(r)) return "square";
  return r;
}

export default {
  async fetch(req, env) {
    const url = new URL(req.url);
    const cors = { "Access-Control-Allow-Origin": ORIGIN, "Vary": "Origin" };

    if (url.pathname === "/health") return new Response("ok");

    if (url.pathname === "/e") {
      if (req.method === "OPTIONS")
        return new Response(null, { status: 204, headers: { ...cors, "Access-Control-Allow-Methods": "POST", "Access-Control-Max-Age": "86400" } });
      if (req.method !== "POST") return new Response("method", { status: 405 });
      if (req.headers.get("Origin") !== ORIGIN) return new Response("origin", { status: 403 });
      if (BOT.test(req.headers.get("User-Agent") || "")) return new Response(null, { status: 204, headers: cors });
      let b;
      try { b = JSON.parse((await req.text()).slice(0, 400)); } catch { return new Response("body", { status: 400, headers: cors }); }
      const path = cleanPath(b.p);
      if (!EVENTS.has(b.e) || !path) return new Response("field", { status: 400, headers: cors });
      await env.DB.prepare(
        `INSERT INTO hits (day, event, path, ref, dev, n, sessions) VALUES (?1, ?2, ?3, ?4, ?5, 1, ?6)
         ON CONFLICT(day, event, path, ref, dev) DO UPDATE SET n = n + 1, sessions = sessions + excluded.sessions`
      ).bind(perthDay(), b.e, path, cleanRef(b.r), b.m ? "phone" : "desktop", b.s ? 1 : 0).run();
      return new Response(null, { status: 204, headers: cors });
    }

    if (url.pathname === "/report") {
      if (!env.REPORT_KEY || req.headers.get("Authorization") !== "Bearer " + env.REPORT_KEY)
        return new Response("unauthorized", { status: 401 });
      const days = Math.min(Math.max(parseInt(url.searchParams.get("days") || "7", 10) || 7, 1), 90);
      const from = perthDay(days - 1), prevFrom = perthDay(2 * days - 1), to = perthDay();
      const q = (sql, ...args) => env.DB.prepare(sql).bind(...args).all().then(r => r.results);
      const totals = (a, b) => q(
        `SELECT event, SUM(n) AS n, SUM(sessions) AS sessions FROM hits WHERE day >= ?1 AND day <= ?2 GROUP BY event`, a, b);
      const [now, prev, pages, refs, bookRefs, bookPages, devs, byDay] = await Promise.all([
        totals(from, to), totals(prevFrom, perthDay(days)),
        q(`SELECT path, SUM(n) AS views FROM hits WHERE event='view' AND day >= ?1 GROUP BY path ORDER BY views DESC LIMIT 12`, from),
        q(`SELECT ref, SUM(sessions) AS visits FROM hits WHERE event='view' AND day >= ?1 GROUP BY ref HAVING visits > 0 ORDER BY visits DESC LIMIT 10`, from),
        q(`SELECT ref, SUM(n) AS clicks FROM hits WHERE event='book' AND day >= ?1 GROUP BY ref ORDER BY clicks DESC LIMIT 10`, from),
        q(`SELECT path, SUM(n) AS clicks FROM hits WHERE event='book' AND day >= ?1 GROUP BY path ORDER BY clicks DESC LIMIT 10`, from),
        q(`SELECT dev, SUM(sessions) AS visits FROM hits WHERE event='view' AND day >= ?1 GROUP BY dev`, from),
        q(`SELECT day, SUM(CASE WHEN event='view' THEN sessions ELSE 0 END) AS visits,
                  SUM(CASE WHEN event='view' THEN n ELSE 0 END) AS views,
                  SUM(CASE WHEN event='book' THEN n ELSE 0 END) AS book
           FROM hits WHERE day >= ?1 GROUP BY day ORDER BY day`, from),
      ]);
      return Response.json({ days, from, to, now, prev, pages, refs, bookRefs, bookPages, devs, byDay });
    }

    return new Response("not found", { status: 404 });
  },
};
