import sys

input = sys.stdin.readline

N = int(input())
roads_length = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price = prices[0]

total_sum = 0


for i in range(N-1):
  
    if prices[i] < min_price:
        min_price = prices[i]
    
    total_sum += min_price * roads_length[i]

print(total_sum)
