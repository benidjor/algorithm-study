import sys
from collections import deque

input = sys.stdin.readline

# 테스트 케이스 갯수 
N = int(input())

# 나이트가 이동할 수 있는 범위 (8 방향)
# 1시, 2시, 4시, 5시, 7시, 8시, 10시, 11시
dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]


def chess_bfs(l, start_x, start_y, end_x, end_y):
    
    # 시작점과 도착점 같다면 0번 이동
    if start_x == end_x and start_y == end_y:
        return 0
    
    # 입력 받은 l을 기반으로 체스판 생성
    # 방문하지 않음: -1
    # 시작점: 0
    # 1 이상: 이동 횟수

    chessboard = [[-1 for _ in range(l)] for _ in range(l)]

    queue = deque([(start_x, start_y)])
    chessboard[start_y][start_x] = 0

    while queue:
        current_x, current_y = queue.popleft()

        # queue에서 꺼낸 위치가 목표 지점이면, 저장된 이동 횟수를 반환
        if current_x == end_x and current_y == end_y:
            return chessboard[current_y][current_x]

        for i in range(8):
            next_x = current_x + dx[i]
            next_y = current_y + dy[i]

            if 0 <= next_x < l and 0 <= next_y < l:
                if chessboard[next_y][next_x] == -1:
                    chessboard[next_y][next_x] = chessboard[current_y][current_x] + 1
                    queue.append((next_x, next_y))
    

for _ in range(N):
    l = int(input())

    # 나이트가 현재 있는 칸
    start_x, start_y = map(int, input().split())

    # 나이트가 이동하려는 칸
    end_x, end_y = map(int, input().split())

    result = chess_bfs(l, start_x, start_y, end_x, end_y)
    print(result)
