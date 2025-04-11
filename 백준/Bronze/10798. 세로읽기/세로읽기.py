import sys

lines = sys.stdin.read().splitlines()
array = [list(line) for line in lines]

# print(array)
# array[0][0]
# array[1][0]
# array[2][0]

lst = []
max_cols = max(len(row) for row in array)
# for i, row in enumerate(array):
for i in range(max_cols):
    for j in range(len(array)):
    # for j in range(max_cols):
        try:
            # print(array[j][i])
            lst.extend(array[j][i])
        except:
            continue
# print(max_cols)
print("".join(lst))