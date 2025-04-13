import sys

# 1
# 2 3 4 5 6 7  (6개)
# 8 (12개)
# 20 (18개)
# 38 (24개)
# 62

N = int(sys.stdin.readline().strip())

level = 1 
max = 1   

while max < N:
    max += 6 * level
    level += 1

print(level)