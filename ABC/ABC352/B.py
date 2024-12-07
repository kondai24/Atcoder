# B:Typing
# https://atcoder.jp/contests/abc352/tasks/abc352_b

S = input()
T = input()

index = 0

for i in range(len(T)):
    if S[index] == T[i]:
        print((i + 1), end = " ")
        index += 1
