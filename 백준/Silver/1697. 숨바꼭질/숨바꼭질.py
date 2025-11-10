import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())

graph = [-1] * 100_001

def bfs(graph, start, end):
    
    # 시작점과 도착점 같다면 0번 이동
    if start == end:
        return 0
    
    queue = deque([start])

    graph[start] = 0

    directions = [2, -1, 1]

    while queue:
        cur_x = queue.popleft()

        if cur_x == end:
            # return graph[cur_x]
            return graph[cur_x]

        for direction in directions:
            if direction == 2:
                next_x = cur_x * 2
            else:
                next_x = cur_x + direction

            if 0 <= next_x < len(graph):

                if graph[next_x] == -1:
                
                    graph[next_x] = graph[cur_x] + 1
                    queue.append(next_x)

result = bfs(graph, N, K)
print(result)
