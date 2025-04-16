import sys

N, K = map(int, sys.stdin.readline().split())

aliquot_lst = []
for i in range(1, N+1):
    if (N / i != 0) & (N/i == N//i):
        aliquot_lst.append(i)
if K > len(aliquot_lst):
    print(0)
else:
    print(aliquot_lst[K-1])