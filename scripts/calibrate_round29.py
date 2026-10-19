import json
import os

def load_exam(exam_id):
    path = f"public/data/exams/{exam_id}.json"
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f), path

def save_exam(data, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

print("Starting Round 29 Calibration...")

# ==========================================================
# 1. 2004 ky1 Cloze Q5, Q8, Q12 (47036de0-e57d-5ccb-9bc8-b3f86d4e6457)
# ==========================================================
data_2004, path_2004 = load_exam("47036de0-e57d-5ccb-9bc8-b3f86d4e6457")
for q in data_2004["questions"]:
    so = q.get("sort_order")
    if so == 5:
        q["stem"] = "Choose the best option for blank [5] in the passage:"
        q["explanation"] = (
            "【考点提炼】逻辑关系\n\n"
            "【精准定位】空格处填入的连词连接两个并列谓语动词结构increase和stabilize，它们在语义上构成并列选择关系，即“无论家庭收入是增加还是保持稳定”，只有or可以表示“或者”，符合句意，选［A］。\n\n"
            "【空格设置】本题考查了连词or的用法。or可连接两个或两个以上并列成分，表示选择关系，意为“或者，还是”。例句：Is it green or blue? 它是绿色的还是蓝色的？\n\n"
            "【干扰项设置】but rather不是固定搭配，通常以rather than的形式出现，意为“与其……倒不如……”；but表示转折关系，意为“但是，而是”；or else表达与上文相反的假设，意为“否则，要不然”。例句：Run, or else you'll be late. 快跑，要不然你就会迟到了。"
        )
    elif so == 8:
        q["stem"] = "Choose the best option for blank [8] in the passage:"
        q["explanation"] = (
            "【考点提炼】固定搭配\n\n"
            "【精准定位】空格处填入的形容词与to搭配做表语，说明青少年更容易受到社会结构变化的影响，四个选项中只有subject与to搭配能表达“易受……影响的”，故选［D］。\n\n"
            "【空格设置】本题考查了形容词短语be subject to的固定搭配，意为“易受……影响的，常遭受……的”。例句：Japan is subject to earthquakes. 日本常发生地震。\n\n"
            "【干扰项设置】immune to意为“对……免疫的，不受……影响的”。例句：No one is immune to criticism. 没有人不受批评。resistant to意为“有抵抗力的；对……抵制的”。例句：Mosquitoes become resistant to insecticides. 蚊子对杀虫剂产生了抗药性。sensitive to意为“对……敏感的”。例句：I am sensitive to cold. 我怕冷。"
        )
    elif so == 12:
        q["stem"] = "Choose the best option for blank [12] in the passage:"
        q["explanation"] = (
            "【考点提炼】句内语义 + 固定搭配。正确率：49%\n\n"
            "【精准定位】空格所在句子（④句）的主干结构已经完整：discontent（主语）may lead（谓语）more youths（宾语）into criminal behavior（宾补），填入的介词短语在句中做状语。选项中只有in turn放入后符合逻辑，因为它可以表示一种连锁的因果联系，即“（经济变化导致就业困难，就业困难造成不满情绪，）不满情绪转而又导致更多犯罪”，选［C］。\n\n"
            "【空格设置】本题考查了介词短语in turn的特殊含义及句间逻辑关系。句中的提示线索是resulting“因而发生的，由此产生的”，它在文中指“因就业困难而产生的”。例句：He found that Mary had told Richard's sister, and she in turn had told Richard. 他发现玛丽告诉了理查德的姐姐，然后她又告诉了理查德。\n\n"
            "【干扰项设置】其他项都与介词in构成固定搭配。in case表示假使，如果，万一。例句：Take warm clothes in case the weather is cold. 带上厚衣服以防天气变冷。in short表示简而言之，总而言之。例句：In short, society must be reorganized. 总之，社会必须重组。in essence表示本质上。例句：He is in essence an honest person. 他本质上是个诚实的人。"
        )

save_exam(data_2004, path_2004)
print("Calibrated 2004 ky1 Cloze Q5, Q8, Q12.")

# ==========================================================
# 2. 2005 ky1 Text 3 Q35 (d8ba7d14-5305-538d-b81b-f0f7ef3db461)
# ==========================================================
data_2005, path_2005 = load_exam("d8ba7d14-5305-538d-b81b-f0f7ef3db461")
for q in data_2005["questions"]:
    so = q.get("sort_order")
    if so == 35:
        q["stem"] = "What advice might Cartwright give to those who sometimes have bad dreams?"
        q["explanation"] = (
            "［精准定位］第五段④⑤句明确指出偶尔做噩梦的人（the rest of us 指代“除掉那些长期做噩梦者之外剩下的人”）可安心睡觉或做（噩）梦，因为大脑可以自动消除不良情绪，第二天梦醒后心情都会不错。换言之，Cartwright 建议偶尔做噩梦的人可以照常生活，［A］正确。\n\n"
            "［命题解密］正确项是对该段末两句的概括表达，其中 Lead your life as usual 是对 Sleep — or rather dream — on it 的合理概括。\n\n"
            "［B］将原文所述“寻助人——那些长期受噩梦折磨的人”篡改为“偶尔做噩梦的人”。［C］错将有意识控制的对象由 recurring bad dreams（反复上演的噩梦）转变为 sometimes... bad dreams（偶尔噩梦）。［D］是对第五段②句中 anxiety 的无端捏造，该词主要用以说明人们噩梦不断的原因：白天焦虑感与日俱增，并未用于传达 Cartwright 对偶尔噩梦者的建议；再有 Cartwright 只表达了要有意识地控制梦或任其发展，并未提到避免焦虑这个问题。\n\n"
            "［技巧总结］对比处常设题点，解答时，重在理清比较对象、比较内容，然后对号入座。如本题，第一步重在掌握④句 the rest of us 具体所指，并将其与题干 those who sometimes have bad dreams 相对接；第二步重在寻找针对 the rest of us 所描述的具体信息：③句 should seek help from a therapist“寻求专家帮助”针对的是“长期受噩梦折磨的那些人”；⑤句中祈使句 Sleep — or rather dream — on it “枕着它（指焦虑）入睡或入梦”针对的是“偶尔做噩梦的人”；最后，对号入座，敲定正确答案［A］。"
        )

save_exam(data_2005, path_2005)
print("Calibrated 2005 ky1 Text 3 Q35.")

# ==========================================================
# 3. 2009 ky1 Text 3 Q35 (9369aa41-c91e-548c-bf99-1ad46a07ac25)
# ==========================================================
data_2009, path_2009 = load_exam("9369aa41-c91e-548c-bf99-1ad46a07ac25")
for q in data_2009["questions"]:
    so = q.get("sort_order")
    if so == 35:
        q["stem"] = "According to the last paragraph, development of education ________."
        q["explanation"] = (
            "［精准定位］第五段末句指出：“穷国生产力的束缚解释了其教育落后的原因”，换言之，解放、提高生产力即可推动教育发展，［C］正确。\n\n"
            "［命题解密］［C］既符合末段主要信息，又与全文强调的“经济（生产力）是教育的先决条件”一致。\n\n"
            "［A］源自②句 competitive environment pushed...，而该句文意为“竞争环境是原始人类经济发展的原始动力，经济发展后教育才得以发展”，选项将其“环环相扣、间接促成”的逻辑偷换为“直接促成”逻辑。［B］利用③句碎片信息... education is... but not a sufficient condition... advanced economic performance 拼凑出“教育不依赖于经济表现”，与文意相悖。［D］语意杂糅②句 afford 以及④句 political changes，并且反向曲解了④句句意“只有在更广泛的正规教育的条件下，才能实现政治变革”。\n\n"
            "［技巧总结］解答题干涵盖全文主体论述对象（之一）的末段推理题，捷径为“选择与全文主旨相符的选项”。如本题，题干 development of education 为作者试图论述的两方关系中的一方：教育。虽末段逻辑复杂，涉及“竞争环境、生产力潜能、经济表现、政治体制、政治变革”等名词及其间关系，但“经济决定教育，经济发展促进教育进步”这一主线清晰，生产力与经济挂钩，故可快速锁定选项［C］。"
        )

save_exam(data_2009, path_2009)
print("Calibrated 2009 ky1 Text 3 Q35.")

# ==========================================================
# 4. 2008 ky1 Part B Q42 (d80926ab-1841-5d1f-a999-56773986c46d)
# ==========================================================
data_2008, path_2008 = load_exam("d80926ab-1841-5d1f-a999-56773986c46d")
for q in data_2008["questions"]:
    so = q.get("sort_order")
    if so == 42:
        q["stem"] = "Choose the best paragraph [A]-[G] that fits into gap (42):"
        q["explanation"] = (
            "42. 本题考核的知识点是：词汇复现 ＋ 上下文的衔接。正确率：37%\n\n"
            "【空格推测】上文提出“要灵活运用提纲，随时补充相关要点”，下文提出“初稿要以内容为重，某些错误可留待后续解决”，推测空格内容也应关乎“灵活运用提纲、以思想内容为重”。\n\n"
            "【答案敲定】由选项分析可知，［B］、［D］、［G］为本题备选项。\n"
            "［B］针对正文已经完成后的写作阶段提出建议“如何写首尾两部分”，与空格上下文内容可形成“合理利用提纲、补充文章要点（即写好正文）→写结尾、开头→检查语法、拼写等错误”的顺序，看似合乎逻辑，但选项首句“已经清晰地、充分地展开正文”暗示前文围绕“正文写作”展开，而空格上文“灵活应用提纲”实质针对整个写作过程而言，尤其是针对“写作过程中出现的新想法”而言，并未重点说明“正文”，也未提及任何“写作顺序”相关内容，故排除。\n"
            "［D］中复现关键词 outline，且 just so you do（倒装句，正常语序为 you just do so, so 为省略指代词）看似是对空格上文 work it into the draft 的省略指代，引人误解。但选项中 begin to flesh out... outline 表明写作仍处于“开始充实提纲，提纲还未确定”的阶段，而第二段②句指出“你的提纲应引导你行文”表明“提纲已经确定”，若选项出现在空格 42，显然与第二段空格前内容顺序颠倒，故排除。\n"
            "［G］首句指出“在写初稿的过程中会想到更多新要点”，与空格上文“如果你突然想到一个重要观点就写进初稿”内容一致，语义顺承第二段主旨“要灵活运用提纲、不拘泥于提纲”，选项②句随即列举“许多优秀作家不列提纲、而是边写边摸索写作顺序的做法”进一步论证主旨；选项③句“不要企图第一次就写出完美无误的初稿”又与下文“语法、标点、拼写等问题”衔接自然，因此［G］能承上启下，敲定为答案。"
        )

save_exam(data_2008, path_2008)
print("Calibrated 2008 ky1 Part B Q42.")

# ==========================================================
# 5. 2006 ky1 Part B Q45 (c6e9dbac-6148-532e-90d2-2a8d3682a6ac)
# ==========================================================
data_2006, path_2006 = load_exam("c6e9dbac-6148-532e-90d2-2a8d3682a6ac")
for q in data_2006["questions"]:
    so = q.get("sort_order")
    if so == 45:
        q["stem"] = "Choose the best paragraph [A]-[G] that fits into gap (45):"
        q["explanation"] = (
            "45. 本题考核的知识点是：同义复现 ＋ 上下文的衔接。正确率：45%\n\n"
            "【空格推测】上文指出“‘行为问题’医学化”的社会倾向无益于反思赌博这一社会问题，下文介绍美国赌博业的火爆现状，空格处内容可能继续探讨赌博的社会影响，也可能介绍美国的赌博问题。\n\n"
            "【答案敲定】由选项分析可知，［D］、［E］、［G］为本题备选项。\n"
            "［D］顺承上文“社会对赌瘾的认识发生变化”，指出社会对赌博的看法也发生了相似的变化：从人民深恶痛绝的社会弊病转变为政府大力支持的社会政策，该内容可以解释下文“为何美国赌博业火爆异常”，形成因果逻辑；government 与下文 states 为近义替换，［D］为本题答案。\n"
            "［E］表达作者期望“借威廉姆斯一案警醒国人”，继而表示可能性不大，是对全文的总结；this gambling nation 提示上文涉及“美国赌博盛行”的情形，应出现在第十一段之后，而不是之前，故排除。\n"
            "［G］提及“在线赌博”的特征、危害及政府对其的态度，而第十一段第二句（And since the first Internet gambling site was created in 1995）表明“在线赌博”这一概念在全文首次出现，故选项应出现在第十一段之后，而不是之前，故排除。"
        )

save_exam(data_2006, path_2006)
print("Calibrated 2006 ky1 Part B Q45.")

print("All Round 29 calibrations completed successfully.")
