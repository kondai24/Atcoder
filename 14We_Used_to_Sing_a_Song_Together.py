# 14:We Used to Sing a Song Together
# https://atcoder.jp/contests/typical90/tasks/typical90_n

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# ソートしたときのA[i]とB[i]の絶対値の総和を求めると良い。
sorted_A = sorted(A)
sorted_B = sorted(B)

distance_sum = 0
for i in range(N) :
    distance_sum += abs(sorted_A[i] - sorted_B[i])

print(distance_sum)