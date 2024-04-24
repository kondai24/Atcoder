# 21:Come Back in One Piece
# https://atcoder.jp/contests/typical90/tasks/typical90_u

import sys
sys.setrecursionlimit(10 ** 6)

# SCCのアルゴリズムを使う。
# 参考:https://hkawabata.github.io/technical-note/note/Algorithm/graph/scc.html
def strongly_connected_components(graph, reversed_graph) :
    def dfs(v) :
        visited[v] = True
        for neighbor in graph[v] :
            if not visited[neighbor] :
                dfs(neighbor)
        stack.append(v)

    def dfs_scc(v) :
        visited[v] = True
        scc[v] = current_scc
        for neighbor in reversed_graph[v] :
            if not visited[neighbor] :
                dfs_scc(neighbor)
    
    stack = []
    n = len(graph)
    visited = {v : False for v in graph}
    for v in graph :
        if not visited[v] :
            dfs(v)
    # DFSにより最後に通る順番にスタックに入れる。
    # ->ラベル番号が最大の物が一番最初にpopされる。
    # DFSでvisitedを一度Trueにしているので、もう一度すべてFalseにする。
    visited = {v : False for v in graph}
    scc = {v : -1 for v in graph}
    current_scc = 0
    while stack :
        v = stack.pop()
        if not visited[v] :
            dfs_scc(v)
            current_scc += 1
    
    return(scc)

# 双方向に行けるグラフの要素がnこの時nC2 = n*(n-1)/2で計算できる
def count_pairs(scc) :
    scc_size = {component : 0 for component in set(scc.values())}
    for component in scc.values() :
        scc_size[component] += 1

    pairs_count = 0
    for size in scc_size.values() :
        pairs_count += size * (size - 1) // 2
    return(pairs_count) 

def main() :
    N, M = map(int,input().split())
    graph = {i : [] for i in range(1, N + 1)}
    reversed_graph = {i : [] for i in range(1, N + 1)}
    for _ in range(M) :
        A, B = map(int, input().split())
        graph[A].append(B)
        reversed_graph[B].append(A)

    scc = strongly_connected_components(graph, reversed_graph)
    pairs_count = count_pairs(scc)
    print(pairs_count)

if __name__ == "__main__" :
    main()
