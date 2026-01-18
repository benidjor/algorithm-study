import sys
from collections import deque

input = sys.stdin.readline

M, N, K = map(int, input().split())

graph = [[1 for _ in range(N)] for _ in range(M)]

for _ in range(K):
    left_x, left_y, right_x, right_y = map(int, input().split())
    
    for i in range(left_y, right_y):
        for j in range(left_x, right_x):
            graph[i][j] = 0

def bfs(graph, start_x, start_y):
    queue = deque([(start_x, start_y)])
    
    graph[start_y][start_x] = 0
    area_size = 1

    while queue:

        cur_x, cur_y = queue.popleft()

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if (0 <= next_x < N) and (0 <= next_y < M):
                if graph[next_y][next_x] == 1:
                    
                    queue.append((next_x, next_y))
                    area_size += 1

                    graph[next_y][next_x] = 0
    
    return area_size

area_list = []

for m in range(M):
    for n in range(N):
        if graph[m][n] != 0:
            
            area_size = bfs(graph, n, m)
            area_list.append(area_size)

area_list.sort()
print(len(area_list))
print(*area_list)
