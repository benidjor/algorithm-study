import sys
from collections import deque

input = sys.stdin.readline

N, d, k, c = map(int, input().split())

turning_sushi = [int(input()) for _ in range(N)]
turning_sushi_deque = deque(turning_sushi)

window = deque(turning_sushi[:k], maxlen=k)

sushi_length = len(turning_sushi_deque)

max_sushi = 0

for i in range(k, sushi_length+k):
    if i >= sushi_length:
        i = i % sushi_length
    
    window.append(turning_sushi_deque[i])

    sushi_cnt = len(set(window))

    if max_sushi <= sushi_cnt:

        if not c in window:
            sushi_cnt += 1
            
        max_sushi = sushi_cnt
    
print(max_sushi)