# H:Grid1
# https://atcoder.jp/contests/dp/tasks/dp_h

MOD = 10 ** 9 + 7
H, W = map(int, input().split())
a = [input() for _ in range(H)]

# dp[i][j]:(i, j)まで何通りか
dp = [[0] * (W + 1) for _ in range(H + 1)]

dp[1][1] = 1
for i in range(1, H + 1):
    for j in range(1, W + 1):
        if a[i-1][j-1] == '.':
            dp[i][j] = (dp[i][j] + dp[i-1][j] + dp[i][j-1]) % MOD
    
print(dp[H][W])