N, S= map(int, input().split())
A = list(map(int, input().split()))

def is_possible_sum(A: list[int], S: int) -> bool:
    A_length = len(A)
    left, right = 0, 0
    current_sum = A[right]
    list_sum = sum(A)
    target_num = S % list_sum
    if target_num == 0:
        return True
    while left < len(A):
        if current_sum == target_num:
            return True
        elif current_sum > target_num:
            current_sum -= A[left]
            left += 1
        else:
            right += 1
            current_sum += A[right % A_length]

    return False

if is_possible_sum(A, S):
    print("Yes")
else:
    print("No")
    
    