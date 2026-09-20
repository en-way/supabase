// CET-4 & CET-6 Section A (选词填空) & Section B (长篇段落信息匹配) 2015-2024 完整真题语料与考点库

function formatWordBank(words) {
  return words.map((w, idx) => ({
    key: String.fromCharCode(65 + idx),
    text: w
  }));
}

function formatParagraphOptions(count = 11) {
  return Array.from({ length: count }, (_, idx) => {
    const key = String.fromCharCode(65 + idx);
    return { key, text: `[${key}] 段落 ${key}` };
  });
}

// 辅助创建 Section A
export function makeBankedCloze({ title, article, words, answers, explanations }) {
  const options = formatWordBank(words);
  const questions = answers.map((ans, idx) => ({
    q_type: "banked_cloze",
    stem: `Choose the best word for blank (${26 + idx}) in the passage:`,
    options,
    correct_answer: ans,
    explanation: explanations[idx],
    points: 1.5,
    sort_order: idx + 1
  }));
  return {
    section_type: "banked_cloze",
    title: title || "Section A: Banked Cloze (选词填空 26-35题)",
    content: article,
    questions
  };
}

// 辅助创建 Section B
export function makeMatching({ title, article, statements, answers, explanations, count = 11 }) {
  const options = formatParagraphOptions(count);
  const questions = statements.map((stmt, idx) => ({
    q_type: "matching_item",
    stem: `(${36 + idx}) ${stmt}`,
    options,
    correct_answer: answers[idx],
    explanation: explanations[idx],
    points: 3.5,
    sort_order: 10 + idx + 1
  }));
  return {
    section_type: "matching",
    title: title || "Section B: Long Reading & Information Matching (长篇段落信息匹配 36-45题)",
    content: article,
    questions
  };
}
