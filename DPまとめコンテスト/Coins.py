# I:Coins
# https://atcoder.jp/contests/dp/tasks/dp_i

N = int(input())
p = list(map(float, input().split()))
# dp[i][j]:i枚のコインを使用した内、j枚表が出る確率
dp = [[0] * (N + 1) for _ in range(N + 1)]
dp[1][0] = 1 - p[0]
dp[1][1] = p[0] 

for i in range(2, N + 1):
    for j in range(0, i + 1):
        if j > 0:
            dp[i][j] = dp[i-1][j] * (1 - p[i-1]) + dp[i-1][j-1] * p[i-1]
        else:
            dp[i][j] = dp[i-1][j] * (1 - p[i-1])

ans = 0
mid = (N + 1) // 2
for probability in dp[N][mid :]:
    ans += probability

print(ans)
