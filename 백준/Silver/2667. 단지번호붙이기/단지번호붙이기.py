import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

visited = [[False for _ in range(N)] for _ in range(N)]
danji_map = [list(map(int, input().strip())) for _ in range(N)]

# 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(graph, start_x, start_y, visited):
    # 시작점을 queue에 넣고 방문 처리
    queue = deque([(start_x, start_y)])
    visited[start_y][start_x] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()
        # 4방향 체크
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]
            
            if 0 <= next_x < N and 0 <= next_y < N:
                # 아직 방문하지 않았고, 그래프에서 갈 수 있는 곳이면 방문 처리 후 queue에 삽입
                if not visited[next_y][next_x] and graph[next_y][next_x] == 1:
                    visited[next_y][next_x] = True
                    queue.append((next_x, next_y))
                    cnt += 1
    return cnt


cnt_list = []
for y in range(N):
    for x in range(N):

        if danji_map[y][x] == 1 and not visited[y][x]:
            result = bfs(danji_map, x, y, visited)
            cnt_list.append(result)

cnt_list.sort()
print(len(cnt_list))
for cnt in cnt_list: print(cnt)