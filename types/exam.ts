export interface QuestionOption {
  key: string;
  text: string;
}

export type ExamType = "real" | "mock";

export type ExamApprovalStatus = "approved" | "pending_upload" | "pending_delete" | "rejected";

export type PassageSectionType = "reading" | "cloze" | "single";

export type QuestionType = "choice" | "cloze_item" | "reading_item";

export type RawQuestionOptions =
  | QuestionOption[]
  | Record<string, string>
  | string[]
  | string
  | null
  | undefined;

export interface CategoryRecord {
  id: string;
  name: string;
  description?: string | null;
  sort_order?: number;
}

export interface CountAggregation {
  count: number;
}

export interface ExamRecord {
  id: string;
  category_id: string;
  title: string;
  year: number;
  exam_type: ExamType;
  duration_minutes: number;
  total_score: number;
  pass_score: number;
  is_published?: boolean;
  approval_status?: ExamApprovalStatus;
  created_at?: string;
  created_by?: string | null;
  questions?: CountAggregation[];
  passages?: CountAggregation[];
}

export interface PassageRecord {
  id: string;
  exam_id?: string;
  category_id?: string;
  section_type: PassageSectionType;
  title: string;
  content: string;
  sort_order?: number;
}

export interface QuestionRecord {
  id: string;
  exam_id?: string;
  passage_id?: string | null;
  category_id?: string;
  q_type: QuestionType;
  stem: string;
  options: RawQuestionOptions;
  correct_answer: string;
  explanation?: string | null;
  points?: number | null;
  sort_order?: number;
}

export interface ExamDetailData {
  exam: ExamRecord | null;
  passages: PassageRecord[];
  questions: QuestionRecord[];
  fromStaticMirror?: boolean;
}

export interface ExamLobbyData {
  categories: CategoryRecord[];
  exams: ExamRecord[];
}
