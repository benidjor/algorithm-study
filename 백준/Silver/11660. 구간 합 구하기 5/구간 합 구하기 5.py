import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

# 2차원 배열의 누적합 구하는 함수 생성
def prefix_sum_2D(arr, N):

    # 0번 행, 0번 0 전체를 0으로 채우는 더미 패딩을 사용한다
    prefix_sum = [[0 for _ in range(N+1)] for _ in range(N+1)]
    
    # i, j를 1부터 시작하여 누적합 계산
    for i in range(1, N+1):
        for j in range(1, N+1): 
            prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + arr[i-1][j-1]
    
    return prefix_sum

# 2차원 배열의 구간합 구하는 함수 생성
def range_sum(prefix_sum, x1, y1, x2, y2):
    
    range_sum = prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]
    return range_sum

prefix_sum = prefix_sum_2D(arr, N)

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(range_sum(prefix_sum, x1, y1, x2, y2))