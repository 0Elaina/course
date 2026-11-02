profit = [
    [0, 11, 13, 15, 21, 24, 30, 35],
    [0, 12, 16, 21, 23, 25, 24, 34],
    [0, 8, 12, 20, 24, 26, 30, 35],
]
# 总资源
a = 7
# 项目数量
n = len(profit)

# 初始化动态规划表
dp = [[float("-inf")] * (a + 1) for _ in range(n + 1)]
# 记录每个状态下当前项目分配的最佳金额
choice = [[0] * (a + 1) for _ in range(n + 1)]

dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(a + 1):
        for k in range(j + 1):
            # 当前利润为前 i 个项目的利润 + 当前项目的当前利润
            value = dp[i - 1][j - k] + profit[i - 1][k]

            if value > dp[i][j]:
                dp[i][j] = value
                choice[i][j] = k

print(f"最大总利润: {dp[n][a]}")

result = [0] * n
remaining = a

for i in range(n, 0, -1):
    k = choice[i][remaining]
    result[i - 1] = k
    remaining -= k

for i in range(n):
    print(f"项目{chr(65 + i)}: 投资{result[i]}万元")
