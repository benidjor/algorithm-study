import sys

input = sys.stdin.readline

N = int(input())
INF = float("inf")


# 원본 그래프 input으로 입력
graph = [list(map(int, input().split())) for _ in range(N)]

# 0은 아직 직접적으로 연결되었는지 모르는 경로이기 때문에, INF로 변경
graph_inf = [[INF if value == 0 else value for value in row] for row in graph]


# 플로이드 워셜 알고리즘 통해 최단 경로 꼐산
for k in range(N):
    for a in range(N):
        for b in range(N):
            # k를 거치는 경로가 더 짧다면 갱신
            graph_inf[a][b] = min(graph_inf[a][b], graph_inf[a][k] + graph_inf[k][b])

# 최종 거리가 INF라면 경로가 없다는 뜻이고, INF가 아닌 숫자라면 경로가 있다는 의미이다
result = [[0 if value == INF else 1 for value in row] for row in graph_inf]

for row in result:
    print(*row)
