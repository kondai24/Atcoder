# 4:Cross Sum
# https://atcoder.jp/contests/typical90/tasks/typical90_d

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

line_sum = []
column_sum = []

# 愚直に計算するとO(HW)になる。
# 前処理として、行と列でそれぞれ合計を出しておく。
# (i, j) = line_sum[i] + column[j] - A[i, j]
# 自分自身を2回足しているので、1回分引く。
for i in range(W):
    tempsum = sum(row[i] for row in A)
    column_sum.append(tempsum)
# column_sum = list(map(sum, zip(*A)))と同じ

for row in A:
    tempsum = sum(row)
    line_sum.append(tempsum)
# line_sum = list(map(sum, A))と同じ

for i in range(H):
    # lambda式を使って書いている。
    # 2重for文と同じ。
    print(' '.join(map(lambda j : str(line_sum[i] + column_sum[j] - A[i][j]), range(W))))
