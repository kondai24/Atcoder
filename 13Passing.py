# 13:Passing
# https://atcoder.jp/contests/typical90/tasks/typical90_m

import heapq

def main():
    # N個の街　M本の橋
    N, M = map(int, input().split())
    graph = {i : {} for i in range(1, N+1)}
    for _ in range(M):
        A, B, C = map(int, input().split())
        graph[A][B] = C
        graph[B][A] = C
    
    # 街1から街kを経由して街Nまで移動するときにかかる時間の最小値
    # = (街1からk) + (街Nからk)
    from_first = dijkstra(graph, 1)
    from_last = dijkstra(graph, N)
    for i in range(1, N+1) :
        shortest_way = from_first[i] + from_last[i]
        print(shortest_way)


# ダイクストラ法の実装(DFSに似ている)
def dijkstra(graph, start):
    # スタート地点から、それぞれの街までの距離を格納する辞書
    distaces = {city : float('infinity') for city in graph}
    distaces[start] = 0

    # ヒープキューを使って、未確定の街を管理する
    # 未確定のノードについて、そのノードへの距離が短いものから順に取り出される。
    priority_queue = [[0, start]]

    while priority_queue :
        current_distace, current_city = heapq.heappop(priority_queue)

        if current_distace > distaces[current_city] :
            continue

        for neighbor, weight in graph[current_city].items() :
            distance = current_distace + weight
            if distance < distaces[neighbor] :
                distaces[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return(distaces)

if __name__ == "__main__" :
    main()

