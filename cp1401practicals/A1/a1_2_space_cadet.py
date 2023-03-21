"""
CP1401 2022-2 Assignment 2
Program 2 - Space Cadet
Student Name: <Jevan Chandra>
Date started: <14/08/2022>

Pseudocode:
display Welcome Trainee Space Cadet. How did you do?
get practical_score, exam_score
total_score = practical_score + exam_score
if total_score < 50
    display total score
    display You failed. Please try again next year.
elif exam_score <= practical_score
    display total score
    display You will become a field agent
else
    display total score
    display You will become a desk officer.
    display Congratulations on making the honour roll!
"""

MAXIMUM = 50
MINIMUM = 0
print("Welcome Trainee Space Cadet. How did you do?")
practical_score = int(input(f"Practical score ({MINIMUM}-{MAXIMUM}): "))
# use of f string to remove magic numbers
exam_score = int(input(f"     Exam score ({MINIMUM}-{MAXIMUM}): "))
total_score = practical_score + exam_score

print("Your total score is", total_score, "out of 100.", sep=" ")
# total score is placed above, so I don't have to repeat
if total_score < MAXIMUM:                   # decision making
    print("You failed. Please try again next year.")
elif exam_score <= practical_score:
    print("You will become a field agent.")
else:            # no elif needed as there are no other options
    print("You will become a desk officer.")
    print("Congratulations on making the honour roll!")