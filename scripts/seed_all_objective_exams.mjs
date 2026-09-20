/**
 * scripts/seed_all_objective_exams.mjs
 * 
 * 原地无缝平滑升级 40 套真题试卷（CET-4 10套 + CET-6 10套 + 考研 20套）
 * 保持现有试卷 ID 不变，全量替换篇章与题目为完整客观题（共 1500 题）
 * 并在入库完成后自动触发静态 CDN 镜像导出
 */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { createClient } from "@supabase/supabase-js";
import { execSync } from "child_process";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, "..");

function loadEnv() {
  const env = {};
  const envFiles = [".env", ".env.local"];
  for (const f of envFiles) {
    const p = path.join(ROOT_DIR, f);
    if (fs.existsSync(p)) {
      const content = fs.readFileSync(p, "utf-8");
      content.split("\n").forEach((line) => {
        line = line.trim();
        if (line && !line.startsWith("#") && line.includes("=")) {
          const idx = line.indexOf("=");
          const key = line.slice(0, idx).trim();
          const val = line.slice(idx + 1).trim().replace(/^["']|["']$/g, "");
          env[key] = val;
        }
      });
    }
  }
  return env;
}

const env = loadEnv();
const supabaseUrl = env.SUPABASE_URL || env.NEXT_PUBLIC_SUPABASE_URL;
const serviceRoleKey = env.SUPABASE_SERVICE_ROLE_KEY || env.SUPABASE_ANON_KEY;

if (!supabaseUrl || !serviceRoleKey) {
  console.error("❌ 错误：未找到有效 SUPABASE_URL 或 SUPABASE_SERVICE_ROLE_KEY！");
  process.exit(1);
}

const supabase = createClient(supabaseUrl, serviceRoleKey, {
  auth: { persistSession: false }
});

async function main() {
  console.log("=================================================================");
  console.log("🚀 Enway 历年真题库全量客观题【原地平滑升级】入库流水线启动...");
  console.log(`🔗 数据库终端: ${supabaseUrl}`);
  console.log("=================================================================\n");

  // 收集待入库文件列表
  const examFiles = [];

  // CET-4
  const cet4Dir = path.join(ROOT_DIR, "data", "cet4");
  if (fs.existsSync(cet4Dir)) {
    fs.readdirSync(cet4Dir).filter(f => f.endsWith(".json")).forEach(f => examFiles.push(path.join(cet4Dir, f)));
  }

  // CET-6
  const cet6Dir = path.join(ROOT_DIR, "data", "cet6");
  if (fs.existsSync(cet6Dir)) {
    fs.readdirSync(cet6Dir).filter(f => f.endsWith(".json")).forEach(f => examFiles.push(path.join(cet6Dir, f)));
  }

  // Kaoyan
  const kyDir = path.join(ROOT_DIR, "data", "kaoyan");
  if (fs.existsSync(kyDir)) {
    fs.readdirSync(kyDir).filter(f => f.endsWith(".json")).forEach(f => examFiles.push(path.join(kyDir, f)));
  }

  console.log(`📂 共发现待升级试卷文件: ${examFiles.length} 套 (四六级各 10 套 + 考研 20 套)`);

  let totalExams = 0;
  let totalPassages = 0;
  let totalQuestions = 0;

  for (let i = 0; i < examFiles.length; i++) {
    const filePath = examFiles[i];
    const examData = JSON.parse(fs.readFileSync(filePath, "utf-8"));
    const fileName = path.basename(filePath);

    console.log(`\n[${i + 1}/${examFiles.length}] 正在升级: ${fileName} -> 【${examData.title}】(${examData.year}年)`);

    // 1. 查询现有试卷 ID
    const { data: existingExam } = await supabase
      .from("exams")
      .select("id")
      .eq("category_id", examData.category_id)
      .eq("year", examData.year)
      .maybeSingle();

    let targetExamId;

    if (existingExam) {
      targetExamId = existingExam.id;
      console.log(`  🔄 找到现有试卷记录 (ID: ${targetExamId})，原地更新试卷元数据...`);
      
      const { error: updateErr } = await supabase
        .from("exams")
        .update({
          title: examData.title,
          total_score: examData.total_score,
          pass_score: examData.pass_score,
          duration_minutes: examData.duration_minutes,
          is_published: true,
          approval_status: "approved"
        })
        .eq("id", targetExamId);

      if (updateErr) console.error(`  ❌ 试卷元数据更新异常: ${updateErr.message}`);

      // 清空旧篇章（级联清空旧题目）
      const { error: delErr } = await supabase
        .from("passages")
        .delete()
        .eq("exam_id", targetExamId);
      if (delErr) console.warn(`  ⚠️ 清理旧篇章提示: ${delErr.message}`);
    } else {
      console.log(`  ✨ 试卷尚不存在，正在创建新试卷记录...`);
      const { data: newExam, error: insErr } = await supabase
        .from("exams")
        .insert({
          category_id: examData.category_id,
          title: examData.title,
          year: examData.year,
          exam_type: examData.exam_type || "real",
          duration_minutes: examData.duration_minutes || 60,
          total_score: examData.total_score || 100,
          pass_score: examData.pass_score || 60,
          is_published: true,
          approval_status: "approved"
        })
        .select()
        .single();

      if (insErr) {
        console.error(`  ❌ 试卷插入失败: ${insErr.message}`);
        continue;
      }
      targetExamId = newExam.id;
    }

    totalExams++;

    // 2. 依次插入新篇章与新试题
    const passages = examData.passages || [];
    for (let pIdx = 0; pIdx < passages.length; pIdx++) {
      const p = passages[pIdx];

      const { data: insertedPassage, error: pErr } = await supabase
        .from("passages")
        .insert({
          exam_id: targetExamId,
          category_id: examData.category_id,
          title: p.title,
          content: p.content,
          section_type: p.section_type || "reading",
          sort_order: pIdx + 1
        })
        .select()
        .single();

      if (pErr) {
        console.error(`  ❌ 篇章写入失败 (${p.title}): ${pErr.message}`);
        continue;
      }

      totalPassages++;

      // 插入试题
      const questions = p.questions || [];
      if (questions.length > 0) {
        const questionRows = questions.map((q, qIdx) => ({
          exam_id: targetExamId,
          passage_id: insertedPassage.id,
          category_id: examData.category_id,
          q_type: q.q_type || "reading_item",
          stem: q.stem,
          options: q.options,
          correct_answer: q.correct_answer,
          explanation: q.explanation || "暂无详细解析",
          points: q.points || 2.0,
          sort_order: q.sort_order || qIdx + 1
        }));

        const { error: qErr } = await supabase.from("questions").insert(questionRows);
        if (qErr) {
          console.error(`    ❌ 试题批量写入失败 (${p.title}): ${qErr.message}`);
        } else {
          totalQuestions += questionRows.length;
          console.log(`    📖 [${p.title.slice(0, 32)}] 成功录入 ${questionRows.length} 道客观题`);
        }
      }
    }
  }

  console.log("\n=================================================================");
  console.log("🎉🎉🎉 全量客观真题库入库升级大获成功！");
  console.log(`📊 统计汇总:`);
  console.log(`   - 试卷总数: ${totalExams} 套`);
  console.log(`   - 篇章总数: ${totalPassages} 篇`);
  console.log(`   - 客观题总数: ${totalQuestions} 道`);
  console.log("=================================================================\n");

  // 3. 自动同步静态 CDN 镜像
  console.log("⚡ 正在触发静态 CDN 镜像自动导出 (scripts/export_exams_to_static.mjs)...");
  try {
    execSync("node scripts/export_exams_to_static.mjs", { stdio: "inherit", cwd: ROOT_DIR });
    console.log("✅ 静态 CDN 镜像全量同步完成！");
  } catch (err) {
    console.error("❌ 静态镜像导出出错:", err);
  }
}

main().catch(console.error);
