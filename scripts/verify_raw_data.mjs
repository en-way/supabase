import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const dataRoot = path.join(__dirname, "..", "data");
const folders = ["cet4", "cet6", "kaoyan"];

let totalFiles = 0;
let totalPassages = 0;
let totalQuestions = 0;
let rawIssues = [];

for (const folder of folders) {
  const dirPath = path.join(dataRoot, folder);
  if (!fs.existsSync(dirPath)) continue;

  const files = fs.readdirSync(dirPath).filter(f => f.endsWith(".json"));
  totalFiles += files.length;

  for (const file of files) {
    const full = path.join(dirPath, file);
    try {
      const data = JSON.parse(fs.readFileSync(full, "utf-8"));
      const passages = data.passages || [];
      totalPassages += passages.length;

      for (const p of passages) {
        const questions = p.questions || [];
        totalQuestions += questions.length;
        for (const q of questions) {
          if (!q.stem) rawIssues.push({ file, err: "missing stem" });
          if (!q.correct_answer) rawIssues.push({ file, err: "missing correct_answer" });
          if (!q.explanation) rawIssues.push({ file, err: "missing explanation" });
          if (!q.options || q.options.length < 2) rawIssues.push({ file, err: "options invalid" });
        }
      }
    } catch (e) {
      rawIssues.push({ file, err: e.message });
    }
  }
}

console.log("=== Raw Source Datasets Inspection ===");
console.log(`Scanned ${totalFiles} raw files in data/`);
console.log(`Total Passages: ${totalPassages}`);
console.log(`Total Questions: ${totalQuestions}`);
console.log(`Raw Issues: ${rawIssues.length}`);
if (rawIssues.length === 0) {
  console.log("✅ 原始数据源（Git-Tracked data/ 目录）全部 100% 格式无误！");
} else {
  console.log("Issues:", rawIssues);
}
