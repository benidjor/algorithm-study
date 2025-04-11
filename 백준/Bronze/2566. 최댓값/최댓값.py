import sys

n = 9
array = []
max_num = 0
max_row = 1
max_col = 1

for i in range(9):
    lst = list(map(int, sys.stdin.readline().split()))
    if max(lst) > max_num:
        max_num = max(lst)
        max_row = i + 1
        max_col = lst.index(max_num) + 1
    array.append(lst)

print(max_num)
print(max_row, max_col)