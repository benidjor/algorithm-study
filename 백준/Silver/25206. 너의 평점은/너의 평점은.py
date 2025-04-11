import sys

score_dict = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

total_score = 0
total_rating = 0

for _ in range(20):
    a, b, c = sys.stdin.readline().split()
    
    if c == "P":
        continue
    else:
        score = float(b) * score_dict[c]
        total_score += score
        total_rating += float(b)

print(total_score / total_rating)