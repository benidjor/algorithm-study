import sys
from string import ascii_lowercase

S = sys.stdin.readline().strip()

alphabet = list(ascii_lowercase)
answer = []

for word in alphabet:
    if word not in S:
        answer.append(-1)
    else:
        idx = S.index(word)
        answer.append(idx)

print(*answer)