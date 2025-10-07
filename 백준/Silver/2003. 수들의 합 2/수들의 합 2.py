import sys

input = sys.stdin.readline

N, M = map(int, input().split())

numbers = list(map(int, input().split()))

cnt = 0
current_sum = 0
end = 0

# start를 차례대로 증가시키면서 반복
for start in range(N):

    # end를 가능한만큼 이동
    while current_sum < M and end < N:
        current_sum += numbers[end]
        end += 1
    
    # 부분 합이 M일 때 카운팅
    if current_sum == M:
        cnt += 1
    
    # for문이 다음 반복으로 넘어가기 전, 현재 start의 값을 current_sum에서 제거
    current_sum -= numbers[start]

print(cnt)
