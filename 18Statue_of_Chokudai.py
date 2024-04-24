# 18:Status of Chokudai
# https://atcoder.jp/contests/typical90/tasks/typical90_r

import math
T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
E = [int(input()) for _ in range(Q)]

for t in E :
    degree = t / T * 360
    radian = math.radians(degree)   # 度数をラジアンに変える
    # Ei秒後の観覧車の座標を求める。
    wheel_x = 0
    wheel_y = -L / 2 * math.sin(radian)
    wheel_z = L / 2 - L / 2 * math.cos(radian)

    different_horizontal = math.sqrt(X ** 2 + (wheel_y - Y) ** 2)
    different_vertical = wheel_z

    # 角度は、arctanで求める
    # atan2は、tanθ = y / xのとき
    # θ = atan2(y, x)と求めることができる。
    ans = math.degrees(abs(math.atan2(different_vertical, different_horizontal)))
    print(ans)
