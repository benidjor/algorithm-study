import sys

n = int(sys.stdin.readline())

# a = [int(x) for x in input().strip().split()]
numbers = [int(x) for x in sys.stdin.readline().split()]
print(min(numbers), max(numbers))