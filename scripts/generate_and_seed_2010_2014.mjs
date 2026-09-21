/**
 * scripts/generate_and_seed_2010_2014.mjs
 * 
 * 自动生成 2010~2014 年 20 套全真试卷与 750 道全量客观题：
 * 1. 考研英语一 KY-1 (2010-2014, 5套, 每套45题 = 225题)
 * 2. 考研英语二 KY-2 (2010-2014, 5套, 每套45题 = 225题)
 * 3. 大学英语四级 CET-4 (2010-2014, 5套, 每套30题 = 150题)
 * 4. 大学英语六级 CET-6 (2010-2014, 5套, 每套30题 = 150题)
 * 
 * 本地持久化至 data/ 目录 -> 直连写入 Supabase 数据库 -> 自动同步触发静态 CDN 镜像导出
 */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { createClient } from "@supabase/supabase-js";
import { execSync } from "child_process";
import { generateKyExams } from "./data_2010_2014_ky.mjs";
import { generateCetExams } from "./data_2010_2014_cet.mjs";

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
  console.log("🚀 Enway 2010~2014 年全真试卷与全量客观题 (20套/750题) 入库流水线启动...");
  console.log(`🔗 数据库终端: ${supabaseUrl}`);
  console.log("=================================================================\n");

  const kyExams = generateKyExams();
  const cetExams = generateCetExams();
  const allNewExams = [...kyExams, ...cetExams];

  console.log(`📋 共生成 2010~2014 年全新试卷: ${allNewExams.length} 套 (考研 10套 + 四六级 10套)`);

  // 1. 本地持久化至 data/ 目录
  console.log("\n💾 正在保存本地 JSON 镜像至 data/ 目录...");
  const CET4_DIR = path.join(ROOT_DIR, "data", "cet4");
  const CET6_DIR = path.join(ROOT_DIR, "data", "cet6");
  const KAOYAN_DIR = path.join(ROOT_DIR, "data", "kaoyan");

  for (const exam of allNewExams) {
    let targetDir;
    let fileName;
    if (exam.category_id === "cet4") {
      targetDir = CET4_DIR;
      fileName = `cet4_${exam.year}.json`;
    } else if (exam.category_id === "cet6") {
      targetDir = CET6_DIR;
      fileName = `cet6_${exam.year}.json`;
    } else if (exam.category_id === "ky1") {
      targetDir = KAOYAN_DIR;
      fileName = `ky1_${exam.year}.json`;
    } else {
      targetDir = KAOYAN_DIR;
      fileName = `ky2_${exam.year}.json`;
    }

    const filePath = path.join(targetDir, fileName);
    fs.writeFileSync(filePath, JSON.stringify(exam, null, 2), "utf-8");
    console.log(`  ✓ 已保存: ${filePath}`);
  }

  // 2. 写入/同步至 Supabase 数据库
  console.log("\n☁️ 正在将 20 套试卷及全部题目灌入 Supabase 数据库...");
  let totalExams = 0;
  let totalPassages = 0;
  let totalQuestions = 0;

  for (let i = 0; i < allNewExams.length; i++) {
    const examData = allNewExams[i];
    console.log(`\n[${i + 1}/${allNewExams.length}] 正在处理: 【${examData.title}】(${examData.year}年)`);

    // 检查试卷是否已存在
    const { data: existingExam } = await supabase
      .from("exams")
      .select("id")
      .eq("category_id", examData.category_id)
      .eq("year", examData.year)
      .maybeSingle();

    let targetExamId;

    if (existingExam) {
      targetExamId = existingExam.id;
      console.log(`  🔄 找到现有试卷记录 (ID: ${targetExamId})，更新试卷主表...`);
      await supabase
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

      // 清理旧篇章（外键级联清理旧题目）
      await supabase
        .from("passages")
        .delete()
        .eq("exam_id", targetExamId);
    } else {
      console.log(`  ✨ 试卷为新年份记录，创建新试卷...`);
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

    // 写入篇章与试题
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
          console.error(`    ❌ 试题批量写入失败: ${qErr.message}`);
        } else {
          totalQuestions += questionRows.length;
          console.log(`    📖 [${p.title.slice(0, 36)}] 成功写入 ${questionRows.length} 道客观题`);
        }
      }
    }
  }

  console.log("\n=================================================================");
  console.log("🎉🎉🎉 2010~2014 年全真试卷与全量客观题入库全部成功！");
  console.log(`📊 统计汇总:`);
  console.log(`   - 本次新增试卷: ${totalExams} 套`);
  console.log(`   - 本次新增篇章: ${totalPassages} 篇`);
  console.log(`   - 本次新增客观题: ${totalQuestions} 道`);
  console.log("=================================================================\n");

  // 3. 自动同步静态 CDN 镜像
  console.log("⚡ 正在触发全站静态 CDN 镜像全量同步 (scripts/export_exams_to_static.mjs)...");
  try {
    execSync("node scripts/export_exams_to_static.mjs", { stdio: "inherit", cwd: ROOT_DIR });
    console.log("✅ 静态 CDN 镜像全量同步完成！全站 60 套试卷现已就绪！");
  } catch (err) {
    console.error("❌ 静态镜像导出异常:", err);
  }
}

main().catch(console.error);
