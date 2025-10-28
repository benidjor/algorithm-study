import sys
from itertools import combinations
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

# 입력받는 능력치 2차원 배열
arr = [list(map(int, input().split())) for _ in range(N)]

# 팀원들로 생성할 수 있는 팀 조합 생성
team_combis_list = list(combinations(range(N), N//2))

# 팀원들의 능력치 조회를 위한 조합 생성
combinations_list = list(combinations(range(N), 2))

# 팀 조합을 위해 defaultdict 사용
team_dict = defaultdict(list)

for team_combi in team_combis_list:
    # 생성된 팀원 조합에 없는 사람들은 반대 팀에 배정
    opposit_list = [item for item in list(range(N)) if item not in team_combi]

    # team[홈 팀 팀원] = 어웨이 팀 팀원
    team_dict[team_combi] = opposit_list

for key, value in team_dict.items():

    # 홈, 어웨이 팀원들의 능력치를 알아보기 위해 조합 생성
    key_combis = list(combinations(key, 2))
    value_combis = list(combinations(value, 2))

    key_attribute = 0
    value_attribute = 0
    
    # 홈팀 팀원들의 능력치 계산
    for x, y in key_combis:
        key_attribute += arr[y][x] + arr[x][y]
        # 홈팀 팀원들의 능력치 계산하여 value로 지정
        team_dict[key] = [key_attribute]
    
    # 어웨이 팀원들의 능력치 계산
    for x, y in value_combis:
        value_attribute += arr[y][x] + arr[x][y]
    # 어웨이팀 팀원들의 능력치 계산하여 이미 value로 지정되어 잇는 홈팀 능력치 리스트에 요소 추가
    team_dict[key].append(value_attribute)
    
result = float("inf")

# 홈팀과 어웨이팀 전력차를 계산
for value in team_dict.values():
    diff = abs(value[0] - value[1])
    
    if diff < result:
        result = diff

print(result)