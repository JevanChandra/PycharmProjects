"""
4. BMIs

function main()
    bmi = calculate_bmi(height, weight)
    category = determine_weight_category(bmi)
    for i in range(50, 101, 2)
        display i, bmi, category


function determine_weight_category(bmi)
    if bmi < 18.5
        return considered underweight
    else if bmi < 25
        return considered normal
    else if bmi < 30
        return considered overweight
    else
        return considered obese


function calculate_bmi(height, weight)
    return weight / (height ** 2)
"""


def main():
    HEIGHT = 1.75
    for weight in range(50, 101, 2):
        bmi = calculate_bmi(HEIGHT, weight)
        category = determine_weight_category(bmi)
        print(f"Height {HEIGHT}m, Weight {weight}kg = BMI {bmi:.1f}, {category}")


def determine_weight_category(bmi):
    if bmi < 18.5:
        return "considered underweight"
    elif bmi < 25:
        return "considered normal"
    elif bmi < 30:
        return "considered overweight"
    else:
        return "considered obese"


def calculate_bmi(height, weight):
    return weight / (height ** 2)

main()