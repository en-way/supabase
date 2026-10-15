import fs from "fs";
import path from "path";
import { execSync } from "child_process";
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

const supabase = createClient(SUPABASE_URL, SUPABASE_KEY);

const DATA_DIR = path.join(__dirname, "..", "public", "data");
const EXAMS_DATA_DIR = path.join(DATA_DIR, "exams");

if (!fs.existsSync(DATA_DIR)) fs.mkdirSync(DATA_DIR, { recursive: true });
if (!fs.existsSync(EXAMS_DATA_DIR)) fs.mkdirSync(EXAMS_DATA_DIR, { recursive: true });

async function main() {
  console.log("=" .repeat(70));
  console.log("🚀 [Supabase -> 边缘镜像] 全自动化题库拉取与发布流水线启动");
  console.log(`🔗 目标云端: ${SUPABASE_URL}`);
  console.log("=" .repeat(70));

  // 1. 获取分类列表
  console.log("📥 [1/4] 正在拉取试卷分类 (Categories)...");
  const { data: categories, error: catErr } = await supabase
    .from("categories")
    .select("*")
    .order("sort_order");
  if (catErr) throw new Error(`拉取分类失败: ${catErr.message}`);

  fs.writeFileSync(
    path.join(DATA_DIR, "categories.json"),
    JSON.stringify(categories, null, 2),
    "utf-8"
  );
  console.log(`  ✓ 成功保存 categories.json (${categories.length} 个分类)`);

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
    .order("year", { ascending: false });
  if (examErr) throw new Error(`拉取考卷目录失败: ${examErr.message}`);

  fs.writeFileSync(
    path.join(DATA_DIR, "exams.json"),
    JSON.stringify(exams, null, 2),
    "utf-8"
  );
  console.log(`  ✓ 成功保存 exams.json (${exams.length} 套正式发布的真题)`);

  // 3. 逐卷拉取篇章与试题并落盘
  console.log("📥 [3/4] 正在逐卷同步篇章 (Passages) 与试题解析 (Questions)...");
  let totalPassages = 0;
  let totalQuestions = 0;

  for (let i = 0; i < exams.length; i++) {
    const exam = exams[i];
    const examId = exam.id;
    process.stdout.write(`  [${i + 1}/${exams.length}] 同步 ${exam.year} ${exam.title}... `);

    const [pRes, qRes] = await Promise.all([
      supabase
        .from("passages")
        .select("*")
        .eq("exam_id", examId)
        .order("sort_order", { ascending: true }),
      supabase
        .from("questions")
        .select("*")
        .eq("exam_id", examId)
        .order("sort_order", { ascending: true }),
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

    const examPayload = {
      exam,
      passages,
      questions,
      exportedAt: new Date().toISOString(),
    };

    const outPath = path.join(EXAMS_DATA_DIR, `${examId}.json`);
    fs.writeFileSync(outPath, JSON.stringify(examPayload, null, 2), "utf-8");

    totalPassages += passages.length;
    totalQuestions += questions.length;
    console.log(`✓ (${passages.length} 篇章, ${questions.length} 试题)`);
  }

  console.log(`\n🎉 数据落地完成: 共同步 ${exams.length} 套真题、${totalPassages} 篇文章、${totalQuestions} 道试题。`);

  // 4. 自动化法医级质量门控 (Quality Gate)
  console.log("\n🛡️ [4/4] 正在执行 17 项法医级全量质量自检断言...");
  try {
    const pythonBin = process.platform === "win32" ? "python" : "python3";
    const verifyScript = path.join(__dirname, "verify_deep_text_calibration.py");
    const verifyOutput = execSync(`${pythonBin} "${verifyScript}"`, { encoding: "utf-8" });
    console.log(verifyOutput.trim());
    console.log("  ✅ 质量守门 100% 通过: 0 错题、0 格式缺陷、0 答案冲突！");
  } catch (err) {
    console.error("❌ 质量守门断言拦截: 发现真题数据缺陷，已紧急中止发布！");
    if (err.stdout) console.error(err.stdout);
    if (err.stderr) console.error(err.stderr);
    process.exit(1);
  }

  // 5. 自动刷新静态版本哈希
  console.log("\n🔄 正在生成最新版本号与时间戳...");
  const versionScript = path.join(__dirname, "generate_static_version.mjs");
  execSync(`node "${versionScript}"`, { stdio: "inherit" });

  console.log("\n" + "=".repeat(70));
  console.log("🏁 全自动同步流水线执行完毕！所有静态真题镜像已完全就绪。");
  console.log("=".repeat(70));
}

main().catch((err) => {
  console.error("❌ 流水线执行失败:", err);
  process.exit(1);
});
