import sys

N, B = map(int, sys.stdin.readline().split())

numbers = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
    "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z"
]

"""
숫자를 N으로 더 이상 나누어지지 않을 때까지 반복하고, 나머지 값을 역순으로 써주면 N진법으로 변환된다
"""

digits = []

while N > 0:
    m = N % B   # 나머지 값을 따로 모아서 변환한다
    N = N // B  # 몫
    
    digit = numbers[m]
    # insert를 사용하여, digit를 역순으로 삽입한다
    digits.insert(0, digit)

print("".join(digits))