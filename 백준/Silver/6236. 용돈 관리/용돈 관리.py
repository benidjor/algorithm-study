import sys

input = sys.stdin.readline

N, M = map(int, input().split())

money_list = [int(input()) for _ in range(N)]

def find_withdraw_count(withdrawn_money, money_list):
    cnt = 1
    pocket_money = withdrawn_money

    for money in money_list:
        if pocket_money < money:
            pocket_money = withdrawn_money  # 인출
            cnt += 1
        
        # 사용한 금액 차감
        pocket_money -= money
    
    return cnt


def parametric_binary_search(array, target, start, end):
    # target은 cnt
    
    while start <= end:
        mid = (start + end) // 2

        # mid (K)로 인출 시 총 횟수
        total_count = find_withdraw_count(mid, array)

        # total_count가 M보다 크다 (K가 너무 작아서 목표 횟수보다 많이 인출한다)
        if total_count > target:
            # K를 늘려야 한다 (오른쪽 탐색)
            start = mid + 1
        
        # total_count가 M보다 작거나 같다 (K가 적절하거나 너무 커서 목표 횟수보다 적게 인출한다)
        else:
            # 현재 mid는 조건을 만족하는 후보
            result = mid
            # 최소 K를 찾기 위해, 더 작은 K가 있는지 확인하려 왼쪽 탐색
            end = mid - 1
        
    return result

# K의 최솟값 (하루 최대 사용량보다 커야 한다)
start = max(money_list)
# K의 최댓값 (모든 금액의 합)
end = sum(money_list)

K = parametric_binary_search(money_list, M, start, end)
print(K)