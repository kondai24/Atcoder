# Make Them Narrow
# https://atcoder.jp/contests/abc361/tasks/abc361_c
from collections import deque
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
B_len = len(A) - K
ans = float("inf")
for i in range(K + 1):
    ans = min(ans, A[i+B_len-1] - A[i])


print(ans)