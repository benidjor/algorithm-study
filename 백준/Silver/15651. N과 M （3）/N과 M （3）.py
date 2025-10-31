import sys

input = sys.stdin.readline
N, M = map(int, input().split())

result = []

def backtracking(start):
    
    # 종료 조건: M개의 숫자가 result에 저장
    if len(result) == M:
        print(*result)
        return  # 함수 종료 (이전 단계로 되돌아 간다)
    
    for i in range(1, N+1):
        result.append(i)

        # 재귀: 다음 숫자는 i or i보다 큰 숫자가 result에 들어가야 한다
        backtracking(i)

        # 위에서 추가했던 i를 리스트에서 제거
        result.pop()

backtracking(1)