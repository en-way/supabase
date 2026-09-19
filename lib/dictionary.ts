export interface DictEntry {
  phonetic?: string;
  pos: string; // n., v., adj., adv.
  definition: string;
}

// Built-in offline high-frequency CET-4/6 and Kaoyan core dictionary
export const CORE_DICTIONARY: Record<string, DictEntry> = {
  agriculture: { phonetic: "/ˈæɡrɪkʌltʃər/", pos: "n.", definition: "农业；农学" },
  conventional: { phonetic: "/kənˈvenʃənl/", pos: "adj.", definition: "传统的；惯例的" },
  logistical: { phonetic: "/ləˈdʒɪstɪkl/", pos: "adj.", definition: "后勤方面的；物流的" },
  ecological: { phonetic: "/ˌiːkəˈlɒdʒɪkl/", pos: "adj.", definition: "生态的；生态学的" },
  emission: { phonetic: "/ɪˈmɪʃn/", pos: "n.", definition: "散发；排放（物）" },
  vulnerability: { phonetic: "/ˌvʌlnərəˈbɪləti/", pos: "n.", definition: "脆弱性；易受损性" },
  disruption: { phonetic: "/dɪsˈrʌpʃn/", pos: "n.", definition: "中断；扰乱" },
  hydroponics: { phonetic: "/ˌhaɪdrəˈpɒnɪks/", pos: "n.", definition: "水耕法；水培法" },
  conserve: { phonetic: "/kənˈsɜːv/", pos: "v.", definition: "保护；节约；保存" },
  agrarian: { phonetic: "/əˈɡreəriən/", pos: "adj.", definition: "土地的；农业的" },
  mitigate: { phonetic: "/ˈmɪtɪɡeɪt/", pos: "v.", definition: "缓解；减轻；缓和" },
  infrastructure: { phonetic: "/ˈɪnfrəstrʌktʃər/", pos: "n.", definition: "基础设施；公共建设" },
  expenditure: { phonetic: "/ɪkˈspendɪtʃər/", pos: "n.", definition: "开支；支出；花费" },
  prohibitive: { phonetic: "/prəˈhɪbətɪv/", pos: "adj.", definition: "（价格等）高得令人望而却步的；禁止性的" },
  regulatory: { phonetic: "/ˈreɡjələtəri/", pos: "adj.", definition: "监管的；管理的" },
  bureaucratic: { phonetic: "/ˌbjʊərəˈkrætɪk/", pos: "adj.", definition: "官僚主义的；繁文缛节的" },
  resilience: { phonetic: "/rɪˈzɪliəns/", pos: "n.", definition: "恢复力；韧性；适应力" },
  sovereignty: { phonetic: "/ˈsɒvrənti/", pos: "n.", definition: "主权；自主统治权" },
  deprivation: { phonetic: "/ˌdeprɪˈveɪʃn/", pos: "n.", definition: "剥夺；丧失；缺乏" },
  epidemic: { phonetic: "/ˌepɪˈdemɪk/", pos: "n./adj.", definition: "流行病；盛行；大范围普及的" },
  cognitive: { phonetic: "/ˈkɒɡnətɪv/", pos: "adj.", definition: "认知的；感知的" },
  metabolic: { phonetic: "/ˌmetəˈbɒlɪk/", pos: "adj.", definition: "新陈代谢的" },
  neurodegenerative: { phonetic: "/ˌnjʊərəʊdɪˈdʒenərətɪv/", pos: "adj.", definition: "神经退行性的" },
  consolidation: { phonetic: "/kənˌsɒlɪˈdeɪʃn/", pos: "n.", definition: "巩固；强化；合并" },
  unintentional: { phonetic: "/ˌʌnɪnˈtenʃənl/", pos: "adj.", definition: "无意的；非故意的" },
  monopoly: { phonetic: "/məˈnɒpəli/", pos: "n.", definition: "垄断；专卖；独占" },
  doctrine: { phonetic: "/ˈdɒktrɪn/", pos: "n.", definition: "教义；主义；原则；信条" },
  infringement: { phonetic: "/ɪnˈfrɪndʒmənt/", pos: "n.", definition: "侵犯；违反；侵权" },
  conglomerate: { phonetic: "/kənˈɡlɒmərət/", pos: "n.", definition: "大型企业集团；联合企业" },
  verbatim: { phonetic: "/vɜːˈbeɪtɪm/", pos: "adv./adj.", definition: "逐字逐句地；一字不差的" },
  conflate: { phonetic: "/kənˈfleɪt/", pos: "v.", definition: "合并；混淆；混合" },
  assimilation: { phonetic: "/əˌsɪməˈleɪʃn/", pos: "n.", definition: "吸收；同化" },
  cannibalize: { phonetic: "/ˈkænɪbəlaɪz/", pos: "v.", definition: "自相残杀；侵蚀（自身市场/利益）" },
  judicial: { phonetic: "/dʒuˈdɪʃl/", pos: "adj.", definition: "司法的；审判的" },
  unfettered: { phonetic: "/ʌnˈfetəd/", pos: "adj.", definition: "不受约束的；自由无拘的" },
  stringent: { phonetic: "/ˈstrɪndʒənt/", pos: "adj.", definition: "严格的；严厉的；紧缩的" },
  behemoth: { phonetic: "/bɪˈhiːmɒθ/", pos: "n.", definition: "巨兽；庞然大物（如科技巨头）" },
  statutory: { phonetic: "/ˈstætʃətri/", pos: "adj.", definition: "法定的；依法制定的" },
  sustainable: { phonetic: "/səˈsteɪnəbl/", pos: "adj.", definition: "可持续的；合理利用的" },
  contemporary: { phonetic: "/kənˈtemprəri/", pos: "adj./n.", definition: "当代的；同时代的；同代人" },
  deficit: { phonetic: "/ˈdefɪsɪt/", pos: "n.", definition: "赤字；亏损；不足；缺乏" },
  hygiene: { phonetic: "/ˈhaɪdʒiːn/", pos: "n.", definition: "卫生；保健法" },
  monopolistic: { phonetic: "/məˌnɒpəˈlɪstɪk/", pos: "adj.", definition: "垄断的；独占性的" },
  incentive: { phonetic: "/ɪnˈsentɪv/", pos: "n.", definition: "激励；奖励；诱因" },
  dispute: { phonetic: "/dɪˈspjuːt/", pos: "n./v.", definition: "辩论；争端；争议" },
  royalty: { phonetic: "/ˈrɔɪəlti/", pos: "n.", definition: "版税；特许权使用费；王室" },
  imperative: { phonetic: "/ɪmˈperətɪv/", pos: "adj./n.", definition: "极其重要的；必要的；当务之急" },
  eliminate: { phonetic: "/ɪˈlɪmɪneɪt/", pos: "v.", definition: "排除；消除；淘汰" },
  provisional: { phonetic: "/prəˈvɪʒənl/", pos: "adj.", definition: "临时的；暂时的" },
  negligible: { phonetic: "/ˈneɡlɪdʒəbl/", pos: "adj.", definition: "微不足道的；可以忽略的" },
  beneficial: { phonetic: "/ˌbenɪˈfɪʃl/", pos: "adj.", definition: "有益的；有利的" },
  consequence: { phonetic: "/ˈkɒnsɪkwəns/", pos: "n.", definition: "后果；重要性" },
  precaution: { phonetic: "/prɪˈkɔːʃn/", pos: "n.", definition: "预防措施；防备" },
  detriment: { phonetic: "/ˈdetrɪmənt/", pos: "n.", definition: "损害；伤害；造成伤害的事物" }
};

