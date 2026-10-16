import json
import glob
import sys

sys.stdout.reconfigure(encoding='utf-8')

q5_2018 = """5. [A] Until直到... 为止 [B] Unless除非 [C] Although虽然；但是 [D] When在.... 情况下
[考点提炼]句内语义逻辑。
[解题思路]本题考查从句“人们寄予信任”与主句“大脑释放oxytocin”的逻辑关系。上文已知“人们信任他人是因为这让他们感觉很好（feels good）”，所以应先确认oxytocin是好是坏，同位语 a hormone that... pleasurable feelings 信息不足，结合第6题的四个选项大方向可知 oxytocin 与“愉悦感”是正向关系，所以空格句逻辑应该是：付出信任时，就会产生这种快乐荷尔蒙，[D] When 表示“当（某种条件出现）时会（产生某种状况）”，符合语义逻辑。
[错项排除][A] Until 引出主句事件终止的时间，如：I waited until it got dark.（意即：天黑后我就没等了。），但“人们寄予信任后，大脑就不再释放快乐荷尔蒙”恰好与上文相悖。[B] Unless 在意义上相当于 if... not，如：I can't leave her unless I know she's all right.（意即：如果我知道她不顺利，我不会离开她。），但“如果人们不付出信任，大脑就会释放快乐荷尔蒙”也与文意相悖；[C] Although 表让步转折，而空格前后为顺承条件关系，故排除。"""

exams_dir = 'public/data/exams'
for f in glob.glob(f'{exams_dir}/*.json'):
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    exam = d.get('exam', {})
    if exam.get('category_id') == 'ky1' and exam.get('year') == 2018:
        for q in d.get('questions', []):
            if q.get('sort_order') == 5:
                q['explanation'] = q5_2018.strip()
                with open(f, 'w', encoding='utf-8') as fp:
                    json.dump(d, fp, ensure_ascii=False, indent=2)
                print("2018 Q5 updated to authentic explanation!")
                break
