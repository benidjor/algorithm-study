import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coins = [int(input()) for _ in range(N)]

coin_cnt = 0
for coin in reversed(coins):
    if K >= coin:
        coin_cnt += (K // coin)
        K %= coin

print(coin_cnt)
