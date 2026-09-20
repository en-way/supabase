import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { allKaoyanExams } from "./data/kaoyan/index.mjs";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, "..");

const CET4_DIR = path.join(ROOT_DIR, "data", "cet4");
const CET6_DIR = path.join(ROOT_DIR, "data", "cet6");
const KAOYAN_DIR = path.join(ROOT_DIR, "data", "kaoyan");

if (!fs.existsSync(KAOYAN_DIR)) fs.mkdirSync(KAOYAN_DIR, { recursive: true });

// --- Helper to build Section A Banked Cloze ---
export function buildBankedCloze({ title, articleWithBlanks, wordBank, answers, explanations }) {
  // wordBank: array of 15 strings like "A) arbitrary", "B) boost"... or words
  const options = wordBank.map((wb, idx) => {
    const key = String.fromCharCode(65 + idx);
    const text = wb.replace(/^[A-O]\)\s*/, "").trim();
    return { key, text };
  });

  const questions = answers.map((ans, idx) => {
    const blankNum = 26 + idx;
    return {
      q_type: "cloze_item",
      stem: `Choose the best word for blank (${blankNum}) in the passage:`,
      options,
      correct_answer: ans,
      explanation: explanations[idx] || `【考点精析】空格(${blankNum})：根据上下文句法结构与语义搭配，应填入 ${ans} 项。`,
      points: 1.5,
      sort_order: idx + 1
    };
  });

  return {
    section_type: "cloze",
    title: title || "Section A: Banked Cloze (选词填空 26-35题)",
    content: articleWithBlanks,
    questions
  };
}

// --- Helper to build Section B Information Matching ---
export function buildMatching({ title, articleWithParagraphs, statements, answers, explanations, paraCount = 11 }) {
  // Paragraph options A to K/L
  const options = Array.from({ length: paraCount }, (_, idx) => {
    const key = String.fromCharCode(65 + idx);
    return { key, text: `[${key}] 段落 ${key}` };
  });

  const questions = statements.map((stmt, idx) => {
    const qNum = 36 + idx;
    return {
      q_type: "reading_item",
      stem: `(${qNum}) ${stmt}`,
      options,
      correct_answer: answers[idx],
      explanation: explanations[idx] || `【考点精析】题目(${qNum})对应原文段落 [${answers[idx]}]，句中核心词汇与段落主旨互为同义替换。`,
      points: 3.5,
      sort_order: 10 + idx + 1
    };
  });

  return {
    section_type: "reading",
    title: title || "Section B: Long Reading & Information Matching (长篇段落信息匹配 36-45题)",
    content: articleWithParagraphs,
    questions
  };
}

// --- Helper to build Kaoyan Part B New Type ---
export function buildKaoyanPartB({ title, content, typeName, questionsData }) {
  // questionsData: [{ stem, options, correct_answer, explanation }]
  const questions = questionsData.map((q, idx) => ({
    q_type: "reading_item",
    stem: q.stem || `Question ${41 + idx}:`,
    options: q.options,
    correct_answer: q.correct_answer,
    explanation: q.explanation,
    points: 2.0,
    sort_order: 40 + idx + 1
  }));

  return {
    section_type: "new_type",
    title: title || `Section II: Reading Comprehension Part B (${typeName || "新题型 41-45题"})`,
    content,
    questions
  };
}
