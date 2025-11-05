import sys

input = sys.stdin.readline

N = int(input())
INF = float("inf")

# # 2차원 리스트 (그래프 표현) 만들고, 무한으로 초기화
# graph = [[INF] * (N+1) for _ in range(N+1)]

# # 자기 자신에게서 자기 자신으로 가는 비용 0으로 초기화
# for a in range(1, N+1):
#     for b in range(1, N+1):
#         if a == b:
#             graph[a][b] = 0

graph = [list(map(int, input().split())) for _ in range(N)]

graph_inf = [[INF if value == 0 else value for value in row] for row in graph]
# print(graph_inf)


for k in range(N):
    for a in range(N):
        for b in range(N):
            graph_inf[a][b] = min(graph_inf[a][b], graph_inf[a][k] + graph_inf[k][b])

# print(graph_inf)


result = [[0 if value == INF else 1 for value in row] for row in graph_inf]

for row in result:
    print(*row)
