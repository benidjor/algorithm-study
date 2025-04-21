import sys

a, b, c, d, e = map(int, sys.stdin.readline().split())

denominator = (a**2) + (b**2) + (c**2) + (d**2) + (e**2)

numerator = 10

print(denominator % numerator)
