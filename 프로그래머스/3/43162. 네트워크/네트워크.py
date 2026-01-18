from collections import deque

def solution(n, computers):
    
    visited = [False] * n
    
    def bfs(graph, start, visited):
        queue = deque([start])
        visited[start] = True
        
        while queue:
            cur = queue.popleft()
            
            for neighbour in range(n):
                if graph[cur][neighbour] == 1:
                    if not visited[neighbour]:
                        queue.append(neighbour)
                        visited[neighbour] = True
    
    answer = 0
    for i in range(n):
        if not visited[i]:
            bfs(computers, i, visited)
            answer += 1
    
    
    return answer