import sys
import re

# 여러 줄 입력받기
lines = sys.stdin.readlines()

def is_balanced(line):
    stack = []
    brackets_dict = {
        "]": "[", 
        ")": "("
    }

    for word in line:
        # 여는 괄호일 때, stack에 저장
        if word in "[(":
            stack.append(word)
        
        elif word in ")]":
            # 닫는 괄호일 때, 미리 선언된 stack이 없거나 stack에서 괄호 짝이 안 맞을때 no 반환
            if not stack or stack[-1] != brackets_dict[word]:
                return "no"
            
            # 닫는 괄호일 때, 미리 선언된 stack이 있고 stack에서 괄호 짝이 맞을때 stack에서 여는 괄호 뺀다
            else:
                stack.pop()
    
    # stack 남아 있다: 짝이 안 맞다
    if stack:
        return "no"
    # stack 비어 있다: 짝 맞다
    else:
        return "yes"


for line in lines:
    line = line.rstrip('\n')  # 개행 제거
    
    if line == '.':
        break

    # 정규표현식으로 괄호 제거
    brackets = "".join(re.findall(r"[\[\]\(\)]", line))
    print(is_balanced(brackets))
