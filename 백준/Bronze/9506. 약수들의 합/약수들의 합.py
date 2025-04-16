import sys

for line in sys.stdin:

    # 입력된 문자열의 공백 제거 후 정수로 변환
    n = int(line.strip())
    if n == -1:
        break

    aliquot_lst = []
    for i in range(1, n):
        if n % i == 0:
            aliquot_lst.append(i)

    if n == sum(aliquot_lst):
        sum_string = " + ".join(map(str, aliquot_lst))
        print(f"{n} = {sum_string}")

    else:
        print(f"{n} is NOT perfect.")