import sys
from collections import Counter

N = int(sys.stdin.readline().strip())

cnt = 0

for _ in range(N):
    word_lst = []
    word = sys.stdin.readline().strip()
    
    for i, w in enumerate(word):
        # i가 word의 마지막 문자라면, 그냥 마지막 문자를 word_lst에 추가한다
        if i == len(word)-1:
            word_lst.append(w)
        else:
            # 연속된 단어가 다르다면, word_lst에 문자를 추가한다
            if word[i] != word[i+1]:
                word_lst.append(w)

    # 추가된 문자들 (연속되지만 다른 문자) 개수를 센다
    # 문자의 개수가 2가 넘어간다면 그룹 단어가 아니라는 뜻
    word_cnt = Counter(word_lst)

    # 그룹 단어가 아닌 것들의 개수를 센다
    if all(count == 1 for count in word_cnt.values()):
        cnt += 1

print(cnt)

