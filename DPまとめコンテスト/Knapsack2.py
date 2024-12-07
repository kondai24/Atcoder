# E:Knapsack2
# https://atcoder.jp/contests/dp/tasks/dp_e

N, W = map(int, input().split())
goods = [list(map(int, input().split())) for _ in range(N)]

"""
dp[i][sum_v] = i-1 番目までの品物から価値が 
sum_v となるように選んだときの、重さの総和の最小値
"""

dp = [[float("inf")] * 100100 for _ in range(N + 1)]
dp[0][0] = 0
for i in range(N):
    for j in range(100100):
        if (j - goods[i][1]) < 0:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j])
        else:
            dp[i + 1][j] = min(dp[i + 1][j], dp[i][j], dp[i][j - goods[i][1]] + goods[i][0])
        
ans = 0
for i in range(100100):
    if dp[N][i] <= W:
        ans = i

print(ans)

