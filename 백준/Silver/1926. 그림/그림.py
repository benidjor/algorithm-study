import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def bfs(graph, start_row, start_col, visited):
    queue = deque([(start_row, start_col)])
    visited[start_row][start_col] = True
    cnt = 1

    while queue:

        row, col = queue.popleft()
        
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        
        for drow, dcol in directions:
            nrow = row + drow
            ncol = col + dcol

            if 0 <= nrow < n and 0 <= ncol < m:
                if not visited[nrow][ncol] and graph[nrow][ncol] == 1:
                    queue.append((nrow, ncol))
                    visited[nrow][ncol] = True
                    cnt += 1
    return cnt

cnt_list = []
for row in range(n):
    for col in range(m):
        if not visited[row][col] and paper[row][col] == 1:
            result = bfs(paper, row, col, visited)
            cnt_list.append(result)

print(len(cnt_list))
if cnt_list:
    print(max(cnt_list))
else:
    print(0)