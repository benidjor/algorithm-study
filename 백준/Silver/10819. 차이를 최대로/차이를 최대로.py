import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

visited = [False] * N
current_permutation = []

def calculate_sum(permutation):
    current_sum = 0
    for i in range(len(permutation)-1):
        current_sum += abs(permutation[i] - permutation[i+1])
    return current_sum

def backtrack():
    # 1. 이 함수 내에서 찾은 최댓값을 저장할 지역 변수
    #    (합은 항상 0 이상이므로 0으로 초기화)
    max_num = 0 

    # 2. 재귀 종료 조건: 순열이 완성되면 합을 계산하여 반환
    if len(current_permutation) == N:
        return calculate_sum(current_permutation)

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            current_permutation.append(A[i])

            # 3. 재귀 호출의 결과 recursive_result
            recursive_result = backtrack()

            # 4. 현재까지의 최댓값과 방금 받은 결과 중 더 큰 값을 저장
            max_num = max(max_num, recursive_result)

            current_permutation.pop()
            visited[i] = False

    # 5. 이 재귀 단계에서 찾은 최종 최댓값을 상위 호출로 반환
    return max_num

print(backtrack())