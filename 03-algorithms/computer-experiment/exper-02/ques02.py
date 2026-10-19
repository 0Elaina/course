"""
2.编程实现带有截止期限的作业调度问题
要求先接受作业数量n，然后后面的n行分别为作业编号、效益值、和截止期限
要求给出最终调度的作业编号，及最优效益值（利用实验一中实现的union find方法）
例如：
输入：
5
1 120 3
2 100 3
3  90  2
4  80  2
5  78  2
输出
1，2，3
310
注：1输入的作业效益值可以是无序的
      2(选做步骤：可以随机生成n（n<=2147483647）观察程序运行时间，与插入排序思想的作业调度对比)
"""

n = int(input())
jobs = []

for i in range(n):
    id, p, d = map(int, input().split())
    jobs.append((id, p, d))

jobs.sort(key=lambda x: x[1], reverse=True)

F = list(range(n + 1))

def find(x):
    if F[x] != x:
        F[x] = find(F[x])
    return F[x]

ans, total = [], 0

for id, p, d in jobs:
    t = find(min(d, n))

    if (t > 0):
        ans.append(id)
        total += p
        F[t] = find(t - 1)

print(",".join(map(str, ans)))
print(total)