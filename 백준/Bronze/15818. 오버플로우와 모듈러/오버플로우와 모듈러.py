N, M = map(int, input().split())
numlist = list(map(int, input().split()))

res = numlist[0] % M
for i in numlist[1:]:
    res *= i
    res %= M
print(res)