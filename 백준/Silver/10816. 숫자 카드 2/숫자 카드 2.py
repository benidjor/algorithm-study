import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
number_cards = list(map(int, input().split()))

M = int(input())
card_needed = list(map(int, input().split()))

number_cards_count = Counter(number_cards)

key_list = list(number_cards_count.keys())
key_list.sort()
# print(key_list)

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        
        # 찾은 경우, 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        
        # 중간점의 값보다 target이 작은 경우, 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        
        # 중간점의 값보다 target이 큰 경우, 오른쪽 확인
        else:
            start = mid + 1
    
    return None

answer = []

for i in range(M):
    target = card_needed[i]
    
   
    result = binary_search(key_list, target, 0, len(key_list)-1)
    if result == None:
        answer.append(0)
    else:
        answer.append(number_cards_count[target])

print(*answer)