# 12:Red Painting
# https://atcoder.jp/contests/typical90/tasks/typical90_l

H, W = map(int, input().split())
Q = int(input())
q = [list(map(int, input().split())) for _ in range(Q)]

# Union Find木を使う
# 最初すべての要素の親を自分自身にする。
# union(x, y)を使うことで、xとyの親を同じにする。
# （深さが深い方に親を合わせる）
class UnionFind:
    # m行n列
    def __init__(self, n, m):
        self.parent = [[(i, j) for j in range(n)] for i in range(m)]  # 各要素の親を格納する配列
        self.rank = [[0] * n for _ in range(m)]  # 各集合のランク（またはサイズ）を格納する配列

    def find(self, cell):
        y, x = cell
        if self.parent[y][x] != cell:
            self.parent[y][x] = self.find(self.parent[y][x])  # 経路圧縮
        return self.parent[y][x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        if self.rank[root_x[0]][root_x[1]] < self.rank[root_y[0]][root_y[1]]:
            self.parent[root_x[0]][root_x[1]] = root_y
        elif self.rank[root_x[0]][root_x[1]] > self.rank[root_y[0]][root_y[1]]:
            self.parent[root_y[0]][root_y[1]] = root_x
        else:
            self.parent[root_y[0]][root_y[1]] = root_x
            self.rank[root_x[0]][root_x[1]] += 1


uf = UnionFind(W, H)
is_red = [[False] * W for _ in range(H)]

for i in range(Q):
    if q[i][0] == 1:
        r, c = q[i][1:]
        r -= 1
        c -= 1
        is_red[r][c] = True
        #上下左右にマスがあるか確認して、あれば赤に塗る。
        if (r != 0) and (is_red[r-1][c]):   uf.union((r, c), (r-1, c))
        if (c != 0) and (is_red[r][c-1]):   uf.union((r, c), (r, c-1))
        if (r != H - 1) and (is_red[r+1][c]):   uf.union((r, c), (r+1, c))
        if (c != W - 1) and (is_red[r][c+1]):   uf.union((r, c), (r, c+1))

    else:
        ra, ca, rb, cb = q[i][1:]
        ra -= 1
        ca -= 1
        rb -= 1
        cb -= 1
        if(is_red[ra][ca]) and (is_red[rb][cb]) and (uf.find((ra, ca)) == uf.find((rb, cb))):
            print("Yes")
        else:
            print("No")
