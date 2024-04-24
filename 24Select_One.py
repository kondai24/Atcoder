# Select+/- One
# https://atcoder.jp/contests/typical90/tasks/typical90_x

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A[i]とB[i]の差の合計を計算する
# 差の合計がKより大きければ、一致しない。
# あとはA[i]-1, A[i]+1の2回操作を行うことで元に戻る。 -> 2で割り切れるか
cnt = 0
for i in range(len(A)) :
    cnt += abs(A[i] - B[i])

check = K - cnt
if ((check % 2) == 0) and (check >= 0):
    print("Yes")
else :
    print("No")
