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

interface RawDictItem {
  p?: string;
  pos?: string;
  d: string;
}

// Memory cache for fully resolved words
const resolvedWordCache: Record<string, DictEntry | undefined> = {};

// Memory cache for loaded 26-letter shards from Cloudflare Pages
const loadedLetterPacks: Record<string, Record<string, RawDictItem> | undefined> = {};

// In-flight fetch promises to prevent redundant simultaneous requests
const pendingLetterFetches: Record<string, Promise<Record<string, RawDictItem>> | undefined> = {};

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
 * Fetch and memory-cache a letter shard (/dict/{letter}.json) from Cloudflare Pages static CDN.
 */
export async function loadLetterPack(letter: string): Promise<Record<string, RawDictItem>> {
  const char = letter.toLowerCase();
  if (char < "a" || char > "z") return {};

  const cached = loadedLetterPacks[char];
  if (cached) {
    return cached;
  }

  const pending = pendingLetterFetches[char];
  if (pending) {
    return pending;
  }

  const task = (async () => {
    try {
      const res = await fetch(`/dict/${char}.json`, {
        cache: "force-cache",
      });
      if (!res.ok) {
        throw new Error(`HTTP ${res.status}`);
      }
      const data: Record<string, RawDictItem> = await res.json();
      loadedLetterPacks[char] = data;
      return data;
    } catch (err) {
      console.warn(`[Dict] Failed to load shard /dict/${char}.json:`, err);
      return {};
    } finally {
      delete pendingLetterFetches[char];
    }
  })();

  pendingLetterFetches[char] = task;
  return task;
}

/**
 * Helper to test candidates for morphological stemming
 */
function findStemMatch(
  clean: string,
  dict: Record<string, RawDictItem>
): { baseWord: string; item: RawDictItem } | null {
  const candidates: string[] = [];

  // Plurals and 3rd person singular: -s, -es, -ies
  if (clean.endsWith("ies") && clean.length > 4) candidates.push(clean.slice(0, -3) + "y");
  if (clean.endsWith("es") && clean.length > 3) candidates.push(clean.slice(0, -2));
  if (clean.endsWith("s") && clean.length > 2) candidates.push(clean.slice(0, -1));

  // Past tense / past participle: -ed, -ied
  if (clean.endsWith("ied") && clean.length > 4) candidates.push(clean.slice(0, -3) + "y");
  if (clean.endsWith("ed") && clean.length > 3) {
    candidates.push(clean.slice(0, -2)); // walked -> walk
    candidates.push(clean.slice(0, -1)); // changed -> change
    // doubled consonants: e.g. stopped -> stop
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
    if (dict[cand]) {
      return { baseWord: cand, item: dict[cand] };
    }
  }

  return null;
}

/**
 * Synchronous offline lookup from already loaded letter packs or in-memory cache.
 */
export function lookupWord(rawWord: string): DictEntry | null {
  const clean = cleanEnglishWord(rawWord);
  if (!clean || clean.length < 2) return null;

  if (resolvedWordCache[clean]) {
    return resolvedWordCache[clean];
  }

  const firstChar = clean[0];
  const pack = loadedLetterPacks[firstChar];
  if (!pack) return null;

  const audio = getAudioUrls(clean);

  // 1. Direct match
  if (pack[clean]) {
    const raw = pack[clean];
    const entry: DictEntry = {
      word: clean,
      phonetic: raw.p || `/${clean}/`,
      pos: raw.pos || "考研词汇",
      definition: raw.d,
      audioUrl: audio.us,
      usAudioUrl: audio.us,
      ukAudioUrl: audio.uk,
      isOnline: false,
    };
    resolvedWordCache[clean] = entry;
    return entry;
  }

  // 2. Stem match
  const stem = findStemMatch(clean, pack);
  if (stem) {
    const entry: DictEntry = {
      word: clean,
      baseWord: stem.baseWord,
      phonetic: stem.item.p || `/${clean}/`,
      pos: stem.item.pos || "衍生词",
      definition: `${stem.item.d} (原形: ${stem.baseWord})`,
      audioUrl: audio.us,
      usAudioUrl: audio.us,
      ukAudioUrl: audio.uk,
      isOnline: false,
    };
    resolvedWordCache[clean] = entry;
    return entry;
  }

  return null;
}

/**
 * Asynchronous High-Speed Sharded Lookup:
 * 1. Checks memory cache (0ms).
 * 2. Fetches Cloudflare Pages static shard (/dict/{letter}.json) if not yet loaded.
 * 3. Performs exact or morphological stem lookup.
 * 4. 0 Supabase API calls, 0 Supabase egress, 0 CORS issues.
 */
export async function lookupWordAsync(rawWord: string): Promise<DictEntry | null> {
  const clean = cleanEnglishWord(rawWord);
  if (!clean || clean.length < 2) return null;

  // 1. Fast memory cache check
  if (resolvedWordCache[clean]) {
    return resolvedWordCache[clean];
  }

  // 2. Load letter shard from Cloudflare Pages static CDN
  const firstChar = clean[0];
  const pack = await loadLetterPack(firstChar);

  // 3. Check exact match
  const audio = getAudioUrls(clean);

  if (pack && pack[clean]) {
    const raw = pack[clean];
    const entry: DictEntry = {
      word: clean,
      phonetic: raw.p || `/${clean}/`,
      pos: raw.pos || "考研核心词",
      definition: raw.d,
      audioUrl: audio.us,
      usAudioUrl: audio.us,
      ukAudioUrl: audio.uk,
      isOnline: false,
    };
    resolvedWordCache[clean] = entry;
    return entry;
  }

  // 4. Morphological stemming match
  if (pack) {
    const stem = findStemMatch(clean, pack);
    if (stem) {
      const entry: DictEntry = {
        word: clean,
        baseWord: stem.baseWord,
        phonetic: stem.item.p || `/${clean}/`,
        pos: stem.item.pos || "衍生词",
        definition: `${stem.item.d} (原形: ${stem.baseWord})`,
        audioUrl: audio.us,
        usAudioUrl: audio.us,
        ukAudioUrl: audio.uk,
        isOnline: false,
      };
      resolvedWordCache[clean] = entry;
      return entry;
    }
  }

  // 5. Fallback placeholder for rare unregistered words
  const fallbackEntry: DictEntry = {
    word: clean,
    phonetic: `/${clean}/`,
    pos: "词汇",
    definition: "考研真题高频词汇（可点击下方加入生词本重点复习）",
    audioUrl: audio.us,
    usAudioUrl: audio.us,
    ukAudioUrl: audio.uk,
    isOnline: false,
  };
  resolvedWordCache[clean] = fallbackEntry;
  return fallbackEntry;
}
