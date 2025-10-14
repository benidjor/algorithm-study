import sys
input = sys.stdin.readline

# 옮길 원판의 개수 입력
N = int(input())

moves = []

def hanoi_tower(N, start, via, end):

    # 재귀 종료 조건: 옮길 원판 1개
    # 마지막 남은 원판을 시작 기둥에서 목적지로 바로 옮긴다
    if N == 1:
        moves.append(f"{start} {end}")
        return

    # 1단계: N-1개의 원판을 경유지로 옮긴다
    hanoi_tower(N-1, start=start, via=end, end=via)

    # 2단계: 가장 큰 원판 (N)을 시작 기둥에서 목적지로 옮긴다
    moves.append(f"{start} {end}")

    # 3단계: N-1개의 원판을 경유지에서 목적지로 옮긴다 (이 때, start가 경유지가 된다)
    hanoi_tower(N-1, start=via, via=start, end=end)

# 하노이의 탑 움직이는 전체 횟수 출력
total_moves = 2**N - 1
print(total_moves)

if N > 20:
    pass
else:
    hanoi_tower(N, start=1, via=2, end=3)
    
    for move in moves:
        print(move)
