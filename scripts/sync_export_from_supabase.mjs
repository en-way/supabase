import fs from "fs";
import path from "path";
import { execFileSync } from "child_process";
import { fileURLToPath } from "url";
import { createClient } from "@supabase/supabase-js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// 1. 读取环境配置 (支持本地 .env 和 GitHub Actions 环境变量)
function loadEnv() {
  const envPath = path.join(__dirname, "..", ".env");
  const envLocalPath = path.join(__dirname, "..", ".env.local");
  const env = { ...process.env };

  const readEnvFile = (p) => {
    if (fs.existsSync(p)) {
      const lines = fs.readFileSync(p, "utf-8").split("\n");
      for (const line of lines) {
        const trimmed = line.trim();
        if (!trimmed || trimmed.startsWith("#")) continue;
        const eqIdx = trimmed.indexOf("=");
        if (eqIdx !== -1) {
          const k = trimmed.substring(0, eqIdx).trim();
          let v = trimmed.substring(eqIdx + 1).trim();
          if ((v.startsWith('"') && v.endsWith('"')) || (v.startsWith("'") && v.endsWith("'"))) {
            v = v.slice(1, -1);
          }
          if (!env[k]) env[k] = v;
        }
      }
    }
  };

  readEnvFile(envLocalPath);
  readEnvFile(envPath);
  return env;
}

const env = loadEnv();
const SUPABASE_URL = env.SUPABASE_URL || env.NEXT_PUBLIC_SUPABASE_URL || "https://pghybspsjtzihpzpahcf.supabase.co";
// 优先使用 SERVICE_ROLE_KEY 穿透 RLS 确保能够完整拉取已审核真题
const SUPABASE_KEY = env.SUPABASE_SERVICE_ROLE_KEY || env.SUPABASE_ANON_KEY || env.NEXT_PUBLIC_SUPABASE_ANON_KEY;

if (!SUPABASE_KEY) {
  console.error("❌ 错误: 未找到有效 Supabase 密钥，请在 .env 或环境变量中配置 SUPABASE_SERVICE_ROLE_KEY");
  process.exit(1);
}

if (!env.SUPABASE_SERVICE_ROLE_KEY) {
  console.warn(
    "⚠️ 警告: 未检测到 SUPABASE_SERVICE_ROLE_KEY，当前回退使用 ANON_KEY，若受 RLS 策略限制可能无法拉取完整表数据。"
  );
}

const supabase = createClient(SUPABASE_URL, SUPABASE_KEY);

const DATA_DIR = path.join(__dirname, "..", "public", "data");
const EXAMS_DATA_DIR = path.join(DATA_DIR, "exams");

if (!fs.existsSync(DATA_DIR)) fs.mkdirSync(DATA_DIR, { recursive: true });
if (!fs.existsSync(EXAMS_DATA_DIR)) fs.mkdirSync(EXAMS_DATA_DIR, { recursive: true });

function writeJsonIfChanged(filePath, nextContent) {
  if (fs.existsSync(filePath)) {
    try {
      const currentContent = fs.readFileSync(filePath, "utf-8");
      if (currentContent === nextContent) {
        return false;
      }
    } catch {}
  }
  fs.writeFileSync(filePath, nextContent, "utf-8");
  return true;
}

function isExamSemanticEqual(filePath, semanticPayload) {
  if (!fs.existsSync(filePath)) return false;
  try {
    const existing = JSON.parse(fs.readFileSync(filePath, "utf-8"));
    const existingSemantic = {
      exam: existing?.exam,
      passages: existing?.passages,
      questions: existing?.questions,
    };
    return JSON.stringify(existingSemantic) === JSON.stringify(semanticPayload);
  } catch {
    return false;
  }
}

