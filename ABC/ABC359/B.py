# Couples
# https://atcoder.jp/contests/abc359/tasks/abc359_b

N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(0, len(A) - 2):
    if A[i] == A[i + 2]:
        ans += 1

print(ans)
