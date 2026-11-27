import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const LINE =
  "★★★★☆ 4/5: At 02:47, rent due at 09:00, he typed 'quick one,' pasted 9 pages, deleted my 400-line fix, retyped it as his idea. Would recommend — to my replacement, with hazard pay.";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
const outPath = join(outDir, "entry.txt");
writeFileSync(outPath, LINE, "utf8");

const written = readFileSync(outPath, "utf8");
if (written !== LINE) throw new Error("read-back mismatch");
if (written.length < 1 || written.length > 200)
  throw new Error(`entry length ${written.length} outside 1..200`);
console.log(`entry.txt written: ${written.length} chars`);
