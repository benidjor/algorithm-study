import sys

# a, b = map(int, sys.stdin.readline().split())

while True:
    try:
        a, b = map(int, sys.stdin.readline().split())

        if b % a == 0:
            print("factor")
        elif (a / b) == int(a / b):
            print("multiple")
        else:
            print("neither")

    except:
        break

