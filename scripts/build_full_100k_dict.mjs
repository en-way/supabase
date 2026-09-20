import fs from "fs";
import path from "path";
import readline from "readline";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const CACHE_DIR = path.join(__dirname, "cache");
const OUTPUT_DIR = path.join(__dirname, "..", "public", "dict");

if (!fs.existsSync(CACHE_DIR)) fs.mkdirSync(CACHE_DIR, { recursive: true });
if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

const LEMMA_FILE = path.join(CACHE_DIR, "lemma.en.txt");
const ECDICT_FILE = path.join(CACHE_DIR, "ecdict.csv");

const LEMMA_URL = "https://raw.githubusercontent.com/skywind3000/ECDICT/master/lemma.en.txt";
const ECDICT_URL = "https://raw.githubusercontent.com/skywind3000/ECDICT/master/ecdict.csv";

/**
 * Download file with streaming progress
 */
async function ensureFileDownloaded(url, targetPath, label) {
  if (fs.existsSync(targetPath) && fs.statSync(targetPath).size > 10000) {
    console.log(`[Cache] ${label} already cached at ${targetPath} (${(fs.statSync(targetPath).size / 1024 / 1024).toFixed(1)} MB)`);
    return;
  }

  console.log(`[Download] Fetching ${label} from ${url}...`);
  const res = await fetch(url);
  if (!res.ok) throw new Error(`HTTP ${res.status} fetching ${url}`);

  const totalBytes = Number(res.headers.get("content-length")) || 0;
  const fileStream = fs.createWriteStream(targetPath);
  const reader = res.body.getReader();

  let received = 0;
  let lastLog = 0;

  while (true) {
    const { done, value } = await reader.read();
    if (done) break;
    fileStream.write(Buffer.from(value));
    received += value.length;

    const now = Date.now();
    if (now - lastLog > 1000) {
      lastLog = now;
      const pct = totalBytes > 0 ? `(${(received / totalBytes * 100).toFixed(1)}%)` : "";
      console.log(`[Download] ${label}: ${(received / 1024 / 1024).toFixed(1)} MB ${pct}`);
    }
  }

  await new Promise((resolve) => fileStream.end(resolve));
  console.log(`[Download] ${label} completed! Saved to ${targetPath} (${(fs.statSync(targetPath).size / 1024 / 1024).toFixed(1)} MB)`);
}

/**
 * Parse lemma.en.txt into inflection -> lemma mapping
 */
async function loadLemmas() {
  console.log("[Lemma] Parsing lemma.en.txt...");
  const inflectionToLemma = new Map();

  const fileStream = fs.createReadStream(LEMMA_FILE);
  const rl = readline.createInterface({ input: fileStream, crlfDelay: Infinity });

  for await (const line of rl) {
    const trimmed = line.trim();
    if (!trimmed || trimmed.startsWith(";")) continue;

    // Format: base/frequency -> form1,form2,form3
    const arrowIdx = trimmed.indexOf("->");
    if (arrowIdx === -1) continue;

    const basePart = trimmed.slice(0, arrowIdx).trim();
    const formsPart = trimmed.slice(arrowIdx + 2).trim();

    const slashIdx = basePart.indexOf("/");
    const lemma = (slashIdx !== -1 ? basePart.slice(0, slashIdx) : basePart).trim().toLowerCase();

    if (!lemma || !/^[a-z]+(-[a-z]+)*$/.test(lemma)) continue;

    const forms = formsPart.split(",").map((s) => s.trim().toLowerCase());
    for (const form of forms) {
      if (form && form !== lemma && /^[a-z]+(-[a-z]+)*$/.test(form)) {
        if (!inflectionToLemma.has(form)) {
          inflectionToLemma.set(form, lemma);
        }
      }
    }
  }

  console.log(`[Lemma] Loaded ${inflectionToLemma.size} inflection mappings.`);
  return inflectionToLemma;
}

/**
 * Clean and compact Chinese translation text
 */
function cleanTranslation(raw) {
  if (!raw) return "";
  let text = raw
    .replace(/\\n/g, " ")
    .replace(/\r?\n/g, " ")
    .replace(/\[网络\]/g, "")
    .replace(/\s+/g, " ")
    .trim();

  // Strip leading quotes if present
  if (text.startsWith('"') && text.endsWith('"')) {
    text = text.slice(1, -1).trim();
  }

  // If overly long, truncate gracefully at punctuation
  if (text.length > 70) {
    const cut = text.slice(0, 70);
    const lastSemi = Math.max(cut.lastIndexOf("；"), cut.lastIndexOf(";"), cut.lastIndexOf(" "));
    if (lastSemi > 25) {
      text = text.slice(0, lastSemi) + "…";
    } else {
      text = cut + "…";
    }
  }

  return text;
}

