# 22 Cubic Cake
# https://atcoder.jp/contests/typical90/tasks/typical90_v

from math import gcd
#幅A, 奥行B, 高さC
A, B, C = map(int, input().split())

# 立方体が何個作れるか？
# ->全ての長さが等しいものが何個できるか？
# ->3辺の長さの最大公約数を求める。
oneside_cube = gcd(A, B, C)
# n個に分解する -> (n-1)回切る
ans = (A // oneside_cube - 1) + (B // oneside_cube - 1) + (C // oneside_cube - 1)
print(ans)
