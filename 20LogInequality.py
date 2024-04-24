# 20:Log Inequality
# https://atcoder.jp/contests/typical90/tasks/typical90_t

# log2(a) < blog2(c)だと、小さい値になり、比較する際にエラーになることがある。
# そのため式を簡単にしておく（前処理）
# a < c ** b
a, b ,c = map(int, input().split())

if a < (c ** b) :
    print("Yes")
else :
    print("No")
