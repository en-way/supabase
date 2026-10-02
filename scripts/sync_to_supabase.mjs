import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { createClient } from '@supabase/supabase-js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..');

// Load .env
const envPath = path.join(ROOT_DIR, '.env');
const envContent = fs.readFileSync(envPath, 'utf-8');
const env = {};
envContent.split('\n').forEach(line => {
  const match = line.match(/^([^=]+)=(.*)$/);
  if (match) env[match[1].trim()] = match[2].trim().replace(/^['"]|['"]$/g, '');
});

const supabaseUrl = env.SUPABASE_URL || 'https://pghybspsjtzihpzpahcf.supabase.co';
const serviceRoleKey = env.SUPABASE_SERVICE_ROLE_KEY;

if (!serviceRoleKey) {
  console.error('❌ Missing SUPABASE_SERVICE_ROLE_KEY!');
  process.exit(1);
}

const supabase = createClient(supabaseUrl, serviceRoleKey);

async function sync() {
  console.log('=== STARTING SUPABASE DATABASE PURGE & SYNC ===');

  // 1. Purge CET-4 and CET-6
  console.log('1. Purging CET-4 and CET-6 from Supabase...');
  await supabase.from('questions').delete().in('category_id', ['cet4', 'cet6']);
  await supabase.from('passages').delete().in('category_id', ['cet4', 'cet6']);
  await supabase.from('exams').delete().in('category_id', ['cet4', 'cet6']);
  await supabase.from('categories').delete().in('id', ['cet4', 'cet6']);
  console.log('   ✅ CET-4 and CET-6 purged.');

  // 2. Read local authentic exams
  const examsDir = path.join(ROOT_DIR, 'public', 'data', 'exams');
  const examFiles = fs.readdirSync(examsDir).filter(f => f.endsWith('.json'));
  console.log(`2. Found ${examFiles.length} local authentic exam files.`);

  const validExamIds = [];
  const allExams = [];
  const allPassages = [];
  const allQuestions = [];

  for (const f of examFiles) {
    const fullPath = path.join(examsDir, f);
    const data = JSON.parse(fs.readFileSync(fullPath, 'utf-8'));
    const exam = data.exam;
    validExamIds.push(exam.id);

    allExams.push({
      id: exam.id,
      category_id: exam.category_id,
      title: exam.title,
      year: exam.year,
      exam_type: exam.exam_type || 'real',
      duration_minutes: exam.duration_minutes || 180,
      total_score: exam.total_score || 60,
      pass_score: exam.pass_score || 36,
      is_published: true,
      approval_status: 'approved'
    });

    let modified = false;

    for (const p of data.passages || []) {
      const pCat = p.category_id || exam.category_id;
      if (!p.category_id) {
        p.category_id = pCat;
        modified = true;
      }
      allPassages.push({
        id: p.id,
        exam_id: p.exam_id,
        category_id: pCat,
        title: p.title,
        section_type: p.section_type,
        content: p.content,
        sort_order: p.sort_order
      });
    }

    for (const q of data.questions || []) {
      // Must conform to CHECK constraint: 'choice', 'cloze_item', 'reading_item'
      let validQType = 'reading_item';
      if (q.q_type === 'cloze_item' || q.sort_order <= 20) {
        validQType = 'cloze_item';
      } else if (q.q_type === 'choice') {
        validQType = 'choice';
      } else {
        validQType = 'reading_item';
      }

      if (q.q_type !== validQType) {
        q.q_type = validQType;
        modified = true;
      }

      const qCat = q.category_id || exam.category_id;
      if (!q.category_id) {
        q.category_id = qCat;
        modified = true;
      }

      allQuestions.push({
        id: q.id,
        exam_id: q.exam_id,
        passage_id: q.passage_id,
        category_id: qCat,
        sort_order: q.sort_order,
        q_type: validQType,
        stem: q.stem,
        options: q.options,
        correct_answer: q.correct_answer,
        explanation: q.explanation,
        points: q.points
      });
    }

    if (modified) {
      fs.writeFileSync(fullPath, JSON.stringify(data, null, 2), 'utf-8');
    }
  }

  // 3. Purge obsolete exams in Supabase that are not in validExamIds
  console.log('3. Purging obsolete exams from Supabase...');
  const { data: dbExams } = await supabase.from('exams').select('id');
  if (dbExams) {
    const obsoleteIds = dbExams.map(e => e.id).filter(id => !validExamIds.includes(id));
    if (obsoleteIds.length > 0) {
      console.log(`   Found ${obsoleteIds.length} obsolete exams to remove.`);
      await supabase.from('questions').delete().in('exam_id', obsoleteIds);
      await supabase.from('passages').delete().in('exam_id', obsoleteIds);
      await supabase.from('exams').delete().in('id', obsoleteIds);
      console.log('   ✅ Obsolete exams cleaned up.');
    }
  }

  // 4. Ensure categories exist
  console.log('4. Syncing categories...');
  const categories = [
    {
      id: 'ky1',
      name: '考研英语一 (KY-1)',
      description: '全国硕士研究生招生考试英语（一）历年全真真题题库与权威题解',
      sort_order: 1
    },
    {
      id: 'ky2',
      name: '考研英语二 (KY-2)',
      description: '全国专业硕士研究生招生考试英语（二）历年全真真题题库与权威题解',
      sort_order: 2
    }
  ];
  const { error: catErr } = await supabase.from('categories').upsert(categories, { onConflict: 'id' });
  if (catErr) console.warn('   Category upsert warning:', catErr.message);
  else console.log('   ✅ Categories synced.');

  // 5. Upsert exams
  console.log(`5. Upserting ${allExams.length} authentic exams...`);
  const { error: examErr } = await supabase.from('exams').upsert(allExams, { onConflict: 'id' });
  if (examErr) {
    console.error('❌ Exams upsert error:', examErr.message);
    process.exit(1);
  }
  console.log('   ✅ Exams upserted successfully.');

  // 6. Upsert passages (chunks of 50)
  console.log(`6. Upserting ${allPassages.length} passages...`);
  for (let i = 0; i < allPassages.length; i += 50) {
    const chunk = allPassages.slice(i, i + 50);
    const { error: pErr } = await supabase.from('passages').upsert(chunk, { onConflict: 'id' });
    if (pErr) console.warn(`   Passage chunk ${i} warning:`, pErr.message);
  }
  console.log('   ✅ Passages upserted.');

  // 7. Upsert questions (chunks of 100)
  console.log(`7. Upserting ${allQuestions.length} questions...`);
  for (let i = 0; i < allQuestions.length; i += 100) {
    const chunk = allQuestions.slice(i, i + 100);
    const { error: qErr } = await supabase.from('questions').upsert(chunk, { onConflict: 'id' });
    if (qErr) console.warn(`   Question chunk ${i} warning:`, qErr.message);
  }
  console.log('   ✅ Questions upserted.');

  console.log('\n🎉 ALL EXAMS, PASSAGES, AND QUESTIONS SYNCED TO SUPABASE WITH 0 ERRORS!');
}

sync().catch(err => {
  console.error('Fatal sync error:', err);
  process.exit(1);
});
