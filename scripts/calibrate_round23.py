import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("=== Starting Round 23 Calibration Implementation ===")

DATA_DIR = 'public/data/exams'

# Exam file mapping
EXAM_MAP = {
    '2001_ky1': '2c892204-071f-5943-86be-d49bca93fe71.json',
    '2005_ky1': 'd8ba7d14-5305-538d-b81b-f0f7ef3db461.json',
    '2006_ky1': 'c6e9dbac-6148-532e-90d2-2a8d3682a6ac.json',
    '2007_ky1': 'e560bab8-4d9a-5149-a93f-1ee1d7bf4225.json',
    '2008_ky1': 'd80926ab-1841-5d1f-a999-56773986c46d.json',
    '2009_ky1': '9369aa41-c91e-548c-bf99-1ad46a07ac25.json',
    '2022_ky2': 'cc4bf627-e456-538f-87e2-4a99ebb613ed.json',
}

def load_exam(key):
    path = os.path.join(DATA_DIR, EXAM_MAP[key])
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f), path

def save_exam(path, data):
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

updated_questions = []

# ----------------------------------------------------
# 1. 2008 ky1 Q35
# ----------------------------------------------------
d2008, p2008 = load_exam('2008_ky1')
for q in d2008['questions']:
    if q['sort_order'] == 35:
        print("[Calibrating] 2008 ky1 Q35")
        q['options'] = [
            {'key': 'A', 'text': 'the change of human height follows a cyclic pattern', 'value': 'A'},
            {'key': 'B', 'text': 'human height is becoming even more predictable', 'value': 'B'},
            {'key': 'C', 'text': 'Americans have reached their genetic growth limit', 'value': 'C'},
            {'key': 'D', 'text': 'the genetic pattern of Americans has altered', 'value': 'D'}
        ]
        q['correct_answer'] = 'C'
        q['answer'] = 'C'
        q['explanation'] = (
            "［精准定位］文章前三段指出：美国人总体身高已停止增长；第四段明确原因：达到基因设定极限；"
            "第五段则指出这种基因最大值近期不会改变。可见［C］为文章意在传达的主旨。\n\n"
            "［命题解密］［C］是全文主旨句（第二段①句）Americans have generally stopped growing 以及其同义表达 "
            "reached their limit ... aren't likely to get any taller ... average height hasn't really changed since 1960 的概括改写。"
            "其中 genetic 对应第四段所述“真正原因” real constraints that are set by the genetic architecture。\n\n"
            "［干扰排除］\n"
            "［A］将第三段②③④句所述历史个别现象“20 世纪初美国人身高增长缓慢，随后出现了较快的增长；至 1960 年又停止了增长”篡改为“整体趋势”，且其本身也算不上是“循环模式”。\n"
            "［B］误将末段末句 And if you need to predict human height 包含的信息引申为“人类身高的可预测性”，偏离了文章关于身高停止增长的核心主旨。\n"
            "［D］将末段首句 can 歪曲为事实，误以为基因模式“已经改变”，实际上该句转折之后指出 don't expect this to happen soon，说明短期内不会改变。\n\n"
            "［技巧总结］主旨大意题的解题关键在于：透过各段观点处、结论处及转折处掌握文章核心线索。正确选项往往是对全文核心主旨的同义替换或高度概括。"
        )
        updated_questions.append(('2008_ky1', q['id'], 35))
save_exam(p2008, d2008)

