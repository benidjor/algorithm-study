import sys

input = sys.stdin.readline

a_1, a_0 = map(int, input().split())

c = int(input())
n_0 = int(input())

# 함수 f(n) 선언
fn = a_1*n_0 + a_0

if fn <= (n_0 * c) and a_1 <= c:
    print(1)
else:
    print(0)


