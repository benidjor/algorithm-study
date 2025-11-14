import sys

input = sys.stdin.readline
N, M = map(int, input().split())

A = [list(input().strip()) for _ in range(N)]
B = [list(input().strip()) for _ in range(N)]


def transform_numbers(arr, start_row, start_col):
    
    for i in range(3):
        for j in range(3):
            
            row = start_row + i
            col = start_col + j

            if arr[row][col] == "0":
                arr[row][col] = "1"
            else:
                arr[row][col] = "0"
        
        
cnt = 0
for i in range(N-2):
    for j in range(M-2):

        # A[i][j] != B[i][j]일 때만 연산을 수행한다
        if A[i][j] != B[i][j]:

            transform_numbers(A, i, j)
            cnt += 1


if A == B:
    print(cnt)
else:
    print(-1)