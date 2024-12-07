# Insert
# https://atcoder.jp/contests/abc361/tasks/abc361_a

N, K ,X = map(int, input().split())
A = list(map(int, input().split()))

A.insert(K, X)

B = ' '.join(map(str, A))
print(B)
