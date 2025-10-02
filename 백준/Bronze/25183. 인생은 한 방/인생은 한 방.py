import sys

input = sys.stdin.readline

N = int(input())
lotto = input()

cnt = 1
ans = 1

for i in range(N):
    # print(ord(lotto[i]) - ord(lotto[i-1]))
    if abs(ord(lotto[i]) - ord(lotto[i-1])) == 1:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 1

if ans >= 5:
    print("YES")
else:
    print("NO")