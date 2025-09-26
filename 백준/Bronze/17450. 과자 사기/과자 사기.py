import sys

res, ans = 0, 0
snacks = ["S", "N", "U"]

for i in range(3):
    price, weight = map(int,sys.stdin.readline().split())
    
    total_price = (price * 10) - 500 if (price * 10) >= 5000 else (price * 10)
    if (weight * 10) / total_price > res:
        res = (weight * 10) / total_price
        ans = i

print(snacks[ans])
