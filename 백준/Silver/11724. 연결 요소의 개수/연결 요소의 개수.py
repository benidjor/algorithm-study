import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)



def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        cur_x = queue.popleft()

        for i in graph[cur_x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

cnt = 0
for i in range(1, N+1):
    if not visited[i]:
        bfs(graph, i, visited)
        cnt += 1

print(cnt)
