import sys

number = sys.stdin.readline()
# num_list = list(str(number))
# num_list.reverse()

# original_num = 0
# for i, num in enumerate(num_list):
#     original_num += (2**i * int(num))

# # print(original_num)

# num_eight = []
# while original_num != 0:
#     num_eight.append(original_num % 8)
#     original_num = original_num // 8

# num_eight.reverse()
# print(int("".join(map(str, num_eight))))

decimal = int(number, 2)
print(oct(decimal)[2:])