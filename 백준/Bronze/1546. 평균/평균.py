import sys

N = int(sys.stdin.readline().strip())

scores = [int(x) for x in sys.stdin.readline().split()]
M = max(scores)

new_scores = [score / M * 100 for score in scores]

print(sum(new_scores) / N)