# 2:Encyclopedia of Parentheses
# https://atcoder.jp/contests/typical90/tasks/typical90_b
from itertools import product
def isvalid(S):
    score = 0
    for char in S:
        if(char == '('):
            score += 1
        else:
            score -= 1
        if(score < 0):
            return(False)
        
    return(score == 0)

N = int(input())
# このfor文により、()の並び替えの全パターンを抽出
for S in product(['(', ')'], repeat = N):
    if(isvalid(S)):
        print(*S, sep = '')