import sys
import math

M = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())

num_list = range(M, N+1)
answer_list = []
cnt = 0

for n in num_list:
    if n <= 1:
        continue

    prime_num = True

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            prime_num = False
            break
    
    if prime_num:
        answer_list.append(n)

if len(answer_list) == 0:
    print(-1)
else:
    print(sum(answer_list))
    print(min(answer_list))