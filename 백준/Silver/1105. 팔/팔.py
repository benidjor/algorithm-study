import sys

input = sys.stdin.readline

L, R = input().split()

cnt = 0

if len(L) != len(R):
    print(cnt)
    
else:
    for num_l, num_r in zip(L, R):
        if num_l != num_r:
            break
        if num_l == "8" and num_r == "8":
            cnt += 1

    print(cnt)