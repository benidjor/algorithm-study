import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]
    # scores.sort(reverse=True)
    scores.sort()


    in_set = set()
    in_set.add(tuple(scores[0]))

    min_rank = scores[0][1]
    
    for i in range(1, N):

        if scores[i][1] < min_rank:
            in_set.add(tuple(scores[i]))
            min_rank = scores[i][1]
    
    print(len(in_set))