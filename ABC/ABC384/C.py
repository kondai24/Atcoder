contest_score = list(map(int, input().split()))

S = "ABCDE"
examini_score = {}
S = "ABCDE"
for bit in range(2 ** 5, 0, -1):
    score = 0
    subset = ""
    for i in range(5):
        if bit & (1 << (5-i-1)):
            subset += S[i]
            score += contest_score[i]
    examini_score[subset] = score

sorted_key = sorted(examini_score, key=lambda x: examini_score[x], reverse=True)

for key in sorted_key:
    print(key)
