N, c1, c2 = input().split()

S = list(input())

for i in range(len(S)) :
    if S[i] != c1:
        S[i] = c2

print("".join(S))