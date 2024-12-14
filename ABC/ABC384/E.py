import heapq

H, W, X = map(int, input().split())
P, Q = map(int, input().split())
S = [list(map(int, input().split())) for _ in range(H)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
current_lebel = S[P-1][Q-1]
queue = []
is_visited = [[False] * W for _ in range(H)]
is_visited[P-1][Q-1] = True

for i in range(4):
    nx, ny = Q-1 + dx[i], P-1 + dy[i]
    if nx < 0 or nx >= W or ny < 0 or ny >= H:
        continue
    heapq.heappush(queue, (S[ny][nx], (nx, ny)))

while queue:
    x, y = heapq.heappop(queue)[1]
    if is_visited[y][x]:
        continue
    else:
        is_visited[y][x] = True
    if (current_lebel / X) > S[y][x]:
        current_lebel += S[y][x]
    else:
        break

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= W or ny < 0 or ny >= H:
            continue
        if  is_visited[ny][nx]:
            continue
        heapq.heappush(queue, (S[ny][nx], (nx, ny)))
        
print(current_lebel)