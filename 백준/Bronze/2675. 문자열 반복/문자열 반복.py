import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    input_line = sys.stdin.readline().strip()
    tokens = input_line.split()

    R = int(tokens[0])
    S = tokens[1]

    result = ''.join(map(lambda x: x * R, S))
    print(result)


