import sys

input = sys.stdin.readline

fibo = [0, 1]
while fibo[-1] < 1_000_000_000:
    next_fibo = fibo[-1] + fibo[-2]
    fibo.append(next_fibo)
    
T = int(input())

for _ in range(T):
    num = int(input())

    for i in range(1_000_000_000):
        if fibo[i] > num:
            idx = i
            break
    
    fibo_list = fibo[:idx][::-1]
    
    ans = []

    for fibo_num in fibo_list:
        # gap = num - fibo_num
        if num >= fibo_num and fibo_num != 0:
            num -= fibo_num
            # print(fibo_num)

            ans.append(fibo_num)
    
    ans = reversed(ans)

    print(*ans)