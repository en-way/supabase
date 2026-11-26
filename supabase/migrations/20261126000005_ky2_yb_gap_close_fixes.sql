-- KY2 Yellow Book Gap-Close Verification Fixes (2018 Q32 & 2017 Q36)
BEGIN;

-- 2018 Q32: Restore official Yellow Book option order ([A] <-> [C]), key (C -> A), and explanation
UPDATE public.questions
SET
    options = '[{"key": "A", "value": "A", "text": "pose a risk to Facebook users", "content": "pose a risk to Facebook users"}, {"key": "B", "value": "B", "text": "mislead the European commission", "content": "mislead the European commission"}, {"key": "C", "value": "C", "text": "worsen political disputes", "content": "worsen political disputes"}, {"key": "D", "value": "D", "text": "mess up customer records", "content": "mess up customer records"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［考点提炼］事实细节题＋后果推断。
［解题思路］根据定位词 Linking phone numbers to Facebook identities 定位至第二段：Facebook 违背承诺将手机号与社交身份关联，即使不知道消息内容，了解谁与谁通信也是极其泄密的（enormously revealing），后文以政界丑闻和用户购买记录为例，说明个人隐私面临严重泄露风险。A项 pose a risk to Facebook users（对 Facebook 用户构成风险）准确概括了其潜在危害。
［错项排除］[B] mislead the European commission（误导欧盟委员会）是批准收购时的误导与违约行为，并非绑定账号本身的后果；[C] worsen political disputes（加剧政治争端）源自“特蕾莎·梅政敌在群内密谋”的隐私泄露例证，文中并未提及会加剧政治争端；[D] mess up customer records（弄乱客户记录）违背原文记录变得极具价值并暴露隐私的表述。'
WHERE id = '498f1cd4-cdeb-55df-b4fb-86081cd848c4';

-- 2017 Q36: Restore official Yellow Book distractor order ([B]/[C]/[D]) and explanation
UPDATE public.questions
SET
    options = '[{"key": "A", "value": "A", "text": "consumed a record-high percentage of budget", "content": "consumed a record-high percentage of budget"}, {"key": "B", "value": "B", "text": "severely damaged the ecology of western states", "content": "severely damaged the ecology of western states"}, {"key": "C", "value": "C", "text": "caused a huge rise of infrastructure expenditure", "content": "caused a huge rise of infrastructure expenditure"}, {"key": "D", "value": "D", "text": "exhausted unprecedented management efforts", "content": "exhausted unprecedented management efforts"}]'::jsonb,
    correct_answer = 'A',
    explanation = '［考点提炼］因果细节题（第一、二段）。
［精准定位］定位至第一段与第二段第一句：“...the growing frequency of wildfires is a national concern because of its impact on federal tax dollars, says Professor Max Moritz, a specialist in fire ecology and management. In 2015, the US Forest Service for the first time spent more than half of its $5.5 billion annual budget fighting fires — nearly double the percentage it spent on such efforts 20 years ago.”
［解题思路］野火频发之所以成为全美关切，关键在于对联邦税收的挤压：2015年美国林务局首次将55亿美元年度预算的过半数额（几乎是20年前占比的两倍）用于扑救山火，耗费了创纪录高比例的财政预算，故选 [A] consumed a record-high percentage of budget。
［错项排除］[B] severely damaged the ecology of western states 利用第一段 western states 与 ecology 等碎片信息拼凑干扰，脱离“影响联邦税收成为全国关切”的主干；[C] caused a huge rise of infrastructure expenditure 与第二段末句“fewer federal funds today are going towards... infrastructure upkeep”正好相反；[D] exhausted unprecedented management efforts 利用第二段 for the first time、efforts 与 management 等词捏造“消耗史无前例的管理力度”，曲解原意。'
WHERE id = '2f22b13c-13f3-5965-9773-70355058acde';

COMMIT;