# ----------------------------------------------------
# 2. 2006 ky1 Q22, Q25, Q31, Q32, Q36, Q38, Q39
# ----------------------------------------------------
d2006, p2006 = load_exam('2006_ky1')
for q in d2006['questions']:
    so = q['sort_order']
    if so == 22:
        print("[Calibrating] 2006 ky1 Q22")
        q['stem'] = 'According to the author, the department stores of the 19th century'
        q['options'] = [
            {'key': 'A', 'text': 'played a role in the spread of popular culture', 'value': 'A'},
            {'key': 'B', 'text': 'became intimate shops for common consumers', 'value': 'B'},
            {'key': 'C', 'text': 'satisfied the needs of a knowledgeable elite', 'value': 'C'},
            {'key': 'D', 'text': 'owed its emergence to the culture of consumption', 'value': 'D'}
        ]
        q['correct_answer'] = 'A'
        q['answer'] = 'A'
        q['explanation'] = (
            "［精准定位］首段②句指出大众文化有着服饰和言语上大众化的一致，以及随意和不拘礼节的特点。"
            "③④⑤句指出：人们被一种由 19 世纪的百货商店掀起的消费文化同化，当时的百货商店将购物转变为一种公共和大众的行为。"
            "概括可知，19 世纪的百货商店在传播大众文化方面发挥了重要作用，［A］正确。\n\n"
            "［命题解密］正确项［A］是对文中 ... launched a culture of consumption ... turned shopping into a public and democratic act 等内容的概括。\n\n"
            "［干扰排除］\n"
            "［B］将文中信息“百货商店与私密商店存在本质不同（Instead of intimate shops ... these were stores ...）”改为“百货商店成为了私密商店（became intimate shops）”。\n"
            "［C］偷换概念：满足有见识的精英人士需求（satisfied the needs of a knowledgeable elite）的不是百货商场（department stores of the 19th century）而是私密商店（intimate shops）。\n"
            "［D］颠倒因果：将“19 世纪的百货商店是消费文化出现的原因（... a culture of consumption launched by the 19th century department stores）”改为“19 世纪的百货商店出现的原因是消费文化（owed its emergence to the culture of consumption）”。\n\n"
            "［技巧总结］本题意在考查学生区分概念、理清关系的能力。解题时需要从“启动逻辑推理，得出正确项”和“理解事实细节，识别干扰项”两个角度同时进行，并不断相互检测排除矛盾、最终确定正确项。"
        )
        updated_questions.append(('2006_ky1', q['id'], 22))

    elif so == 25:
        print("[Calibrating] 2006 ky1 Q25")
        for opt in q['options']:
            if opt['key'] == 'B':
                opt['text'] = 'successful'
        updated_questions.append(('2006_ky1', q['id'], 25))

    elif so == 31:
        print("[Calibrating] 2006 ky1 Q31")
        for opt in q['options']:
            if opt['key'] == 'A':
                opt['text'] = 'large animals were vulnerable to the changing'
            elif opt['key'] == 'D':
                opt['text'] = 'slow-growing fish outlive fast-growing ones'
        updated_questions.append(('2006_ky1', q['id'], 31))

    elif so == 32:
        print("[Calibrating] 2006 ky1 Q32")
        q['stem'] = "We can infer from Dr. Myers and Dr. Worm’s paper that"
        q['options'] = [
            {'key': 'A', 'text': 'the stock of large predators in some old fisheries has reduced by 90%', 'value': 'A'},
            {'key': 'B', 'text': 'there are only half as many fisheries as there were 15 years ago', 'value': 'B'},
            {'key': 'C', 'text': 'the catch sizes in new fisheries are only 20% of the original amount', 'value': 'C'},
            {'key': 'D', 'text': 'the number of large predators dropped faster in new fisheries than in the old', 'value': 'D'}
        ]
        q['correct_answer'] = 'A'
        q['answer'] = 'A'
        q['explanation'] = (
            "［精准定位］第二段⑤句指出，新渔场在被开发后的 15 年中大型食肉鱼类减少 80%，即剩下 20%。"
            "⑥句指出，一些长期捕鱼的地区，生物量自那之后又减少了一半，即再减 10%。"
            "因此，旧渔场中大型食肉鱼类共减少了 90%，［A］正确。\n\n"
            "［命题解密］正确项［A］是对第二段⑤⑥句内容进行简单计算得出的结果。"
            "old fisheries 对应文中 long-fished areas，结合句中的数据计算：减少了 80% + (20% × 1/2) = 90%。\n\n"
            "［干扰排除］\n"
            "［B］误将原文中 15 年前大型食肉鱼类生物量减少了 80% 曲解为渔场数量减少了一半。\n"
            "［C］曲解文意，新渔场的捕捞量并不是原来总量的 20%，而是生物量减少了 80%。\n"
            "［D］无中生有，文中并未将新渔场和旧渔场中大型食肉鱼类减少的速度进行比较。\n\n"
            "［技巧总结］细节推断题解题时需要严格依据原文提供的数据和逻辑关系进行计算或推导，不能凭常识主观臆断。"
        )
        updated_questions.append(('2006_ky1', q['id'], 32))

    elif so == 36:
        print("[Calibrating] 2006 ky1 Q36")
        q['stem'] = 'By citing the examples of poets Wordsworth and Baudelaire, the author intends to show that'
        q['options'] = [
            {'key': 'A', 'text': 'poetry is not as expressive of joy as painting or music', 'value': 'A'},
            {'key': 'B', 'text': 'art grows out of both positive and negative feelings', 'value': 'B'},
            {'key': 'C', 'text': 'poets today are less skeptical of happiness', 'value': 'C'},
            {'key': 'D', 'text': 'artists have changed their focus of interest', 'value': 'D'}
        ]
        q['correct_answer'] = 'D'
        q['answer'] = 'D'
        q['explanation'] = (
            "［精准定位］第一段指出现代艺术家喜欢表达悲伤主题；第二段指出过去并非如此，最早期的艺术形式最适合表达快乐主题，"
            "但大约从 19 世纪开始，艺术家们开始认为快乐虚假无聊。随后举例指出华兹华斯《水仙花》向波德莱尔《恶之花》的转变。"
            "显然，作者举例意在以点带面说明艺术家关注点从“积极情感”到“负面情感”的改变，［D］正确。\n\n"
            "［命题解密］正确项［D］artists have changed their focus of interest 概括前两段 "
            "focus on the ones that feel bad ... This wasn’t always so ... best suited for expressing joy 所体现的今昔变化。\n\n"
            "［干扰排除］\n"
            "［A］将第二段用以证实不同论点的例子［绘画和音乐（painting and music）用以说明最早期艺术最适合表达快乐主题，"
            "诗歌（daffodils ... flowers of evil）用以说明艺术家对快乐看法的渐次转变］杂糅设置干扰，而文中并未将“绘画”和“音乐与诗歌”进行比较。\n"
            "［B］将文中的“转变关系——艺术从关注正面情感变化为关注负面情感”改为“共存关系——艺术既产生于正面情感也产生于负面情感（both ... and ...）”。\n"
            "［C］将第二段③句（所考事例例证对象）“艺术家们开始质疑快乐（began seeing happiness as meaningless ... boring）”改为与之相悖的“艺术家们不再那么质疑快乐”。\n\n"
            "［技巧总结］第一、二段重在今昔对比说明变化，紧就其中涉及的举例命题，实则变相考查两段主旨。"
            "解答此题时需：先借助“路标词”和“反义表达”识别今昔对比逻辑；后对信息进行具体区分，并理清例子究竟归属于哪一方。"
        )
        updated_questions.append(('2006_ky1', q['id'], 36))

    elif so == 38:
        print("[Calibrating] 2006 ky1 Q38")
        for opt in q['options']:
            if opt['key'] == 'A':
                opt['text'] = 'emerges in the wake of the anti-happy art'
        updated_questions.append(('2006_ky1', q['id'], 38))

    elif so == 39:
        print("[Calibrating] 2006 ky1 Q39")
        q['stem'] = 'We can learn from the last paragraph that the author believes'
        q['options'] = [
            {'key': 'A', 'text': 'happiness more often than not ends in sadness', 'value': 'A'},
            {'key': 'B', 'text': 'the anti-happy art is distasteful but refreshing', 'value': 'B'},
            {'key': 'C', 'text': 'misery should be enjoyed rather than denied', 'value': 'C'},
            {'key': 'D', 'text': 'the anti-happy art flourishes when economy booms', 'value': 'D'}
        ]
        updated_questions.append(('2006_ky1', q['id'], 39))

