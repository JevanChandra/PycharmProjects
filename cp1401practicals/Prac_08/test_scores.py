"""
2. Test Scores
scores.txt = empty
grades = empty


function main():
    for i in range(0, 4):
        score = check_errors("Score: ")
        scores.txt.append(score)
        grade = check_grade(score)
        grades.append(grade)
    average = get_the_average()
    trend = get_the_trend(average)
    display list, average, trend


function get_the_average():
    return (sum(scores.txt)) / len(scores.txt)


function get_the_trend(average):
    if average < scores.txt[3]:
        return "positive"
    else:
        return "not positive"


function check_grade(score):
    if score < 50:
        return "N"
    elif score < 65:
        return "P"
    elif score < 75:
        return "C"
    elif score < 85:
        return "D"
    else:
        return "HD"


function check_errors(prompt):
    get number
    while number < 0 or number > 100:
        display error
        get number
    else:
        return number


main()
"""
scores = []
grades = []
MAX = 4


def main():
    for i in range(0, MAX):
        score = check_errors("Score: ")
        scores.append(score)
        grade = check_grade(score)
        grades.append(grade)
    average = get_the_average()
    trend = get_the_trend(average)
    for i in range(0, MAX):
        print(f"Score {i + 1} was {scores[i]}, which is {grades[i]}")
    print(f"The average score was {average}")
    print(f"The trend is {trend}")


def get_the_average():
    return (sum(scores)) / len(scores)


def get_the_trend(average):
    if average < scores[3]:
        return "positive"
    else:
        return "not positive"


def check_grade(score):
    if score < 50:
        return "N"
    elif score < 65:
        return "P"
    elif score < 75:
        return "C"
    elif score < 85:
        return "D"
    else:
        return "HD"


def check_errors(prompt):
    number = float(input(prompt))
    while number < 0 or number > 100:
        print("Invalid input")
        number = float(input(prompt))
    else:
        return number


main()