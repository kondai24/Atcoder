# B:Frog2
# https://atcoder.jp/contests/dp/tasks/dp_b

N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [float("inf")] * N
dp[0] = 0

for i in range(N):
    for j in range(1, K + 1):
        if (i + j) < N:
            dp[i + j] = min(dp[i + j], dp[i] + abs(h[i + j] - h[i]))

print(dp[N - 1])
