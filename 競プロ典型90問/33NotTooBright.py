# 33:Not Too Bright
# https://atcoder.jp/contests/typical90/tasks/typical90_ag

H, W = map(int, input().split())

if H == 1 or W == 1:
    ans = H * W
else:
    ans = ((H + 1) // 2) * ((W + 1) // 2)

print(ans)
