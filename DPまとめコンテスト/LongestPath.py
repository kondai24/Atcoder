# G:Longest Path
# https://atcoder.jp/contests/dp/tasks/dp_g

# 再帰回数の上限を高くしておかないとテストデータが長い時にエラーになる。
# setrecursionlimitのデフォルトは1000
import sys
sys.setrecursionlimit(10**6)

# メモ化再帰(DFSで実装)
# 一度確定するとその値は変わらない
def memo_DFS(v):
    # 値が確定しているとdp[v]を返す
    if flag[v]:
        return(dp[v])
    # 頂点vが葉（どこの頂点への辺が存在しない）場合
    if(len(graph[v]) == 0):
        flag[v] = True
        dp[v] = 0
        return(0)
    else:
        result = 0
        # dp[v] = (隣の頂点) + 1 の中の最大値
        for neighbor in graph[v]:
            result = max(result, memo_DFS(neighbor) + 1)
        dp[v] = result
        flag[v] = True
        return(result)

N, M = map(int, input().split())
graph = [[] for _ in range(N)]

for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    graph[x].append(y)

# dp[i]:iを始点としたときの最長の長さ
dp = [0] * N
flag = [False] * N

# 全ての頂点に対してDFSを行いdpを更新する。
for i in range(N):
    if not flag[i]:
        memo_DFS(i)

ans = 0
for i in range(N):
    ans = max(ans, dp[i])

print(ans)
