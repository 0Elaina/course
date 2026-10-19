"""
1.实现贪心法求普通背包问题的算法，并输出给定问题的最优解向量以最优效益值。
输入：第一个两个数，分别表示n和M，M表示背包容量，n表示n个物品，接下来n行分别是物品的效益值pi和重量wi。
输出：第一行解向量（按原来物品的顺序），第二行效益值
例如：
输入：n 5
1 4
5 2
1 3
输出
（0 1 1）
6
"""

# 物品数量n 背包容量m
n, m = map(int, input().split())

items = []

for i in range(n):
    p, w = map(int, input().split())
    items.append((p, w, i))

# 按照单位重量价值排序
items.sort(key=lambda x: x[0] / x[1], reverse=True)
# 记录结果
ans, total = [0] * n, 0

for p, w, i in items:
    if m == 0:
        break

    # 最小可取值
    take = min(m, w)
    # 记录向量
    ans[i] = take / w
    total += p * ans[i]
    m -= take

print("(" + " ".join(f"{int(x)}" for x in ans) + ")")
print(f"{int(total)}")