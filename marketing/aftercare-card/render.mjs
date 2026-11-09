// aftercare-cards-a4.html -> aftercare-cards-a4.pdf, then a check picture of the back page for verify.py.
// Needs headless Chrome: ~/JesseOS/workspace/skills/browser-probe/scripts/launch.sh card 9377
import { connect } from "/Users/jessechance/JesseOS/workspace/skills/browser-probe/scripts/cdp.mjs";
import fs from "fs"; import path from "path"; import { fileURLToPath } from "url";
const here = path.dirname(fileURLToPath(import.meta.url));
const port = Number(process.argv[2] || 9377);
let c = await connect({ port, device: { width: 794, height: 1123, scale: 2 } });
await c.goto("file://" + path.join(here, "aftercare-cards-a4.html"), 1200);
await c.ev("document.fonts.ready.then(()=>true)");
const fit = await c.ev(`[...document.querySelectorAll('.card')].some(e=>e.scrollHeight>e.clientHeight+1||e.scrollWidth>e.clientWidth+1)`);
if (fit) { console.log("  TEXT DOES NOT FIT ON A CARD"); process.exit(1); }
await c.shot("/tmp/aftercare-front-check.png", 300);
await c.ev(`scrollTo({top:document.querySelectorAll('.sheet')[1].offsetTop,behavior:'instant'})`);
await c.shot("/tmp/aftercare-back-check.png", 400);
c.close();
c = await connect({ port, device: null });
await c.goto("file://" + path.join(here, "aftercare-cards-a4.html"), 1200);
await c.ev("document.fonts.ready.then(()=>true)");
const pdf = await c.send("Page.printToPDF", { printBackground: true, preferCSSPageSize: true, marginTop: 0, marginBottom: 0, marginLeft: 0, marginRight: 0 });
fs.writeFileSync(path.join(here, "aftercare-cards-a4.pdf"), Buffer.from(pdf.result.data, "base64"));
c.close();
console.log("  wrote aftercare-cards-a4.pdf");
