import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { createClient } from "@supabase/supabase-js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const SUPABASE_URL = process.env.NEXT_PUBLIC_SUPABASE_URL || "https://pghybspsjtzihpzpahcf.supabase.co";
const SUPABASE_ANON_KEY = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBnaHlic3BzanR6aWhwenBhaGNmIiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODk3NjQ2OTgsImV4cCI6MjEwNTM0MDY5OH0.64uRYk9fCvrEfn4ifhk-PSd1ypGjVz_PTiHwgBPiHpM";

const supabase = createClient(SUPABASE_URL, SUPABASE_ANON_KEY);

const DATA_DIR = path.join(__dirname, "..", "public", "data");
const EXAMS_DATA_DIR = path.join(DATA_DIR, "exams");

if (!fs.existsSync(DATA_DIR)) fs.mkdirSync(DATA_DIR, { recursive: true });
if (!fs.existsSync(EXAMS_DATA_DIR)) fs.mkdirSync(EXAMS_DATA_DIR, { recursive: true });

async function main() {
  console.log("=== Exporting Kaoyan Real Exams to Cloudflare Pages Static Mirror ===");

  // 1. Fetch categories
  console.log("Fetching categories...");
  const { data: categories, error: catErr } = await supabase
    .from("categories")
    .select("*")
    .order("sort_order");
  if (catErr) throw catErr;

  fs.writeFileSync(
    path.join(DATA_DIR, "categories.json"),
    JSON.stringify(categories, null, 2),
    "utf-8"
  );
  console.log(`Saved categories.json (${categories.length} categories)`);

  // 2. Fetch approved & published exams
  console.log("Fetching exams list with counts...");
  const { data: exams, error: examErr } = await supabase
    .from("exams")
    .select(`
      *,
      questions(count),
      passages(count)
    `)
    .eq("is_published", true)
    .eq("approval_status", "approved")
    .order("year", { ascending: false });
  if (examErr) throw examErr;

  fs.writeFileSync(
    path.join(DATA_DIR, "exams.json"),
    JSON.stringify(exams, null, 2),
    "utf-8"
  );
  console.log(`Saved exams.json (${exams.length} published exams)`);

  // 3. For each exam, fetch its passages and questions, then write to public/data/exams/{id}.json
  let totalExamsExported = 0;
  let totalPassagesExported = 0;
  let totalQuestionsExported = 0;

  for (const exam of exams) {
    const examId = exam.id;
    console.log(`Exporting exam [${exam.year} ${exam.title}] (${examId})...`);

    const [pRes, qRes] = await Promise.all([
      supabase
        .from("passages")
        .select("*")
        .eq("exam_id", examId)
        .order("sort_order"),
      supabase
        .from("questions")
        .select("*")
        .eq("exam_id", examId)
        .order("sort_order"),
    ]);

    if (pRes.error) console.error(`Error fetching passages for ${examId}:`, pRes.error);
    if (qRes.error) console.error(`Error fetching questions for ${examId}:`, qRes.error);

    const passages = pRes.data || [];
    const questions = qRes.data || [];

    const examPayload = {
      exam,
      passages,
      questions,
      exportedAt: new Date().toISOString(),
    };

    const outPath = path.join(EXAMS_DATA_DIR, `${examId}.json`);
    fs.writeFileSync(outPath, JSON.stringify(examPayload), "utf-8");

    totalExamsExported++;
    totalPassagesExported += passages.length;
    totalQuestionsExported += questions.length;
  }

  console.log(`\n✅ Static Mirror Export Complete!`);
  console.log(`- Total Exams: ${totalExamsExported}`);
  console.log(`- Total Passages: ${totalPassagesExported}`);
  console.log(`- Total Questions: ${totalQuestionsExported}`);
  console.log(`- Destination: public/data/exams/{id}.json`);
}

main().catch(console.error);
