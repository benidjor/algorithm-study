import sys
import math

"""
+2 (2)
-1 (1)
+2 (3)
-1 (2)
+2 (5)
"""

A, B, V = map(int, sys.stdin.readline().split())

days_before_last = math.ceil((V-A) / (A-B))


print(days_before_last + 1)