import sys

m = int(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline().rstrip())

for i in str(n)[::-1]:

    print(int(i) * m)

print(m * n)
