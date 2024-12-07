# C:Vacation
#https://atcoder.jp/contests/dp/tasks/dp_c

N = int(input())
activity = [list(map(int,input().split())) for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]

dp[0][0] = activity[0][0]
dp[0][1] = activity[0][1]
dp[0][2] = activity[0][2]

for i in range(N - 1):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + activity[i + 1][k])

print(max(dp[N - 1]))
