export interface DictEntry {
  word: string;
  phonetic?: string;
  pos?: string; // n., v., adj., adv.
  definition: string; // Chinese translation
  enDefinition?: string; // English definition
  audioUrl?: string; // Real pronunciation audio URL
  isOnline?: boolean;
}

// Built-in offline high-frequency CET-4/6 and Kaoyan core dictionary
export const CORE_DICTIONARY: Record<string, { phonetic?: string; pos: string; definition: string; enDefinition?: string }> = {
  agriculture: { phonetic: "/ˈæɡrɪkʌltʃər/", pos: "n.", definition: "农业；农学", enDefinition: "The practice of farming and cultivating land" },
  conventional: { phonetic: "/kənˈvenʃənl/", pos: "adj.", definition: "传统的；惯例的；常规的", enDefinition: "Conforming to established practice or standard" },
  logistical: { phonetic: "/ləˈdʒɪstɪkl/", pos: "adj.", definition: "后勤方面的；运筹的；物流的", enDefinition: "Relating to the organization of moving supplies" },
  ecological: { phonetic: "/ˌiːkəˈlɒdʒɪkl/", pos: "adj.", definition: "生态的；生态学的", enDefinition: "Relating to living organisms and their environment" },
  emission: { phonetic: "/ɪˈmɪʃn/", pos: "n.", definition: "散发；排放（物）", enDefinition: "The production and discharge of something" },
  vulnerability: { phonetic: "/ˌvʌlnərəˈbɪləti/", pos: "n.", definition: "脆弱性；易受攻击性", enDefinition: "The state of being susceptible to harm" },
  disruption: { phonetic: "/dɪsˈrʌpʃn/", pos: "n.", definition: "中断；扰乱；颠覆", enDefinition: "Disturbance or problems that interrupt an event" },
  hydroponics: { phonetic: "/ˌhaɪdrəˈpɒnɪks/", pos: "n.", definition: "水耕法；水培栽培", enDefinition: "The process of growing plants in water without soil" },
  conserve: { phonetic: "/kənˈsɜːv/", pos: "v.", definition: "保护；节约；保存", enDefinition: "Protect from harm, decay, or loss" },
  agrarian: { phonetic: "/əˈɡreəriən/", pos: "adj.", definition: "土地的；农业的；耕地的", enDefinition: "Relating to cultivated land or the cultivation of land" },
  mitigate: { phonetic: "/ˈmɪtɪɡeɪt/", pos: "v.", definition: "缓解；减轻；平息", enDefinition: "Make less severe, serious, or painful" },
  infrastructure: { phonetic: "/ˈɪnfrəstrʌktʃər/", pos: "n.", definition: "基础设施；公共建设", enDefinition: "Basic physical and organizational structures of a society" },
  expenditure: { phonetic: "/ɪkˈspendɪtʃər/", pos: "n.", definition: "开支；支出；经费", enDefinition: "The action of spending funds" },
  prohibitive: { phonetic: "/prəˈhɪbətɪv/", pos: "adj.", definition: "（价格等）高得令人望而却步的；禁止性的", enDefinition: "Excessively high or restricting" },
  regulatory: { phonetic: "/ˈreɡjələtəri/", pos: "adj.", definition: "监管的；管理的；规制的", enDefinition: "Serving or intended to regulate something" },
  bureaucratic: { phonetic: "/ˌbjʊərəˈkrætɪk/", pos: "adj.", definition: "官僚主义的；繁文缛节的", enDefinition: "Relating to a system of government with many rules" },
  resilience: { phonetic: "/rɪˈzɪliəns/", pos: "n.", definition: "恢复力；韧性；适应力", enDefinition: "The capacity to recover quickly from difficulties" },
  sovereignty: { phonetic: "/ˈsɒvrənti/", pos: "n.", definition: "主权；自主统治权", enDefinition: "Supreme power or authority" },
  deprivation: { phonetic: "/ˌdeprɪˈveɪʃn/", pos: "n.", definition: "剥夺；匮乏；缺失", enDefinition: "The damaging lack of material benefits considered basic necessities" },
  epidemic: { phonetic: "/ˌepɪˈdemɪk/", pos: "n./adj.", definition: "流行病；泛滥；大范围盛行的", enDefinition: "A widespread occurrence of an infectious disease" },
  cognitive: { phonetic: "/ˈkɒɡnətɪv/", pos: "adj.", definition: "认知的；知觉的", enDefinition: "Relating to cognition or mental action" },
  metabolic: { phonetic: "/ˌmetəˈbɒlɪk/", pos: "adj.", definition: "新陈代谢的", enDefinition: "Relating to or deriving from metabolism" },
  neurodegenerative: { phonetic: "/ˌnjʊərəʊdɪˈdʒenərətɪv/", pos: "adj.", definition: "神经退行性的", enDefinition: "Resulting in progressive loss of structure or function of neurons" },
  consolidation: { phonetic: "/kənˌsɒlɪˈdeɪʃn/", pos: "n.", definition: "巩固；强化；合并", enDefinition: "The process of making something stronger or more solid" },
  unintentional: { phonetic: "/ˌʌnɪnˈtenʃənl/", pos: "adj.", definition: "无意的；非故意的", enDefinition: "Not done on purpose" },
  monopoly: { phonetic: "/məˈnɒpəli/", pos: "n.", definition: "垄断；独占；专利", enDefinition: "The exclusive possession or control of the supply or trade" },
  doctrine: { phonetic: "/ˈdɒktrɪn/", pos: "n.", definition: "教义；信条；学说", enDefinition: "A belief or set of beliefs held and taught by a church, political party, etc." },
  infringement: { phonetic: "/ɪnˈfrɪndʒmənt/", pos: "n.", definition: "侵犯；侵权；违反", enDefinition: "The action of breaking the terms of a law, agreement, etc." },
  conglomerate: { phonetic: "/kənˈɡlɒmərət/", pos: "n.", definition: "大型企业集团；跨行业公司", enDefinition: "A multi-industry company formed by corporate mergers" },
  verbatim: { phonetic: "/vɜːˈbeɪtɪm/", pos: "adv./adj.", definition: "逐字逐句地；一字不差的", enDefinition: "In exactly the same words as were used originally" },
  conflate: { phonetic: "/kənˈfleɪt/", pos: "v.", definition: "合并；混淆；混合", enDefinition: "Combine two or more texts or ideas into one" },
  assimilation: { phonetic: "/əˌsɪməˈleɪʃn/", pos: "n.", definition: "吸收；同化；融入", enDefinition: "The process of taking in and fully understanding information or ideas" },
  cannibalize: { phonetic: "/ˈkænɪbəlaɪz/", pos: "v.", definition: "侵蚀（本公司现有产品的市场份额）", enDefinition: "Reduce the sales of a product by introducing a similar product" },
  judicial: { phonetic: "/dʒuˈdɪʃl/", pos: "adj.", definition: "司法的；审判的；法官的", enDefinition: "Of, by, or appropriate to a court or judge" },
  unfettered: { phonetic: "/ʌnˈfetəd/", pos: "adj.", definition: "不受约束的；自由无羁的", enDefinition: "Not confined or restricted" },
  stringent: { phonetic: "/ˈstrɪndʒənt/", pos: "adj.", definition: "严格的；严厉的；紧缩的", enDefinition: "Strict, precise, and exacting" },
  behemoth: { phonetic: "/bɪˈhiːmɒθ/", pos: "n.", definition: "庞然大物；行业巨头", enDefinition: "A huge or monstrous creature, or an enormous organization" },
  statutory: { phonetic: "/ˈstætʃətri/", pos: "adj.", definition: "法定的；依法制定的", enDefinition: "Required, permitted, or enacted by statute" },
  sustainable: { phonetic: "/səˈsteɪnəbl/", pos: "adj.", definition: "可持续的；可合理维持的", enDefinition: "Able to be maintained at a certain rate or level" },
  contemporary: { phonetic: "/kənˈtemprəri/", pos: "adj./n.", definition: "当代的；同时代的；同代人", enDefinition: "Living or occurring at the same time" },
  deficit: { phonetic: "/ˈdefɪsɪt/", pos: "n.", definition: "赤字；逆差；不足", enDefinition: "The amount by which something is too small" },
  hygiene: { phonetic: "/ˈhaɪdʒiːn/", pos: "n.", definition: "卫生；保健", enDefinition: "Conditions or practices conducive to maintaining health" },
  incentive: { phonetic: "/ɪnˈsentɪv/", pos: "n.", definition: "激励；诱因；动机", enDefinition: "A thing that motivates or encourages someone to do something" },
  dispute: { phonetic: "/dɪˈspjuːt/", pos: "n./v.", definition: "争端；纠纷；质疑", enDefinition: "A disagreement, argument, or debate" },
  royalty: { phonetic: "/ˈrɔɪəlti/", pos: "n.", definition: "版税；特许使用费；王室", enDefinition: "A payment made by one party to another for using their property" },
  imperative: { phonetic: "/ɪmˈperətɪv/", pos: "adj./n.", definition: "极重要的；必要的；紧迫之事", enDefinition: "Of vital importance; crucial" },
  eliminate: { phonetic: "/ɪˈlɪmɪneɪt/", pos: "v.", definition: "消除；排除；淘汰", enDefinition: "Completely remove or get rid of" },
  provisional: { phonetic: "/prəˈvɪʒənl/", pos: "adj.", definition: "临时的；暂定的", enDefinition: "Arranged or existing for the present, possibly to be changed later" },
  negligible: { phonetic: "/ˈneɡlɪdʒəbl/", pos: "adj.", definition: "微不足道的；可以忽略的", enDefinition: "So small or unimportant as to be not worth considering" },
  beneficial: { phonetic: "/ˌbenɪˈfɪʃl/", pos: "adj.", definition: "有益的；有利的", enDefinition: "Favorable or advantageous; resulting in good" },
  consequence: { phonetic: "/ˈkɒnsɪkwəns/", pos: "n.", definition: "后果；重要性", enDefinition: "A result or effect of an action or condition" },
  precaution: { phonetic: "/prɪˈkɔːʃn/", pos: "n.", definition: "预防措施；警惕", enDefinition: "A measure taken in advance to prevent something dangerous" },
  detriment: { phonetic: "/ˈdetrɪmənt/", pos: "n.", definition: "损害；伤害；不利因素", enDefinition: "The state of being harmed or damaged" },
  ubiquitous: { phonetic: "/juːˈbɪkwɪtəs/", pos: "adj.", definition: "无处不在的；普遍存在的", enDefinition: "Present, appearing, or found everywhere" },
  paradigm: { phonetic: "/ˈpærədaɪm/", pos: "n.", definition: "范式；典范；模式", enDefinition: "A typical example or pattern of something; a model" },
  scrutiny: { phonetic: "/ˈskruːtəni/", pos: "n.", definition: "仔细审查；彻底审视", enDefinition: "Critical observation or examination" },
  pervasive: { phonetic: "/pəˈveɪsɪv/", pos: "adj.", definition: "弥漫的；遍布的；普遍的", enDefinition: "Spreading widely throughout an area or a group of people" },
  deteriorate: { phonetic: "/dɪˈtɪəriəreɪt/", pos: "v.", definition: "恶化；变坏；退化", enDefinition: "Become progressively worse" },
  unprecedented: { phonetic: "/ʌnˈpresɪdentɪd/", pos: "adj.", definition: "史无前例的；空前的", enDefinition: "Never done or known before" },
  manifest: { phonetic: "/ˈmænɪfest/", pos: "v./adj.", definition: "显现；表明；明显的", enDefinition: "Clear or obvious to the eye or mind; display or show" },
  indispensable: { phonetic: "/ˌɪndɪˈspensəbl/", pos: "adj.", definition: "不可或缺的；必需的", enDefinition: "Absolutely necessary" },
  consensus: { phonetic: "/kənˈsensəs/", pos: "n.", definition: "共识；一致意见", enDefinition: "A general agreement" },
  hypothesis: { phonetic: "/haɪˈpɒθəsɪs/", pos: "n.", definition: "假设；假说", enDefinition: "A proposed explanation made on the basis of limited evidence" },
  empirical: { phonetic: "/ɪmˈpɪrɪkl/", pos: "adj.", definition: "基于经验的；实证的", enDefinition: "Based on, concerned with, or verifiable by observation or experience" },
  catalyst: { phonetic: "/ˈkætəlɪst/", pos: "n.", definition: "催化剂；促成因素", enDefinition: "A person or thing that precipitates an event" },
  counterpart: { phonetic: "/ˈkaʊntəpɑːt/", pos: "n.", definition: "职能相当的人或物；相对应者", enDefinition: "A person or thing corresponding to another in position or function" },
  discrepancy: { phonetic: "/dɪˈskrepənsi/", pos: "n.", definition: "差异；不一致；矛盾", enDefinition: "A lack of compatibility or similarity between two or more facts" },
  fluctuation: { phonetic: "/ˌflʌktʃuˈeɪʃn/", pos: "n.", definition: "波动；起伏", enDefinition: "An irregular rising and falling in number or amount; a variation" },
  homogeneous: { phonetic: "/ˌhɒməˈdʒiːniəs/", pos: "adj.", definition: "同质的；同类的；均匀的", enDefinition: "Of the same kind; alike" },
  heterogeneous: { phonetic: "/ˌhetərəˈdʒiːniəs/", pos: "adj.", definition: "异质的；多元混合的", enDefinition: "Diverse in character or content" },
  incentivize: { phonetic: "/ɪnˈsentɪvaɪz/", pos: "v.", definition: "激励；奖励；促进", enDefinition: "Provide with an incentive for doing something" },
  jeopardize: { phonetic: "/ˈdʒepədaɪz/", pos: "v.", definition: "危及；损害", enDefinition: "Put someone or something into a situation in which there is a danger of loss, harm, or failure" },
  lucrative: { phonetic: "/ˈluːkrətɪv/", pos: "adj.", definition: "获利丰厚的；赚大钱的", enDefinition: "Producing a great deal of profit" },
  monotonous: { phonetic: "/məˈnɒtənəs/", pos: "adj.", definition: "单调的；乏味的", enDefinition: "Dull, tedious, and repetitious; lacking in variety" },
  nostalgia: { phonetic: "/nɒˈstældʒə/", pos: "n.", definition: "怀旧；乡愁", enDefinition: "A sentimental longing or wistful affection for the past" },
  plausible: { phonetic: "/ˈplɔːzəbl/", pos: "adj.", definition: "看似合理的；合乎情理的", enDefinition: "Seeming reasonable or probable" },
  pragmatic: { phonetic: "/præɡˈmætɪk/", pos: "adj.", definition: "务实的；注重实效的", enDefinition: "Dealing with things sensibly and realistically" },
  reconcile: { phonetic: "/ˈrekənsaɪl/", pos: "v.", definition: "使和解；调和；使一致", enDefinition: "Restore friendly relations between; make consistent" },
  spontaneous: { phonetic: "/spɒnˈteɪniəs/", pos: "adj.", definition: "自发的；自然的；未经刻意安排的", enDefinition: "Performed or occurring as a result of a sudden impulse" },
  tangible: { phonetic: "/ˈtændʒəbl/", pos: "adj.", definition: "有形的；切实的；可感知的", enDefinition: "Perceptible by touch; clear and definite" },
  unravel: { phonetic: "/ʌnˈrævl/", pos: "v.", definition: "解开；阐明；瓦解", enDefinition: "Undo twisted or woven threads; investigate and solve" },
  versatile: { phonetic: "/ˈvɜːsətaɪl/", pos: "adj.", definition: "多才多艺的；多功能的", enDefinition: "Able to adapt or be adapted to many different functions" },
  warrant: { phonetic: "/ˈwɒrənt/", pos: "v./n.", definition: "证明…是正当的；搜查令；凭单", enDefinition: "Justify or necessitate; an authorization" }
};

