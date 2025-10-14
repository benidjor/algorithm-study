import sys

input = sys.stdin.readline

T = int(input())

def recursion(s, l, r):
    # 함수 호출 횟수
    recursion.counter += 1

    if l >= r:
        return 1
    else:
        if s[l] != s[r]:
            return 0
        else:
            return recursion(s, l+1, r-1)
        
def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


recursion.counter = 0

for _ in range(T):
    
    S = input().strip()
    print(isPalindrome(S), recursion.counter)
    recursion.counter = 0