save_exam(p2006, d2006)

# ----------------------------------------------------
# 3. 2005 ky1 (Q21, Q22, Q23, Q24, Q26, Q27, Q28, Q29, Q30, Q32, Q33, Q35, Q36, Q38, Q39)
# ----------------------------------------------------
d2005, p2005 = load_exam('2005_ky1')
for q in d2005['questions']:
    so = q['sort_order']
    if so == 21:
        print("[Calibrating] 2005 ky1 Q21")
        q['stem'] = 'In the opening paragraph, the author introduces his topic by'
        updated_questions.append(('2005_ky1', q['id'], 21))

    elif so == 22:
        print("[Calibrating] 2005 ky1 Q22")
        q['stem'] = 'The statement “it is all too monkey” (Last line, Paragraph 1) implies that'
        updated_questions.append(('2005_ky1', q['id'], 22))

    elif so == 23:
        print("[Calibrating] 2005 ky1 Q23")
        q['stem'] = 'Female capuchin monkeys were chosen for the research most probably because they are'
        updated_questions.append(('2005_ky1', q['id'], 23))

    elif so == 24:
        print("[Calibrating] 2005 ky1 Q24")
        q['stem'] = 'Dr. Brosnan and Dr. de Waal have eventually found in their study that the monkeys'
        for opt in q['options']:
            if opt['key'] == 'C':
                opt['text'] = 'will not be cooperative if feeling cheated'
        updated_questions.append(('2005_ky1', q['id'], 24))

    elif so == 26:
        print("[Calibrating] 2005 ky1 Q26")
        q['stem'] = 'An argument made by supporters of smoking was that'
        q['options'] = [
            {'key': 'A', 'text': 'there was no scientific evidence of the correlation between smoking and death', 'value': 'A'},
            {'key': 'B', 'text': 'the number of early deaths of smokers in the past decades was insignificant', 'value': 'B'},
            {'key': 'C', 'text': 'people had the freedom to choose their own way of life', 'value': 'C'},
            {'key': 'D', 'text': 'antismoking people were usually talking nonsense', 'value': 'D'}
        ]
        updated_questions.append(('2005_ky1', q['id'], 26))

    elif so == 27:
        print("[Calibrating] 2005 ky1 Q27")
        for opt in q['options']:
            if opt['key'] == 'D':
                opt['text'] = 'a guide'
        updated_questions.append(('2005_ky1', q['id'], 27))

    elif so == 28:
        print("[Calibrating] 2005 ky1 Q28")
        for opt in q['options']:
            if opt['key'] == 'A':
                opt['text'] = 'Endless studies kill action.'
        updated_questions.append(('2005_ky1', q['id'], 28))

    elif so == 29:
        print("[Calibrating] 2005 ky1 Q29")
        q['stem'] = 'According to the author, what should the Administration do about global warming?'
        for opt in q['options']:
            if opt['key'] == 'A':
                opt['text'] = 'Offer aid to build cleaner power plants.'
        updated_questions.append(('2005_ky1', q['id'], 29))

    elif so == 30:
        print("[Calibrating] 2005 ky1 Q30")
        q['stem'] = 'The author associates the issue of global warming with that of smoking because'
        for opt in q['options']:
            if opt['key'] == 'B':
                opt['text'] = 'a lesson from the latter is applicable to the former'
            elif opt['key'] == 'C':
                opt['text'] = 'the outcome of the latter aggravates the former'
        updated_questions.append(('2005_ky1', q['id'], 30))

    elif so == 32:
        print("[Calibrating] 2005 ky1 Q32")
        q['stem'] = 'By referring to the limbic system, the author intends to show'
        updated_questions.append(('2005_ky1', q['id'], 32))

    elif so == 33:
        print("[Calibrating] 2005 ky1 Q33")
        for opt in q['options']:
            if opt['key'] == 'A':
                opt['text'] = 'aggravate in our unconscious mind'
            elif opt['key'] == 'C':
                opt['text'] = 'persist till the time we fall asleep'
            elif opt['key'] == 'D':
                opt['text'] = 'show up in dreams early at night'
        updated_questions.append(('2005_ky1', q['id'], 33))

    elif so == 35:
        print("[Calibrating] 2005 ky1 Q35")
        q['stem'] = 'What advice might Cartwright give to those who sometimes have bad dreams?'
        updated_questions.append(('2005_ky1', q['id'], 35))

    elif so == 36:
        print("[Calibrating] 2005 ky1 Q36")
        for opt in q['options']:
            if opt['key'] == 'C':
                opt['text'] = 'has caused the controversy over the counter-culture'
            elif opt['key'] == 'D':
                opt['text'] = 'brought about changes in public attitudes in the 1960s'
        updated_questions.append(('2005_ky1', q['id'], 36))

    elif so == 38:
        print("[Calibrating] 2005 ky1 Q38")
        for opt in q['options']:
            if opt['key'] == 'D':
                opt['text'] = 'Of all the varieties standard English can best convey complex ideas.'
        updated_questions.append(('2005_ky1', q['id'], 38))

    elif so == 39:
        print("[Calibrating] 2005 ky1 Q39")
        for opt in q['options']:
            if opt['key'] == 'C':
                opt['text'] = 'admiration for their memory'
            elif opt['key'] == 'D':
                opt['text'] = 'contempt for their old-fashionedness'
        updated_questions.append(('2005_ky1', q['id'], 39))

