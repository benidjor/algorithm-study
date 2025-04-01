n = int(input())

fib = [0 for _ in range(117)]

# fib 설정
fib[1] = 1
fib[2] = 1
fib[3] = 1

# fib 채우기
for i in range(4, 117):
    fib[i] = fib[i-3] + fib[i-1]

print(fib[n])