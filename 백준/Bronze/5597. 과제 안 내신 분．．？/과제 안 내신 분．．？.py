import sys

numbers = [i for i in range(1, 31)]
no_submit = []

for _ in range(28):
    n = int(sys.stdin.readline().strip())

    numbers.remove(n)
    numbers.sort()

print(min(numbers))
print(numbers[1])