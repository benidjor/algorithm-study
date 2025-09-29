import sys

# N개의 정수 A[1], A[2], …, A[N] 입력 받는다
n = sys.stdin.readline().strip()
list_a = sys.stdin.readline().split()

# M개의 정수 B[1], B[2], …, B[M] 입력 받는다
m = sys.stdin.readline().strip()
list_b = sys.stdin.readline().split()

# 이진 탐색을 수행하기 위해 A를 정렬한다
list_a.sort()

# 이진 탐색 소스코드 구현 (반복문)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우, 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우, 오른쪽 확인
        else:
            start = mid + 1
    
    return None


# B의 각 원소가 A에 존재하는지 확인한다
for i in range(int(m)):
    result = binary_search(list_a, list_b[i], 0, int(n) - 1)
    if result == None:
        print("0")
    else:
        print("1")