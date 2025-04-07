import sys
from datetime import datetime, timedelta, date, time

H, M = map(int, sys.stdin.readline().split())

total_minutes = H * 60 + M

# 모듈로 연산을 사용하여 음수 값을 항상 0 ~ 1439 의 값으로 만들어준다
new_total_minutes = (total_minutes - 45) % (24 * 60)

new_h = new_total_minutes // 60
new_m = new_total_minutes % 60

print(new_h, new_m)