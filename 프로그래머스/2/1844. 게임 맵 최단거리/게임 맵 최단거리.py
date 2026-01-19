from collections import deque

def solution(maps):
    
    def bfs(graph, start_x, start_y):
        
        queue = deque([(start_x, start_y)])
        graph[start_y][start_x] = 1
        
        while queue:
            
            cur_x, cur_y = queue.popleft()
            
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]
            
            for i in range(4):
                next_x = cur_x + dx[i]
                next_y = cur_y + dy[i]
                
                if 0 <= next_x < len(graph[0]) and 0 <= next_y < len(graph):
                    if graph[next_y][next_x] == 1:
                        queue.append((next_x, next_y))
                        
                        graph[next_y][next_x] = graph[cur_y][cur_x] + 1
        
        return graph
    
    result_graph = bfs(maps, 0, 0)
    
    target = result_graph[len(maps)-1][len(maps[0])-1]
    
    if target != 1:
        return target
    else:
        return -1
    
    