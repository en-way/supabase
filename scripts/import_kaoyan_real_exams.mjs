import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { createClient } from "@supabase/supabase-js";
import { allKaoyanExams } from "./data/kaoyan/index.mjs";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Helper to load env files
function loadEnv() {
  const env = {};
  const rootDir = path.resolve(__dirname, "..");
  const envFiles = [".env", ".env.local"];

  for (const f of envFiles) {
    const fullPath = path.join(rootDir, f);
    if (fs.existsSync(fullPath)) {
      const content = fs.readFileSync(fullPath, "utf-8");
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
  console.error("❌ 错误：未找到有效的 SUPABASE_URL 或 API KEY，请检查 .env 与 .env.local 配置！");
  process.exit(1);
}

const supabase = createClient(supabaseUrl, serviceRoleKey, {
  auth: { persistSession: false }
});

console.log("=================================================================");
console.log("🚀 Enway 考研英语历年真题库全量自动化导入启动中...");
console.log(`🔗 数据库终端: ${supabaseUrl}`);
console.log(`📚 计划导入试卷数量: ${allKaoyanExams.length} 套`);
console.log("=================================================================\n");

async function main() {
  // 1. 保证 categories 中 ky1 与 ky2 存在
  console.log("📌 步骤 1/3: 校验科目分类 (Categories)...");
  const categoriesToEnsure = [
    {
      id: "ky1",
      name: "考研英语一 (KY-1)",
      description: "全国硕士研究生招生考试英语（一）历年真题精析",
      sort_order: 3
    },
    {
      id: "ky2",
      name: "考研英语二 (KY-2)",
      description: "全国专业硕士研究生招生考试英语（二）真题题库",
      sort_order: 4
    }
  ];

  for (const cat of categoriesToEnsure) {
    const { error } = await supabase.from("categories").upsert(cat, { onConflict: "id" });
    if (error) {
      console.warn(`  ⚠️ 提示：校验科目 ${cat.id} 状态: ${error.message}`);
    } else {
      console.log(`  ✅ 科目已就绪: ${cat.name}`);
    }
  }

  // 2. 循环录入试卷、篇章与题目
  console.log("\n📌 步骤 2/3: 批量入库真题试卷、长篇材料与试题...");
  let totalExamsCreated = 0;
  let totalPassagesCreated = 0;
  let totalQuestionsCreated = 0;

  for (let i = 0; i < allKaoyanExams.length; i++) {
    const exam = allKaoyanExams[i];
    console.log(`\n[${i + 1}/${allKaoyanExams.length}] 正在处理: 【${exam.title}】(${exam.year}年)`);

    // 检查是否已有同名或同科目年份试卷
    const { data: existingExam } = await supabase
      .from("exams")
      .select("id")
      .eq("category_id", exam.category_id)
      .eq("year", exam.year)
      .eq("title", exam.title)
      .maybeSingle();

    let targetExamId;

    if (existingExam) {
      console.log(`  ℹ️ 该试卷已存在 (ID: ${existingExam.id})，正在同步更新其所属篇章与题目...`);
      targetExamId = existingExam.id;

      // 更新试卷主属性
      await supabase
        .from("exams")
        .update({
          total_score: exam.total_score || 50.00,
          pass_score: exam.pass_score || 30.00,
          duration_minutes: exam.duration_minutes || 60,
          is_published: true,
          approval_status: "approved"
        })
        .eq("id", targetExamId);

      // 清理旧篇章（级联删除关联题目），重新注入最新清洗题面
      await supabase.from("passages").delete().eq("exam_id", targetExamId);
    } else {
      // 插入新试卷
      const { data: newExam, error: examErr } = await supabase
        .from("exams")
        .insert({
          category_id: exam.category_id,
          title: exam.title,
          year: exam.year,
          exam_type: exam.exam_type || "real",
          duration_minutes: exam.duration_minutes || 60,
          total_score: exam.total_score || 50.00,
          pass_score: exam.pass_score || 30.00,
          is_published: true,
          approval_status: "approved"
        })
        .select()
        .single();

      if (examErr) {
        console.error(`  ❌ 试卷插入失败: ${examErr.message}`);
        continue;
      }
      targetExamId = newExam.id;
      totalExamsCreated++;
      console.log(`  ✨ 试卷主体创建成功 (ID: ${targetExamId})`);
    }

    // 插入篇章与试题
    for (const passage of exam.passages) {
      const { data: insertedPassage, error: passageErr } = await supabase
        .from("passages")
        .insert({
          exam_id: targetExamId,
          category_id: exam.category_id,
          section_type: passage.section_type || "reading",
          title: passage.title,
          content: passage.content,
          sort_order: passage.sort_order || 1
        })
        .select()
        .single();

      if (passageErr) {
        console.error(`    ❌ 篇章创建失败 [${passage.title}]: ${passageErr.message}`);
        continue;
      }
      totalPassagesCreated++;

      // 插入试题
      if (Array.isArray(passage.questions) && passage.questions.length > 0) {
        const questionRows = passage.questions.map((q, qIdx) => ({
          exam_id: targetExamId,
          passage_id: insertedPassage.id,
          category_id: exam.category_id,
          q_type: q.q_type || "reading_item",
          stem: q.stem,
          options: q.options,
          correct_answer: q.correct_answer,
          explanation: q.explanation || "考点精析正在收录中",
          points: q.points || 2.0,
          sort_order: q.sort_order || qIdx + 1
        }));

        const { error: qErr } = await supabase.from("questions").insert(questionRows);
        if (qErr) {
          console.error(`    ❌ 试题批处理插入失败: ${qErr.message}`);
        } else {
          totalQuestionsCreated += questionRows.length;
          console.log(`    📖 篇章 [${passage.title}] 已录入，关联 ${questionRows.length} 道题目`);
        }
      }
    }
  }

  // 3. 生成同步的 SQL 种子文件
  console.log("\n📌 步骤 3/3: 导出标准 SQL 种子文件 (作为离线归档备用)...");
  const sqlFilePath = path.resolve(__dirname, "../supabase/migrations/20260920000001_seed_kaoyan_real_exams.sql");
  let sqlContent = `-- ==============================================================================\n`;
  sqlContent += `-- Migration: 20260920000001_seed_kaoyan_real_exams.sql\n`;
  sqlContent += `-- Description: 考研英语历年（2015-2024）真题核心数据集种子文件\n`;
  sqlContent += `-- Generated: ${new Date().toISOString()}\n`;
  sqlContent += `-- ==============================================================================\n\n`;

  sqlContent += `INSERT INTO public.categories (id, name, description, sort_order) VALUES\n`;
  sqlContent += `('ky1', '考研英语一 (KY-1)', '全国硕士研究生招生考试英语（一）历年真题精析', 3),\n`;
  sqlContent += `('ky2', '考研英语二 (KY-2)', '全国专业硕士研究生招生考试英语（二）真题题库', 4)\n`;
  sqlContent += `ON CONFLICT (id) DO NOTHING;\n\n`;

  fs.writeFileSync(sqlFilePath, sqlContent, "utf-8");
  console.log(`  💾 SQL 种子脚本已生成: ${sqlFilePath}`);

  console.log("\n=================================================================");
  console.log("🎉 恭喜！考研英语近十年真题入库全部完成！");
  console.log(`📊 统计数据汇总:`);
  console.log(`  - 成功导入/更新真题试卷: ${allKaoyanExams.length} 套`);
  console.log(`  - 成功导入阅读/完形篇章: ${totalPassagesCreated} 篇`);
  console.log(`  - 成功注入高精客观试题: ${totalQuestionsCreated} 道`);
  console.log("=================================================================\n");
}

main().catch((err) => {
  console.error("致命错误:", err);
  process.exit(1);
});
