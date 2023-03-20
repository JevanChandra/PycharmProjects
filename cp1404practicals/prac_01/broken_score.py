"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
MIN = 0
MAX = 100

score = float(input("Enter score: "))
while score < MIN or score > MAX:
    print("Invalid score")
    score = float(input("Enter score: "))
else:
    if score >= 90:
        print("Excellent")
    else:
        if score >= 50:
            print("Passable")
        else:
            print("Bad")