import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 2차원 리스트 (그래프 표현) 만들고, 무한으로 초기화
graph = [[float("inf")] * (N+1) for _ in range(N+1)]

# 자기 자신에게서 자기 자신으로 가는 비용은 0으로 초기화
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

# a,b가 친구라면 graph에서 1로 처리
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


# 플로이드 워셜 알고리즘 수행하여, a, k, b 중 최단 거리 구한다
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# inf로 초기화 했던 값을 제거한 배열을 result로 선언
result = [row[1:] for row in graph[1:]]

# 각 행별로 값들을 더하여 유저별 케빈 베이컨 수를 구한다
row_sums = [sum(row) for row in result]

print(row_sums.index(min(row_sums))+1)