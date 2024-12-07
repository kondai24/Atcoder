# 38:Large LCM
# https://atcoder.jp/contests/typical90/tasks/typical90_al

Max_ans = 10 ** 18

def main():
    A, B = map(int, input().split())
    gcc = calc_gcc(A, B)
    if A * B // gcc > Max_ans:
        print("Large")
    else:
        print(A * B // gcc)


def calc_gcc(n, m):
    while (n % m) != 0:
        tmp_m = m
        m = n % m
        n = tmp_m
    
    return(m)

if __name__ == "__main__":
    main()

