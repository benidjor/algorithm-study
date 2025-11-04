import sys

input = sys.stdin.readline

string = input()
q = int(input())

def prefix_sum(arr, length):
    prefix_sum_list = [0] * (length+1)
    for i in range(1, length+1):
        prefix_sum_list[i] = prefix_sum_list[i-1] + arr[i-1]
    
    return prefix_sum_list


for _ in range(q):
    a, l, r = input().split()
    l = int(l)
    r = int(r)
    count_alphabet = [1 if char == a else 0 for char in string]

    prefix_sum_list = prefix_sum(count_alphabet, len(string))
    # print(prefix_sum_list)
    print(prefix_sum_list[r+1] - prefix_sum_list[l])



