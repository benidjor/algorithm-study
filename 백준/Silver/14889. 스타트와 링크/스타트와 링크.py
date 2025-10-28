import sys
from itertools import combinations

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# 스타트, 링크 팀 차집합 계산 위해 set 설정
players = set(range(N))

# 팀원들로 생성할 수 있는 팀 조합 생성
team_combis_list = list(combinations(range(N), N//2))

result = float("inf")

list_len = len(team_combis_list)

# 스타트, 링크 팀이 바뀌어도 능력치 차이는 동일하기 때문에, 중복 계산 방지를 위해 절반만 순회
for i in range(list_len//2):
    
    start_team = team_combis_list[i]

    link_team = list(players - set(start_team))

    start_attribute = 0
    link_attribute = 0

    # 스타트, 링크 팀의 능력치를 즉시 계산
    for x, y in combinations(start_team, 2):
        start_attribute += arr[y][x] + arr[x][y]
    
    for x, y in combinations(link_team, 2):
        link_attribute += arr[y][x] + arr[x][y]
    
    # 즉시 최소값 갱신
    diff = abs(start_attribute - link_attribute)

    if diff < result:
        result = diff
    
    # 만약 스타트, 링크 팀 능력치 차이가 0이라면, 더 이상 탐색할 필요가 없다
    if result == 0:
        break

print(result)