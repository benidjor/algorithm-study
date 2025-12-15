import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())


def bfs(start, visited):

    queue = deque([start])
    visited[start] = 0

    while queue:

        cur = queue.popleft()
        
        for step in (U, -D):
            next_floor = cur + step
            
            if 1 <= next_floor <= F:
                if visited[next_floor] == -1:
                    queue.append(next_floor)
                    visited[next_floor] = visited[cur] + 1
    
    if visited[G] == -1:
        print("use the stairs")
    else:
        print(visited[G])
                

visited = [-1] * (F+1)


bfs(S, visited)
# print(visited[G])
