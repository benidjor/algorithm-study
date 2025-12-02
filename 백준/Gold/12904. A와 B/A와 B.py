import sys

input = sys.stdin.readline

S = list(input().strip())
T = list(input().strip())

while len(S) != len(T):
    if T[-1] == "A":
        T.pop()
    
    else:
        T.pop()
        T.reverse()

if S == T:
    print(1)
else:
    print(0)
