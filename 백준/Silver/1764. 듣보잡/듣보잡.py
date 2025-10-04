import sys

input = sys.stdin.readline

N, M = map(int, input().split())

no_hear_list = []
no_see_list = []

for _ in range(N):
    no_hear_list.append(input().strip())


for _ in range(M):
    no_see_list.append(input().strip())

# set으로 변경하여 교집합 사용
no_hear_no_see = set(no_hear_list) & set(no_see_list)

# 사전 순으로 출력하기 위해 오름차순 정렬
no_hear_no_see_sorted = sorted(no_hear_no_see)

print(len(no_hear_no_see_sorted))

for name in no_hear_no_see_sorted:
    print(name)