export function lookupWord(rawWord: string): DictEntry | null {
  if (!rawWord) return null;
  // Clean word: lower, strip quotes, commas, dots
  let clean = rawWord.toLowerCase().replace(/[^a-z-]/g, "");
  if (!clean) return null;

  // Direct match
  if (CORE_DICTIONARY[clean]) {
    return CORE_DICTIONARY[clean];
  }

  // Stemming fallbacks
  // Plural -s / -es
  if (clean.endsWith("s") && CORE_DICTIONARY[clean.slice(0, -1)]) {
    return CORE_DICTIONARY[clean.slice(0, -1)];
  }
  if (clean.endsWith("es") && CORE_DICTIONARY[clean.slice(0, -2)]) {
    return CORE_DICTIONARY[clean.slice(0, -2)];
  }
  // Past -ed
  if (clean.endsWith("ed") && CORE_DICTIONARY[clean.slice(0, -2)]) {
    return CORE_DICTIONARY[clean.slice(0, -2)];
  }
  if (clean.endsWith("ed") && CORE_DICTIONARY[clean.slice(0, -1)]) {
    return CORE_DICTIONARY[clean.slice(0, -1)];
  }
  // -ing
  if (clean.endsWith("ing") && CORE_DICTIONARY[clean.slice(0, -3)]) {
    return CORE_DICTIONARY[clean.slice(0, -3)];
  }
  if (clean.endsWith("ing") && CORE_DICTIONARY[clean.slice(0, -3) + "e"]) {
    return CORE_DICTIONARY[clean.slice(0, -3) + "e"];
  }
  // -ly
  if (clean.endsWith("ly") && CORE_DICTIONARY[clean.slice(0, -2)]) {
    return CORE_DICTIONARY[clean.slice(0, -2)];
  }

  // Default fallback if not in offline seed
  return {
    pos: "word",
    definition: `[${clean}] (在当前语境中出现，点击“加入生词本”可在生词本中复习)`
  };
}
