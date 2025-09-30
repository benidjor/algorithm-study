import sys
from itertools import combinations, product
from collections import Counter, defaultdict

# 테스트 케이스 수
n = int(sys.stdin.readline())

for _ in range(n):
    # 의상 수 입력
    m = int(sys.stdin.readline())

    # {의상 종류 : [의상 이름]} 형태로 만들기 위해, defaultdict(list) 선언
    clothes_dict = defaultdict(list)

    # 입력 받는 의상 이름, 의상 종류를 딕셔너리에 넣는다
    for _ in range(m):
        clothes, category = sys.stdin.readline().split()
        clothes_dict[category].append(clothes)

    # 해당 의상 종류를 입지 않는 경우까지 포함해서 1을 더해준다
    result = 1
    for value_list in clothes_dict.values():
        length = len(value_list) + 1
        result *= length

    # 의상 종류들을 모두 입지 않는 경우의 수인 1을 제외한다
    print(result - 1)
