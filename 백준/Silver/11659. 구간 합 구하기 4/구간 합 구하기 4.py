import sys

input = sys.stdin.readline

N, M = map(int, input().split())

num_list = list(map(int, input().split()))

def prefix_sum(num_list, N):
    prefix_sum_list = [0] * (N+1)
    for i in range(1, N+1):
        prefix_sum_list[i] = prefix_sum_list[i-1] + num_list[i-1]
    
    return prefix_sum_list

prefix_sum_list = prefix_sum(num_list, N)

for _ in range(M):
    i, j = map(int, input().split())
    print(prefix_sum_list[j] - prefix_sum_list[i-1])

