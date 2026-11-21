export interface DictEntry {
  word: string;
  phonetic?: string;
  pos?: string; // n., v., adj., adv.
  definition: string; // Chinese translation
  enDefinition?: string; // English definition
  baseWord?: string; // Morphological base word if derived
  audioUrl?: string; // Default audio (US)
  usAudioUrl?: string; // US pronunciation audio
  ukAudioUrl?: string; // UK pronunciation audio
  isOnline?: boolean;
}

export interface FormattedDefinitionLine {
  pos?: string;
  meaning: string;
}

const NICHE_DOMAIN_TAG_RE =
  /\[(?:计|计算机|医|医学|外科|内科|解剖|生化|药|法|法律|化|化学|化工|无化|有化|机|机械|机械学|电|电子|电学|电脑|电讯|建|建筑学|数|数学|物|物理学|天|天文学|地|地理|地质|地物|矿|矿业|矿物|冶|冶金|农|农学|林|植|植物|植物学|动|动物|生物|生物学|生理|生态|菌|虫|昆|昆虫|鱼|鸟|鸟类|航|航海|航空|船|造船|铁路|军|军事|体|体育|乐|音乐|心|心理|哲|宗教|神学|宗|经|经管|财|金融|会计|统计|印刷|摄影|纺|戏|戏剧|网球|高尔夫|棒球|冰球|赛马)\]/g;

