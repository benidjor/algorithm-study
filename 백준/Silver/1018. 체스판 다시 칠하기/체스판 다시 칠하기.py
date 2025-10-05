import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 2차원 배열로 입력 받는다
board = [list(input()) for _ in range(N)]

# 기본 최소값 
min_cnt = None

# 8*8 크기의 체스판 설정
for row in range(N-7):
    for col in range(M-7):
        
        # 왼쪽 위가 W, B 시작할 때 각각 카운트
        # miss_w_cnt = 이 블록의 왼쪽 위 칸이 W라고 가정했을 때, 잘못 칠해진 칸의 개수
        # miss_b_cnt = 이 블록의 왼쪽 위 칸이 B라고 가정했을 때, 잘못 칠해진 칸의 개수
        miss_w_cnt = 0
        miss_b_cnt = 0

        for i in range(8):
            for j in range(8):
                
                # 현재 칸 설정
                current = board[row+i][col+j]
                
                # i+j 짝수: 왼쪽 위 색깔과 같아야 한다
                # i+k 홀수: 왼쪽 위 색깔과 반대여야 한다

                if (i+j) % 2 == 0:
                    # i+j가 짝수일 때 현재 칸이 W가 아니라면, miss_w_cnt += 1
                    if current != "W":
                        miss_w_cnt += 1
                    # i+j가 짝수일 때 현재 칸이 B가 아니라면, miss_b_cnt += 1
                    if current != "B":
                        miss_b_cnt += 1
                else:
                    # i+j가 홀수일 때 현재 칸이 W가 아니라면, miss_b_cnt += 1
                    if current != "W":
                        miss_b_cnt += 1
                    # i+j가 홀수일 때 현재 칸이 B가 아니라면, miss_w_cnt += 1
                    if current != "B":
                        miss_w_cnt += 1
        
        # 잘못 칠해진 칸의 개수가 적은 것 선택
        local_min = min(miss_w_cnt, miss_b_cnt)

        # 8*8 블록 중 첫 번째 블록이라면 min_cnt가 None이기 때문에 if 문에 조건 명시
        if min_cnt is None or local_min < min_cnt:
            min_cnt = local_min
        
print(min_cnt)
