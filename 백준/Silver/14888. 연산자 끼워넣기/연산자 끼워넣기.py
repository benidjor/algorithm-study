import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
operator_counts = list(map(int, input().split()))

min_result = 10**9
max_result = -10**9

def backtrack(idx, current_result):
    global min_result, max_result

    if idx == N:
        min_result = min(min_result, current_result)
        max_result = max(max_result, current_result)
        return

    if operator_counts[0] > 0:
        operator_counts[0] -= 1
        backtrack(idx + 1, current_result + numbers[idx])
        operator_counts[0] += 1

    if operator_counts[1] > 0:
        operator_counts[1] -= 1
        backtrack(idx + 1, current_result - numbers[idx])
        operator_counts[1] += 1

    if operator_counts[2] > 0:
        operator_counts[2] -= 1
        backtrack(idx + 1, current_result * numbers[idx])
        operator_counts[2] += 1

    if operator_counts[3] > 0:
        # 0으로 나누는 경우 방지
        if numbers[idx] == 0:
            return
        operator_counts[3] -= 1
        if current_result < 0:
            backtrack(idx + 1, -(-current_result // numbers[idx]))
        else:
            backtrack(idx + 1, current_result // numbers[idx])
        operator_counts[3] += 1

backtrack(1, numbers[0])

print(max_result)
print(min_result)
