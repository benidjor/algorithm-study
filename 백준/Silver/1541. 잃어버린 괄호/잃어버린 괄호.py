import sys

input = sys.stdin.readline

expression = input().strip()

split_by_minus = expression.split("-")

def process_initial_sign(data_list):
    """
    리스트의 첫 요소가 빈 문자열이면 두 번째 요소에 음수 부호를 붙이고,
    아니면 리스트를 그대로 반환
    """
    # 리스트가 비어있지 않고, 첫 번째 요소가 빈 문자열이며, 요소가 2개 이상인지 확인
    if data_list and data_list[0] == '' and len(data_list) > 1:
        # 첫 번째 빈 문자열을 제외하고 새로운 리스트를 생성
        # 1. 두 번째 요소(data_list[1]) 앞에 '-'를 붙인다
        # 2. 세 번째 요소부터(data_list[2:]) 끝까지의 요소를 가져온다.
        # 3. 두 결과를 합쳐 새로운 리스트 생성
        processed_list = ['-' + data_list[1]] + data_list[2:]
        return processed_list
    else:
        # 위의 조건에 해당하지 않으면 원본 리스트를 그대로 반환
        return data_list
  
def safe_sum(string_number):
    """'50+40' 또는 '00009' 같은 문자열을 받아 안전하게 합계를 계산하는 함수."""
    return sum(int(num) for num in string_number.split('+'))

processed_string_number = map(safe_sum, process_initial_sign(split_by_minus))

processed_list = [num if index == 0 else -num for index, num in enumerate(processed_string_number)]

sum = 0
for num in processed_list:
    sum += num

print(sum)
