import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const CACHE_DIR = path.join(__dirname, "cache");
const OUTPUT_DIR = path.join(__dirname, "..", "public", "dict");

if (!fs.existsSync(CACHE_DIR)) fs.mkdirSync(CACHE_DIR, { recursive: true });
if (!fs.existsSync(OUTPUT_DIR)) fs.mkdirSync(OUTPUT_DIR, { recursive: true });

// Curated high-frequency Kaoyan vocabulary with accurate phonetics and parts of speech
const CURATED_KAOYAN = {
  agriculture: { p: "/ˈæɡrɪkʌltʃər/", pos: "n.", d: "农业；农学" },
  conventional: { p: "/kənˈvenʃənl/", pos: "adj.", d: "传统的；惯例的；常规的" },
  logistical: { p: "/ləˈdʒɪstɪkl/", pos: "adj.", d: "后勤方面的；运筹的；物流的" },
  ecological: { p: "/ˌiːkəˈlɒdʒɪkl/", pos: "adj.", d: "生态的；生态学的" },
  emission: { p: "/ɪˈmɪʃn/", pos: "n.", d: "散发；排放（物）" },
  vulnerability: { p: "/ˌvʌlnərəˈbɪləti/", pos: "n.", d: "脆弱性；易受攻击性" },
  disruption: { p: "/dɪsˈrʌpʃn/", pos: "n.", d: "中断；扰乱；颠覆" },
  hydroponics: { p: "/ˌhaɪdrəˈpɒnɪks/", pos: "n.", d: "水耕法；水培栽培" },
  conserve: { p: "/kənˈsɜːv/", pos: "v.", d: "保护；节约；保存" },
  agrarian: { p: "/əˈɡreəriən/", pos: "adj.", d: "土地的；农业的；耕地的" },
  mitigate: { p: "/ˈmɪtɪɡeɪt/", pos: "v.", d: "缓解；减轻；平息" },
  infrastructure: { p: "/ˈɪnfrəstrʌktʃər/", pos: "n.", d: "基础设施；公共建设" },
  expenditure: { p: "/ɪkˈspendɪtʃər/", pos: "n.", d: "开支；支出；经费" },
  prohibitive: { p: "/prəˈhɪbətɪv/", pos: "adj.", d: "（价格等）高得令人望而却步的；禁止性的" },
  regulatory: { p: "/ˈreɡjələtəri/", pos: "adj.", d: "监管的；管理的；规制的" },
  bureaucratic: { p: "/ˌbjʊərəˈkrætɪk/", pos: "adj.", d: "官僚主义的；繁文缛节的" },
  resilience: { p: "/rɪˈzɪliəns/", pos: "n.", d: "恢复力；韧性；适应力" },
  sovereignty: { p: "/ˈsɒvrənti/", pos: "n.", d: "主权；自主统治权" },
  deprivation: { p: "/ˌdeprɪˈveɪʃn/", pos: "n.", d: "剥夺；匮乏；缺失" },
  epidemic: { p: "/ˌepɪˈdemɪk/", pos: "n./adj.", d: "流行病；泛滥；大范围盛行的" },
  cognitive: { p: "/ˈkɒɡnətɪv/", pos: "adj.", d: "认知的；知觉的" },
  metabolic: { p: "/ˌmetəˈbɒlɪk/", pos: "adj.", d: "新陈代谢的" },
  neurodegenerative: { p: "/ˌnjʊərəʊdɪˈdʒenərətɪv/", pos: "adj.", d: "神经退行性的" },
  consolidation: { p: "/kənˌsɒlɪˈdeɪʃn/", pos: "n.", d: "巩固；强化；合并" },
  unintentional: { p: "/ˌʌnɪnˈtenʃənl/", pos: "adj.", d: "无意的；非故意的" },
  monopoly: { p: "/məˈnɒpəli/", pos: "n.", d: "垄断；独占；专利" },
  doctrine: { p: "/ˈdɒktrɪn/", pos: "n.", d: "教义；信条；学说" },
  infringement: { p: "/ɪnˈfrɪndʒmənt/", pos: "n.", d: "侵犯；侵权；违反" },
  conglomerate: { p: "/kənˈɡlɒmərət/", pos: "n.", d: "大型企业集团；跨行业公司" },
  verbatim: { p: "/vɜːˈbeɪtɪm/", pos: "adv./adj.", d: "逐字逐句地；一字不差的" },
  conflate: { p: "/kənˈfleɪt/", pos: "v.", d: "合并；混淆；混合" },
  assimilation: { p: "/əˌsɪməˈleɪʃn/", pos: "n.", d: "吸收；同化；融入" },
  cannibalize: { p: "/ˈkænɪbəlaɪz/", pos: "v.", d: "侵蚀（本公司现有产品的市场份额）" },
  judicial: { p: "/dʒuˈdɪʃl/", pos: "adj.", d: "司法的；审判的；法官的" },
  unfettered: { p: "/ʌnˈfetəd/", pos: "adj.", d: "不受约束的；自由无羁的" },
  stringent: { p: "/ˈstrɪndʒənt/", pos: "adj.", d: "严格的；严厉的；紧缩的" },
  behemoth: { p: "/bɪˈhiːmɒθ/", pos: "n.", d: "庞然大物；行业巨头" },
  statutory: { p: "/ˈstætʃətri/", pos: "adj.", d: "法定的；依法制定的" },
  sustainable: { p: "/səˈsteɪnəbl/", pos: "adj.", d: "可持续的；可合理维持的" },
  contemporary: { p: "/kənˈtemprəri/", pos: "adj./n.", d: "当代的；同时代的；同代人" },
  deficit: { p: "/ˈdefɪsɪt/", pos: "n.", d: "赤字；逆差；不足" },
  hygiene: { p: "/ˈhaɪdʒiːn/", pos: "n.", d: "卫生；保健" },
  incentive: { p: "/ɪnˈsentɪv/", pos: "n.", d: "激励；诱因；动机" },
  dispute: { p: "/dɪˈspjuːt/", pos: "n./v.", d: "争端；纠纷；质疑" },
  royalty: { p: "/ˈrɔɪəlti/", pos: "n.", d: "版税；特许使用费；王室" },
  imperative: { p: "/ɪmˈperətɪv/", pos: "adj./n.", d: "极重要的；必要的；紧迫之事" },
  eliminate: { p: "/ɪˈlɪmɪneɪt/", pos: "v.", d: "消除；排除；淘汰" },
  provisional: { p: "/prəˈvɪʒənl/", pos: "adj.", d: "临时的；暂定的" },
  negligible: { p: "/ˈneɡlɪdʒəbl/", pos: "adj.", d: "微不足道的；可以忽略的" },
  beneficial: { p: "/ˌbenɪˈfɪʃl/", pos: "adj.", d: "有益的；有利的" },
  consequence: { p: "/ˈkɒnsɪkwəns/", pos: "n.", d: "后果；重要性" },
  precaution: { p: "/prɪˈkɔːʃn/", pos: "n.", d: "预防措施；警惕" },
  detriment: { p: "/ˈdetrɪmənt/", pos: "n.", d: "损害；伤害；不利因素" },
  ubiquitous: { p: "/juːˈbɪkwɪtəs/", pos: "adj.", d: "无处不在的；普遍存在的" },
  paradigm: { p: "/ˈpærədaɪm/", pos: "n.", d: "范式；典范；模式" },
  scrutiny: { p: "/ˈskruːtəni/", pos: "n.", d: "仔细审查；彻底审视" },
  pervasive: { p: "/pəˈveɪsɪv/", pos: "adj.", d: "弥漫的；遍布的；普遍的" },
  deteriorate: { p: "/dɪˈtɪəriəreɪt/", pos: "v.", d: "恶化；变坏；退化" },
  unprecedented: { p: "/ʌnˈpresɪdentɪd/", pos: "adj.", d: "史无前例的；空前的" },
  manifest: { p: "/ˈmænɪfest/", pos: "v./adj.", d: "显现；表明；明显的" },
  indispensable: { p: "/ˌɪndɪˈspensəbl/", pos: "adj.", d: "不可或缺的；必需的" },
  consensus: { p: "/kənˈsensəs/", pos: "n.", d: "共识；一致意见" },
  hypothesis: { p: "/haɪˈpɒθəsɪs/", pos: "n.", d: "假设；假说" },
  empirical: { p: "/ɪmˈpɪrɪkl/", pos: "adj.", d: "基于经验的；实证的" },
  catalyst: { p: "/ˈkætəlɪst/", pos: "n.", d: "催化剂；促成因素" },
  counterpart: { p: "/ˈkaʊntəpɑːt/", pos: "n.", d: "职能相当的人或物；相对应者" },
  discrepancy: { p: "/dɪˈskrepənsi/", pos: "n.", d: "差异；不一致；矛盾" },
  fluctuation: { p: "/ˌflʌktʃuˈeɪʃn/", pos: "n.", d: "波动；起伏" },
  homogeneous: { p: "/ˌhɒməˈdʒiːniəs/", pos: "adj.", d: "同质的；同类的；均匀的" },
  heterogeneous: { p: "/ˌhetərəˈdʒiːniəs/", pos: "adj.", d: "异质的；多元混合的" },
  incentivize: { p: "/ɪnˈsentɪvaɪz/", pos: "v.", d: "激励；奖励；促进" },
  jeopardize: { p: "/ˈdʒepədaɪz/", pos: "v.", d: "危及；损害" },
  lucrative: { p: "/ˈluːkrətɪv/", pos: "adj.", d: "获利丰厚的；赚大钱的" },
  monotonous: { p: "/məˈnɒtənəs/", pos: "adj.", d: "单调的；乏味的" },
  nostalgia: { p: "/nɒˈstældʒə/", pos: "n.", d: "怀旧；乡愁" },
  plausible: { p: "/ˈplɔːzəbl/", pos: "adj.", d: "看似合理的；合乎情理的" },
  pragmatic: { p: "/præɡˈmætɪk/", pos: "adj.", d: "务实的；注重实效的" },
  reconcile: { p: "/ˈrekənsaɪl/", pos: "v.", d: "使和解；调和；使一致" },
  spontaneous: { p: "/spɒnˈteɪniəs/", pos: "adj.", d: "自发的；自然的；未经刻意安排的" },
  tangible: { p: "/ˈtændʒəbl/", pos: "adj.", d: "有形的；切实的；可感知的" },
  unravel: { p: "/ʌnˈrævl/", pos: "v.", d: "解开；阐明；瓦解" },
  versatile: { p: "/ˈvɜːsətaɪl/", pos: "adj.", d: "多才多艺的；多功能的" },
  warrant: { p: "/ˈwɒrənt/", pos: "v./n.", d: "证明…是正当的；搜查令；凭单" },
};

