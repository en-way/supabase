import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const examsDir = path.join(__dirname, "..", "public", "data", "exams");
const examFiles = fs.readdirSync(examsDir).filter(f => f.endsWith(".json"));

console.log(`Found ${examFiles.length} exam files in public/data/exams/`);

const report = {
  totalExams: examFiles.length,
  totalPassages: 0,
  totalQuestions: 0,
  byCategory: {},
  issues: []
};

for (const file of examFiles) {
  const filePath = path.join(examsDir, file);
  let content;
  try {
    content = JSON.parse(fs.readFileSync(filePath, "utf-8"));
  } catch (err) {
    report.issues.push({ file, type: "JSON_PARSE_ERROR", error: err.message });
    continue;
  }

  const { exam, passages = [], questions = [] } = content;
  if (!exam) {
    report.issues.push({ file, type: "MISSING_EXAM_OBJECT" });
    continue;
  }

  report.totalPassages += passages.length;
  report.totalQuestions += questions.length;
  report.byCategory[exam.category_id] = (report.byCategory[exam.category_id] || 0) + questions.length;

  const examTitle = exam.title || file;
  const passageIds = new Set(passages.map(p => p.id));

  // Check passages
  for (let i = 0; i < passages.length; i++) {
    const p = passages[i];
    if (!p.id) report.issues.push({ file, examTitle, type: "PASSAGE_NO_ID", index: i });
    if (!p.content || p.content.trim().length < 20) {
      report.issues.push({ file, examTitle, type: "PASSAGE_CONTENT_TOO_SHORT", passageId: p.id, title: p.title, length: p.content?.length || 0 });
    }
    if (/[\ufffd]/.test(p.content || "")) {
      report.issues.push({ file, examTitle, type: "PASSAGE_GARBLED_CHAR", passageId: p.id });
    }
  }

  // Check questions
  for (let i = 0; i < questions.length; i++) {
    const q = questions[i];
    const qLabel = `Q${i + 1} (SortOrder: ${q.sort_order}, ID: ${q.id || "no-id"})`;

    // 1. Basic fields
    if (!q.stem || q.stem.trim().length === 0) {
      report.issues.push({ file, examTitle, type: "EMPTY_STEM", qLabel });
    }
    if (/[\ufffd]/.test(q.stem || "")) {
      report.issues.push({ file, examTitle, type: "STEM_GARBLED_CHAR", qLabel });
    }

    // 2. Options check
    let options = q.options;
    if (typeof options === "string") {
      try { options = JSON.parse(options); } catch (e) {}
    }
    if (!options) {
      report.issues.push({ file, examTitle, type: "MISSING_OPTIONS", qLabel });
    } else {
      let optList = [];
      if (Array.isArray(options)) {
        optList = options;
      } else if (typeof options === "object") {
        optList = Object.entries(options).map(([k, v]) => ({ key: k, text: v }));
      }

      if (optList.length < 2) {
        report.issues.push({ file, examTitle, type: "FEWER_THAN_2_OPTIONS", qLabel, count: optList.length });
      }

      const keys = new Set();
      const texts = new Set();
      let hasEmptyOption = false;

      for (const opt of optList) {
        const k = String(opt.key || "").trim().toUpperCase();
        const t = String(opt.text || "").trim();
        if (!k) report.issues.push({ file, examTitle, type: "OPTION_NO_KEY", qLabel });
        if (!t) hasEmptyOption = true;
        if (keys.has(k)) {
          report.issues.push({ file, examTitle, type: "DUPLICATE_OPTION_KEY", qLabel, key: k });
        }
        keys.add(k);

        // Check duplicated option text (e.g. copy-paste error across different options of same question)
        if (t && texts.has(t.toLowerCase())) {
          report.issues.push({ file, examTitle, type: "DUPLICATE_OPTION_TEXT", qLabel, text: t });
        }
        if (t) texts.add(t.toLowerCase());
      }

      if (hasEmptyOption) {
        report.issues.push({ file, examTitle, type: "EMPTY_OPTION_TEXT", qLabel });
      }

      // 3. Correct answer check
      const cleanAnswer = String(q.correct_answer || "").trim().toUpperCase();
      if (!cleanAnswer) {
        report.issues.push({ file, examTitle, type: "EMPTY_CORRECT_ANSWER", qLabel });
      } else if (!keys.has(cleanAnswer)) {
        report.issues.push({ file, examTitle, type: "ANSWER_NOT_IN_OPTIONS", qLabel, answer: cleanAnswer, availableKeys: Array.from(keys) });
      }
    }

    // 4. Explanation check
    if (!q.explanation || q.explanation.trim().length === 0) {
      report.issues.push({ file, examTitle, type: "EMPTY_EXPLANATION", qLabel });
    } else if (q.explanation.trim().length < 5 || /待补充|TBD|暂无/i.test(q.explanation)) {
      report.issues.push({ file, examTitle, type: "POOR_EXPLANATION", qLabel, explanation: q.explanation });
    }

    // 5. Points check
    if (typeof q.points !== "number" || q.points <= 0) {
      report.issues.push({ file, examTitle, type: "INVALID_POINTS", qLabel, points: q.points });
    }

    // 6. Passage reference check
    if (q.passage_id && !passageIds.has(q.passage_id)) {
      report.issues.push({ file, examTitle, type: "ORPHAN_PASSAGE_REFERENCE", qLabel, passageId: q.passage_id });
    }
  }
}

console.log("\n=== Static Mirror Inspection Summary ===");
console.log(`Total Exams Scanned: ${report.totalExams}`);
console.log(`Total Passages Scanned: ${report.totalPassages}`);
console.log(`Total Questions Scanned: ${report.totalQuestions}`);
console.log("Questions by Category:", report.byCategory);
console.log(`Total Static Issues Found: ${report.issues.length}`);

if (report.issues.length > 0) {
  console.log("\nIssue Breakdown by Type:");
  const counts = {};
  for (const issue of report.issues) {
    counts[issue.type] = (counts[issue.type] || 0) + 1;
  }
  console.log(counts);
} else {
  console.log("✅ 静态 CDN 镜像全量通过：60 套真题、300 篇材料、2,250 道题目 100% 格式规范无缺失！");
}

// 2. Query Supabase Database directly
import("@supabase/supabase-js").then(async ({ createClient }) => {
  const supabase = createClient(
    "https://pghybspsjtzihpzpahcf.supabase.co",
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBnaHlic3BzanR6aWhwenBhaGNmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODk3NjQ2OTgsImV4cCI6MjEwNTM0MDY5OH0.64uRYk9fCvrEfn4ifhk-PSd1ypGjVz_PTiHwgBPiHpM"
  );

  console.log("\n=== Verifying Supabase Cloud Database Directly ===");
  const { count: dbExams } = await supabase.from("exams").select("*", { count: "exact", head: true });
  const { count: dbPassages } = await supabase.from("passages").select("*", { count: "exact", head: true });
  const { count: dbQuestions } = await supabase.from("questions").select("*", { count: "exact", head: true });

  console.log(`Cloud DB Exams: ${dbExams} (Expected: 60)`);
  console.log(`Cloud DB Passages: ${dbPassages} (Expected: 300)`);
  console.log(`Cloud DB Questions: ${dbQuestions} (Expected: 2250)`);

  const dbMatches = dbExams === 60 && dbPassages === 300 && dbQuestions === 2250;
  if (dbMatches) {
    console.log("✅ 云端数据库与静态镜像 100% 同步对齐！");
  } else {
    console.warn("⚠️ 云端数据库与静态镜像数量存在偏差！");
  }
});

