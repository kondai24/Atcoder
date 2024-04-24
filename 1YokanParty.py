# 1:Yokan Party
# https://atcoder.jp/contests/typical90/tasks/typical90_a
N, L = map(int,input().split())
K = int(input())
A = list(map(int, input().split()))

def check(x):
    num = 0
    pre = 0
    for i in range(N):
        if(A[i] - pre >= x):
            num += 1
            pre = A[i]

    if((L - pre) >= x):
        num += 1
    
    if(num >= K + 1):
        return(True)
    else:
        return(False)
    
# 二分探索により、最適解を見つける
# left以下はcheckを満たし、right以上はcheckを満たさない
ans = 0
left = -1
right = L + 1
while((right - left) > 1) :
    mid = (right + left) // 2
    if(check(mid)):
        left = mid
    else:
        right = mid

print(left)