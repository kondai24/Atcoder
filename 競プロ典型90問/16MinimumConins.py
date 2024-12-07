# 16:Minimum Coins
# https://atcoder.jp/contests/typical90/tasks/typical90_p

import math
N = int(input())
A, B, C = map(int, input().split())

# A,B,Cのどれかの枚数を1つに固定したときのBとCについて求める。
# aを1つ定めると、b*B + c*C = N - a*Aになる。
# 拡張ユークリッドの互除法を使うと、上の式が成り立つかがわかる。
# ax + by = cが整数解を持つ <-> cがgcd(a,b)で割り切れる。
ans = float('Infinity')
for a in range(10000) :
    money = N - a * A
    if money < 0 :
        break
    gcd = math.gcd(B, C)    #最大公約数
    if money % gcd == 0 :
        for b in range(10000) :
            money = N - a * A - b * B
            if money < 0 :
                break
            if money % C == 0 :
                c = money // C
                ans = min(ans, int(a + b + c))

print(ans)
