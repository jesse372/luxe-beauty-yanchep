// Turns the two card HTML files into review-cards-a4.pdf and review-card.png.
// Needs headless Chrome on a debugging port: ~/JesseOS/workspace/skills/browser-probe/scripts/launch.sh card 9377
import { connect } from "/Users/jessechance/JesseOS/workspace/skills/browser-probe/scripts/cdp.mjs";
import fs from "fs"; import path from "path"; import { fileURLToPath } from "url";
const here = path.dirname(fileURLToPath(import.meta.url));
const port = Number(process.argv[2] || 9377);
let c = await connect({ port, device: null });
await c.goto("file://" + path.join(here, "review-cards-a4.html"), 1500);
await c.ev("document.fonts.ready.then(()=>true)");
const pdf = await c.send("Page.printToPDF", { printBackground: true, preferCSSPageSize: true, marginTop: 0, marginBottom: 0, marginLeft: 0, marginRight: 0 });
fs.writeFileSync(path.join(here, "review-cards-a4.pdf"), Buffer.from(pdf.result.data, "base64"));
c.close();
// a picture of the A4 sheet, only so verify.py can scan the printed QR codes
c = await connect({ port, device: { width: 794, height: 1123, scale: 2 } });
await c.goto("file://" + path.join(here, "review-cards-a4.html"), 1200);
await c.shot("/tmp/review-cards-a4-check.png", 300);
c.close();
// 108mm x 135mm at 96dpi is 408 x 510 css px; scale 2.647 -> 1080 x 1350
c = await connect({ port, device: { width: 408, height: 510, scale: 1080 / 408 } });
await c.goto("file://" + path.join(here, "review-card.html"), 1500);
await c.ev("document.fonts.ready.then(()=>true)");
await c.shot(path.join(here, "review-card.png"), 400);
c.close();
console.log("  wrote review-cards-a4.pdf and review-card.png");