async function fetchCachedJson(url, filename) {
  const filePath = path.join(CACHE_DIR, filename);
  if (fs.existsSync(filePath)) {
    console.log(`[Cache] Loading ${filename} from local cache...`);
    return JSON.parse(fs.readFileSync(filePath, "utf-8"));
  }
  console.log(`[Network] Fetching ${url}...`);
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    const data = await res.json();
    fs.writeFileSync(filePath, JSON.stringify(data, null, 2), "utf-8");
    return data;
  } catch (err) {
    console.warn(`[Warn] Failed to fetch ${url}: ${err.message}`);
    return null;
  }
}

async function main() {
  console.log("=== Generating Cloudflare Pages 26-Letter Dictionary Shards ===");

  const netemData = await fetchCachedJson(
    "https://raw.githubusercontent.com/exam-data/NETEMVocabulary/master/netem_full_list.json",
    "netem_full_list.json"
  );

  const cetData = await fetchCachedJson(
    "https://raw.githubusercontent.com/exam-data/CETVocabulary/master/cet_full_list.json",
    "cet_full_list.json"
  );

  // Master word pool: word -> { p?: string, pos?: string, d: string }
  const masterDict = new Map();

  // 1. Ingest NETEM Vocabulary (5530 words)
  const netemList = Array.isArray(netemData)
    ? netemData
    : netemData?.["5530考研词汇词频排序表"] || Object.values(netemData || {})[0] || [];

  if (Array.isArray(netemList)) {
    for (const item of netemList) {
      const word = (item["单词"] || "").trim().toLowerCase();
      const def = (item["释义"] || "").trim();
      if (word && /^[a-z]+(-[a-z]+)*$/.test(word)) {
        masterDict.set(word, {
          d: def,
          pos: item["子分类"] || item["分类"] || "",
        });
      }
    }
    console.log(`Ingested NETEM words: ${netemList.length}. Current master size: ${masterDict.size}`);
  }

  // 2. Ingest CET Vocabulary (5278 words)
  const cetList = Array.isArray(cetData)
    ? cetData
    : cetData?.["四六级词汇词频排序表"] || Object.values(cetData || {})[0] || [];

  if (Array.isArray(cetList)) {
    for (const item of cetList) {
      const word = (item["单词"] || "").trim().toLowerCase();
      const def = (item["释义"] || "").trim();
      if (word && /^[a-z]+(-[a-z]+)*$/.test(word)) {
        if (!masterDict.has(word)) {
          masterDict.set(word, {
            d: def,
            pos: item["六级"] ? "六级" : "四级",
          });
        }
      }
    }
    console.log(`Ingested CET words: ${cetList.length}. Current master size: ${masterDict.size}`);
  }

  // 3. Ingest Curated High-Frequency Kaoyan Words (with accurate phonetics)
  for (const [w, entry] of Object.entries(CURATED_KAOYAN)) {
    masterDict.set(w, {
      p: entry.p,
      pos: entry.pos,
      d: entry.d,
    });
  }

  console.log(`Total Master Dictionary Vocabulary Size: ${masterDict.size} words.`);

  // 4. Partition into 26 letters: 'a' through 'z'
  const letterBuckets = {};
  for (let i = 97; i <= 122; i++) {
    letterBuckets[String.fromCharCode(i)] = {};
  }

  for (const [word, info] of masterDict.entries()) {
    const firstChar = word[0];
    if (letterBuckets[firstChar]) {
      letterBuckets[firstChar][word] = info;
    }
  }

  // 5. Write to public/dict/a.json ~ z.json
  let totalBytes = 0;
  for (const letter of Object.keys(letterBuckets)) {
    const filePath = path.join(OUTPUT_DIR, `${letter}.json`);
    const content = JSON.stringify(letterBuckets[letter]);
    fs.writeFileSync(filePath, content, "utf-8");
    const bytes = Buffer.byteLength(content, "utf-8");
    totalBytes += bytes;
    console.log(
      `Saved ${letter}.json: ${Object.keys(letterBuckets[letter]).length} words (${(bytes / 1024).toFixed(1)} KB)`
    );
  }

  console.log(`\n✅ All 26 dictionary shards generated successfully! Total size: ${(totalBytes / 1024).toFixed(1)} KB`);
}

main().catch(console.error);
