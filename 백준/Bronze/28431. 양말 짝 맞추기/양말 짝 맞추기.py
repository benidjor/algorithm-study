import sys
from collections import Counter

# 여러 줄에 걸쳐 입력받은 숫자들을 하나의 리스트로 만들기
numbers = []
while True:
    line = sys.stdin.readline().strip()
    if not line:
        break
    numbers.append(int(line))

num_cnt = Counter(numbers)

filtered = [num for num, cnt in num_cnt.items() if cnt % 2 == 1]
print(*filtered)
