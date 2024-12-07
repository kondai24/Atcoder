# 8:AtCounter
# https://atcoder.jp/contests/typical90/tasks/typical90_h
MOD = 10 ** 9 + 7
T = 'atcoder'

N = int(input())
S = input()

# DPにより求める
# dp[i][j] : 文字列Sの最初のi文字から
# "atcoder"の最初のj文字まで一致している方法の個数
dp = [[0] * (len(T) + 1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(len(T) + 1):
        # S[i]を選ばない場合
        dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % MOD

        # S[i]を選ぶ場合
        if (j < len(T)) and (S[i] == T[j]):
            dp[i + 1][j + 1] = (dp[i + 1][j + 1] + dp[i][j]) % MOD
    
print(dp[N][len(T)])