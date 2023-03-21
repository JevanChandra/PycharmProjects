"""Strings"""


# 1. Processing Strings
def question_1():
    data_strings = ["Result = 95%", "Final Score = 8%", "Relative Value = 178%",
                "Something else that's very important = 9.2%", "x = 42%"]

    for i in data_strings:
        print(float(i[i.find("=")+2:len(i) - 1]))


# 2. Date Strings
def question_2():
    YEAR = 2023
    DOB = str(input("DOB: "))  # dd/mm/year
    birth_year = int(DOB[6:len(DOB)])
    age = YEAR - birth_year
    print(f"You were born in {birth_year}.")
    print(f"You will turn {age} in {YEAR}.")


# 3. Subject Code Strings
def question_3():
    subject_code = str(input("Enter subject code: "))
    while subject_code != "":
        subject = get_subject(subject_code)
        subject_year = get_subject_year(subject_code)
        print(f"That is a {subject_year} {subject} subject")
        subject_code = str(input("Enter subject code: "))


def get_subject_year(subject_code):
    code = int(subject_code[2])
    if code == 1:
        return "first-year"
    elif code == 2:
        return "second-year"
    elif code == 3:
        return "third-year"
    elif code:
        return "Masters or other"


def get_subject(subject_code):
    if subject_code.startswith("CP"):
        return "IT"
    elif subject_code.startswith("MA"):
        return "Maths"
    elif subject_code.startswith("PH"):
        return "Public Health"


# question_1()
# question_2()
question_3()