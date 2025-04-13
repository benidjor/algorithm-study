import sys

N, B = sys.stdin.readline().split()

numbers = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z"
]

"""
만약 ZZZZZ라면 35*36**4 + 35*36**3 + 35*36**2 + 35*36**1 + 35*36**0
"""

total_sum = 0

for i, n in enumerate(N[::-1]):
    number = numbers.index(n)
    number = int(number)
    total_sum += (number * (int(B) ** i))

print(total_sum)

