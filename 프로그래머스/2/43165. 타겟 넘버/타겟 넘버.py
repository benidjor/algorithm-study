from collections import deque

def solution(numbers, target):
    visited = [False] * len(numbers)
    queue = deque([0])
    
    def bfs(numbers, queue, target):
        
        for num in numbers:
            cur_level_size = len(queue)
            
            for _ in range(cur_level_size):    
                cur_num_in_queue = queue.popleft()
                
                queue.append(cur_num_in_queue - num)
                queue.append(cur_num_in_queue + num)
        return queue.count(target)
    
    return bfs(numbers, queue, target)