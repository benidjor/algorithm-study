import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

bfs_visited = [False] * (N+1)
dfs_visited = [False] * (N+1)

for _ in range(M):
    node, neighbour = map(int, input().split())
    graph[node].append(neighbour)
    graph[neighbour].append(node)

for i in range(1, N+1):
    graph[i].sort()


def dfs(graph, start, visited):

    visited[start] = True

    print(start, end=" ")

    for neighbour in graph[start]:

        if not visited[neighbour]:

            dfs(graph, neighbour, visited)



def bfs(graph, start, visited):

    queue = deque([start])
    visited[start] = True

    while queue:
        current_node = queue.popleft()
        print(current_node, end=" ")

        for neighbour in graph[current_node]:
            
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = True


dfs(graph, V, dfs_visited)
print()
bfs(graph, V, bfs_visited)
                
