import sys
word = sys.stdin.readline().strip()
dial = {
    2: ["A", "B", "C"],
    3: ["D", "E", "F"],
    4: ["G", "H", "I"],
    5: ["J", "K", "L"],
    6: ["M", "N", "O"],
    7: ["P", "Q", "R", "S"],
    8: ["T", "U", "V"],
    9: ["W", "X", "Y", "Z"]
}

estimated_time = 0

for w in word:

    for key, value in dial.items():
        if w in value:
            num = key
    
    estimated_time += num +1
print(estimated_time)