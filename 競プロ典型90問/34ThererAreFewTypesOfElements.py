# 34:There are few types of elements
# https://atcoder.jp/contests/typical90/tasks/typical90_ah

from collections import defaultdict

N, K = map(int, input().split())
a = list(map(int, input(). split()))
dict = defaultdict(int)
ans = 0
right = 0
dict[a[right]] += 1
# 尺取り法で実装
for left in range(N):
    while right < N and len(dict) <= K:
        right += 1
        if right < N:
            dict[a[right]] += 1
    ans = max(right - left, ans)
    dict[a[left]] -= 1
    if dict[a[left]] <= 0:
        del dict[a[left]]

print(ans)
