import sys

input = sys.stdin.readline

K, N = map(int, input().split())
lan_lines = [int(input()) for _ in range(K)]

def cutting_lan_line(lan_lines, lan_length):
    result = 0

    for lan_line in lan_lines:
        result += (lan_line // lan_length)

    return result

# print(cutting_lan_line(lan_lines, 200))

def parametric_binary_search(array, target, start, end):
    result = 0

    while start <= end:

        mid = (start + end) // 2

        cutting_cnt = cutting_lan_line(array, mid)

        if cutting_cnt < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    
    return result

start = 1
end = max(lan_lines)
print(parametric_binary_search(lan_lines, N, start, end))