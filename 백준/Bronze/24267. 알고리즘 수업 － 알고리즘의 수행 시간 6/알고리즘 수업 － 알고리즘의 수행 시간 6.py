import sys


input = sys.stdin.readline

N = int(input())

cnt = N*(N-1)*(N-2) // 6

print(cnt)
print(3)