// Client-side in-memory session cache for fast instant query
const resolvedWordCache: Record<string, DictEntry> = {};

/**
 * Clean and normalize a query string into a canonical English word.
 */
export function cleanEnglishWord(raw: string): string {
  if (!raw) return "";
  // Strip trailing punctuation, markdown, numbers, whitespace
  return raw
    .trim()
    .toLowerCase()
    .replace(/^[^a-z]+|[^a-z]+$/g, "")
    .replace(/[^a-z-]/g, "");
}

/**
 * Synchronous offline lookup from local core dictionary with stemming fallbacks.
 */
export function lookupWord(rawWord: string): DictEntry | null {
  const clean = cleanEnglishWord(rawWord);
  if (!clean || clean.length < 2) return null;

  // 1. Check in-memory cache
  if (resolvedWordCache[clean]) {
    return resolvedWordCache[clean];
  }

  // 2. Direct match in core offline dictionary
  if (CORE_DICTIONARY[clean]) {
    const item = CORE_DICTIONARY[clean];
    const entry: DictEntry = {
      word: clean,
      phonetic: item.phonetic,
      pos: item.pos,
      definition: item.definition,
      enDefinition: item.enDefinition,
      isOnline: false,
    };
    resolvedWordCache[clean] = entry;
    return entry;
  }

  // 3. Heuristic morphological stem match
  const candidates: string[] = [];
  if (clean.endsWith("s")) candidates.push(clean.slice(0, -1));
  if (clean.endsWith("es")) candidates.push(clean.slice(0, -2));
  if (clean.endsWith("ed")) {
    candidates.push(clean.slice(0, -2));
    candidates.push(clean.slice(0, -1));
  }
  if (clean.endsWith("ing")) {
    candidates.push(clean.slice(0, -3));
    candidates.push(clean.slice(0, -3) + "e");
  }
  if (clean.endsWith("ly")) candidates.push(clean.slice(0, -2));
  if (clean.endsWith("er")) candidates.push(clean.slice(0, -2));
  if (clean.endsWith("est")) candidates.push(clean.slice(0, -3));

  for (const c of candidates) {
    if (CORE_DICTIONARY[c]) {
      const item = CORE_DICTIONARY[c];
      const entry: DictEntry = {
        word: clean,
        phonetic: item.phonetic,
        pos: item.pos,
        definition: `${item.definition} (原形: ${c})`,
        enDefinition: item.enDefinition,
        isOnline: false,
      };
      resolvedWordCache[clean] = entry;
      return entry;
    }
  }

  return null;
}

