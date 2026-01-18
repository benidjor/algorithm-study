def solution(tickets):
    tickets.sort()
    answer = []
    
    visited = [False] * len(tickets)
    
    def dfs(cur_airport, path):
        if len(path) == len(tickets) + 1:
            answer.extend(path)
            return True
        
        for i, ticket in enumerate(tickets):
            departure, arrival = ticket
            
            if cur_airport == departure and not visited[i]:
                visited[i] = True
                path.append(arrival)
                
                if dfs(arrival, path):
                    return True
                
                visited[i] = False
                path.pop()
    
    dfs("ICN", ["ICN"])
    return answer
                



# from collections import deque

# def solution(tickets):
#     tickets.sort()
    
#     for departure, arrival in tickets:
#         if departure == "ICN":
#             first_destination = arrival
#             break
    
#     visited = []
    
#     def bfs(graph, start, visited):
#         queue = deque([(start, first_destination)])
#         visited.append(start)
#         visited.append(first_destination)
        
#         while queue:
#             cur_start, cur_destination = queue.popleft()
            
#             for ticket in tickets:
#                 if (cur_destination == ticket[0]) and ticket[1] not in visited:
#                     queue.append((ticket[0], ticket[1]))            
                    
#                     visited.append(ticket[1])
        
#         return visited
                
#     return bfs(tickets, "ICN", visited)