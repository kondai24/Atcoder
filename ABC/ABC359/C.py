# Tile Distance2
# https://atcoder.jp/contests/abc359/tasks/abc359_c

Sx, Sy = map(int, input().split())
Tx, Ty = map(int, input().split())


if Sx < Tx:
    Sx = Sx + 1 if (Sx + Sy) % 2 == 0 else Sx
else:
    Sx = Sx - 1 if (Sx + Sy) % 2 == 1 else Sx 
    
diff_x = abs(Sx - Tx)
diff_y = abs(Sy - Ty)

ans = 0
if diff_x <= diff_y:
    ans += diff_x
    diff_y -= diff_x
    ans += diff_y
else:
    ans += diff_y
    diff_x -= diff_y
    ans += (diff_x + 1) // 2


print(ans)
