import sys

input = sys.stdin.readline

brackets = list(input().strip())

brackets_stack = []

cnt = 0

for i in range(len(brackets)):
    if brackets[i] == "(":
        brackets_stack.append(brackets[i])
        
    # 괄호가 ")"일 경우
    else:
        if brackets[i-1] == "(":
            brackets_stack.pop()
            cnt += len(brackets_stack)
        
        else:
            brackets_stack.pop()
            cnt += 1

print(cnt)