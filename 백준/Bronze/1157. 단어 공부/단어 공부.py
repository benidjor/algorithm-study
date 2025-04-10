import sys
from collections import Counter

word = sys.stdin.readline().strip().upper()
cnt = Counter(word).most_common()

if len(cnt) >= 2:
    if cnt[0][1] == cnt[1][1]:
        print("?")
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])