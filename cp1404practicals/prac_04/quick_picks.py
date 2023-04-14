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
    joined_numbers = " ".join("{:2d}".format(number) for number in numbers)
    print(f"{joined_numbers}")