import sys

lst = []
N = 9
while N:
    n = int(sys.stdin.readline().strip())
    lst.append(n)
    N -= 1

print(max(lst))
print(lst.index(max(lst))+1)