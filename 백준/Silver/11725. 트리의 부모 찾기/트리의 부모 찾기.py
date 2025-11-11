import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
# visited = [False] * (N+1)
parents = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start, parents):
    queue = deque([start])
    # visited[start] = True
    parents[start] = start

    while queue:

        cur = queue.popleft()
        
        for neighbour in graph[cur]:
            if parents[neighbour] == 0:
                parents[neighbour] = cur
                queue.append(neighbour)
                

bfs(graph, 1, parents)
# print(graph)
for i in range(2, N+1):
    print(parents[i])