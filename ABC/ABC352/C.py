# C:Standing On The Shoulders
# https://atcoder.jp/contests/abc352/tasks/abc352_c

N = int(input())

A = []
B = []

max = 0
index = 0
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    if max < (abs(b - a)):
        index = i
        max = abs(b - a)

ans = 0
for i in range(N):
    if i == index:
        ans += B[i]
    else:
        ans += A[i]

print(ans)
