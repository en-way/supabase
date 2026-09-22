/**
 * scripts/rename_all_exams.mjs
 * 
 * 全站 60 套真题试卷全链路规范化重命名流水线
 * 1. 同步更新 Supabase PostgreSQL 生产数据库中的 exams.title
 * 2. 同步更新 public/data/exams.json 中的 title
 * 3. 同步更新 public/data/exams/{id}.json 中的 exam.title
 * 4. 同步更新 data/ 目录下的 60 个原始真题数据文件
 */

import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { createClient } from "@supabase/supabase-js";

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
  auth: { persistSession: false },
});

export function getNewTitle(category_id, year) {
  switch (category_id) {
    case "cet4":
      return `${year}年6月 CET-4 真题 (第1套)`;
    case "cet6":
      return `${year}年6月 CET-6 真题 (第1套)`;
    case "ky1":
      return `${year}年 考研英语(一) 真题`;
    case "ky2":
      return `${year}年 考研英语(二) 真题`;
    default:
      return null;
  }
}

async function main() {
  console.log("=================================================================");
  console.log("🚀 全站 60 套真题试卷全链路规范化重命名流水线启动");
  console.log(`🔗 连接终端: ${supabaseUrl}`);
  console.log("=================================================================\n");

  // 1. 同步更新 Supabase 生产数据库
  console.log("📡 [1/4] 正在拉取 Supabase 数据库试卷列表并批量原地更新...");
  const { data: dbExams, error: fetchErr } = await supabase
    .from("exams")
    .select("id, category_id, year, title");

  if (fetchErr) {
    console.error("❌ 获取 Supabase exams 表数据失败:", fetchErr);
    process.exit(1);
  }

  console.log(`共获取到 ${dbExams.length} 套数据库试卷记录`);
  let dbSuccessCount = 0;

  for (const ex of dbExams) {
    const newTitle = getNewTitle(ex.category_id, ex.year);
    if (!newTitle) {
      console.warn(`⚠️ 跳过未知分类试卷 [${ex.id}]: category=${ex.category_id}, year=${ex.year}`);
      continue;
    }

    if (ex.title === newTitle) {
      dbSuccessCount++;
      continue;
    }

    const { error: updateErr } = await supabase
      .from("exams")
      .update({ title: newTitle })
      .eq("id", ex.id);

    if (updateErr) {
      console.error(`❌ 更新试卷 [${ex.id}] 失败:`, updateErr.message);
    } else {
      dbSuccessCount++;
      console.log(`  ✓ DB: [${ex.category_id.toUpperCase()} ${ex.year}] -> ${newTitle}`);
    }
  }
  console.log(`✅ 数据库更新完毕: 成功 ${dbSuccessCount} / ${dbExams.length}\n`);

  // 2. 同步更新 public/data/exams.json
  console.log("📁 [2/4] 正在更新 public/data/exams.json 大厅静态镜像...");
  const staticExamsPath = path.join(ROOT_DIR, "public", "data", "exams.json");
  if (fs.existsSync(staticExamsPath)) {
    const staticExams = JSON.parse(fs.readFileSync(staticExamsPath, "utf-8"));
    let staticCount = 0;
    for (const item of staticExams) {
      const newTitle = getNewTitle(item.category_id, item.year);
      if (newTitle) {
        item.title = newTitle;
        staticCount++;
      }
    }
    fs.writeFileSync(staticExamsPath, JSON.stringify(staticExams, null, 2), "utf-8");
    console.log(`✅ 已更新 public/data/exams.json，共同步 ${staticCount} 套试卷标题\n`);
  } else {
    console.warn("⚠️ 未找到 public/data/exams.json 文件\n");
  }

  // 3. 同步更新 public/data/exams/{id}.json 静态详情包
  console.log("📦 [3/4] 正在更新 public/data/exams/{id}.json 单卷静态详情包...");
  const staticDetailsDir = path.join(ROOT_DIR, "public", "data", "exams");
  let detailCount = 0;
  if (fs.existsSync(staticDetailsDir)) {
    const detailFiles = fs.readdirSync(staticDetailsDir).filter((f) => f.endsWith(".json"));
    for (const f of detailFiles) {
      const filePath = path.join(staticDetailsDir, f);
      try {
        const detailData = JSON.parse(fs.readFileSync(filePath, "utf-8"));
        if (detailData.exam) {
          const newTitle = getNewTitle(detailData.exam.category_id, detailData.exam.year);
          if (newTitle) {
            detailData.exam.title = newTitle;
            fs.writeFileSync(filePath, JSON.stringify(detailData, null, 2), "utf-8");
            detailCount++;
          }
        }
      } catch (e) {
        console.error(`❌ 处理静态包 ${f} 失败:`, e);
      }
    }
    console.log(`✅ 已更新 public/data/exams/*.json，共同步 ${detailCount} 份试卷数据包\n`);
  }

  // 4. 同步更新 data/ 源码数据文件
  console.log("📝 [4/4] 正在更新 data/ 原始数据源文件（cet4, cet6, kaoyan）...");
  const sourceDirs = [
    path.join(ROOT_DIR, "data", "cet4"),
    path.join(ROOT_DIR, "data", "cet6"),
    path.join(ROOT_DIR, "data", "kaoyan"),
  ];

  let rawSourceCount = 0;
  for (const sDir of sourceDirs) {
    if (!fs.existsSync(sDir)) continue;
    const rawFiles = fs.readdirSync(sDir).filter((f) => f.endsWith(".json"));
    for (const rf of rawFiles) {
      const rPath = path.join(sDir, rf);
      try {
        const rawJson = JSON.parse(fs.readFileSync(rPath, "utf-8"));
        const newTitle = getNewTitle(rawJson.category_id, rawJson.year);
        if (newTitle) {
          rawJson.title = newTitle;
          fs.writeFileSync(rPath, JSON.stringify(rawJson, null, 2), "utf-8");
          rawSourceCount++;
        }
      } catch (e) {
        console.error(`❌ 处理源码文件 ${rf} 失败:`, e);
      }
    }
  }
  console.log(`✅ 已更新 data/ 源码数据文件，共同步 ${rawSourceCount} 个文件\n`);

  console.log("=================================================================");
  console.log("🎉 全部 60 套真题试卷全链路名称规范化同步执行成功！");
  console.log("=================================================================");
}

main().catch((err) => {
  console.error("执行脚本时发生未捕获异常:", err);
  process.exit(1);
});
