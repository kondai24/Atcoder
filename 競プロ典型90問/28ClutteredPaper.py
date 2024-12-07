# 28:Clutterd Paper
# https://atcoder.jp/contests/typical90/tasks/typical90_ab

# 2次元いもす法を用いる。
# 参考 : https://note.com/kirimin_chan/n/n7663e3bb8a05
# (重ねる命令がN回) × (2重for文で足し合わせる) = 3重for文
N = int(input())
max_length = 1001
plane = [[0] * max_length for _ in range(max_length)]

for _ in range(N) :
    lx, ly, rx, ry = map(int, input().split())
    plane[ly][lx] += 1
    plane[ly][rx] -= 1
    plane[ry][lx] -= 1
    plane[ry][rx] += 1

# max_length = 1001より2重for文はO(10^6)なので実行できる。
# いもす法で横方向に足し合わせる
for y in range(max_length) :
    for x in range(max_length - 1) :
        plane[y][x+1] += plane[y][x]

# いもす法で縦方向に足し合わせる。
for y in range(max_length - 1) :
    for x in range(max_length) :
        plane[y+1][x] += plane[y][x]

ans = [0] * N
for y in range(max_length) :
    for x in range(max_length) :
        if plane[y][x] != 0 :
            ans[plane[y][x] - 1] += 1

for i in range(N) :
    print(ans[i])
