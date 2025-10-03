import sys

input = sys.stdin.readline

N = int(input().strip())
numbers_N = list(map(int, input().split()))

M = int(input().strip())
numbers_M = list(map(int, input().split()))

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우, 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작다면 왼쪽 확인
        elif target < array[mid]:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 크다면 오른쪽 확인
        else:
            start = mid + 1
    
    return None

numbers_N.sort()

for num in numbers_M:
    result = binary_search(numbers_N, num, 0, N-1)
    if result is None:
        print(0)
    else:
        print(1)

