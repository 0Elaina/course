"""
3（选做）多机作业调度问题，输出最终完成时间
先输入两个数分别是m和n，m表示机器的数量，n表示作业的数量，接下来n行是作业编号以及完成作业需要的时间
例如：
输入：
3  7（表示3台机器，7个作业）
1 2（作业1，处理时间2）
2 14
3 4
4 16
5 6
6 5
7 3
输出：
17（最终7个作业，3台机器调度总的处理时间是17）
"""

m, n = map(int, input().split())

jobs = []

for i in range(n):
    id, t = map(int, input().split())
    jobs.append((id, t))

# 按耗时排序
jobs.sort(key=lambda x: x[1], reverse=True)
# 记录机器工作时间
machines = [0] * m

# 依次安排
for id, t in jobs:
    # 找到当前工作时间最少的机器
    k = machines.index(min(machines))
    machines[k] += t

print(max(machines))
