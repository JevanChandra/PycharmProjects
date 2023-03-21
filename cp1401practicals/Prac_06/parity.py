"""
2. Parity

function main()
get number
    parity = calculate_parity(number)
    display number, parity

function calculate_parity(number)
    return number % 2

function is_odd(number):
    if number == EVEN:
        return "is even"
    else:
        return "is odd"
"""
EVEN = 0
PARITY_CALCULATION = 2


def main():
    number = int(input("Number: "))
    odd_or_even = is_odd(4)
    # parity_result_4 = calculate_parity(4)
    # print(f"Parity of 4 should be 0: {parity_result_4}")
    # parity_result_41 = calculate_parity(41)
    # print(f"Parity of 41 should be 1: {parity_result_41}")
    parity = calculate_parity(number)
    print(f"Parity of {number}: {parity}")


def calculate_parity(number):
    return number % PARITY_CALCULATION


def is_odd(number):
    if number == EVEN:
        return "is even"
    else:
        return "is odd"


main()