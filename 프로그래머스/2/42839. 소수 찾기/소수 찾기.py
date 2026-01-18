from itertools import permutations, combinations
import math

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    return True

def solution(numbers):
    
    num_set = set()
    for i in range(1, len(numbers)+1):
    
        for p in permutations(numbers, i):
            num = int("".join(list(p)))
            num_set.add(num)

        # print(num_set)
    
    cnt = 0
    
    for num_made in num_set:
        if is_prime(num_made):
            cnt += 1
    return cnt