def solution(n, times):
    
    def test(times, time_length):
        
        estimated_man = 0
        for time in times:
            estimated_man += time_length // time
        
        return estimated_man
        
    def binary_search(target, start, end):
        
        while start <= end:
            mid = (start + end) // 2
            estimated_people = test(times, mid)
            
            if estimated_people >= target:
                result = mid
                end = mid - 1
            else:
                start = mid + 1
    
        return result
    
    return binary_search(n, 1, max(times)*n)
        
        