# 6:Smallest Subsequence
# https://atcoder.jp/contests/typical90/tasks/typical90_f
#データの前処理を行う
def calc_next(S):
    N = len(S)
    #result[i][j] : 文字列Sのi文字目以降で、
    #文字jが出現する最小の添字（存在しない場合はN）
    result = [[N] * 26 for _ in range(N+1)]
    #文字列の最後から、順番に戻りながら調べる。
    #DPのようなやり方
    for i in range(N-1, -1, -1):
        for j in range(26):
            result[i][j] = result[i + 1][j]
        result[i][ord(S[i]) - ord('a')] = i
    return(result)

N, K = map(int, input().split())
S = input()

result = ''
next = calc_next(S)
#前処理をすることで、計算量が抑えられる。
j = -1
for i in range(K):
    #Aから順番に存在するか確認する。
    for ordc in range(26):
        k = next[j+1][ordc]

        #k番目の文字を取った時に、残りの文字数と
        #指定の文字数が足りているか確認する。
        if(N - k >= K - i):
            result += chr(ord('a') + ordc)
            j = k
            break

print(result)