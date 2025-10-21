import sys

input = sys.stdin.readline

N = int(input())

triangle = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    for j in range(len(triangle[i])):
        
        # 가장 왼쪽
        if j == 0:
            triangle[i][j] = triangle[i-1][j] + triangle[i][j]
        # 가장 오른쪽
        elif j == len(triangle[i])-1:
            triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
        else:
            triangle[i][j] = max(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]


print(max(triangle[N-1]))