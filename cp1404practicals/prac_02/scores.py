import random


def main():
    score = float(input("Enter score: "))
    message = score_result(score)
    print(message)
    random_score = random.randint(1, 100)
    print(f"random score: {random_score}")
    random_message = score_result(random_score)
    print(random_message)


def score_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()