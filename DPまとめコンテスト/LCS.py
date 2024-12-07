# F:LCS
# https://atcoder.jp/contests/dp/tasks/dp_f

s = input()
t = input()
slen = len(s)
tlen = len(t)

# dp[i][j]:tのi文字目までとsのj文字目までの部分列の一致する最長
dp = [[0] * (slen + 1) for _ in range(tlen + 1)]

for i in range(1, tlen + 1):
    for j in range(1, slen + 1):
        #s[j]とt[i]が一致->s[j-1]とt[i-1]までの一致の部分列+1
        if(s[j-1] == t[i-1]):
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
        dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])

ans = ""

i = tlen
j = slen
ans = ""
while(i > 0) and (j > 0):
    if(dp[i][j] == dp[i-1][j]):
        i -= 1
    elif(dp[i][j] == dp[i][j-1]):
        j -= 1
    else:
        ans = t[i - 1] + ans
        i -= 1
        j -= 1

print(ans)