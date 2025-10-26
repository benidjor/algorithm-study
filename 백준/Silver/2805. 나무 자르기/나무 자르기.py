import sys

input = sys.stdin.readline

N, M = map(int, input().split())

heights = list(map(int, input().split()))

# 가져갈 수 있는 나무 길이를 구한다
def tree_cutting(heights, height_needed):
    cutting_length = 0

    for height in heights:
        if height > height_needed:
            cutting_length += (height - height_needed)
    
    return cutting_length


def parametric_binary_search(array, target, start, end):
    result = 0
    
    while start <= end:
        
        mid = (start + end) // 2

        metre = tree_cutting(array, mid)

        # 가져갈 수 있는 나무의 길이가 target보다 작으면 왼쪽 탐색 (나무를 잘게 잘라야 한다)
        if metre < target:
            end = mid - 1
            
        else:
            result = mid
            start = mid + 1

    return result

start = 1
end = max(heights)

print(parametric_binary_search(heights, M, start, end))

