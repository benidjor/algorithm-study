from collections import deque

def difference(word1, word2):
    
    diff_cnt = 0
    
    for w1, w2 in zip(word1, word2):
        if w1 != w2:
            diff_cnt += 1
    
    return diff_cnt == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = []
    
    def bfs(words, begin, visited):
        queue = deque([(begin, 0)])
        visited.append(begin)
        # cnt = 0
        
        while queue:
            cur_word, cur_cnt = queue.popleft()
            
            for word in words:
                if difference(cur_word, word):
                    if word == target:
                        return cur_cnt + 1
                    
                    if word not in visited:
                        cur_cnt += 1
                        queue.append([word, cur_cnt])
                        visited.append(word)
        
        return 0
    
    return bfs(words, begin, visited)