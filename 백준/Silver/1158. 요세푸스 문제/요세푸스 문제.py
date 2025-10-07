import sys

input = sys.stdin.readline

N, K = map(int, input().split())

people = list(range(1, N+1))
delete_list = []
delete_idx = 0

while people:
    
    delete_idx += (K-1)

    if delete_idx >= len(people):
        delete_idx %= len(people)
    
    deleted = people.pop(delete_idx)
    delete_list.append(deleted)

print(f'<{", ".join(map(str, delete_list))}>')
