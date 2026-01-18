from itertools import permutations

# def solution(numbers):
#     permutation_list = []
#     for i in permutations(numbers):
#         a = list(i)
#         permutation_list.append(int("".join(map(str, a))))
    
#     return str(max(permutation_list))
#     # return 

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    
    return str(int("".join(numbers)))