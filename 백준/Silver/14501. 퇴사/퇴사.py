import sys
input = sys.stdin.readline

N = int(input())

D = [0] * (N+1)
T = [0] * (N+1)
P = [0] * (N+1)

for i in range(N):
    t, p = map(int, input().split())
    T[i] = t
    P[i] = p

# print(T)
# print(P)

for i in range(N-1, -1, -1):
    # i번째 상담을 퇴사일 까지 끝낼 수 있을 때
    if T[i] <= (N-i):
        
        # D[i+1] = i번째 날의 일을 스킵한 경우
        # D[i+T[i]] = i번째 날에 일하고, 그 다음 일할 때 받을 수 있는 최대 금액
        # P[i] = i번째 날에 일하면 받는 금액
        # i번째 날에 일했을 경우와 일하지 않은 경우를 비교해서 큰 값을 가져온다
        D[i] = max(D[i+1], D[i+T[i]] + P[i])
    #i 번째 상담을 퇴사일 까지 끝낼 수 없을 때
    else:
        D[i] = D[i+1]

print(max(D))