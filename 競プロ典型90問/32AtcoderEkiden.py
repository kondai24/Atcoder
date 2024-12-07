# 32:Atcoder Ekiden
# https://atcoder.jp/contests/typical90/tasks/typical90_af

from itertools import permutations

N = int(input())    # 人数
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())    # 仲が悪い組数
passPossible = [[True] * N for _ in range(N)]
for _ in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    passPossible[x][y] = False
    passPossible[y][x] = False

minTime = float("inf")
# permutationsは引数の配列を並び替えを全通り出力する
for runner in permutations(range(N)):
    sum_time = 0
    isPossible = True
    for i in range(N):
        sum_time += A[runner[i]][i]
        if i < N - 1 and not passPossible[runner[i]][runner[i+1]]:
            isPossible = False
            break
    if isPossible:
        minTime = min(minTime, sum_time)
    
if minTime == float('inf'):
    print("-1")
else:
    print(minTime)
