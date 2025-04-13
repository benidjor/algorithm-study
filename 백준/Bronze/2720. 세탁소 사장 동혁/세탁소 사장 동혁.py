import sys

T = int(sys.stdin.readline().strip())
changes = []
money = [25, 10, 5, 1]

for _ in range(T):
    C = int(sys.stdin.readline().strip())
    
    for m in money:
        change = C // m
        changes.append(change)
        C -= (change * m)

for i in range(0, len(changes), 4):
    print(" ".join(map(str, changes[i:i+4])))