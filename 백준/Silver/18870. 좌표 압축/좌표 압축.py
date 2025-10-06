import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
coordinate = list(map(int, input().split()))

# 중복을 먼저 제거(set)한 후, 그 결과를 정렬(sorted)
coordinate_ordered = deque(sorted(set(coordinate), reverse=True))

# print(coordinate_ordered)

compression_dict = {}
while coordinate_ordered:
    num = coordinate_ordered.popleft()
    compression_dict[num] = len(coordinate_ordered)
# print(compression_dict)




# # 좌표 압축한 값을 딕셔너리로 생성
# compression_dict = {}
# for i, num in enumerate(coordinate_ordered):
#     # compression_dict[num] = len(coordinate_ordered[i+1:])
#     c(num)
#     compression_dict[num] = len(coordinate_ordered[i+1:])


# # 입력 받은 원본 리스트와 좌표 압축 딕셔너리 값을 맵핑
result = [compression_dict[num] for num in coordinate]

print(*result)
