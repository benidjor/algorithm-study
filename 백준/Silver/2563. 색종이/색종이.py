import sys

# 가로, 세로 크기가 각각 100인 흰색 도화지를 만든다
array = [[0 for _ in range(100)] for _ in range(100)]

n = int(sys.stdin.readline().strip())

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    
    # 검은색 영역을 구해준다
    # 흰색 영역: 0, 검은색 영역: 1

    for i in range(x, x+10):
        for j in range(y, y+10):
            array[i][j] = 1

# 검은색 영역은 전부 1로 표시되어 있다 (겹치는 영역도 1로 되어 있다)
# 1로 표시된 검은색 영역 전부 더해준다
black = sum(sum(row) for row in array)    

print(black)

