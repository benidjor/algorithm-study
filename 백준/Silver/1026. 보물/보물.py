N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

# (A의 가장 작은 수 * B의 가장 큰 수) + (A의 두번째로 작은 수 * B의 두번째로 큰 수) 이런식으로 합산

result = 0
for _ in range(N):

    min_a = min(A)
    max_b = max(B)

    min_a_idx = A.index(min_a)
    max_b_idx = B.index(max_b)

    # (A의 가장 작은 수 * B의 가장 큰 수)를 result에 더해준다
    result += (min_a * max_b)

    # A의 가장 작은 수와 B의 가장 큰 수를 리스트에서 제거한다
    A.pop(min_a_idx)
    B.pop(max_b_idx)

print(result)