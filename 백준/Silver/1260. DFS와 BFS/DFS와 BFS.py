import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

# 정점의 개수 N
# 간선의 개수 M
# 탐색을 시작할 정점의 번호 V
N, M, V = map(int, input().split())

# 각 노드가 방문된 정보를 표현
visited_dfs = set()
visited_bfs = set()

# 딕셔너리로 그래프 구현
graph_dict = defaultdict(list)

for i in range(M):
    node, neighbour = map(int, input().split())
    graph_dict[node].append(neighbour) 
    graph_dict[neighbour].append(node) 

# 그래프에서, 노드의 이웃 리스트 정렬
for key in graph_dict:
    graph_dict[key].sort()

# DFS 함수 정의
def dfs(graph, start_node, visited):
    
    # 방문 확인: 만약 현재 노드가 이미 visited set에 있다면, 이미 방문한 것이므로 함수 종료
    if start_node in visited:
        return

    # 방문 처리: visited set에 현재 노드 추가
    visited.add(start_node)
    print(f"{start_node}", end=" ")

    # 현재 노드와 연결된 모든 이웃 노드를 확인
    for neighbour in graph[start_node]:

        # 아직 방문하지 않은 이웃 노드라면, 이 이웃 노드를 시작점으로 하여 DFS 함수 재귀 호출
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


# BFS 함수 정의
def bfs(graph, start_node, visited):
    queue = deque([start_node])

    # 방문 처리
    visited.add(start_node)

    # queue가 빌 때까지 반복
    while queue:
        # queue에서 하나의 노드를 뽑아 출력
        current_node = queue.popleft()
        print(f"{current_node}", end=" ")
        
        # 해당 노드와 연결된 이웃 노드 중, 아직 방문하지 않은 노드 큐에 삽입
        for neighbour in graph[current_node]:

            # 아직 방문하지 않은 이웃이면 방문 처리 후 queue에 추가
            if neighbour not in visited:
                visited.add(neighbour)  # 방문 처리
                queue.append(neighbour) # queue에 추가
                

dfs(graph_dict, V, visited_dfs)
print()
bfs(graph_dict, V, visited_bfs)