save_exam(p2005, d2005)

# ----------------------------------------------------
# 4. 2001 ky1 Q28
# ----------------------------------------------------
d2001, p2001 = load_exam('2001_ky1')
for q in d2001['questions']:
    if q['sort_order'] == 28:
        print("[Calibrating] 2001 ky1 Q28")
        q['stem'] = "It seems that now a country's economy depends much on"
        for opt in q['options']:
            if opt['key'] == 'D':
                opt['text'] = 'how much control it has over foreign corporations'
        # clean OCR error from explanation
        q['explanation'] = q['explanation'].replace('2&现在看来', '现在看来').replace('for&gn', 'foreign')
        updated_questions.append(('2001_ky1', q['id'], 28))
save_exam(p2001, d2001)

# ----------------------------------------------------
# 5. 2007 ky1 Cloze (Q1, Q2, Q6, Q9, Q12, Q13, Q25, Q31, Q39)
# ----------------------------------------------------
d2007, p2007 = load_exam('2007_ky1')
for q in d2007['questions']:
    so = q['sort_order']
    if so == 1:
        print("[Calibrating] 2007 ky1 Q1")
        for opt in q['options']:
            if opt['key'] == 'C': opt['text'] = 'peoples'
            elif opt['key'] == 'D': opt['text'] = 'individuals'
        updated_questions.append(('2007_ky1', q['id'], 1))
    elif so == 2:
        print("[Calibrating] 2007 ky1 Q2")
        q['options'] = [
            {'key': 'A', 'text': 'confusedly', 'value': 'A'},
            {'key': 'B', 'text': 'cheerfully', 'value': 'B'},
            {'key': 'C', 'text': 'worriedly', 'value': 'C'},
            {'key': 'D', 'text': 'hopefully', 'value': 'D'}
        ]
        updated_questions.append(('2007_ky1', q['id'], 2))
    elif so == 6:
        print("[Calibrating] 2007 ky1 Q6")
        q['options'] = [
            {'key': 'A', 'text': 'Presumably', 'value': 'A'},
            {'key': 'B', 'text': 'Incidentally', 'value': 'B'},
            {'key': 'C', 'text': 'Obviously', 'value': 'C'},
            {'key': 'D', 'text': 'Generally', 'value': 'D'}
        ]
        updated_questions.append(('2007_ky1', q['id'], 6))
    elif so == 9:
        print("[Calibrating] 2007 ky1 Q9")
        q['options'] = [
            {'key': 'A', 'text': 'therefore', 'value': 'A'},
            {'key': 'B', 'text': 'however', 'value': 'B'},
            {'key': 'C', 'text': 'indeed', 'value': 'C'},
            {'key': 'D', 'text': 'moreover', 'value': 'D'}
        ]
        updated_questions.append(('2007_ky1', q['id'], 9))
    elif so == 12:
        print("[Calibrating] 2007 ky1 Q12")
        for opt in q['options']:
            if opt['key'] == 'C': opt['text'] = 'Unless'
            elif opt['key'] == 'D': opt['text'] = 'While'
        updated_questions.append(('2007_ky1', q['id'], 12))
    elif so == 13:
        print("[Calibrating] 2007 ky1 Q13")
        for opt in q['options']:
            if opt['key'] == 'B': opt['text'] = 'for'
        updated_questions.append(('2007_ky1', q['id'], 13))
    elif so == 25:
        print("[Calibrating] 2007 ky1 Q25")
        for opt in q['options']:
            if opt['key'] == 'A': opt['text'] = '“Faith will move mountains.”'
        updated_questions.append(('2007_ky1', q['id'], 25))
    elif so == 31:
        print("[Calibrating] 2007 ky1 Q31")
        for opt in q['options']:
            if opt['key'] == 'A': opt['text'] = 'the safety net they used to enjoy has disappeared'
        updated_questions.append(('2007_ky1', q['id'], 31))
    elif so == 39:
        print("[Calibrating] 2007 ky1 Q39")
        for opt in q['options']:
            if opt['key'] == 'C': opt['text'] = 'realize the high cost of data restoration'
        updated_questions.append(('2007_ky1', q['id'], 39))
