import sys

# 1               2              3           4               5
# (2+1)*(2+1)  (3+2)*(3+2)    (5+4)*(5+4) (9+8)* (9+8)    (17+16) * (17+16)

N = int(sys.stdin.readline().strip())
plus_dot = 2**(N-1)
answer = ((plus_dot + 1) + plus_dot) ** 2

print(answer)
