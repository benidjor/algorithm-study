import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
start, end = map(int, input().split())

m = int(input())

graph = [[] for _ in range(n+1)]
distance = [-1] * (n+1)


for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

    
def bfs(graph, start, end, distance):
    queue = deque([start])
    distance[start] = 0

    while queue:

        cur = queue.popleft()
        
        if cur == end:
            return distance[cur]

        for i in graph[cur]:
            if distance[i] == -1:
                queue.append(i)
                distance[i] = distance[cur] + 1

    return -1

result = bfs(graph, start, end, distance)
print(result)