# Count Takahashi
# https://atcoder.jp/contests/abc359/tasks/abc359_a

N = int(input())
S = [input() for _ in range(N)]

ans = 0
for name in S:
    if name == "Takahashi":
        ans += 1

print(ans)
