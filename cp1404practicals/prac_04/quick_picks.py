import random

quick_picks = input("How many quick picks? ")

for i in range(0, int(quick_picks)):
    numbers = []
    for j in range(0, 6):
        number = random.randint(1, 45)
        if number in numbers:
            number = random.randint(number + 1, 45)
            numbers.append(number)
        else:
            numbers.append(number)
    numbers.sort()
    numbers_string = [str(number) for number in numbers]
    joined_numbers = " ".join(numbers_string)
    print(f"{joined_numbers}")