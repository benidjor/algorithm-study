import sys

input = sys.stdin.readline

input_num_list = input().split()

def making_clock_num(num_list):
    
    clock_num_list = []

    for i in range(len(num_list)):

        modified_list = num_list[i:] + num_list[:i]
        
        possible_clock_num = int("".join(modified_list))
        clock_num_list.append(possible_clock_num)

    return min(clock_num_list)

clock_num = making_clock_num(input_num_list)

cnt = 0
checked = []

for num in range(1111, 10000):

    if "0" in list(str(num)):
        continue

    num = making_clock_num(list(str(num)))

    if num in checked:
        continue
    
    cnt += 1
    if num == clock_num:    
        break

    checked.append(num)
    

print(cnt)