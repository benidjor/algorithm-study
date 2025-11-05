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

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# for g in graph:
#     print(g)

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# for g in graph:
#     print(g)

# row_sums = [sum([value for value in row if value != float("inf")]) for row in graph]

result = [row[1:] for row in graph[1:]]
row_sums = [sum(row) for row in result]

# print(row_sums)
print(row_sums.index(min(row_sums))+1)