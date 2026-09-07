"""
一场卷面总分为 100 分的考试，每个学生的得分都是一个0到 100 的整数。
如果得分至少是 60 分，则称为及格。如果得分至少为 85 分，则称为优秀。
请计算及格率和优秀率，用百分数表示，百分号前的部分四舍五入保留整数。

【输入描述】
    输入的第一行包含一个整数 n(1 ≤ n < 104)，表示考试人数。
    接下来 几 行，每行包含一个0至 100 的整数，表示一个学生的得分。

【输出描述】
    输出两行，每行一个百分数，分别表示及格率和优秀率。百分号前的部分四舍五入保留整数。
"""

from decimal import ROUND_HALF_UP, Decimal

while True:
    stu_count = int(input("请输入考试人数(1 ~ 103)"))
    if stu_count < 1 or stu_count >= 104:
        print("考试人数过多, 请重新输入合法数字")
        continue
    great_count = pass_count = 0
    index = 0
    while index < stu_count:
        score = int(input("请输入学生的分数(0 ~ 100)"))
        if score < 0 or score > 100:
            print("输入的分数不合法, 请重试")
            continue
        if score >= 60:
            pass_count += 1
        if score >= 85:
            great_count += 1
        index += 1

    pass_rate = int(pass_count * 100 / stu_count + 0.5)
    great_rate = int(great_count * 100 / stu_count + 0.5)
    print(f"pass_rate={pass_rate}%\n great_rate={great_rate}%")
    break