save_exam(p2007, d2007)

# ----------------------------------------------------
# 6. 2009 ky1 Cloze (Q7, Q9, Q16)
# ----------------------------------------------------
d2009, p2009 = load_exam('2009_ky1')
for q in d2009['questions']:
    so = q['sort_order']
    if so == 7:
        print("[Calibrating] 2009 ky1 Q7")
        for opt in q['options']:
            if opt['key'] == 'A': opt['text'] = 'incredible'
            elif opt['key'] == 'C': opt['text'] = 'inevitable'
        updated_questions.append(('2009_ky1', q['id'], 7))
    elif so == 9:
        print("[Calibrating] 2009 ky1 Q9")
        q['options'] = [
            {'key': 'A', 'text': 'invisible', 'value': 'A'},
            {'key': 'B', 'text': 'limited', 'value': 'B'},
            {'key': 'C', 'text': 'indefinite', 'value': 'C'},
            {'key': 'D', 'text': 'different', 'value': 'D'}
        ]
        updated_questions.append(('2009_ky1', q['id'], 9))
    elif so == 16:
        print("[Calibrating] 2009 ky1 Q16")
        for opt in q['options']:
            if opt['key'] == 'B': opt['text'] = 'overcome'
            elif opt['key'] == 'C': opt['text'] = 'determine'
        updated_questions.append(('2009_ky1', q['id'], 16))
save_exam(p2009, d2009)

# ----------------------------------------------------
# 7. 2022 ky2 Cloze Q6
# ----------------------------------------------------
d2022, p2022 = load_exam('2022_ky2')
for q in d2022['questions']:
    if q['sort_order'] == 6:
        print("[Calibrating] 2022 ky2 Q6")
        for opt in q['options']:
            if opt['key'] == 'A': opt['text'] = 'well-known'
        updated_questions.append(('2022_ky2', q['id'], 6))
save_exam(p2022, d2022)

print(f"\nSuccessfully calibrated {len(updated_questions)} questions across 7 exams locally.")

# Save updated questions list for sync
with open('scripts/round23_updated_questions.json', 'w', encoding='utf-8') as f:
    json.dump(updated_questions, f, ensure_ascii=False, indent=2)
print("Saved scripts/round23_updated_questions.json for batch DB sync.")
