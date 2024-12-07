# A:Atcoder Line
# https://atcoder.jp/contests/abc352/tasks/abc352_a

N, X, Y, Z = map(int, input().split())

small = X if X < Y else Y
big = X if X > Y else Y

if small < Z and Z < big:
    print("Yes")
else:
    print("No")
