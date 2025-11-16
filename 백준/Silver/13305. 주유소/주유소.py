import sys

input = sys.stdin.readline

N = int(input())
roads_length = list(map(int, input().split()))
prices = list(map(int, input().split()))

total_length = sum(roads_length)

prices.pop()


cur_sum = 0
for price, length in list(zip(prices, roads_length)):
    if price == min(prices):
        cur_sum += price * (total_length)
        break
    else:
        cur_sum += price * length

    total_length -= length

print(cur_sum)