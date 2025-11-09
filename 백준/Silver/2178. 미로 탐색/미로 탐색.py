import sys
from collections import deque


input = sys.stdin.readline

N, M = map(int, input().split())

graph = [list(map(int, input().strip())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
distance = [[0] * M for _ in range(N)]
distance[0][0] = 1

def bfs(graph, visited, start_x, start_y):
    queue = deque([(start_x, start_y)])
    visited[start_y][start_x] = True
    

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        cur_x, cur_y = queue.popleft()

        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if 0 <= next_x < M and 0 <= next_y < N:
                if not visited[next_y][next_x] and graph[next_y][next_x] == 1:
                    queue.append((next_x, next_y))
                    visited[next_y][next_x] = True
                    distance[next_y][next_x] = distance[cur_y][cur_x] + 1

    return distance[N-1][M-1]


result = bfs(graph, visited, 0, 0)

print(result)
