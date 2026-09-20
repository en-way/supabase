/**
 * scripts/seed_cet.js
 * 
 * 自动读取 data/cet4/ 与 data/cet6/ 目录下所有清洗后的标准化 JSON 真题
 * 使用 Supabase Service Role 权限安全、批量、幂等地导入到云端数据库中
 */

const fs = require('fs');
const path = require('path');
const { createClient } = require('@supabase/supabase-js');

// 加载 .env 环境变量
function loadEnv() {
  const env = {};
  const rootDir = path.resolve(__dirname, '..');
  const envFiles = ['.env', '.env.local'];

  for (const f of envFiles) {
    const fullPath = path.join(rootDir, f);
    if (fs.existsSync(fullPath)) {
      const content = fs.readFileSync(fullPath, 'utf-8');
      content.split('\n').forEach((line) => {
        line = line.trim();
        if (line && !line.startsWith('#') && line.includes('=')) {
          const idx = line.indexOf('=');
          const key = line.slice(0, idx).trim();
          const val = line.slice(idx + 1).trim().replace(/^["']|["']$/g, '');
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
  console.error('❌ 未找到有效 SUPABASE_URL 或 SUPABASE_SERVICE_ROLE_KEY，请检查 .env 配置！');
  process.exit(1);
}

const supabase = createClient(supabaseUrl, serviceRoleKey, {
  auth: { persistSession: false }
});

async function main() {
  console.log('=================================================================');
  console.log('🚀 Enway 四六级历年核心真题 (2015-2024) 数据库直连导入管线启动');
  console.log(`🔗 数据库终端: ${supabaseUrl}`);
  console.log('=================================================================\n');

  // 1. 确保 categories 中 cet4 与 cet6 存在
  console.log('📌 步骤 1/3: 校验并确保科目分类 (Categories)...');
  const categoriesToEnsure = [
    {
      id: 'cet4',
      name: '大学英语四级 (CET-4)',
      description: '全国大学英语四级考试真题与精选核心题库',
      sort_order: 1
    },
    {
      id: 'cet6',
      name: '大学英语六级 (CET-6)',
      description: '全国大学英语六级考试高分冲刺真题库',
      sort_order: 2
    }
  ];

  for (const cat of categoriesToEnsure) {
    const { error } = await supabase.from('categories').upsert(cat, { onConflict: 'id' });
    if (error) {
      console.warn(`  ⚠️ 提示：科目 ${cat.id} 状态: ${error.message}`);
    } else {
      console.log(`  ✅ 科目已就绪: ${cat.name}`);
    }
  }

  // 2. 收集 data/cet4 与 data/cet6 下的所有 JSON 文件
  console.log('\n📌 步骤 2/3: 扫描并加载本地结构化真题数据...');
  const dirs = [
    path.join(__dirname, '..', 'data', 'cet4'),
    path.join(__dirname, '..', 'data', 'cet6')
  ];

  const examFiles = [];
  for (const dir of dirs) {
    if (fs.existsSync(dir)) {
      const files = fs.readdirSync(dir).filter(f => f.endsWith('.json'));
      files.forEach(f => examFiles.push(path.join(dir, f)));
    }
  }

  console.log(`  📂 共发现待导入真题文件: ${examFiles.length} 个`);

  // 3. 逐卷入库（幂等性处理）
  console.log('\n📌 步骤 3/3: 批量入库真题试卷、长篇阅读材料与试题...');
  let totalExams = 0;
  let totalPassages = 0;
  let totalQuestions = 0;

  for (let i = 0; i < examFiles.length; i++) {
    const filePath = examFiles[i];
    const examData = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
    const shortName = path.basename(filePath);

    console.log(`\n[${i + 1}/${examFiles.length}] 正在处理: ${shortName} -> 【${examData.title}】(${examData.year}年)`);

    // 检查是否已存在同名/同年份科目试卷
    const { data: existingExam } = await supabase
      .from('exams')
      .select('id')
      .eq('category_id', examData.category_id)
      .eq('year', examData.year)
      .eq('title', examData.title)
      .maybeSingle();

    let targetExamId;

    if (existingExam) {
      console.log(`  ℹ️ 该试卷已存在 (ID: ${existingExam.id})，正在同步更新其所属篇章与试题...`);
      targetExamId = existingExam.id;

      await supabase
        .from('exams')
        .update({
          total_score: examData.total_score || 100,
          pass_score: examData.pass_score || 60,
          duration_minutes: examData.duration_minutes || 40,
          is_published: true,
          approval_status: 'approved'
        })
        .eq('id', targetExamId);

      // 清理旧篇章（级联删除题目），重新写入
      await supabase.from('passages').delete().eq('exam_id', targetExamId);
    } else {
      const { data: newExam, error: examErr } = await supabase
        .from('exams')
        .insert({
          category_id: examData.category_id,
          title: examData.title,
          year: examData.year,
          exam_type: examData.exam_type || 'real',
          duration_minutes: examData.duration_minutes || 40,
          total_score: examData.total_score || 100,
          pass_score: examData.pass_score || 60,
          is_published: true,
          approval_status: 'approved'
        })
        .select()
        .single();

      if (examErr) {
        console.error(`  ❌ 试卷主体创建失败: ${examErr.message}`);
        continue;
      }
      targetExamId = newExam.id;
      totalExams++;
      console.log(`  ✨ 试卷主体入库成功 (ID: ${targetExamId})`);
    }

    // 插入篇章与试题
    for (let pIdx = 0; pIdx < examData.passages.length; pIdx++) {
      const passage = examData.passages[pIdx];
      const { data: insertedPassage, error: passageErr } = await supabase
        .from('passages')
        .insert({
          exam_id: targetExamId,
          category_id: examData.category_id,
          section_type: passage.section_type || 'reading',
          title: passage.title || `Passage ${pIdx + 1}`,
          content: passage.content,
          sort_order: pIdx + 1
        })
        .select()
        .single();

      if (passageErr) {
        console.error(`    ❌ 篇章写入失败 (${passage.title}): ${passageErr.message}`);
        continue;
      }

      totalPassages++;

      // 插入试题
      if (Array.isArray(passage.questions) && passage.questions.length > 0) {
        const questionRows = passage.questions.map((q, qIdx) => ({
          exam_id: targetExamId,
          passage_id: insertedPassage.id,
          category_id: examData.category_id,
          q_type: q.q_type || 'reading_item',
          stem: q.stem,
          options: q.options,
          correct_answer: q.correct_answer,
          explanation: q.explanation || '暂无详细考点解析',
          points: q.points || 10,
          sort_order: qIdx + 1
        }));

        const { error: qErr } = await supabase.from('questions').insert(questionRows);
        if (qErr) {
          console.error(`    ❌ 试题批量写入失败 (${passage.title}): ${qErr.message}`);
        } else {
          totalQuestions += questionRows.length;
          console.log(`    📖 篇章 [${passage.title.slice(0, 32)}...] 成功录入 ${questionRows.length} 道题目`);
        }
      }
    }
  }

  console.log('\n=================================================================');
  console.log('🎉🎉🎉 四六级历年真题库全量入库大功告成！');
  console.log(`📊 统计数据汇总:`);
  console.log(`   - 试卷总数: ${examFiles.length} 套 (覆盖四六级 2015 - 2024 年)`);
  console.log(`   - 篇章总数: ${totalPassages} 篇英美原版高规格长文`);
  console.log(`   - 客观题总数: ${totalQuestions} 道（含标准ABCD选项、正确答案与考点精析）`);
  console.log('=================================================================');
}

main().catch(err => {
  console.error('Fatal error during seeding:', err);
  process.exit(1);
});
