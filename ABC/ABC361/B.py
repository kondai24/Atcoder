# Intesection of Cuboids
#https://atcoder.jp/contests/abc361/tasks/abc361_b
cube1 = list(map(int, input().split()))
cube2 = list(map(int, input().split()))

max_X = max(cube1[0], cube2[0])
min_X = min(cube1[3], cube2[3])
max_Y = max(cube1[1], cube2[1])
min_Y = min(cube1[4], cube2[4])
max_z = max(cube1[2], cube2[2])
min_z = min(cube1[5], cube2[5])


if max_X < min_X and max_Y < min_Y and max_z < min_z:
    print("Yes")
else:
    print("No")

