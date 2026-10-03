import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const ROOT_DIR = path.resolve(__dirname, '..');

const DATA_DIR = path.join(ROOT_DIR, 'public', 'data');
const EXAMS_DIR = path.join(DATA_DIR, 'exams');

const files = fs.readdirSync(EXAMS_DIR).filter(f => f.endsWith('.json'));
console.log(`Found ${files.length} exam files in public/data/exams.`);

const examsSummary = [];

for (const file of files) {
  const filePath = path.join(EXAMS_DIR, file);
  const data = JSON.parse(fs.readFileSync(filePath, 'utf-8'));
  const exam = data.exam;
  const questionsCount = (data.questions || []).length;
  const passagesCount = (data.passages || []).length;

  examsSummary.push({
    id: exam.id,
    category_id: exam.category_id,
    title: exam.title,
    year: exam.year,
    exam_type: exam.exam_type || 'real',
    duration_minutes: exam.duration_minutes || 180,
    total_score: exam.total_score || 60,
    pass_score: exam.pass_score || 36,
    is_published: true,
    approval_status: 'approved',
    created_at: exam.created_at || new Date().toISOString(),
    created_by: exam.created_by || null,
    questions: [{ count: questionsCount }],
    passages: [{ count: passagesCount }]
  });
}

// Sort by year descending, then category
examsSummary.sort((a, b) => {
  if (b.year !== a.year) return b.year - a.year;
  return a.category_id.localeCompare(b.category_id);
});

fs.writeFileSync(
  path.join(DATA_DIR, 'exams.json'),
  JSON.stringify(examsSummary, null, 2),
  'utf-8'
);

console.log(`✅ Successfully updated public/data/exams.json with ${examsSummary.length} exams.`);
