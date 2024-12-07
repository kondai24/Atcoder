# K:Stones
# https://atcoder.jp/contests/dp/tasks/dp_k

N, K = map(int, input().split())
a = list(map(int, input().split()))

# dp[i]:残りi個の場合に勝てるならTrue
dp = [False] * (10 ** 5 + 1)

for i in range(K + 1):
    win = False
    for j in range(N):
        if (i - a[j]) >= 0:
            # dp[i-j]がFalseのとき
            if not dp[i - a[j]]:
                win = True
                break
        else:
            break
    dp[i] = win

if dp[K]:
    print("First")
else:
    print("Second")
