# D:Permutation Subsequence
# https://atcoder.jp/contests/abc352/tasks/abc352_d
import numpy as np

N, K = map(int, input().split())

P = list(map(int, input().split()))

P = np.array(P)
min_sorted = np.argsort(P)
ans = float("inf")
i = 0
count = 0
ans = float("inf")
while((i < N - K + 1) and (i < N - 1)):
    if min_sorted[i] < min_sorted[i+1]:
        count += 1
    else:
        count = 0
    if count >= K - 1:
        candidate = min_sorted[i+1] - min_sorted[i - K + 2]
        ans = min(ans, candidate)
    i += 1

print(ans)