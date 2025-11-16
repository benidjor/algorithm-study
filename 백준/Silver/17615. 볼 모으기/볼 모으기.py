import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
balls = list(input().strip())

ball_count = Counter(balls)

all_r = ball_count["R"]
all_b = ball_count["B"]


left_r = 0
left_b = 0
right_r = 0
right_b = 0


for i in range(N):
    if balls[i] == "R":
        left_r += 1
    else:
        break

for i in range(N):
    if balls[i] == "B":
        left_b += 1
    else:
        break

for i in range(N-1, -1, -1):
    if balls[i] == "R":
        right_r += 1
    else:
        break

for i in range(N-1, -1, -1):
    if balls[i] == "B":
        right_b += 1
    else:
        break


print(min(all_r-left_r, all_r-right_r, all_b-left_b, all_b-right_b))