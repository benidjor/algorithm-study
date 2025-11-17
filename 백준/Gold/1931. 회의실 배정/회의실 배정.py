import sys

input = sys.stdin.readline
N = int(input())

meeting = [tuple(map(int, input().split())) for _ in range(N)]
meeting.sort(key=lambda x: (x[1], x[0]))

cnt = 0
max_end = 0

for start, end in meeting:
    
    if start >= max_end:
        
        cnt += 1
        max_end = end

print(cnt)