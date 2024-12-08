import itertools

H, W, D = map(int, input().split())

S = [list(input()) for _ in range(H)]

ans = 0

block_location = []

def calc_number_humidity(a, b, block_location):
    result = 0
    for i in range(len(block_location)):
        if calc_manhattan_distance(a, block_location[i]) <= D or calc_manhattan_distance(b, block_location[i]) <= D:
            result += 1
    return result

def calc_manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

for y in range(H):
    for x in range(W):
        if S[y][x] == ".":
            block_location.append((x, y))

for comb in itertools.combinations(block_location, 2):
    ans = max(ans, calc_number_humidity(comb[0], comb[1], block_location))

print(ans)
    

