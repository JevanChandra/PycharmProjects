def main():
    score = float(input("Enter score: "))
    message = score_result(score)
    print(message)


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