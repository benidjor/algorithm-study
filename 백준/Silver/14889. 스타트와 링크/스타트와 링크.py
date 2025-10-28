import sys
from itertools import combinations
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]


team_combis_list = list(combinations(range(N), N//2))
combinations_list = list(combinations(range(N), 2))

# print(team_combis_list)

attribute_list = []

team_dict = defaultdict(list)

for team_combi in team_combis_list:
    opposit_list = [item for item in list(range(N)) if item not in team_combi]
    # print(opposit_list)
    team_dict[team_combi] = opposit_list
    # combis = list(combinations(team_combi, 2))
    # print(combis)

    # for combi in combis:
    #     new_list = [item for item in list(range(N)) if item not in combi]
    #     print(new_list)
# print(team_dict)

for key, value in team_dict.items():

    key_combis = list(combinations(key, 2))
    value_combis = list(combinations(value, 2))

    key_attribute = 0
    value_attribute = 0
    
    for x, y in key_combis:
        key_attribute += arr[y][x] + arr[x][y]
        team_dict[key] = [key_attribute]
    
    for x, y in value_combis:
        value_attribute += arr[y][x] + arr[x][y]
    team_dict[key].append(value_attribute)
    


result = float("inf")
for value in team_dict.values():
    diff = abs(value[0] - value[1])
    
    if diff < result:
        result = diff


print(result)