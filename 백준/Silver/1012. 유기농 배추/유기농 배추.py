import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

def bfs(graph, start_row, start_col, visited):
    queue = deque([(start_row, start_col)])
    visited[start_row][start_col] = True

    # 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:

        row, col = queue.popleft()

        for drow, dcol in directions:
            nrow = row + drow
            ncol = col + dcol
        
            if 0 <= nrow < N and 0 <= ncol < M:
                if not visited[nrow][ncol] and graph[nrow][ncol] == 1:
                    queue.append((nrow, ncol))
                    visited[nrow][ncol] = True


for _ in range(T):
    M, N, K = map(int, input().split())

    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    
    cnt = 0
    for row in range(N):
        for col in range(M):
            if field[row][col] == 1 and not visited[row][col]:
                bfs(field, row, col, visited)
                cnt += 1
    
    print(cnt)

