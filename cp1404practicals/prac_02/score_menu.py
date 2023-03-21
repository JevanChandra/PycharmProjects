

def main():
    MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    score = 0
    print(MENU)
    option = input(">>>").upper()
    while option != "Q":
        if option == "G":
            score = get_valid_score()
        elif option == "P":
            print(score)
            message = score_result(score)
            print(message)
        elif option == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        option = input(">>>").upper()

    else:
        print("farewell")


def print_stars(score):
    for i in range(0, score + 1):
        print("*", end='')
    print(" ")


def get_valid_score():
    score_input = int(input("Enter your score:"))
    while score_input < 0 or score_input > 100:
        print("Invalid score")
        score_input = int(input("Enter your score:"))
    else:
        return score_input


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
