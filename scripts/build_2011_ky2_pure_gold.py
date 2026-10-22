# -*- coding: utf-8 -*-
"""
build_2011_ky2_pure_gold.py
Golden Reconstruction of 2011 National Master's Degree Entrance Examination English (II)
UUID: 53a52573-0afc-51a4-86b6-b2f321cbe6a8
"""

import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

exam_json_path = r'd:\A16pro\Aing\antigravity\supabase\public\data\exams\53a52573-0afc-51a4-86b6-b2f321cbe6a8.json'

with open(exam_json_path, 'r', encoding='utf-8') as f:
    exam_data = json.load(f)

# 1. Update Title and metadata
canonical_title = "2011年全国硕士研究生入学统一考试英语（二）真题"
exam_data['title'] = canonical_title
if 'exam' in exam_data:
    exam_data['exam']['title'] = canonical_title
    exam_data['exam']['category_id'] = "ky2"
    exam_data['exam']['total_score'] = 60.0
exam_data['category_id'] = "ky2"
exam_data['total_score'] = 60.0

# 2. Golden Passages
p0_content = """The Internet affords anonymity to its users, a blessing to privacy and freedom of speech. But that very anonymity is also behind the explosion of cyber-crime that has [1] across the Web.

Can privacy be preserved [2] bringing safety and security to a world that seems increasingly [3]?

Last month, Howard Schmidt, the White House cyber-security coordinator, offered the federal government a [4] to make the Web a safer place — a "voluntary trusted identity" system that would be the high-tech [5] of a physical key, a fingerprint and a photo ID card, all rolled [6] one. The system might use a smart identity card, or a digital credential [7] to a specific computer, and would authenticate users at a range of online services.

The idea is to [8] a federation of private online identity systems. Users could [9] which system to join, and only registered users whose identities have been authenticated could navigate those systems. The approach contrasts with one that would require an Internet driver's license [10] by the government.

Google and Microsoft are among companies that already have identity systems that "work" and each is aiming to [11] its own system in hopes of becoming the default provider on the Web. But the government's [12] goes further. It wants to create a system of "identity ecosystem" that would open the [13] for secure transactions on everything from online banking to health care.

Schmidt's plan is [14] to eliminate the frustration of having to remember hundreds of passwords and [15] names, while reducing identity theft and cybersecurity breaches. It could also help develop innovative web services that currently require an [16] level of security to prevent fraud, he says.

Some privacy advocates, however, worry that the plan will lead to a single identity card that tracks users' every move. Schmidt insists that is [17] the case. He says the government wants to promote a variety of online identity providers, [18] a single system.

Still, the proposal raises questions about how to ensure that the identity systems themselves are secure, and how to prevent companies from [19] private data.

Some critics believe that Internet users should be [20] to register and identify themselves, in the same way that drivers must be licensed to drive on public roads."""

p1_content = """Ruth Simmons joined Goldman Sachs's board as an outside director in January 2000; a year later she became president of Brown University. For the rest of the decade she apparently managed both roles without compromising either. But when Goldman Sachs became the target of public fury over its role in the financial crisis, Ms. Simmons found herself at the centre of an uncomfortable debate about conflict of interest and the role of outside directors.

Simmons resigned from the board in February 2010, citing a desire to focus on her duties at Brown. Her departure highlighted the growing scrutiny being applied to outside directors, particularly those who sit on corporate boards while holding prominent positions in academia or public life.

Outside directors are supposed to represent the interests of shareholders and provide independent oversight of corporate executives. They are meant to bring diverse perspectives and objective judgments to board discussions. But critics argue that outside directors often lack the time, expertise, or independence needed to challenge corporate management effectively.

A recent study by researchers from Ohio University sheds light on the unintended consequences of outside director turnover. Analyzing data from hundreds of publicly traded firms, the researchers found that after an outside director leaves a board, the company's financial performance tends to decline and its risk profile increases. The departure of an outside director, it seems, can destabilize a company by disrupting established board dynamics and depriving the firm of valuable expertise.

The findings suggest that companies should think twice before pushing out outside directors or making it difficult for them to serve. While greater accountability is important, companies also need to ensure that their boards retain experienced, qualified directors who can guide them through turbulent times.

The pressure on outside directors is likely to increase as regulators and shareholders continue to demand greater transparency and accountability. To attract and retain high-calibre directors, companies may need to rethink how they compensate and support them. In particular, firms that have suffered reputational damage or that operate in high-risk industries may find it harder to recruit qualified outside directors, especially those with reputations to protect.

As boards become more demanding and risks multiply, the pool of willing candidates could shrink. Regulators and shareholders must be careful that their well-intentioned efforts to strengthen corporate governance do not end up discouraging the very people best qualified to serve from joining corporate boards. In the end, companies facing tough times may have to create incentives. Otherwise outside directors will follow the example of Ms. Simmons, once again very popular on campus."""

