from collections import deque

N = int(input())
M = int(input())

# graph 만드는 코드
graph = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in range(N+1):
    graph[i].sort()

# print(graph)

visited = [False] * (N+1)


def dfs(graph, v, visited):
	# 현재 노드를 방문 처리
	visited[v] = True
	# print(v, end=' ')
	# print(visited)
	# 현재 노드와 연결된 다른 노드를 재귀적으로 방문
	for i in graph[v]:
		if not visited[i]:
			dfs(graph, i, visited)

dfs(graph, 1, visited)

count = 0
for i in range(2, N+1):
	if visited[i]:
		count += 1
print(count)
		