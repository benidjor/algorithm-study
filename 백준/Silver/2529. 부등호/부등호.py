import sys

input = sys.stdin.readline

k = int(input())
signs = list(input().split())

current_permutation = []

# 결과를 문자열로 저장
result = []

visited = [False] * 10

def check_sign(a, b, sign):
    if sign == "<":
        return a < b
    if sign == ">":
        return a > b


def backtrack():
    # 종료 조건
    if len(current_permutation) > k:
        # 문자열로 조합을 저장        
        result.append("".join(map(str, current_permutation)))
        # 종료 조건에 도달했으면 재귀 종료
        return
            
    # 재귀 단계
    for i in range(10):
        # 아직 사용하지 않은 숫자인지 확인
        if not visited[i]:
            # 가지치기 1: 첫 번째 숫자를 뽑는 경우, 리스트에 비교할 숫자가 없다 (어떤 숫자든 첫 번째 숫자로 올 수 있다)
            # 가지치기 2: 넣으려는 숫자가 직전에 넣은 숫자와 부등호 관계 만족하는가
            if len(current_permutation) == 0 or check_sign(current_permutation[-1], i, signs[len(current_permutation) - 1]):

                visited[i] = True
                current_permutation.append(i)

                # 다음 숫자 뽑기 위해 재귀 호출
                backtrack()

                # 재귀 끝나고 돌아오면, 방금 넣었던 숫자 원상복구 (다음 순열 시도 위해서)
                current_permutation.pop()
                visited[i] = False
    
    
backtrack()       
print(result[-1]) 
print(result[0])  