# 27:Sign Up Requests
# https://atcoder.jp/contests/typical90/tasks/typical90_aa

# setはhashの役割なので、キーを入力すると存在するかをすぐに返すことができる。
N = int(input())
S = [input() for _ in range(N)]
registered = set()
for i in range(N) :
    if S[i] not in registered :
        registered.add(S[i])
        print(i + 1)
    