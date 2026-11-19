import fs from "fs";
import path from "path";
import crypto from "crypto";
import { fileURLToPath } from "url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const dataDir = path.join(__dirname, "..", "public", "data");
const examsDir = path.join(dataDir, "exams");
const versionFile = path.join(dataDir, "version.json");

if (!fs.existsSync(dataDir)) {
  fs.mkdirSync(dataDir, { recursive: true });
}

let hash = crypto.createHash("md5");
let examCount = 0;

if (fs.existsSync(examsDir)) {
  const files = fs.readdirSync(examsDir).filter(f => f.endsWith(".json")).sort();
  examCount = files.length;
  for (const f of files) {
    const content = fs.readFileSync(path.join(examsDir, f));
    hash.update(f);
    hash.update(content);
  }
}

// Include exams.json and categories.json in hash calculation
const examsListFile = path.join(dataDir, "exams.json");
if (fs.existsSync(examsListFile)) {
  hash.update(fs.readFileSync(examsListFile));
}

const categoriesFile = path.join(dataDir, "categories.json");
if (fs.existsSync(categoriesFile)) {
  hash.update(fs.readFileSync(categoriesFile));
}

const nextVersion = hash.digest("hex").slice(0, 12);
let existing = null;
if (fs.existsSync(versionFile)) {
  try {
    existing = JSON.parse(fs.readFileSync(versionFile, "utf-8"));
  } catch {
    existing = null;
  }
}

if (
  existing &&
  existing.version === nextVersion &&
  existing.examCount === examCount &&
  typeof existing.buildTime === "string"
) {
  console.log("✅ Static version unchanged:", existing);
} else {
  const versionInfo = {
    version: nextVersion,
    buildTime: new Date().toISOString(),
    examCount,
  };
  fs.writeFileSync(versionFile, JSON.stringify(versionInfo, null, 2), "utf-8");
  console.log("✅ Generated public/data/version.json:", versionInfo);
}
