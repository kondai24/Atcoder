# D:Knapsack1
# https://atcoder.jp/contests/dp/tasks/dp_d

N, W = map(int, input().split())
goods = [list(map(int, input().split())) for _ in range(N)]

"""
dp[i][sum_w] : i-1番目までの品物から重さがWを超えないように
選んだ時の価値の総和の最大値
"""
dp = [[0] * (W + 1) for _ in range(N + 1)]

for i in range(N):
    for j in range(W + 1):
        if (j - goods[i][0]) < 0:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        else:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j], dp[i][j - goods[i][0]] + goods[i][1])

print(dp[N][W])
