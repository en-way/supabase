-- ==============================================================================
-- Migration: 20260919000006_add_table_comments_and_documentation.sql
-- Description: Add comprehensive Chinese documentation comments for Supabase Table Editor
-- ==============================================================================

-- 1. Categories (考试科目分类表)
COMMENT ON TABLE public.categories IS '考试科目分类表 (定义四六级、考研英语等不同分类体系)';
COMMENT ON COLUMN public.categories.id IS '科目标识码 (主键，如 cet4:大学英语四级, cet6:大学英语六级, ky1:考研英语一, ky2:考研英语二)';
COMMENT ON COLUMN public.categories.name IS '科目全称 (如: 大学英语四级 (CET-4))';
COMMENT ON COLUMN public.categories.description IS '科目详细介绍与题库说明';
COMMENT ON COLUMN public.categories.sort_order IS '在网站首页中的展示排序号 (数字越小越靠前)';

-- 2. Exams (试卷主表)
COMMENT ON TABLE public.exams IS '试卷主表 (统一百分制：满分100分，及格60分)';
COMMENT ON COLUMN public.exams.id IS '试卷唯一UUID编号 (主键)';
COMMENT ON COLUMN public.exams.category_id IS '所属科目分类 (关联 categories.id，如 cet4, cet6, ky1, ky2)';
COMMENT ON COLUMN public.exams.title IS '试卷完整标题 (例如: 2024年12月大学英语四级真题精选卷(卷一))';
COMMENT ON COLUMN public.exams.year IS '真题/模拟考试年份 (例如: 2024)';
COMMENT ON COLUMN public.exams.exam_type IS '试卷性质 (real:历年真题 | mock:考前全真模拟卷)';
COMMENT ON COLUMN public.exams.duration_minutes IS '考试限时时长 (分钟，默认60分钟)';
COMMENT ON COLUMN public.exams.total_score IS '试卷总满分 (统一百分制: 100.00)';
COMMENT ON COLUMN public.exams.pass_score IS '及格基准分 (统一百分制: 60.00)';
COMMENT ON COLUMN public.exams.is_published IS '公开状态 (true:前台试卷大厅公开可见 | false:下架隐藏仅管理员可见)';
COMMENT ON COLUMN public.exams.approval_status IS '审核状态 (approved:已批准上架 | pending_upload:待超管审批发布 | pending_delete:待超管审批删除 | rejected:已驳回)';
COMMENT ON COLUMN public.exams.created_by IS '上传或导入该试卷的管理员账号UUID';
COMMENT ON COLUMN public.exams.created_at IS '试卷创建或导入时间';

-- 3. Passages (篇章长文材料表)
COMMENT ON TABLE public.passages IS '篇章材料表 (包含长篇仔细阅读、完形填空等英文长文，支持在后台直接双击修改正文)';
COMMENT ON COLUMN public.passages.id IS '篇章唯一UUID编号 (主键)';
COMMENT ON COLUMN public.passages.exam_id IS '所属试卷UUID (关联 exams.id)';
COMMENT ON COLUMN public.passages.category_id IS '所属科目分类 (关联 categories.id)';
COMMENT ON COLUMN public.passages.section_type IS '题型版块 (reading:仔细阅读 | cloze:完形填空 | single:独立语法词汇单选)';
COMMENT ON COLUMN public.passages.title IS '材料小节大标题 (例如: Section C: Reading Comprehension 或 Text 1)';
COMMENT ON COLUMN public.passages.content IS '英文篇章长文完整正文 (支持多段落直接排版换行)';
COMMENT ON COLUMN public.passages.sort_order IS '在整套试卷中的篇章展示排序号 (1, 2, 3...)';

-- 4. Questions (题目明细表)
COMMENT ON TABLE public.questions IS '客观题明细表 (含题干、选项、标准答案与深度解析，支持在后台直接双击改题)';
COMMENT ON COLUMN public.questions.id IS '题目唯一UUID编号 (主键)';
COMMENT ON COLUMN public.questions.exam_id IS '所属试卷UUID (关联 exams.id)';
COMMENT ON COLUMN public.questions.passage_id IS '所属篇章长文UUID (关联 passages.id，独立单选题可为空)';
COMMENT ON COLUMN public.questions.category_id IS '所属科目分类 (关联 categories.id)';
COMMENT ON COLUMN public.questions.q_type IS '题目子类型 (reading_item:阅读小题 | cloze_item:完形填空空缺小题 | choice:单项选择题)';
COMMENT ON COLUMN public.questions.stem IS '题目题干说明或问题文字 (支持双击修改)';
COMMENT ON COLUMN public.questions.options IS '选项内容JSON (支持数组 [{"key":"A","text":"内容"}] 或极简键值对 {"A":"选项A内容","B":"选项B内容"})';
COMMENT ON COLUMN public.questions.correct_answer IS '标准正确答案字母 (填大写字母 A, B, C 或 D)';
COMMENT ON COLUMN public.questions.explanation IS '题目考点深度精析与解题思路说明 (前台做题与错题本解析中展示)';
COMMENT ON COLUMN public.questions.points IS '该小题分值 (默认2.00~20.00分)';
COMMENT ON COLUMN public.questions.sort_order IS '在该篇章或试卷中的小题排序号 (1, 2, 3...)';

-- 5. Profiles (用户资料与权限表)
COMMENT ON TABLE public.profiles IS '用户档案与权限表 (纯用户名/学号体系)';
COMMENT ON COLUMN public.profiles.id IS '用户唯一UUID (关联 auth.users.id)';
COMMENT ON COLUMN public.profiles.username IS '用户名/学号 (全站唯一凭据，首选英文字母、数字)';
COMMENT ON COLUMN public.profiles.nickname IS '学员个性昵称 (登录后在个人中心可随时修改)';
COMMENT ON COLUMN public.profiles.role IS '权限角色 (super_admin:最高权限超级管理员 | admin:普通管理员 | student:普通学员)';
COMMENT ON COLUMN public.profiles.created_at IS '账号注册创建时间';

-- 6. System Settings (系统全局配置单例表)
COMMENT ON TABLE public.system_settings IS '系统全局参数单例表 (全站人数上限与注册开关控制)';
COMMENT ON COLUMN public.system_settings.id IS '单例主键 (固定为1)';
COMMENT ON COLUMN public.system_settings.max_students_limit IS '全站普通学员注册上限人数 (0表示不设限；大于0时，达到人数自动硬拦截暂停新注册)';
COMMENT ON COLUMN public.system_settings.registration_enabled IS '全站新学员开放注册总开关 (true:开放注册 | false:临时关闭注册通道)';
COMMENT ON COLUMN public.system_settings.updated_at IS '配置最后修改时间';

-- 7. User Backups (云端存档元数据表)
COMMENT ON TABLE public.user_backups IS '云端备份元数据表 (仅存轻量状态摘要，大JSON存放在1GB Storage桶中，行仅占50字节)';
COMMENT ON COLUMN public.user_backups.user_id IS '学员账号UUID (主键)';
COMMENT ON COLUMN public.user_backups.summary IS '学习存档统计摘要JSON (包含错题数、生词数、模考数等概要信息)';
COMMENT ON COLUMN public.user_backups.file_path IS '存放于 Supabase Storage 私有桶 user-backups 中的文件路径 (如: uid/backup.json)';
COMMENT ON COLUMN public.user_backups.updated_at IS '上次更新同步时间';