const POS_SPLIT_RE =
  /(?:^|(?<=[\s;；,，\u4e00-\u9fff]))((?:n|v|vt|vi|a|adj|adv|prep|conj|pron|art|num|int|interj|aux|modal|pl|abbr)\.)(?=\s|$|[\u4e00-\u9fff\[（(])/gi;

const POS_LOOKAHEAD_STR =
  "(?:n|v|vt|vi|a|adj|adv|prep|conj|pron|art|num|int|interj|aux|modal|pl|abbr)\\.";

function cleanAndSplitSingleDefinition(rawSegment: string): FormattedDefinitionLine[] {
  const cleaned = rawSegment
    .replace(/\\r\\n|\\r|\\n/g, " ")
    .replace(/[\r\n]+/g, " ")
    .replace(/\s+/g, " ")
    .replace(/\s*[（(]原形[:：]\s*[a-zA-Z-]+[）)]\s*$/g, "")
    .trim();

  if (!cleaned) return [];

  // Remove niche domain-tagged sub-segments up to the next POS tag, semicolon, or end
  const domainSegmentRe = new RegExp(
    `${NICHE_DOMAIN_TAG_RE.source}[^;；]*?(?=\\s+${POS_LOOKAHEAD_STR}|[;；]|$)`,
    "gi"
  );
  let filtered = cleaned
    .replace(domainSegmentRe, "")
    .replace(/[;；,\s]+$/g, "")
    .replace(/\s+/g, " ")
    .trim();

  // Drop trailing orphaned POS marker left behind after stripping its domain segment (e.g. "art.")
  const trailingOrphanPosRe = new RegExp(`(?:^|\\s)${POS_LOOKAHEAD_STR}$`, "i");
  filtered = filtered
    .replace(trailingOrphanPosRe, "")
    .replace(/[;；,\s]+$/g, "")
    .trim();

  const source = filtered || cleaned;

  const matches = Array.from(source.matchAll(POS_SPLIT_RE));
  if (matches.length === 0) {
    return [{ meaning: source }];
  }

  const lines: FormattedDefinitionLine[] = [];
  const firstIdx = matches[0].index ?? 0;
  const leading = source.slice(0, firstIdx).replace(/[;；\s]+$/g, "").trim();
  if (leading) {
    lines.push({ meaning: leading });
  }

  for (let i = 0; i < matches.length; i++) {
    const m = matches[i];
    const pos = m[1].toLowerCase();
    const start = (m.index ?? 0) + m[0].length;
    const end = i + 1 < matches.length ? (matches[i + 1].index ?? source.length) : source.length;
    const meaning = source.slice(start, end).replace(/^[;；,\s]+|[;；,\s]+$/g, "").trim();
    if (meaning) {
      lines.push({ pos, meaning });
    }
  }

  return lines.length > 0 ? lines : [{ meaning: source }];
}

/**
 * Clean raw offline dictionary strings and split by POS markers or compound word parts.
 */
export function parseFormattedDefinition(raw: string): FormattedDefinitionLine[] {
  if (!raw || !raw.trim()) return [];

  // Handle multi-line compound word definitions (e.g. "high：...\nvolume：...")
  if (raw.includes("\n")) {
    const rawLines = raw
      .split(/\n+/)
      .map((l) => l.trim())
      .filter(Boolean);
    const compoundLines: FormattedDefinitionLine[] = [];
    for (const line of rawLines) {
      const colonMatch = line.match(/^([a-zA-Z-]+)\s*[：:]\s*(.+)$/);
      if (colonMatch) {
        const partWord = colonMatch[1];
        const partLines = cleanAndSplitSingleDefinition(colonMatch[2]);
        const joinedMeaning = partLines
          .map((pl) => (pl.pos ? `${pl.pos} ${pl.meaning}` : pl.meaning))
          .join("；");
        if (joinedMeaning) {
          compoundLines.push({ pos: partWord, meaning: joinedMeaning });
        }
      } else {
        compoundLines.push(...cleanAndSplitSingleDefinition(line));
      }
    }
    if (compoundLines.length > 0) return compoundLines;
  }

  return cleanAndSplitSingleDefinition(raw);
}

export type RawDictValue = string | { d: string; b?: string; p?: string; pos?: string };

export function parseRawItem(raw: RawDictValue): { d: string; b?: string; p?: string; pos?: string } {
  if (typeof raw === "string") {
    return { d: raw };
  }
  return raw;
}

// Lightweight LRU cache + persistent offline CacheStorage bucket
const MAX_RESOLVED_WORDS = 500;
const MAX_LOADED_PACKS = 8;
const DICT_CACHE_NAME = "enway-dict-v1";

const resolvedWordCache = new Map<string, DictEntry>();
const loadedLetterPacks = new Map<string, Record<string, RawDictValue>>();
const pendingLetterFetches: Record<string, Promise<Record<string, RawDictValue> | null> | undefined> = {};

function hasCacheStorage(): boolean {
  return typeof window !== "undefined" && "caches" in window;
}

async function readDictPackFromCache(url: string): Promise<Record<string, RawDictValue> | null> {
  if (!hasCacheStorage()) return null;
  try {
    const cache = await caches.open(DICT_CACHE_NAME);
    const cachedRes = await cache.match(url);
    if (!cachedRes || !cachedRes.ok) return null;
    const data: unknown = await cachedRes.json();
    if (!data || typeof data !== "object" || Array.isArray(data)) {
      cache.delete(url).catch(() => {});
      return null;
    }
    return data as Record<string, RawDictValue>;
  } catch {
    try {
      const cache = await caches.open(DICT_CACHE_NAME);
      cache.delete(url).catch(() => {});
    } catch {}
    return null;
  }
}

async function writeDictPackToCache(url: string, data: Record<string, RawDictValue>): Promise<void> {
  if (!hasCacheStorage()) return;
  try {
    const cache = await caches.open(DICT_CACHE_NAME);
    const response = new Response(JSON.stringify(data), {
      headers: { "Content-Type": "application/json" },
    });
    await cache.put(url, response);
  } catch {}
}

export async function clearDictionaryCache(): Promise<void> {
  resolvedWordCache.clear();
  loadedLetterPacks.clear();
  if (hasCacheStorage()) {
    try {
      await caches.delete(DICT_CACHE_NAME);
    } catch {}
  }
}

function putResolvedWord(word: string, entry: DictEntry) {
  if (resolvedWordCache.has(word)) {
    resolvedWordCache.delete(word);
  } else if (resolvedWordCache.size >= MAX_RESOLVED_WORDS) {
    const oldestKey = resolvedWordCache.keys().next().value;
    if (oldestKey !== undefined) resolvedWordCache.delete(oldestKey);
  }
  resolvedWordCache.set(word, entry);
}

function putLoadedPack(char: string, data: Record<string, RawDictValue>) {
  if (loadedLetterPacks.has(char)) {
    loadedLetterPacks.delete(char);
  } else if (loadedLetterPacks.size >= MAX_LOADED_PACKS) {
    const oldestChar = loadedLetterPacks.keys().next().value;
    if (oldestChar !== undefined) loadedLetterPacks.delete(oldestChar);
  }
  loadedLetterPacks.set(char, data);
}

/**
 * Clean and normalize a query string into a canonical English word.
 */
export function cleanEnglishWord(raw: string): string {
  if (!raw) return "";
  return raw
    .trim()
    .toLowerCase()
    .replace(/^[^a-z]+|[^a-z]+$/g, "")
    .replace(/[^a-z-]/g, "");
}

/**
 * Generate high-availability audio URLs using Youdao stream service (100% accessible in China, zero CORS).
 */
export function getAudioUrls(word: string) {
  const clean = cleanEnglishWord(word);
  return {
    us: `https://dict.youdao.com/dictvoice?audio=${encodeURIComponent(clean)}&type=2`,
    uk: `https://dict.youdao.com/dictvoice?audio=${encodeURIComponent(clean)}&type=1`,
  };
}

/**
 * Fetch and cache a letter shard (/dict/{letter}.json):
 * Tier 1: In-memory LRU -> Tier 2: Offline CacheStorage (enway-dict-v1) -> Tier 3: Edge CDN fetch (5s timeout).
 */
export async function loadLetterPack(letter: string): Promise<Record<string, RawDictValue> | null> {
  const char = letter.toLowerCase();
  if (char < "a" || char > "z") return null;

  const cached = loadedLetterPacks.get(char);
  if (cached) {
    loadedLetterPacks.delete(char);
    loadedLetterPacks.set(char, cached);
    return cached;
  }

  const pending = pendingLetterFetches[char];
  if (pending) {
    return pending;
  }

  const url = `/dict/${char}.json`;
  const task = (async () => {
    try {
      // Tier 2: Offline persistent CacheStorage
      const offlinePack = await readDictPackFromCache(url);
      if (offlinePack) {
        putLoadedPack(char, offlinePack);
        return offlinePack;
      }

      // Tier 3: Edge CDN fetch with 5s timeout cleanly cleared in finally
      const controller = new AbortController();
      const timer = setTimeout(() => controller.abort(), 5000);
      try {
        const res = await fetch(url, {
          cache: "force-cache",
          signal: controller.signal,
        });

        if (!res.ok) {
          throw new Error(`HTTP ${res.status}`);
        }
        const ct = (res.headers.get("content-type") || "").toLowerCase();
        if (ct.includes("text/html")) {
          throw new Error("Unexpected HTML response");
        }

        const data: unknown = await res.json();
        if (!data || typeof data !== "object" || Array.isArray(data)) {
          throw new Error("Invalid dictionary shard format");
        }

        const typedData = data as Record<string, RawDictValue>;
        putLoadedPack(char, typedData);
        writeDictPackToCache(url, typedData).catch(() => {});
        return typedData;
      } finally {
        clearTimeout(timer);
      }
    } catch (err) {
      console.warn(`[Dict] Failed to load shard ${url}:`, err);
      return null;
    } finally {
      delete pendingLetterFetches[char];
    }
  })();

  pendingLetterFetches[char] = task;
  return task;
}

function generateBritishToAmericanCandidates(word: string): string[] {
  const variants = new Set<string>();
  const add = (w: string) => {
    if (w && w !== word) variants.add(w);
  };

  if (word.endsWith("ise") && word.length > 4) add(word.slice(0, -3) + "ize");
  if (word.endsWith("ised") && word.length > 5) {
    add(word.slice(0, -4) + "ized");
    add(word.slice(0, -4) + "ize");
  }
  if (word.endsWith("ising") && word.length > 6) {
    add(word.slice(0, -5) + "izing");
    add(word.slice(0, -5) + "ize");
  }
  if (word.endsWith("ises") && word.length > 5) {
    add(word.slice(0, -4) + "izes");
    add(word.slice(0, -4) + "ize");
  }

  if (word.endsWith("yse") && word.length > 4) add(word.slice(0, -3) + "yze");
  if (word.endsWith("ysed") && word.length > 5) {
    add(word.slice(0, -4) + "yzed");
    add(word.slice(0, -4) + "yze");
  }
  if (word.endsWith("ysing") && word.length > 6) {
    add(word.slice(0, -5) + "yzing");
    add(word.slice(0, -5) + "yze");
  }
  if (word.endsWith("yses") && word.length > 5) {
    add(word.slice(0, -4) + "yzes");
    add(word.slice(0, -4) + "yze");
  }

  if (word.endsWith("our") && word.length > 4) add(word.slice(0, -3) + "or");
  if (word.endsWith("oured") && word.length > 6) {
    add(word.slice(0, -5) + "ored");
    add(word.slice(0, -5) + "or");
  }
  if (word.endsWith("ouring") && word.length > 7) {
    add(word.slice(0, -6) + "oring");
    add(word.slice(0, -6) + "or");
  }
  if (word.endsWith("ours") && word.length > 5) {
    add(word.slice(0, -4) + "ors");
    add(word.slice(0, -4) + "or");
  }

  if (word.endsWith("re") && word.length > 4 && /[bcdfghjklmnpqrstvwxyz]re$/.test(word)) {
    add(word.slice(0, -2) + "er");
  }
  if (word.endsWith("res") && word.length > 5 && /[bcdfghjklmnpqrstvwxyz]res$/.test(word)) {
    add(word.slice(0, -3) + "ers");
    add(word.slice(0, -3) + "er");
  }

  if (word.endsWith("lled") && word.length > 5) {
    add(word.slice(0, -4) + "led");
    add(word.slice(0, -3));
  }
  if (word.endsWith("lling") && word.length > 6) {
    add(word.slice(0, -5) + "ling");
    add(word.slice(0, -4));
  }
  if (word.endsWith("ller") && word.length > 5) {
    add(word.slice(0, -4) + "ler");
    add(word.slice(0, -3));
  }
  if (word.endsWith("llor") && word.length > 5) {
    add(word.slice(0, -4) + "lor");
  }

  if (word.endsWith("ogue") && word.length > 5) add(word.slice(0, -2));
  if (word.includes("ae")) add(word.replace(/ae/g, "e"));
  if (word.includes("oe")) add(word.replace(/oe/g, "e"));

  return Array.from(variants);
}

/**
 * Helper to test candidates for morphological stemming and British/American spelling variants
 */
function findStemMatch(
  clean: string,
  dict: Record<string, RawDictValue>
): { baseWord: string; item: { d: string; b?: string; p?: string; pos?: string } } | null {
  const candidates: string[] = [];

  // 0. British -> American spelling variants first
  candidates.push(...generateBritishToAmericanCandidates(clean));

  // Plurals and 3rd person singular: -s, -es, -ies
  if (clean.endsWith("ies") && clean.length > 4) candidates.push(clean.slice(0, -3) + "y");
  if (clean.endsWith("es") && clean.length > 3) candidates.push(clean.slice(0, -2));
  if (clean.endsWith("s") && clean.length > 2) candidates.push(clean.slice(0, -1));

  // Past tense / past participle: -ed, -ied
  if (clean.endsWith("ied") && clean.length > 4) candidates.push(clean.slice(0, -3) + "y");
  if (clean.endsWith("ed") && clean.length > 3) {
    candidates.push(clean.slice(0, -2)); // walked -> walk
    candidates.push(clean.slice(0, -1)); // changed -> change
    if (clean.length > 4 && clean[clean.length - 3] === clean[clean.length - 4]) {
      candidates.push(clean.slice(0, -3));
    }
  }

  // Present participle: -ing
  if (clean.endsWith("ing") && clean.length > 4) {
    candidates.push(clean.slice(0, -3)); // watching -> watch
    candidates.push(clean.slice(0, -3) + "e"); // making -> make
    if (clean.length > 5 && clean[clean.length - 4] === clean[clean.length - 5]) {
      candidates.push(clean.slice(0, -4)); // running -> run
    }
  }

  // Adverbs: -ly
  if (clean.endsWith("ly") && clean.length > 3) {
    candidates.push(clean.slice(0, -2)); // quickly -> quick
    if (clean.endsWith("ily") && clean.length > 4) {
      candidates.push(clean.slice(0, -3) + "y"); // happily -> happy
    }
  }

  // Comparatives / superlatives: -er, -est
  if (clean.endsWith("est") && clean.length > 4) {
    candidates.push(clean.slice(0, -3));
    candidates.push(clean.slice(0, -2));
  }
  if (clean.endsWith("er") && clean.length > 3) {
    candidates.push(clean.slice(0, -2));
    candidates.push(clean.slice(0, -1));
  }

  for (const cand of candidates) {
    if (Object.prototype.hasOwnProperty.call(dict, cand) && dict[cand]) {
      return { baseWord: cand, item: parseRawItem(dict[cand]) };
    }
  }

  return null;
}

function resolveWordFromPack(
  clean: string,
  pack: Record<string, RawDictValue>,
  audio: { us: string; uk: string }
): DictEntry | null {
  // 1. Direct match
  if (Object.prototype.hasOwnProperty.call(pack, clean) && pack[clean]) {
    const raw = parseRawItem(pack[clean]);
    const entry: DictEntry = {
      word: clean,
      baseWord: raw.b,
      phonetic: raw.p,
      pos: raw.pos,
      definition: raw.d,
      audioUrl: audio.us,
      usAudioUrl: audio.us,
      ukAudioUrl: audio.uk,
      isOnline: false,
    };
    putResolvedWord(clean, entry);
    return entry;
  }

  // 2. Stem & British/American variant match
  const stem = findStemMatch(clean, pack);
  if (stem) {
    const entry: DictEntry = {
      word: clean,
      baseWord: stem.baseWord,
      phonetic: stem.item.p,
      pos: stem.item.pos,
      definition: stem.item.d,
      audioUrl: audio.us,
      usAudioUrl: audio.us,
      ukAudioUrl: audio.uk,
      isOnline: false,
    };
    putResolvedWord(clean, entry);
    return entry;
  }

  return null;
}

function buildCompoundEntry(
  clean: string,
  parts: Array<{ part: string; entry: DictEntry }>,
  audio: { us: string; uk: string }
): DictEntry {
  const definition = parts.map((p) => `${p.part}：${p.entry.definition}`).join("\n");
  const entry: DictEntry = {
    word: clean,
    definition,
    audioUrl: audio.us,
    usAudioUrl: audio.us,
    ukAudioUrl: audio.uk,
    isOnline: false,
  };
  putResolvedWord(clean, entry);
  return entry;
}

/**
 * Synchronous offline lookup from already loaded letter packs or in-memory cache.
 */
export function lookupWord(rawWord: string): DictEntry | null {
  const clean = cleanEnglishWord(rawWord);
  if (!clean || clean.length < 2) return null;

  const cached = resolvedWordCache.get(clean);
  if (cached) {
    resolvedWordCache.delete(clean);
    resolvedWordCache.set(clean, cached);
    return cached;
  }

  const audio = getAudioUrls(clean);
  const firstChar = clean[0];
  const pack = loadedLetterPacks.get(firstChar);
  if (pack) {
    loadedLetterPacks.delete(firstChar);
    loadedLetterPacks.set(firstChar, pack);
    const direct = resolveWordFromPack(clean, pack, audio);
    if (direct) return direct;
  }

  // Hyphenated compound fallback when component packs are already cached
  if (clean.includes("-")) {
    const subWords = clean.split("-").filter((p) => p.length >= 2);
    if (subWords.length >= 2) {
      const resolvedParts: Array<{ part: string; entry: DictEntry }> = [];
      for (const sub of subWords) {
        const subPack = loadedLetterPacks.get(sub[0]);
        if (!subPack) continue;
        const subEntry = resolveWordFromPack(sub, subPack, getAudioUrls(sub));
        if (subEntry) resolvedParts.push({ part: sub, entry: subEntry });
      }
      if (resolvedParts.length === subWords.length) {
        return buildCompoundEntry(clean, resolvedParts, audio);
      }
    }
  }

  return null;
}

/**
 * Asynchronous High-Speed Sharded Lookup:
 * 1. Checks memory cache (0ms).
 * 2. Fetches Cloudflare Pages static shard (/dict/{letter}.json) if not yet loaded.
 * 3. Performs exact, British/American, morphological stem, or hyphenated compound lookup.
 * 4. 0 Supabase API calls, 0 Supabase egress, 0 CORS issues.
 */
export async function lookupWordAsync(rawWord: string): Promise<DictEntry | null> {
  const clean = cleanEnglishWord(rawWord);
  if (!clean || clean.length < 2) return null;

  // 1. Fast memory cache check
  const cached = resolvedWordCache.get(clean);
  if (cached) {
    resolvedWordCache.delete(clean);
    resolvedWordCache.set(clean, cached);
    return cached;
  }

  // 2. Load letter shard from Cloudflare Pages static CDN
  const firstChar = clean[0];
  const pack = await loadLetterPack(firstChar);

  const audio = getAudioUrls(clean);

  // If pack failed to load (network error or timeout), return temporary fallback WITHOUT caching
  if (!pack) {
    return {
      word: clean,
      pos: "离线加载中",
      definition: "网络分片加载稍慢或离线，请检查网络后重试",
      audioUrl: audio.us,
      usAudioUrl: audio.us,
      ukAudioUrl: audio.uk,
      isOnline: false,
    };
  }

  // 3 & 4. Check exact, British/American variant, or morphological stem match
  const resolved = resolveWordFromPack(clean, pack, audio);
  if (resolved) {
    return resolved;
  }

  // 4.5 Hyphenated compound fallback (e.g. high-volume, self-sliding)
  if (clean.includes("-")) {
    const subWords = clean.split("-").filter((p) => p.length >= 2);
    if (subWords.length >= 2) {
      const partResults = await Promise.all(
        subWords.map(async (sub) => {
          const subPack = await loadLetterPack(sub[0]);
          if (!subPack) return null;
          const subEntry = resolveWordFromPack(sub, subPack, getAudioUrls(sub));
          return subEntry ? { part: sub, entry: subEntry } : null;
        })
      );
      const validParts = partResults.filter(
        (x): x is { part: string; entry: DictEntry } => x !== null
      );
      if (validParts.length > 0) {
        return buildCompoundEntry(clean, validParts, audio);
      }
    }
  }

  // 5. Fallback placeholder for rare unregistered words (pack was loaded, but word is not in pack)
  const fallbackEntry: DictEntry = {
    word: clean,
    definition: "暂未收录该词释义",
    audioUrl: audio.us,
    usAudioUrl: audio.us,
    ukAudioUrl: audio.uk,
    isOnline: false,
  };
  putResolvedWord(clean, fallbackEntry);
  return fallbackEntry;
}
