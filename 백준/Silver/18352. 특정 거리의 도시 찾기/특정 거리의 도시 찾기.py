import sys
from collections import deque

input = sys.stdin.readline
N, M, K, X = map(int, input().split())

graph = [[] for _ in range(N+1)]

# 방문한 거리를 visited에 넣는다
visited = [-1] * (N+1)

for _ in range(M):
	idx, node = map(int, input().split())
	graph[idx].append(node)


def bfs(graph, start, visited):
	queue = deque([start])
	visited[start] = 0

	while queue:

		current = queue.popleft()
		
		for i in graph[current]:
					
			if visited[i] == -1:
				queue.append(i)
				visited[i] = visited[current] + 1

	return visited

visited_distance = bfs(graph, X, visited)

if K not in visited_distance:
	print(-1)
else:
	for i in range(1, N+1):
		if visited_distance[i] == K:
			print(i)