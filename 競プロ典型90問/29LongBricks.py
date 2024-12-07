# 29:Long Bricks
# https://atcoder.jp/contests/typical90/tasks/typical90_ac

W, N = map(int, input().split())

Li = [0] * N
Ri = [0] * N
order = []
dict = {}
for i in range(N) :
    L, R = map(int, input().split())
    Li[i] = L
    Ri[i] = R
    order.append(L)
    order.append(R)

order.sort()
index = 0
for i in range(2 * N) :
    if order[i] not in dict :
        dict[order[i]] = index
        index += 1

h = [0] * index
for i in range(N) :
    l = dict[Li[i]]
    r = dict[Ri[i]]
    current_h = h[l : r + 1]
    max_h = max(current_h) + 1
    print(max_h)
    h[l : r + 1] = [max_h] * (r + 1 - l)
