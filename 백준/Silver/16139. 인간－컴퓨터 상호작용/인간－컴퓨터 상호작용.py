import sys

input = sys.stdin.readline

strings = input().strip()
q = int(input())
length = len(strings)

result = []

# 0번 인덱스 0으로 더미 패딩
alphabet_count = [[0] * (length+1) for _ in range(26)]

# 2차원 누적합 배열 계산
def prefix_sum_2d_alphabet(arr, length):
    
    # 모든 알파벳을 인덱스로 삼는다 (a ~ z)
    for i in range(26):
        # 문자열의 1부터 length + 1 번째 위치까지 순회
        for j in range(1, length+1):
            
            # 이전 위치의 알파벳 누적합 값 그대로 복사
            arr[i][j] = arr[i][j-1]

            # 문자열의 현재 알파벳에 해당하는 위치가 순회중인 알파벳 인덱스와 동일하다면 누적합에 1 더한다
            current_string_idx = ord(strings[j-1]) - 97

            if current_string_idx == i:
                arr[i][j] += 1
    
    return arr

prefix_sum = prefix_sum_2d_alphabet(alphabet_count, length)

for _ in range(q):
    a, l, r = input().split()
    a_idx = ord(a) - 97
    l = int(l)
    r = int(r)

    cnt = prefix_sum[a_idx][r+1] - prefix_sum[a_idx][l]

    result.append(str(cnt))

print("\n".join(result))
