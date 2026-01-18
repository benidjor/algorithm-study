def solution(citations):
    citations.sort(reverse=True)
    
    for rank, citation in enumerate(citations):
        real_rank = rank + 1
        if citation >= real_rank:
            continue
        else:
            return rank
    
    return len(citations)