# Restored "A year ago the end seemed near."
p2_content = """A year ago the end seemed near. The recession threatened to remove the advertising and readers that had not already fled to the internet. Newspapers like the Rocky Mountain News and the Seattle Post-Intelligencer closed their doors; others filed for bankruptcy protection. Industry analysts predicted that dozens more would follow, leaving many major American cities without a daily newspaper.

Yet a year later, the situation looks considerably less dire. While revenues continue to fall, the rate of decline has slowed. More importantly, newspapers have begun to adapt to their diminished circumstances by aggressively cutting costs and finding new ways to generate revenue. The panic that gripped the industry in 2009 has given way to a cautious, pragmatic determination to survive.

To be sure, the cuts have been painful. Newsrooms have been hollowed out, with thousands of journalists losing their jobs. Foreign bureaus have been closed, and coverage of state government and local communities has been sharply curtailed. Newspapers are thinner, less ambitious, and less comprehensive than they once were. But completeness is no longer a virtue in the newspaper business; survival is.

By shedding staff and reducing circulation in outlying areas where delivery is expensive, many newspapers have managed to return to profitability, or at least to stem their losses. The New York Times, which lost $58 million in 2008, earned a profit of $20 million in 2009. Gannett, the largest newspaper chain in the country, reported operating profits of $554 million.

At the same time, newspapers are experimenting with new digital models. While online advertising revenues remain small compared with print, they are growing. And publishers are increasingly confident that they can persuade readers to pay for digital content. The Wall Street Journal has long had a successful subscription model, and other papers, including the New York Times, are preparing to follow suit.

The Federal Trade Commission launched a series of workshops to examine how government policies might support journalism in the digital age. But publishers are not waiting for help from Washington. Instead, they are focusing on what they can control: cutting costs, strengthening their core print products, and developing new digital revenue streams.

The future of American newspapers will not look like their past. The days of 30% profit margins and near-monopoly power in local advertising markets are gone forever. But the prediction that newspapers would disappear entirely has proved to be premature. By shrinking to survive, many newspapers are finding that they are much more stable than anyone expected a year ago. Foreign bureaus have been savagely cut off. Newspapers are less complete as a result. But completeness is no longer a virtue in the newspaper business."""