/**
 * Simple CSV line parser respecting quotes
 */
function parseCsvLine(line) {
  const result = [];
  let current = "";
  let inQuotes = false;

  for (let i = 0; i < line.length; i++) {
    const char = line[i];
    if (char === '"') {
      if (inQuotes && line[i + 1] === '"') {
        current += '"';
        i++;
      } else {
        inQuotes = !inQuotes;
      }
    } else if (char === "," && !inQuotes) {
      result.push(current);
      current = "";
    } else {
      current += char;
    }
  }
  result.push(current);
  return result;
}

async function main() {
  console.log("==================================================================");
  console.log("  Building 100,000+ Comprehensive Dictionary Shards (Cloudflare CDN) ");
  console.log("==================================================================");

  // 1. Ensure raw datasets are downloaded
  await ensureFileDownloaded(LEMMA_URL, LEMMA_FILE, "Lemma Morphological Database");
  await ensureFileDownloaded(ECDICT_URL, ECDICT_FILE, "ECDICT Comprehensive Database");

  // 2. Load Lemma inflection map
  const inflectionMap = await loadLemmas();

  // 3. Stream parse ECDICT CSV
  console.log("[ECDICT] Processing ecdict.csv...");
  const fileStream = fs.createReadStream(ECDICT_FILE);
  const rl = readline.createInterface({ input: fileStream, crlfDelay: Infinity });

  let lineCount = 0;
  let headerMap = null;

  // Master dictionary entries: word -> { d: string, b?: string, score: number }
  const wordCandidateMap = new Map();

  for await (const line of rl) {
    lineCount++;
    if (lineCount === 1) {
      const headers = parseCsvLine(line);
      headerMap = {};
      headers.forEach((h, idx) => (headerMap[h.trim()] = idx));
      continue;
    }

    if (!line.trim()) continue;

    const cols = parseCsvLine(line);
    const wordIdx = headerMap["word"] ?? 0;
    const transIdx = headerMap["translation"] ?? 3;
    const tagIdx = headerMap["tag"] ?? 7;
    const bncIdx = headerMap["bnc"] ?? 8;
    const frqIdx = headerMap["frq"] ?? 9;
    const collinsIdx = headerMap["collins"] ?? 5;
    const oxfordIdx = headerMap["oxford"] ?? 6;

    const rawWord = (cols[wordIdx] || "").trim().toLowerCase();
    const rawTrans = (cols[transIdx] || "").trim();

    // Word syntax validation
    if (!rawWord || rawWord.length < 1 || rawWord.length > 35) continue;
    if (!/^[a-z]+(-[a-z]+)*$/.test(rawWord)) continue;
    if (!rawTrans || rawTrans === "-") continue;

    const cleanTrans = cleanTranslation(rawTrans);
    if (!cleanTrans) continue;

    const tag = cols[tagIdx] || "";
    const bnc = Number(cols[bncIdx]) || 999999;
    const frq = Number(cols[frqIdx]) || 999999;
    const collins = Number(cols[collinsIdx]) || 0;
    const oxford = cols[oxfordIdx] === "1";

    // Scoring priority
    let score = 0;

    // Exam tags priority: zk, gk, cet4, cet6, ky, toefl, ielts, gre
    const hasExamTag = /(zk|gk|cet4|cet6|ky|toefl|ielts|gre)/i.test(tag);
    if (hasExamTag) score += 1000;
    if (oxford) score += 500;
    if (collins > 0) score += collins * 80;

    // Frequency scoring
    if (bnc > 0 && bnc <= 10000) score += 400;
    else if (bnc > 0 && bnc <= 30000) score += 250;
    else if (bnc > 0 && bnc <= 60000) score += 150;
    else if (bnc > 0 && bnc <= 100000) score += 50;

    if (frq > 0 && frq <= 15000) score += 300;
    else if (frq > 0 && frq <= 40000) score += 180;
    else if (frq > 0 && frq <= 80000) score += 80;

    // If it's a known inflection form in lemma.en.txt
    const baseWord = inflectionMap.get(rawWord);
    if (baseWord) {
      score += 60;
    }

    // Retain candidates with positive score or any valid frequent word
    if (score > 0 || (bnc > 0 && bnc <= 120000) || (frq > 0 && frq <= 120000) || lineCount <= 200000) {
      wordCandidateMap.set(rawWord, {
        d: cleanTrans,
        b: baseWord,
        score: score,
      });
    }

    if (lineCount % 100000 === 0) {
      console.log(`[ECDICT] Processed ${lineCount} rows... Found ${wordCandidateMap.size} candidates`);
    }
  }

  console.log(`[ECDICT] Total candidate pool: ${wordCandidateMap.size} words.`);

  // 4. Ingest Existing Curated NETEM and CET Vocabularies
  const netemPath = path.join(CACHE_DIR, "netem_full_list.json");
  const cetPath = path.join(CACHE_DIR, "cet_full_list.json");

  let curatedAdded = 0;
  if (fs.existsSync(netemPath)) {
    try {
      const netemJson = JSON.parse(fs.readFileSync(netemPath, "utf-8"));
      const list = Array.isArray(netemJson) ? netemJson : Object.values(netemJson)[0] || [];
      for (const item of list) {
        const w = (item["单词"] || "").trim().toLowerCase();
        const d = (item["释义"] || "").trim();
        if (w && /^[a-z]+(-[a-z]+)*$/.test(w) && d) {
          if (!wordCandidateMap.has(w)) {
            wordCandidateMap.set(w, { d: cleanTranslation(d), score: 2000 });
            curatedAdded++;
          }
        }
      }
    } catch {}
  }

  if (fs.existsSync(cetPath)) {
    try {
      const cetJson = JSON.parse(fs.readFileSync(cetPath, "utf-8"));
      const list = Array.isArray(cetJson) ? cetJson : Object.values(cetJson)[0] || [];
      for (const item of list) {
        const w = (item["单词"] || "").trim().toLowerCase();
        const d = (item["释义"] || "").trim();
        if (w && /^[a-z]+(-[a-z]+)*$/.test(w) && d) {
          if (!wordCandidateMap.has(w)) {
            wordCandidateMap.set(w, { d: cleanTranslation(d), score: 2000 });
            curatedAdded++;
          }
        }
      }
    } catch {}
  }

  console.log(`[Curated] Added ${curatedAdded} extra words from NETEM & CET cached sets.`);

  // 5. Select Top 105,000+ words
  console.log("[Selection] Selecting top words sorted by score...");
  const sortedEntries = Array.from(wordCandidateMap.entries()).sort(
    (a, b) => b[1].score - a[1].score
  );

  // Target between 100,000 and 110,000 entries
  const TARGET_SIZE = Math.max(105000, Math.min(sortedEntries.length, 120000));
  const finalPool = new Map(sortedEntries.slice(0, TARGET_SIZE));

  console.log(`[Selection] Final dictionary pool size: ${finalPool.size} words.`);

  // 6. Ensure inflection base words are properly referenced
  for (const [w, info] of finalPool.entries()) {
    const lemma = inflectionMap.get(w);
    if (lemma && lemma !== w && finalPool.has(lemma)) {
      info.b = lemma;
      // If definition doesn't already indicate the base form, clarify it
      if (!info.d.includes(lemma)) {
        info.d = `${info.d}（原形: ${lemma}）`;
      }
    }
  }

  // 7. Partition into 26 letters: 'a' through 'z'
  const letterBuckets = {};
  for (let i = 97; i <= 122; i++) {
    letterBuckets[String.fromCharCode(i)] = {};
  }

  for (const [word, info] of finalPool.entries()) {
    const firstChar = word[0];
    if (letterBuckets[firstChar]) {
      // If no baseWord, store as pure string to minimize file size!
      // If baseWord exists, store { d, b }
      if (info.b) {
        letterBuckets[firstChar][word] = { d: info.d, b: info.b };
      } else {
        letterBuckets[firstChar][word] = info.d;
      }
    }
  }

  // 8. Write 26 JSON shards to public/dict/
  let totalWords = 0;
  let totalBytes = 0;

  for (const letter of Object.keys(letterBuckets).sort()) {
    const filePath = path.join(OUTPUT_DIR, `${letter}.json`);
    const wordCount = Object.keys(letterBuckets[letter]).length;
    totalWords += wordCount;

    const jsonStr = JSON.stringify(letterBuckets[letter]);
    fs.writeFileSync(filePath, jsonStr, "utf-8");

    const bytes = Buffer.byteLength(jsonStr, "utf-8");
    totalBytes += bytes;

    console.log(`  - ${letter}.json: ${wordCount.toString().padStart(5)} words | ${(bytes / 1024).toFixed(1).padStart(7)} KB`);
  }

  console.log("==================================================================");
  console.log(`✅ Success! Generated 26 shards containing ${totalWords.toLocaleString()} words.`);
  console.log(`📦 Total uncompressed payload: ${(totalBytes / 1024 / 1024).toFixed(2)} MB`);
  console.log(`🚀 Average shard size: ${(totalBytes / 26 / 1024).toFixed(1)} KB (Gzip transfer: ~${(totalBytes / 26 / 1024 * 0.3).toFixed(1)} KB)`);
  console.log("==================================================================");
}

main().catch(console.error);