/**
 * Asynchronous Dual-Engine Lookup:
 * 1. Checks local offline dictionary (0ms).
 * 2. If not found, asynchronously queries Free Dictionary API + MyMemory translation in parallel.
 * 3. Falls back gracefully so users always get a structured result.
 */
export async function lookupWordAsync(rawWord: string): Promise<DictEntry | null> {
  const clean = cleanEnglishWord(rawWord);
  if (!clean || clean.length < 2) return null;

  // Check cache or local offline dictionary first
  const localMatch = lookupWord(clean);
  if (localMatch && !localMatch.definition.includes("正在查询权威释义")) {
    return localMatch;
  }

  // Fetch online with a 3.5s timeout
  try {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), 3500);

    const [dictResp, transResp] = await Promise.allSettled([
      fetch(`https://api.dictionaryapi.dev/api/v2/entries/en/${clean}`, { signal: controller.signal }),
      fetch(`https://api.mymemory.translated.net/get?q=${clean}&langpair=en|zh-CN`, { signal: controller.signal })
    ]);

    clearTimeout(timeoutId);

    let phonetic = "";
    let audioUrl = "";
    let pos = "word";
    let enDefinition = "";
    let zhDefinition = "";

    // Parse dictionary definition
    if (dictResp.status === "fulfilled" && dictResp.value.ok) {
      const dictData = await dictResp.value.json();
      const firstEntry = dictData?.[0];
      if (firstEntry) {
        phonetic = firstEntry.phonetic || firstEntry.phonetics?.find((p: any) => p.text)?.text || "";
        audioUrl = firstEntry.phonetics?.find((p: any) => p.audio && p.audio.startsWith("http"))?.audio || "";
        const firstMeaning = firstEntry.meanings?.[0];
        if (firstMeaning) {
          pos = firstMeaning.partOfSpeech || "n.";
          enDefinition = firstMeaning.definitions?.[0]?.definition || "";
        }
      }
    }

    // Parse translation
    if (transResp.status === "fulfilled" && transResp.value.ok) {
      const transData = await transResp.value.json();
      const transText = transData?.responseData?.translatedText;
      if (transText && transText.toLowerCase() !== clean) {
        zhDefinition = transText;
      }
    }

    // Build finalized entry
    const finalDefinition = zhDefinition || (enDefinition ? `[释义] ${enDefinition}` : "在真题语境中出现，点击收录到生词本");

    const entry: DictEntry = {
      word: clean,
      phonetic: phonetic || `/ ${clean} /`,
      pos,
      definition: finalDefinition,
      enDefinition: enDefinition || undefined,
      audioUrl: audioUrl || undefined,
      isOnline: true,
    };

    resolvedWordCache[clean] = entry;
    return entry;
  } catch {
    // Network failure / timeout fallback
    return {
      word: clean,
      phonetic: `/ ${clean} /`,
      pos: "word",
      definition: "在真题语境中出现的高频词，可点击【加入生词本】持续复习",
      isOnline: false,
    };
  }
}

/**
 * Play English pronunciation:
 * Prefers official native speaker MP3 audio URL; falls back to Web Speech API.
 */
export function playWordAudio(word: string, audioUrl?: string) {
  if (typeof window === "undefined") return;

  if (audioUrl) {
    try {
      const audio = new Audio(audioUrl);
      audio.play().catch(() => playWithWebSpeech(word));
      return;
    } catch {
      // Fallback to Web Speech API
    }
  }

  playWithWebSpeech(word);
}

function playWithWebSpeech(word: string) {
  if (typeof window === "undefined" || !("speechSynthesis" in window)) return;
  try {
    window.speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(word);
    u.lang = "en-US";
    u.rate = 0.9;
    window.speechSynthesis.speak(u);
  } catch (e) {
    console.warn("TTS speak failed", e);
  }
}
