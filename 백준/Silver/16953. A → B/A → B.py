import sys

input = sys.stdin.readline
A, B = map(int, input().split())


def calculate(A, B):
    cnt = 1
    while B != A:
        if len(str(B)) > 1 and int(str(B)[-1]) == 1:
            B = int(str(B)[:-1])
        elif B % 2 == 0:
            B = B // 2
        else:
            return -1
        
        cnt += 1
    return cnt

result = calculate(A, B)
print(result)