from collections import deque

H, W, D = map(int, input().split())

S = [input() for _ in range(H)]
dist = [[-1] * W for _ in range(H)]

queue = deque()

for y in range(H):
    for x in range(W):
        if S[y][x] == "H":
            queue.append((y, x))
            dist[y][x] = 0


dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
while queue:
    cy, cx = queue.popleft()
    for i in range(4):
        nx, ny = cx + dx[i], cy + dy[i]
        if nx >= 0 and nx < W and ny >= 0 and ny < H:
            if dist[ny][nx] == -1 and S[ny][nx] == ".":
                dist[ny][nx] = dist[cy][cx] + 1
                queue.append((ny, nx))

ans = 0
for i in range(H):
    for j in range(W):
        if (dist[i][j] >= 0) and (dist[i][j] <= D):
            ans += 1

print(ans)
