import sys

A, B = map(int, sys.stdin.readline().split())

inv_A = int(str(A)[::-1])
inv_B = int(str(B)[::-1])

print(max(inv_A, inv_B))