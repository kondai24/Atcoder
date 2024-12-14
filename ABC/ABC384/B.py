def can_entry(div: int, current_rate: int) -> bool:
    if div == 1:
        if current_rate >= 1600 and current_rate <= 2799:
            return True
        else:
            return False
    elif div == 2:
        if current_rate >= 1200 and current_rate <= 2399:
            return True
        else:
            return False

N, R = map(int, input().split())

current_rate = R
for i in range(N):
    D, A = map(int, input().split())
    if can_entry(D, current_rate):
        current_rate += A

print(current_rate)
