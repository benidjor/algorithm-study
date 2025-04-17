import sys
import math

N = int(sys.stdin.readline().strip())

num_list = [int(num) for num in sys.stdin.read().split()]
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
        cnt += 1

print(cnt)
