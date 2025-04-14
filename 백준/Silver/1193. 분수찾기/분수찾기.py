import sys

X = int(sys.stdin.readline().strip())

"""
(1) 1/1
(2) 1/2, 2/1
(3) 3/1, 2/2, 1/3
(4) 1/4, 2/3, 3/2, 4/1
(5) 5/1, 4/2, 3/3, 2/4, 1/5

홀수 레이어: n/1 ~
짝수 레이어: 1/n ~
X번째를 알려면: 1 + 2 + 3 + 4 + 
"""

idx = 0
layer = 1
cnt = 1

while X > cnt:
    layer += 1
    idx = X - cnt
    cnt += layer

lst = []
if layer % 2 == 0:
    for l in range(1, layer+1):
        lst.append(f"{l}/{layer+1 - l}")
else:
    for m in range(1, layer+1):
        lst.append(f"{layer+1 - m}/{m}")


print(lst[idx-1])
