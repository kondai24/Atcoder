# J:Sushi
# https://atcoder.jp/contests/dp/tasks/dp_j

N = int(input())
a = list(map(int, input().split()))

# dp[i][j][k]:1個の皿がi枚、2個の皿がj枚,3個の皿がk枚の時の期待値(選ぶ回数)
dp = [[[0.0] * (N + 1) for _ in range(N + 1)] for _ in range(N + 1)]

c1, c2, c3 = a.count(1), a.count(2), a.count(3)

for k in range(N + 1):
    for j in range(N + 1):
        for i in range(N + 1):
            sum = i + j + k
            if sum == 0:
                continue
            exp = N

            if i > 0:
                exp += dp[i-1][j][k]* i
            if j > 0 and i < N:
                exp += dp[i+1][j-1][k] * j
            if k > 0 and j < N:
                exp += dp[i][j+1][k-1] * k
            dp[i][j][k] = (exp / sum)

print(dp[a.count(1)][a.count(2)][a.count(3)])
