import sys

input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

cnt = 0
while cnt < m:
    cards.sort()
    
    sub_score = cards[0] + cards[1]
    
    cards[0] = sub_score
    cards[1] = sub_score
    
    cnt += 1

print(sum(cards))