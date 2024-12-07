N = int(input())
h = list(map(int, input().split()))

dp = [0] * N
dp[0] = 0
dp[1] = abs(h[1] - h[0])

for i in range(2, N):
    option1 = dp[i - 2] + abs(h[i] - h[i - 2])
    option2 = dp[i - 1] + abs(h[i] - h[i - 1])
    dp[i] = min(option1, option2)

print(dp[N - 1])
