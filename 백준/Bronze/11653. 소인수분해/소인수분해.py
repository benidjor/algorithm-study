import sys

N = int(sys.stdin.readline().strip())
n = 2

if N == 1:
    pass
else:
    while N != 1:
        if N % n == 0:
            N //= n
            print(n)
        else:
            n += 1
            
