"""
3. JCU Grades


function main()
    get score
    while score is not -1
        grade = check_grade(score)
        display score, grade
        get score
    else
        get = random_scores
        for i in range(random_scores):
            score = random.randint(0, 101)
            grade = check_grade(score)
            display score, grade


function check_grade(score):
    if score < 50:
        return "F"
    elif score < 65:
        return "P"
    elif score < 75:
        return "C"
    elif score < 85:
        return "D"
    else:
        return "HD"
"""
import random


def main():
    score = float(input("Scores: "))
    while score != -1:
        grade = check_grade(score)
        print(f"The score {score} is {grade}")
        score = float(input("Scores: "))
    else:
        random_scores = int(input("How many random scores.txt: "))
        for i in range(random_scores):
            score = random.randint(0, 101)
            grade = check_grade(score)
            print(f"{score} = {grade}")


def check_grade(score):
    if score < 50:
        return "F"
    elif score < 65:
        return "P"
    elif score < 75:
        return "C"
    elif score < 85:
        return "D"
    else:
        return "HD"


def run_test():
    grade = check_grade(65)
    print(grade)
    grade = check_grade(89.5)
    print(grade)


# run_test()
main()