import sys
import heapq

input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    x = int(input())

    # x가 자연수라면, 힙에 x라는 값을 추가한다
    if x > 0:
        heapq.heappush(heap, x)
    
    # x가 0이라면, 배열에서 가장 작은 값을 출력하고 그 값을 배열에서 제거한다.
    else:
        # 만약 배열이 비어 있는 경우인데 가장 작은 앖을 출력하려면, 0을 출력한다.
        if not heap:
            print(0)
        else:
            min_value = heapq.heappop(heap)
            print(min_value)
