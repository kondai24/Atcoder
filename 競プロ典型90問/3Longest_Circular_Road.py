# 3:Longest Circular Road
# https://atcoder.jp/contests/typical90/tasks/typical90_c

N = int(input())
graph = [[] for _ in range(N)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

# 頂点sからの距離
def dfs(s):
    dist = [-1] * N
    dist[s] = 0

    stack = [s]
    while stack:
        v = stack.pop()
        for nv in graph[v]:
            if(dist[nv] == -1):
                stack.append(nv)
                dist[nv] = dist[v] + 1
    return(dist)

# DFSで一番外側の都市まで移動。
# その都市から、一番遠い都市の距離を出力
dist0 = dfs(0)
mv = max(enumerate(dist0), key=lambda x: x[1])[0]
distmv = dfs(mv)
a = enumerate(dist0)
print(max(distmv) + 1)