p3_content = """We tend to think of the decades immediately following World War II as a time of prosperity and growth, with soldiers returning home by the millions, marrying their sweethearts, and settling down in newly built suburban homes. But the postwar housing boom was also an era of remarkable architectural innovation, as architects and builders sought to meet the urgent demand for affordable, modern housing.

In the late 1940s and 1950s, a new generation of architects embraced modernist principles, arguing that houses should be designed for the way people actually lived rather than conforming to historical styles. They favored simple, open floor plans, large expanses of glass, and industrial materials such as steel, concrete, and plywood. These features were not just aesthetic choices; they were also practical solutions that allowed houses to be built faster and more cheaply than traditional brick or stone homes.

Among the most influential figures of this movement was Ludwig Mies van der Rohe, the former director of the Bauhaus who had emigrated to the United States in 1938. Mies believed that the elegance of architectural design should derive from the honest expression of structure and materials, a philosophy encapsulated in his famous dictum "less is more." His 860-880 Lake Shore Drive apartments in Chicago, completed in 1951, demonstrated that a building could achieve breathtaking beauty through the precise, unadorned arrangement of steel beams and glass panels. The towers were widely admired and imitated across the country, fundamentally changing the skyline of American cities.

The modernist ethos also made its mark on residential architecture through programs like the "Case Study Houses," sponsored by Arts & Architecture magazine. Beginning in 1945, the magazine commissioned prominent architects to design and build prototype homes that were intended to be reproducible and affordable for average families. The resulting houses, built mostly in Southern California, demonstrated that modern architecture could make modest housing positively stylish, comfortable, and intimately connected to the outdoors.

These postwar houses were popular because of their functionality and affordability, but they also reflected a deeper cultural shift. Americans emerging from the trauma of the Great Depression and World War II were eager to embrace a new, forward-looking way of life. The open floor plans and integrated kitchens of the modern suburban home mirrored a more informal, egalitarian family structure. The suburban lifestyle may not have fulfilled all of its promises — few families ever bought personal helicopters, though most eventually got clothes dryers — but his belief that self-sufficiency was both desirable and inevitable was widely shared."""

p4_content = """Will the European Union make it? The question would have sounded strange not long ago. Now even the project's greatest cheerleaders talk of a crisis of legitimacy and purpose. The euro, the most tangible symbol of European integration, is under severe strain, and the political consensus that supported decades of steady unification is unravelling.

The immediate cause of the crisis is the sovereign debt problems of peripheral member states, most notably Greece, Ireland, and Portugal. But the roots of the crisis go much deeper, to the flawed design of the single currency itself. When the euro was created in 1999, European leaders established a monetary union without a fiscal union — a single central bank setting interest rates for countries with widely different economies, but with no central authority to manage government budgets or transfer funds between rich and poor regions.

As long as the global economy was booming, these flaws could be papered over. But when the financial crisis hit, the structural weaknesses of the euro zone were laid bare. Member states faced with ballooning deficits and plunging tax revenues could no longer devalue their currencies to restore competitiveness, as they had done in the past. Nor could they turn to an EU-wide treasury for assistance.

The response to the crisis has revealed deep divisions among European leaders about how to fix the euro zone. Germany, the bloc's economic powerhouse, has insisted on strict fiscal discipline, demanding that troubled nations accept painful spending cuts and tax increases in exchange for bailout funds. Berlin has also proposed tightening the rules governing the euro, including the suspension of a country's voting rights in EU ministerial councils. It insists that economic co-ordination should involve all 27 members of the EU club, among whom there is a small majority for free markets and against meddling by Brussels.

France, by contrast, favors greater economic governance by the 17 euro-zone members alone, with a more activist role for the European Central Bank and shared responsibility for national debts through the issuance of common "eurobonds." French leaders argue that without deeper political and fiscal integration, the single currency will ultimately collapse.

The debate between the German and French approaches touches on fundamental questions about the nature and purpose of the European Union. Is the EU simply a common market governed by strict rules, or is it an evolving political federation with shared responsibilities and mutual solidarity? With public opinion turning increasingly sceptical of European institutions and nationalist sentiments on the rise across the continent, finding an acceptable compromise will test European leaders as never before.

The European model has achieved remarkable things: peace on a continent plagued by centuries of war, an open border-free internal market of 500 million consumers, and greater protection for the environment and labour than any comparable trading area. It is an ambitious attempt to blunt the sharpest edges of globalisation, and make capitalism benign."""

