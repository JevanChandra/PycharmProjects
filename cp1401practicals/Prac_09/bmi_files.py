"""
7. BMI Files


"""


def main():
    people = int(input("Number of people: "))
    out_file = open("bmis.txt", "w")
    for i in range(people):
        height = float(input("Height: "))
        weight = float(input("Weight: "))
        bmi = calculate_bmi(height, weight)
        category = determine_weight_category(bmi)
        print(f"BMI {bmi:.1f}, considered {category}", file=out_file)
    out_file.close()
    display_bmi_cat()


def display_bmi_cat():
    in_file = open("bmis.txt", "r")
    for i in in_file:
        text = i.strip()
        print(text)
    in_file.close()


def calculate_bmi(height, weight):
    return weight / (height ** 2)


def determine_weight_category(bmi):
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"


main()