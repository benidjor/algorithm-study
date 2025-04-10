import sys

word = sys.stdin.readline().strip()

# 짝수라면, 1/2한 것으로 나눈다
if len(word) % 2 == 0:
    threshold = int(len(word) / 2)

    if word[:threshold] == word[threshold:][::-1]:
        print(1)
    else:
        print(0)
# noon
# 0123
# ekitike
# 0123456
# 홀수라면, len(word) // 2
else:
    threshold = int(len(word) / 2)

    if word[:threshold] == word[threshold+1:][::-1]:
        print(1)
    else:
        print(0)