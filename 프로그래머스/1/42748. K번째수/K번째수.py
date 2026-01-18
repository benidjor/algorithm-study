def solution(array, commands):
    
    answer = []
    for command in commands:
        i, j, k = command
        array_cut = array[i-1:j]
        array_cut.sort()
        number = array_cut[k-1]
        answer.append(number)

    return answer