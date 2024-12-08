volume = 0
prev_time = 0

N = int(input())

for i in range(N):
    current_time, pour_volume = map(int, input().split())
    volume = volume - (current_time - prev_time)
    if volume < 0:
        volume = 0
    volume += pour_volume
    prev_time = current_time

print(volume)