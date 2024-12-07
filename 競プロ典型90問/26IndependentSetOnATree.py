# 26:Independent Set on Tree
# https://atcoder.jp/contests/typical90/tasks/typical90_z

# DFSを実装する際に、訪れたノードに色を付ける。
# 隣のノードとは色が別になるように、隣の色は(1-color)とする。
def find_independentPoint(graph) :
    visited = set()
    vertices_color = {v : -1 for v in range(1, len(graph))}
    result_set = {i : set() for i in range(2)}

    # DFSの実装
    stack = [(1, 0)]
    while stack :
        v, color = stack.pop()
        if v not in visited :
            visited.add(v)
            vertices_color[v] = color
            result_set[color].add(v)
            for neighbor in graph[v] :
                if neighbor not in visited :
                    stack.append([neighbor, 1 - color])
    
    # 要素数の多い方をreturnする
    if len(result_set[0]) >= len(result_set[1]) :
        return(result_set[0])
    else :
        return(result_set[1])

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1) :
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

result = find_independentPoint(graph)

# 表示するのはN/2個でよいので、indexがN/2以上のときはbreak
index = 0
for element in result:
    if index >= N // 2:
        break
    print(element, end = ' ')
    index += 1
