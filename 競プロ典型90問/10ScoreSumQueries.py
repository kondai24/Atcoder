# 10:Score Sum Queries
# https://atcoder.jp/contests/typical90/tasks/typical90_j

N = int(input())
sum_class1 = [0] * N
sum_class2 = [0] * N
# 前処理を行う
# sum_class1[i]:クラス1に属するi番目までの生徒のテスト合計点
# sum_class2[i]:クラス2に属するi番目までの生徒のテストの合計点
for i in range(N):
    c, p = map(int, input().split())
    if i == 0:
        if c == 1:
            sum_class1[i] = p
        else:
            sum_class2[i] = p
    else:
        if c == 1:
            sum_class1[i] += sum_class1[i-1] + p
            sum_class2[i] += sum_class2[i-1]
        else:
            sum_class1[i] += sum_class1[i-1]
            sum_class2[i] += sum_class2[i-1] + p
sum_class1.insert(0, 0)
sum_class2.insert(0, 0)

Q = int(input())

# 学籍番号Li～Riの1組の合計 = (sum_class1[Ri] - sum_class1[Li-1])
# 2組の場合も同様
# Li = 0のときsum_class1[-1]は都合悪いのでsum_classの0番目に0を挿入する
for _ in range(Q):
    L, R = map(int, input().split())
    A = sum_class1[R] - sum_class1[L-1]
    B = sum_class2[R] - sum_class2[L-1]
    print(A, B)