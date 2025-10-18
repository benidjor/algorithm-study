import sys
from collections import deque

input = sys.stdin.readline

# 가로 M, 세로 N, 직사각형의 개수 K
M, N, K = map(int, input().split())

graph = [[0 for _ in range(N)] for _ in range(M)]

# 방문 처리용 2차원 배열
visited = [[False for _ in range(N)] for _ in range(M)]

for _ in range(K):
    left_x, left_y, right_x, right_y = map(int, input().split())

    for y in range(left_y, right_y):
        for x in range(left_x, right_x):
            graph[y][x] = 1


# 상, 하, 좌, 우 방향 정의
dy = [-1, 1, 0, 0]  # y좌표 변화량 (세로)
dx = [0, 0, -1, 1]  # x좌표 변화량 (가로)

def bfs(graph, start_y, start_x, visited):
    
    # 시작점을 queue에 넣고 방문 처리
    queue = deque([(start_y, start_x)])
    visited[start_y][start_x] = True

    # 영역 넓이를 계산하기 위한 area_size (시작점을 포함해서 1로 잡는다)
    area_size = 1

    # queue가 빌 때까지 확인
    while queue:
        y, x = queue.popleft()

        # 현재 위치에서 상, 하 좌, 우 방향 확인
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if (0 <= ny < M) and (0 <= nx < N):
                
                # 아직 방문하지 않았고, 그래프에서 갈 수 있는 곳이면 방문 처리 후 queue에 삽입
                # 비어 있는 땅 (0)인지 확인
                # if not visited[ny][nx] and graph[ny][nx] == 1:
                if not visited[ny][nx] and graph[ny][nx] == 0:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                    area_size += 1

    return area_size

cnt = 0
cnt_list = []

for y in range(M):
    for x in range(N):

        # 만약 해당 지점이 0이고 (빈 땅이고, 방문 가능), 아직 방문하지 않았다면
        if graph[y][x] == 0 and not visited[y][x]:
            area = bfs(graph, y, x, visited)
            
            cnt_list.append(area)
            cnt += 1

# for row in visited:
#     print(row)

print(cnt) # 총 영역의 개수 출력

cnt_list.sort() # 넓이 리스트를 오름차순으로 정렬
print(*cnt_list) # 리스트의 원소들을 공백으로 구분하여 출력
