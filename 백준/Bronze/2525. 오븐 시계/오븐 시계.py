import sys
import datetime

A, B = map(int, sys.stdin.readline().split())
C = int(sys.stdin.readline())

time_now = datetime.datetime(2025, 1, 1, A, B)

processing_time = datetime.timedelta(minutes=C)

new_time = time_now + processing_time

print(new_time.hour, new_time.minute)