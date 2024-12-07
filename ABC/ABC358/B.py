# Ticket Counter
# https://atcoder.jp/contests/abc358/tasks/abc358_b

N, A = map(int, input().split())
T = list(map(int, input().split()))

current_time = 0

for i in range(N):
    if current_time >= T[i]:
        current_time += A
    else:
        current_time = T[i] + A
    print(current_time)

