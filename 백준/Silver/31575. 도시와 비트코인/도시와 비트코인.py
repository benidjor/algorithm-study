import sys
from collections import deque

input = sys.stdin.readline

# 도시의 가로 크기 N, 세로 크기 M
N, M = map(int, input().split())

# 도시 형태를 나타내는 2차원 배열 생성
graph = [list(map(int, input().split())) for _ in range(M)]

# 방문 체크를 위해 모든 원소가 False인 N * M 크기의 2차원 배열 생성
visited = [[False for _ in range(N)] for _ in range(M)]

y, x = 0, 0

# 상, 하, 좌, 우 방향 정의
# dy = [-1, 1, 0, 0]  # y좌표 변화량 (세로)
# dx = [0, 0, -1, 1]  # x좌표 변화량 (가로)

# 진우는 남쪽 (하), 동쪽 (우)으로만 움직일 수 있다
dy = [1, 0]  # y좌표 변화량 (세로)
dx = [0, 1]  # x좌표 변화량 (가로)


def bfs(start_y, start_x, graph, visited):
    # 시작점을 queue에 넣고 방문 처리
    queue = deque([(start_y, start_x)])
    visited[start_y][start_x] = True

    # queue가 빌 때까지 반복
    while queue:
        y, x = queue.popleft()
        # print(f"방문: y좌표(행) {y}, x좌표(열) {x}")

        # 현재 위치에서 상, 하 좌, 우 방향 확인
        for i in range(2):
            ny = y + dy[i]
            nx = x + dx[i]

            if (0 <= ny < M) and (0 <= nx < N):

                # 아직 방문하지 않았고, 그래프에서 갈 수 있는 곳이라면 방문 처리 후 queue에 삽입
                if not visited[ny][nx] and graph[ny][nx] == 1:
                    visited[ny][nx] = True
                    queue.append((ny, nx))

bfs(y, x, graph, visited)
# print(visited)
if visited[M-1][N-1]:
    print("Yes")
else:
    print("No")




