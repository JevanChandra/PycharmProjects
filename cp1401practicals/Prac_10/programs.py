def question_1():
    for i in range(0, 40):
        print("-", end="")


def question_2():
    some_number = int(input("Number: "))
    if is_even(some_number):
        print(f"{some_number} is even")
    else:
        print(f"{some_number} is odd")


def is_even(some_number):
    if some_number % 2 == 0:
        return True
    else:
        return False


def question_3():
    name = check_empty_string("Name: ").title()
    birthplace = check_empty_string("Birthplace: ").title()
    print(f"Hi {name} from {birthplace}!")


def check_empty_string(prompt):
    user_input = input(prompt)
    while user_input == "":
        print("Invalid")
        user_input = input(prompt)
    else:
        return user_input


def question_4():
    numbers = []
    minimum = int(input("Minimum number: "))
    maximum = check_num("Maximum number: ", minimum)
    for i in range(minimum, maximum + 1):
        numbers.append(i)
    print(numbers)


def check_num(prompt, minimum):
    number = int(input(prompt))
    while number <= minimum:
        print(f"You maximum must be greater than {minimum}")
        number = int(input(prompt))
    else:
        return number


subjects = []


def question_5():
    check_input("Enter subject code: ")


def check_input(prompt):
    subject = str(input(prompt)).upper()
    while subject != "":
        if len(subject) != 6:
            print("Invalid subject code")
            subject = str(input(prompt)).upper()

        if not subject[0:1].isalpha():
            print("Invalid subject code")
            subject = str(input(prompt)).upper()

        if not subject[2:6].isnumeric():
            print("Invalid subject code")
            subject = str(input(prompt)).upper()
        subjects.append(subject)
        subject = str(input(prompt)).upper()
    else:
        print(f"You do these {len(subjects)} subjects")
        display_subjects()
        check_for_cool_subject()


def display_subjects():
    for i in subjects:
        print(i)


def check_for_cool_subject():
    if "CP1401" in subjects:
        print("You are cool")


# question_1()
# question_2()
# question_3()
# question_4()
question_5()
