import sys

input = sys.stdin.readline

N = int(input())
K = int(input())
sensors = list(map(int, input().split()))

sensors.sort()

intervals = [sensors[i+1] - sensors[i] for i in range(N-1)]
top_k_intervals = sorted(intervals, reverse=True)[:K-1]

print(sum(intervals) - sum(top_k_intervals))