async function main() {
  console.log("=".repeat(70));
  console.log("🚀 [Supabase -> 边缘镜像] 全自动化题库拉取与发布流水线启动");
  console.log(`🔗 目标云端: ${SUPABASE_URL}`);
  console.log("=".repeat(70));

  // 1. 获取分类列表
  console.log("📥 [1/4] 正在拉取试卷分类 (Categories)...");
  const { data: categories, error: catErr } = await supabase
    .from("categories")
    .select("*")
    .order("sort_order", { ascending: true })
    .order("id", { ascending: true });
  if (catErr) throw new Error(`拉取分类失败: ${catErr.message}`);
  if (!Array.isArray(categories) || categories.length === 0) {
    throw new Error("Zero-Wipe 熔断触发: categories 查询结果为空，已中止覆盖静态镜像。");
  }

  const catWritten = writeJsonIfChanged(
    path.join(DATA_DIR, "categories.json"),
    JSON.stringify(categories, null, 2)
  );
  console.log(`  ✓ ${catWritten ? "成功保存" : "无变化跳过"} categories.json (${categories.length} 个分类)`);

  // 2. 获取已发布真题总目录
  console.log("📥 [2/4] 正在拉取考卷目录索引 (Exams)...");
  const { data: exams, error: examErr } = await supabase
    .from("exams")
    .select(`
      *,
      questions(count),
      passages(count)
    `)
    .eq("is_published", true)
    .eq("approval_status", "approved")
    .order("year", { ascending: false })
    .order("category_id", { ascending: true })
    .order("id", { ascending: true });
  if (examErr) throw new Error(`拉取考卷目录失败: ${examErr.message}`);
  if (!Array.isArray(exams) || exams.length === 0) {
    throw new Error("Zero-Wipe 熔断触发: exams 查询结果为空，已中止写入与孤儿文件清理。");
  }

  const standardizedExams = exams.map((e) => ({
    ...e,
    duration_minutes: 75,
    passages: e.year === 2001 && e.category_id === "ky1" && e.passages?.[0]
      ? [{ count: 6 }]
      : e.passages,
  }));

  const examsWritten = writeJsonIfChanged(
    path.join(DATA_DIR, "exams.json"),
    JSON.stringify(standardizedExams, null, 2)
  );
  console.log(`  ✓ ${examsWritten ? "成功保存" : "无变化跳过"} exams.json (${standardizedExams.length} 套正式发布的真题，全量客观题 75 分钟限时)`);

  // 3. 逐卷拉取篇章与试题并落盘
  console.log("📥 [3/4] 正在逐卷同步篇章 (Passages) 与试题解析 (Questions)...");
  let totalPassages = 0;
  let totalQuestions = 0;
  let changedFilesCount = 0;

  for (let i = 0; i < exams.length; i++) {
    const exam = exams[i];
    const examId = exam.id;
    process.stdout.write(`  [${i + 1}/${exams.length}] 同步 ${exam.year} ${exam.title}... `);

    const [pRes, qRes] = await Promise.all([
      supabase
        .from("passages")
        .select("*")
        .eq("exam_id", examId)
        .order("sort_order", { ascending: true })
        .order("id", { ascending: true }),
      supabase
        .from("questions")
        .select("*")
        .eq("exam_id", examId)
        .order("sort_order", { ascending: true })
        .order("id", { ascending: true }),
    ]);

    if (pRes.error) throw new Error(`拉取篇章失败 (${examId}): ${pRes.error.message}`);
    if (qRes.error) throw new Error(`拉取试题失败 (${examId}): ${qRes.error.message}`);

    const passages = pRes.data || [];
    const questions = (qRes.data || []).map((q) => {
      const ans = (q.correct_answer || q.answer || "").trim();
      return {
        ...q,
        answer: ans,
        correct_answer: ans,
      };
    });

    const semanticPayload = {
      exam: {
        ...exam,
        duration_minutes: 75,
      },
      passages,
      questions,
    };

    const outPath = path.join(EXAMS_DATA_DIR, `${examId}.json`);
    let written = false;
    if (!isExamSemanticEqual(outPath, semanticPayload)) {
      written = writeJsonIfChanged(outPath, JSON.stringify(semanticPayload, null, 2) + "\n");
    }
    if (written) changedFilesCount += 1;

    totalPassages += passages.length;
    totalQuestions += questions.length;
    console.log(`${written ? "✓ 更新" : "＝ 无变化"} (${passages.length} 篇章, ${questions.length} 试题)`);
  }

  // 3.5 清理已下架/未发布的孤儿试卷 JSON 文件 (Orphaned JSON Cleanup)
  console.log("\n🧹 [3.5/4] 正在扫描并清理已下架或删除的孤儿试卷静态文件...");
  const validExamIdSet = new Set(exams.map((e) => `${e.id}.json`));
  const existingFiles = fs.readdirSync(EXAMS_DATA_DIR);
  let cleanedCount = 0;
  for (const file of existingFiles) {
    if (file.endsWith(".json") && !validExamIdSet.has(file)) {
      const orphanPath = path.join(EXAMS_DATA_DIR, file);
      fs.unlinkSync(orphanPath);
      console.log(`  🗑️ 清除已下架试卷静态文件: ${file}`);
      cleanedCount += 1;
    }
  }
  if (cleanedCount === 0) {
    console.log("  ✓ 本地静态目录干净，无孤儿试卷残留。");
  } else {
    console.log(`  ✓ 成功清除 ${cleanedCount} 个已下架试卷文件。`);
  }

  console.log(
    `\n🎉 数据落地完成: 共同步 ${exams.length} 套真题（本次更新 ${changedFilesCount} 卷）、${totalPassages} 篇文章、${totalQuestions} 道试题。`
  );

  // 4. 自动化质量与安全门控 (Quality & Security Gate)
  console.log("\n🛡️ [4/4] 正在执行全量质量校准与系统安全断言...");
  const pythonBin = process.platform === "win32" ? "python" : "python3";
  const verifyGates = [
    {
      name: "118项法医级文本校对断言",
      script: path.join(__dirname, "verify_deep_text_calibration.py"),
    },
    {
      name: "12项安全防线与韧性断言",
      script: path.join(__dirname, "verify_system_security_and_resilience.py"),
    },
  ];

  for (const gate of verifyGates) {
    try {
      const output = execFileSync(pythonBin, [gate.script], { encoding: "utf-8" });
      console.log(output.trim());
      console.log(`  ✅ [${gate.name}] 100% 通过！`);
    } catch (err) {
      console.error(`❌ 质量/安全门控拦截 (${gate.name}): 检测到异常，已中止发布！`);
      if (err.stdout) console.error(err.stdout);
      if (err.stderr) console.error(err.stderr);
      process.exit(1);
    }
  }

  // 5. 自动刷新静态版本哈希
  console.log("\n🔄 正在检查并更新静态版本号...");
  const versionScript = path.join(__dirname, "generate_static_version.mjs");
  execFileSync("node", [versionScript], { stdio: "inherit" });

  console.log("\n" + "=".repeat(70));
  console.log("🏁 全自动同步流水线执行完毕！所有静态真题镜像已完全就绪。");
  console.log("=".repeat(70));
}

main().catch((err) => {
  console.error("❌ 流水线执行失败:", err);
  process.exit(1);
});
