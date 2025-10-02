import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())

# 4개의 카드 중 3개의 카드 앞면에는 O가 1개
# 나머지 1개의 카드 (4-3) 앞먄에는 X가 1개 적혀 있다

# 뒷면에 O나 X를 하나씩 적는다 
# O는 2개, X는 2개 (4-2개)

front_o = M
front_x = N-M

back_o = K
back_x = N-K

# print("front_o:", front_o)
# print("front_x:", front_x)
# print("back_o:", back_o)
# print("back_x:", back_x)

print(min(front_o, back_o) + min(front_x, back_x))