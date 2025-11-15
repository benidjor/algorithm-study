import sys

input = sys.stdin.readline

N = int(input())
height_memories = list(map(int, input().split()))

queue = [0] * N

for person, memory in enumerate(height_memories):
    # 왼쪽에 확보해야 할 빈칸의 수
    # 앞으로 들어올 사람들은 현재 person보다 모두 키가 크기 때문
    cnt = memory

    # queue에서 0이 나올 때 마다, cnt를 줄인다
    # cnt가 0이 되는 인덱스가 바로 자기보다 큰 사람이 왼쪽에 몇 명 있었는지 기억하는 자리이다
    for i in range(N):
        # 현재 자리가 빈칸 (0)인지 확인
        if not queue[i]:
            # 확보해야 하는 빈 칸의 수가 0인지 확인
            if cnt == 0:
                queue[i] = person+1
                break
            # 빈 칸을 발견했기 때문에, 필요한 빈 칸의 수를 줄인다
            cnt -= 1

print(*queue)

    