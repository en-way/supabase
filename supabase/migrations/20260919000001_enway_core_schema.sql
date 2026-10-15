-- ==============================================================================
-- Migration: 20260919000001_enway_core_schema.sql
-- Description: Core Schema for Enway Online English Practice Platform (Local-First + Minimal Cloud Backup)
-- ==============================================================================

-- 1. Categories (考试科目分类)
CREATE TABLE IF NOT EXISTS public.categories (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    description TEXT,
    sort_order INT DEFAULT 0
);

INSERT INTO public.categories (id, name, description, sort_order) VALUES
('cet4', '大学英语四级 (CET-4)', '全国大学英语四级考试真题与精选核心题库', 1),
('cet6', '大学英语六级 (CET-6)', '全国大学英语六级考试高分冲刺真题库', 2),
('ky1', '考研英语一 (KY-1)', '全国硕士研究生招生考试英语（一）历年真题精析', 3),
('ky2', '考研英语二 (KY-2)', '全国专业硕士研究生招生考试英语（二）真题题库', 4)
ON CONFLICT (id) DO UPDATE SET 
    name = EXCLUDED.name,
    description = EXCLUDED.description,
    sort_order = EXCLUDED.sort_order;

-- 2. Exams (试卷主表 - 统一百分制)
CREATE TABLE IF NOT EXISTS public.exams (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    category_id TEXT NOT NULL REFERENCES public.categories(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    year INT NOT NULL,
    exam_type TEXT NOT NULL DEFAULT 'real' CHECK (exam_type IN ('real', 'mock')),
    duration_minutes INT NOT NULL DEFAULT 60,
    total_score NUMERIC(5,2) NOT NULL DEFAULT 100.00,
    pass_score NUMERIC(5,2) NOT NULL DEFAULT 60.00,
    is_published BOOLEAN NOT NULL DEFAULT true,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- 3. Passages (篇章材料表 - 阅读理解/完形填空)
CREATE TABLE IF NOT EXISTS public.passages (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    exam_id UUID NOT NULL REFERENCES public.exams(id) ON DELETE CASCADE,
    category_id TEXT NOT NULL REFERENCES public.categories(id) ON DELETE CASCADE,
    section_type TEXT NOT NULL CHECK (section_type IN ('reading', 'cloze', 'single')),
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    sort_order INT NOT NULL DEFAULT 0
);

-- 4. Questions (题目明细表 - 纯客观题)
CREATE TABLE IF NOT EXISTS public.questions (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    exam_id UUID NOT NULL REFERENCES public.exams(id) ON DELETE CASCADE,
    passage_id UUID REFERENCES public.passages(id) ON DELETE CASCADE,
    category_id TEXT NOT NULL REFERENCES public.categories(id) ON DELETE CASCADE,
    q_type TEXT NOT NULL CHECK (q_type IN ('choice', 'cloze_item', 'reading_item')),
    stem TEXT NOT NULL,
    options JSONB NOT NULL,
    correct_answer TEXT NOT NULL,
    explanation TEXT NOT NULL,
    points NUMERIC(5,2) NOT NULL DEFAULT 2.00,
    sort_order INT NOT NULL DEFAULT 0
);

-- 5. Profiles (用户资料与权限表)
CREATE TABLE IF NOT EXISTS public.profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    username TEXT UNIQUE NOT NULL,
    nickname TEXT,
    avatar_url TEXT,
    role TEXT NOT NULL DEFAULT 'student' CHECK (role IN ('student', 'admin')),
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- 6. User Backups (云端极简快照备份表 - 每用户仅 1 条记录)
CREATE TABLE IF NOT EXISTS public.user_backups (
    user_id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    backup_data JSONB NOT NULL DEFAULT '{}'::jsonb,
    summary JSONB NOT NULL DEFAULT '{}'::jsonb,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ==============================================================================
-- Triggers & Functions
-- ==============================================================================

-- Trigger Function: Auto create profile on user signup & make 1st user Admin
CREATE OR REPLACE FUNCTION public.handle_new_user()
RETURNS TRIGGER AS $$
DECLARE
    user_count INT;
    assigned_role TEXT;
    raw_user_meta JSONB;
    extracted_username TEXT;
    extracted_nickname TEXT;
BEGIN
    SELECT count(*) INTO user_count FROM public.profiles;
    IF user_count = 0 THEN
        assigned_role := 'admin';
    ELSE
        assigned_role := 'student';
    END IF;

    raw_user_meta := NEW.raw_user_meta_data;
    extracted_username := COALESCE(raw_user_meta->>'username', split_part(NEW.email, '@', 1));
    extracted_nickname := COALESCE(raw_user_meta->>'nickname', extracted_username);

    INSERT INTO public.profiles (id, username, nickname, role, created_at, updated_at)
    VALUES (NEW.id, extracted_username, extracted_nickname, assigned_role, now(), now())
    ON CONFLICT (id) DO UPDATE SET 
        username = EXCLUDED.username,
        updated_at = now();

    RETURN NEW;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- Drop trigger if exists and recreate
DROP TRIGGER IF EXISTS on_auth_user_created ON auth.users;
CREATE TRIGGER on_auth_user_created
    AFTER INSERT ON auth.users
    FOR EACH ROW EXECUTE FUNCTION public.handle_new_user();

-- Helper Function for Admins to reset user passwords
CREATE OR REPLACE FUNCTION public.admin_reset_user_password(target_user_id UUID, new_plain_password TEXT)
RETURNS BOOLEAN AS $$
BEGIN
    -- Only allow if the executing user is an admin
    IF NOT EXISTS (
        SELECT 1 FROM public.profiles 
        WHERE id = auth.uid() AND role = 'admin'
    ) THEN
        RAISE EXCEPTION 'Permission denied. Only administrators can reset user passwords.';
    END IF;

    UPDATE auth.users
    SET encrypted_password = crypt(new_plain_password, gen_salt('bf')),
        updated_at = now()
    WHERE id = target_user_id;

    RETURN true;
END;
$$ LANGUAGE plpgsql SECURITY DEFINER;

-- ==============================================================================
-- Row Level Security (RLS) Policies
-- ==============================================================================

-- Enable RLS
ALTER TABLE public.categories ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.exams ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.passages ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.questions ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.user_backups ENABLE ROW LEVEL SECURITY;

-- 1. Categories: Everyone can read
DROP POLICY IF EXISTS "Anyone can read categories" ON public.categories;
CREATE POLICY "Anyone can read categories" ON public.categories FOR SELECT USING (true);

-- 2. Exams: Authenticated users can read published exams; Admins have full access
DROP POLICY IF EXISTS "Anyone can read published exams" ON public.exams;
CREATE POLICY "Anyone can read published exams" ON public.exams FOR SELECT USING (is_published = true);

DROP POLICY IF EXISTS "Admins can manage exams" ON public.exams;
CREATE POLICY "Admins can manage exams" ON public.exams FOR ALL USING (
    EXISTS (SELECT 1 FROM public.profiles WHERE id = auth.uid() AND role = 'admin')
);

-- 3. Passages: Everyone can read; Admins have full access
DROP POLICY IF EXISTS "Anyone can read passages" ON public.passages;
CREATE POLICY "Anyone can read passages" ON public.passages FOR SELECT USING (true);

DROP POLICY IF EXISTS "Admins can manage passages" ON public.passages;
CREATE POLICY "Admins can manage passages" ON public.passages FOR ALL USING (
    EXISTS (SELECT 1 FROM public.profiles WHERE id = auth.uid() AND role = 'admin')
);

-- 4. Questions: Everyone can read; Admins have full access
DROP POLICY IF EXISTS "Anyone can read questions" ON public.questions;
CREATE POLICY "Anyone can read questions" ON public.questions FOR SELECT USING (true);

DROP POLICY IF EXISTS "Admins can manage questions" ON public.questions;
CREATE POLICY "Admins can manage questions" ON public.questions FOR ALL USING (
    EXISTS (SELECT 1 FROM public.profiles WHERE id = auth.uid() AND role = 'admin')
);

-- 5. Profiles: Users can view their own; Admins can view all and update
DROP POLICY IF EXISTS "Users can view and update own profile" ON public.profiles;
CREATE POLICY "Users can view and update own profile" ON public.profiles 
    FOR ALL USING (auth.uid() = id);

DROP POLICY IF EXISTS "Admins can view and manage all profiles" ON public.profiles;
CREATE POLICY "Admins can view and manage all profiles" ON public.profiles 
    FOR ALL USING (
        EXISTS (SELECT 1 FROM public.profiles WHERE id = auth.uid() AND role = 'admin')
    );

-- 6. User Backups: Users can only read/insert/update their own backup
DROP POLICY IF EXISTS "Users can manage own backup" ON public.user_backups;
CREATE POLICY "Users can manage own backup" ON public.user_backups 
    FOR ALL USING (auth.uid() = user_id) 
    WITH CHECK (auth.uid() = user_id);

-- ==============================================================================
-- Pre-seeded Curated Mock/Real Exams (CET-4 & KY-1 精选真题样卷)
-- ==============================================================================

DO $$
DECLARE
    cet4_exam_id UUID := '11111111-1111-1111-1111-111111111111';
    ky1_exam_id UUID := '22222222-2222-2222-2222-222222222222';
    p1_id UUID := '33333333-3333-3333-3333-333333333333';
    p2_id UUID := '44444444-4444-4444-4444-444444444444';
    p3_id UUID := '55555555-5555-5555-5555-555555555555';
BEGIN
    -- Exam 1: CET-4 精选真题
    INSERT INTO public.exams (id, category_id, title, year, exam_type, duration_minutes, total_score, pass_score, is_published)
    VALUES (cet4_exam_id, 'cet4', '2024年12月大学英语四级真题精选卷(卷一)', 2024, 'real', 50, 100.00, 60.00, true)
    ON CONFLICT (id) DO NOTHING;

    -- Passage 1: CET-4 Reading
    INSERT INTO public.passages (id, exam_id, category_id, section_type, title, content, sort_order)
    VALUES (p1_id, cet4_exam_id, 'cet4', 'reading', 'Section C: Careful Reading (仔细阅读)', 
    'In recent years, urban agriculture has evolved from a grassroots hobby into a vital component of sustainable metropolitan living. As urban centers expand and the global population concentrates in cities, the conventional food supply chain faces severe logistical and ecological challenges. Long-distance transport of fresh produce generates immense greenhouse gas emissions and increases vulnerability to fuel price shocks and supply disruptions.

Urban farming, which encompasses rooftop hydroponics, community gardens, and vertical indoor farms, offers a compelling solution by producing food directly where it is consumed. Beyond reducing "food miles" to mere meters, these localized farms conserve up to 90 percent more water than traditional agrarian methods through closed-loop recycling systems. Furthermore, they transform vacant municipal spaces and barren rooftops into productive green infrastructure that helps mitigate the urban heat island effect.

However, critics highlight economic and regulatory barriers. The capital expenditure required for automated vertical farming technology remains prohibitive for many small enterprises. Additionally, zoning laws in older cities rarely account for agricultural ventures, causing bureaucratic friction. Nonetheless, forward-looking municipalities are beginning to offer tax incentives and revised land-use codes, recognizing that urban agriculture strengthens community resilience and food sovereignty in an unpredictable climate future.',
    1)
    ON CONFLICT (id) DO NOTHING;

    -- Questions for Passage 1
    INSERT INTO public.questions (exam_id, passage_id, category_id, q_type, stem, options, correct_answer, explanation, points, sort_order)
    VALUES 
    (cet4_exam_id, p1_id, 'cet4', 'reading_item', 
    'What is identified as a major challenge of conventional food supply chains?',
    '[{"key":"A","text":"High water consumption in retail stores"},{"key":"B","text":"Heavy carbon emissions and supply vulnerabilities from long-distance transport"},{"key":"C","text":"Lack of consumer interest in fresh farm produce"},{"key":"D","text":"Strict zoning regulations in agricultural rural areas"}]'::jsonb,
    'B',
    '【考点精析】细节事实题。根据第一段末句 "Long-distance transport of fresh produce generates immense greenhouse gas emissions and increases vulnerability..." 可知，长途运输带来的高碳排放与供应链脆弱是传统供应链的主要挑战，故选 B。',
    20.00, 1),

    (cet4_exam_id, p1_id, 'cet4', 'reading_item', 
    'How do modern urban farms achieve substantial water conservation according to the passage?',
    '[{"key":"A","text":"By harvesting rainwater exclusively from suburban reservoirs"},{"key":"B","text":"By relying entirely on low-humidity natural air conditions"},{"key":"C","text":"Through closed-loop recycling systems in indoor or rooftop setups"},{"key":"D","text":"By decreasing the daily frequency of crop irrigation"}]'::jsonb,
    'C',
    '【考点精析】细节事实题。第二段第二句指出 "...conserve up to 90 percent more water than traditional agrarian methods through closed-loop recycling systems"，闭环循环利用系统是节水高达90%的核心途径，故选 C。',
    20.00, 2),

    (cet4_exam_id, p1_id, 'cet4', 'reading_item', 
    'What is one major obstacle that slows down the expansion of automated vertical farms?',
    '[{"key":"A","text":"Shortage of skilled laborers willing to work in urban centers"},{"key":"B","text":"Excessive consumer distrust toward hydroponically grown vegetables"},{"key":"C","text":"High initial capital expenditure required for advanced technology"},{"key":"D","text":"Strict international trade barriers on urban farming equipment"}]'::jsonb,
    'C',
    '【考点精析】细节推断题。根据第三段第二句 "The capital expenditure required for automated vertical farming technology remains prohibitive for many small enterprises" 可知，昂贵的初期资本投入（设备成本）是阻碍小企业扩张的主要障碍，故选 C。',
    20.00, 3);

    -- Passage 2: CET-4 Cloze
    INSERT INTO public.passages (id, exam_id, category_id, section_type, title, content, sort_order)
    VALUES (p2_id, cet4_exam_id, 'cet4', 'cloze', 'Section B: Cloze Test (完形填空精选)',
    'Sleep deprivation has become a silent epidemic in contemporary society. Many professionals sacrifice rest in pursuit of productivity, oblivious to the profound [1] on their cognitive health. Neuroscientific research reveals that during deep sleep, the brain activates the glymphatic system to eliminate metabolic waste that accumulates throughout waking hours. Without sufficient rest, these toxic proteins linger, impairing memory consolidation and increasing the [2] of neurodegenerative disorders over time. Furthermore, chronic sleep deficit disrupts hormonal balance, directly altering appetite regulation and leading to [3] weight gain. Cultivating disciplined sleep hygiene is therefore not a luxury, but a fundamental biological necessity.',
    2)
    ON CONFLICT (id) DO NOTHING;

    -- Questions for Passage 2
    INSERT INTO public.questions (exam_id, passage_id, category_id, q_type, stem, options, correct_answer, explanation, points, sort_order)
    VALUES
    (cet4_exam_id, p2_id, 'cet4', 'cloze_item',
    'Choose the best word for blank [1]:',
    '[{"key":"A","text":"consequence"},{"key":"B","text":"detriment"},{"key":"C","text":"impact"},{"key":"D","text":"precaution"}]'::jsonb,
    'C',
    '【考点精析】固定搭配与语义辨析。have an impact on 为固定搭配，意为“对……产生深远影响/冲击”。oblivious to the profound impact on their cognitive health 意为“忽视了对自身认知健康的深刻影响”，故选 C。',
    15.00, 4),

    (cet4_exam_id, p2_id, 'cet4', 'cloze_item',
    'Choose the best word for blank [2]:',
    '[{"key":"A","text":"probability"},{"key":"B","text":"obstacle"},{"key":"C","text":"remedy"},{"key":"D","text":"advantage"}]'::jsonb,
    'A',
    '【考点精析】语境逻辑题。后文紧接“神经退行性疾病”，此处表示睡眠不足增加患病风险或概率，increasing the probability of... 最贴合语境，故选 A。',
    15.00, 5),

    (cet4_exam_id, p2_id, 'cet4', 'cloze_item',
    'Choose the best word for blank [3]:',
    '[{"key":"A","text":"unintentional"},{"key":"B","text":"beneficial"},{"key":"C","text":"negligible"},{"key":"D","text":"provisional"}]'::jsonb,
    'A',
    '【考点精析】形容词辨析题。unintentional 意为“非本意的、无意识的”。睡眠不足打乱激素平衡，导致食欲亢进进而带来非预期的体重增加，故选 A。',
    10.00, 6);

    -- Exam 2: KY-1 考研英语一精选题卷
    INSERT INTO public.exams (id, category_id, title, year, exam_type, duration_minutes, total_score, pass_score, is_published)
    VALUES (ky1_exam_id, 'ky1', '2024年全国硕士研究生招生考试英语(一)真题精选卷', 2024, 'real', 60, 100.00, 60.00, true)
    ON CONFLICT (id) DO NOTHING;

    -- Passage 3: KY-1 Reading
    INSERT INTO public.passages (id, exam_id, category_id, section_type, title, content, sort_order)
    VALUES (p3_id, ky1_exam_id, 'ky1', 'reading', 'Text 1: Reading Comprehension (仔细阅读精析)',
    'The traditional premise of intellectual property (IP) law rests upon a bargain: society grants creators temporary monopoly privileges in exchange for the eventual enrichment of the public domain. However, the meteoric ascent of generative artificial intelligence is destabilizing this foundational doctrine. Because large models are trained on billions of copyrighted works scrape-mined across the internet without explicit licensing, authors and artists contend that tech conglomerates have committed systematic infringement on an industrial scale.

Silicon Valley giants counter by invoking the "fair use" exception, asserting that training an AI system transforms existing expression into novel statistical correlations rather than reproducing verbatim copies. Yet this defense conflates the mathematical process of algorithmic assimilation with the socioeconomic consequences of market substitution. When an AI tool can instantaneously generate illustrations in the distinctive visual aesthetic of a living illustrator, it ceases to merely "learn" and begins to cannibalize the creator''s livelihood.

The judicial resolution of this dispute will redefine the boundaries of human creative agency. If courts grant unfettered immunity to AI builders under fair use, they risk disincentivizing original cultural production. Conversely, an overly stringent licensing regime could consolidate the AI market into the hands of a few monopolistic behemoths capable of paying blanket licensing settlements. Crafting a balanced statutory framework—perhaps through statutory royalties or collective licensing bodies—is the imperative copyright challenge of our era.',
    1)
    ON CONFLICT (id) DO NOTHING;

    -- Questions for Passage 3
    INSERT INTO public.questions (exam_id, passage_id, category_id, q_type, stem, options, correct_answer, explanation, points, sort_order)
    VALUES
    (ky1_exam_id, p3_id, 'ky1', 'reading_item',
    'According to Paragraph 1, what is the core grievance raised by authors and artists against AI companies?',
    '[{"key":"A","text":"AI developers restrict public access to digital cultural works"},{"key":"B","text":"Copyrighted content was harvested without permission for model training"},{"key":"C","text":"The public domain has ceased to benefit from artistic creations"},{"key":"D","text":"Patent laws fail to protect statistical algorithmic innovations"}]'::jsonb,
    'B',
    '【考点精析】考研细节事实题。第一段指出 "Because large models are trained on billions of copyrighted works scrape-mined across the internet without explicit licensing..."，创作者的核心诉求是其受版权保护的作品未经显式授权便被抓取用于模型训练，故选 B。',
    35.00, 1),

    (ky1_exam_id, p3_id, 'ky1', 'reading_item',
    'Why does the author criticize the tech companies'' "fair use" defense in Paragraph 2?',
    '[{"key":"A","text":"It ignores the devastating market substitution effect on human creators"},{"key":"B","text":"It misunderstands the mathematical principles of neural networks"},{"key":"C","text":"It violates international agreements on statistical copyright standards"},{"key":"D","text":"It prevents living artists from utilizing artificial intelligence"}]'::jsonb,
    'A',
    '【考点精析】考研作者态度与推理题。第二段指出该辩护 "conflates the mathematical process... with the socioeconomic consequences of market substitution"，当 AI 能够精确模仿特定画家风格时，其实质是在吞噬人类创作者的生存空间，造成市场替代效应，故选 A。',
    35.00, 2),

    (ky1_exam_id, p3_id, 'ky1', 'reading_item',
    'What potential consequence does the author warn against if an excessively strict licensing regime is imposed?',
    '[{"key":"A","text":"A rapid degradation of generative AI model accuracy"},{"key":"B","text":"Market monopolization by a few well-funded corporate giants"},{"key":"C","text":"Widespread unemployment among intellectual property attorneys"},{"key":"D","text":"The complete collapse of digital collective licensing bodies"}]'::jsonb,
    'B',
    '【考点精析】段落细节推断题。第三段指出 "Conversely, an overly stringent licensing regime could consolidate the AI market into the hands of a few monopolistic behemoths capable of paying blanket licensing settlements"，若实施过严的授权许可机制，只有极少数财力雄厚的巨头能承担巨额版权许可费，将导致行业垄断加剧，故选 B。',
    30.00, 3);

END $$;
