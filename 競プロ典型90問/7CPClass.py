# 7:CP Classes
# https://atcoder.jp/contests/typical90/tasks/typical90_g

N = int(input())
A = list(map(int, input().split()))
Q = int(input())
B = list(int(input()) for _ in range(Q))

A.sort()
INF = 2 ** 60

# 二分探索によって、不満度が最小のクラスを探す
# for文で実装すると、2重for文になり、O(N^2)になる。
# N <= 300000なので、TLEになる。
def search_min(student_rate):
    left = 0
    right = N - 1
    while((right - left) > 1):
        mid = (right + left) // 2
        if(A[mid] < student_rate):
            left = mid
        else:
            right = mid
    return(left)

for i in range(Q):
    j = search_min(B[i])
    # 二分探索では、B[i]以下で最も大きい値を求めている。
    # |a - b|が最小というわけではない。
    # (j < Nのとき)A[j]とA[j+1]を比較する
    result = float("inf")
    if j < N:
        result = min(result, abs(B[i] - A[j]))
    if j < N - 1:
        result = min(result, abs(B[i] - A[j + 1]))
    print(result)


