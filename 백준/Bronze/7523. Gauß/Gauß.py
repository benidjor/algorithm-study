import sys

input = sys.stdin.readline

test_num = int(input())

for i in range(test_num):
    n, m = map(int, input().split())
    print(f"Scenario #{i+1}:")
    result = ((n+m) * (m-n+1)) // 2
    print(f"{result}\n")
