// build/*.html -> posts/*.png at 1080 x 1350.
// Needs headless Chrome: ~/JesseOS/workspace/skills/browser-probe/scripts/launch.sh tiles 9377
import { connect } from "/Users/jessechance/JesseOS/workspace/skills/browser-probe/scripts/cdp.mjs";
import fs from "fs"; import path from "path"; import { fileURLToPath } from "url";
const here = path.dirname(fileURLToPath(import.meta.url));
fs.mkdirSync(path.join(here, "posts"), { recursive: true });
const c = await connect({ port: Number(process.argv[2] || 9377), device: { width: 1080, height: 1350, scale: 1 } });
let over = 0;
for (const f of fs.readdirSync(path.join(here, "build")).filter(f => f.endsWith(".html")).sort()) {
  await c.goto("file://" + path.join(here, "build", f), 500);
  await c.ev("document.fonts.ready.then(()=>true)");
  // text that does not fit would be clipped silently, so measure it
  const fit = await c.ev(`(()=>{const m=document.querySelector('.mid');return {inner:m.scrollHeight, box:m.clientHeight, wide:[...document.querySelectorAll('.mid *')].some(e=>e.scrollWidth>e.clientWidth+2)}})()`);
  if (fit.inner > fit.box + 2 || fit.wide) { over++; console.log("  DOES NOT FIT:", f, JSON.stringify(fit)); }
  await c.shot(path.join(here, "posts", f.replace(".html", ".png")), 150);
}
c.close();
console.log(over ? `  ${over} tile(s) overflow - fix before using` : "  all tiles fit; wrote posts/*.png");
process.exit(over ? 1 : 0);