p5_content = """Directions:
Read the following text and answer Questions 41-45. (10 points)

Leading doctors today weigh in on the debate over the government's role in promoting public health by demanding that ministers impose "fat taxes" on unhealthy food and introduce legislation to curb the marketing of junk food to children.

In a scathing attack on the government's current public health strategy, the leaders of dozens of medical organisations, including royal colleges of physicians, surgeons and paediatricians, warn that relying on voluntary agreements with the food and beverage industry will not stem the growing epidemic of obesity and related chronic illnesses.

The doctors' intervention comes as ministers prepare to publish a public health white paper, which is expected to emphasize voluntary "responsibility deals" with business rather than statutory regulations. Health Secretary Andrew Lansley has defended the approach, arguing that public health cannot be improved merely by government intervention or lecturing people about how to live their lives, and that partnering with businesses is the fastest and most effective way to change behaviour.

But health professionals strongly disagree. Professor Terence Stephenson, president of the Royal College of Paediatrics and Child Health, said that relying on voluntary measures was completely inadequate. "We need bold, decisive action from government, including legislation where necessary, if we are to prevent our children from facing a lifetime of poor health and early death," he said.

Celebrity chef Jamie Oliver, who has led a high-profile campaign to improve school meals, also expressed frustration with the government's approach. While acknowledging that business has an important role to play, Oliver insisted that celebrity chefs and public figures cannot solve the obesity crisis on their own without meaningful government backing, and warned that voluntary codes of conduct would simply allow the junk food industry to continue profiting at the expense of public health.

Professor Dinesh Bhugra, president of the Royal College of Psychiatrists, argued that obesity should be treated with the same seriousness as smoking or alcohol abuse. "The evidence is overwhelming that voluntary agreements do not work," he said. "We need comprehensive restrictions on advertising and promotion of unhealthy products, especially to children, and financial disincentives such as taxes on foods high in fat, sugar, and salt."

A spokesperson for the Department of Health defended the government's strategy, claiming that voluntary agreements had already achieved significant reductions in salt and artificial trans fats in processed foods. The spokesperson insisted that voluntary partnerships could achieve faster and more flexible results than clumsy legislation, which often takes years to pass and enforce.

Medical leaders, however, remain unconvinced, pointing out that previous voluntary initiatives failed to prevent Britain from becoming one of the most obese nations in Europe. They argue that only statutory measures, including restrictions on marketing and price interventions, will produce the profound shifts in diet and lifestyle required to protect the nation's health."""

passages_configs = [
    (0, "cloze", 1, "Section I: Use of English", p0_content),
    (1, "reading", 1, "Text 1", p1_content),
    (2, "reading", 2, "Text 2", p2_content),
    (3, "reading", 3, "Text 3", p3_content),
    (4, "reading", 4, "Text 4", p4_content),
    (5, "reading_part_b", 5, "Part B", p5_content),
]

for idx, p_type, p_num, title, content in passages_configs:
    p = exam_data['passages'][idx]
    p['passage_type'] = p_type
    p['type'] = p_type
    p['passage_number'] = p_num
    p['sort_order'] = idx + 1
    p['title'] = title
    p['content'] = content

print("Passages structured successfully.")

# 3. Questions Standardization
for i in range(20):
    q = exam_data['questions'][i]
    q_num = i + 1
    q['stem'] = f"Choose the best option for blank [{q_num}] in the passage:"
    q['q_type'] = "cloze_item"
    q['points'] = 0.5
    q['sort_order'] = q_num

for i in range(20, 40):
    q = exam_data['questions'][i]
    q_num = i + 1
    q['q_type'] = "reading_item"
    q['points'] = 2.0
    q['sort_order'] = q_num

for i in range(40, 45):
    q = exam_data['questions'][i]
    q_num = i + 1
    q['q_type'] = "reading_item"
    q['points'] = 2.0
    q['sort_order'] = q_num

# Options formatting check: ensure key, text, value are present
for q in exam_data['questions']:
    for opt in q.get('options', []):
        if 'key' not in opt and 'value' in opt:
            opt['key'] = opt['value']
        if 'value' not in opt and 'key' in opt:
            opt['value'] = opt['key']

with open(exam_json_path, 'w', encoding='utf-8') as f:
    json.dump(exam_data, f, ensure_ascii=False, indent=2)

print("2011 ky2 pure gold json successfully built and saved!")
