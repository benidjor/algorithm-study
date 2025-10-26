import sys

input = sys.stdin.readline

M, N = map(int, input().split())

cookies = list(map(int, input().split()))

# 과자를 잘랐을 때, 몇 조각이 나오는지 계산
def cutting(length, cookies):
    # 총 과자 조각 수
    slices = 0
    # 과자 배열에서 각각의 과자 길이를 가져와서 설정한 길이로 나눈다
    for cookie in cookies:
        # 과자를 특정 길이로 나누었을 때, 몇 조각이 나오는지 더해준다
        slices += (cookie // length)
    
    return slices

def parametic_binary_search(array, target, start, end):
    # 조카들에게 나눠줄 과자가 없다면 0을 출력
    result = 0

    while start <= end:
        mid = (start + end) // 2
        # mid 길이로 과자를 잘랐을 때, 몇 조각이 나오는지 계산
        slices = cutting(mid, array)
        
        # 만약 mid 길이가 너무 커서 target 개수보다 작게 잘렸다
        if slices < target:
            # mid 길이를 줄여야 한다 (왼쪽 탐색) 
            end = mid - 1
        else:
            # mid 길이로 주어도 M명에게 줄 수 있음 (성공)
            # 더 긴 길이도 가능한지 탐색하기 위해 start를 늘리고,
            # result에 현재 가능한 길이(mid)를 저장
            result = mid
            start = mid + 1
    
    return result


start = 1
end = max(cookies)

print(parametic_binary_search(cookies, M, start, end))
