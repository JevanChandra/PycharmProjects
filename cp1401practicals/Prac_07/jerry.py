"""
1. Jerry the Driver
function main
    speed_in_mph = get_valid_number("speed in mph")
    speed_limit_in_kph = get_valid_number("speed limit in kph")
    speed_in_kph = convert_miles_to_km(speed_in_mph)
    fine = determine_fine(speed_in_km, speed_limit_in_kph)
    bank_balance -= fine
    display fine
    display bank_balance

function get_valid_number(prompt)
    get number
    while number < 0
        display error message
        get number
    else
        return number

function convert_miles_to_km(speed_in_mph)
    return speed_in_mph * 0.621371

function determine_fine(speed_in_km, speed_limit_in_kph)
    result = speed_limit_in_kph - speed_in_km
    if result < 0
        return 0
    elif result < 13
        return 177
    elif result < 20
        return 266
    elif result < 30
        return 444
    elif result < 40
        return 622
    else:
        return 1245
"""


def main():
    bank_balance = 100
    speed_in_mph = get_valid_number("speed in mph")
    speed_limit_in_kph = get_valid_number("speed limit in kph")
    speed_in_kph = convert_miles_to_km(speed_in_mph)
    fine = determine_fine(speed_in_kph, speed_limit_in_kph)
    bank_balance -= fine
    print(f"Your fine is ${fine}")
    print(f"Your bank balance is ${bank_balance}")


def get_valid_number(prompt):
    number = int(input(prompt))
    while number < 0:
        print("Invalid number")
        number = int(input(prompt))
    else:
        return number


def convert_miles_to_km(speed_in_mph):
    return speed_in_mph * 0.621371


def determine_fine(speed_in_km, speed_limit_in_kph):
    result = speed_limit_in_kph - speed_in_km
    if result < 0:
        return 0
    elif result < 13:
        return 177
    elif result < 20:
        return 266
    elif result < 30:
        return 444
    elif result < 40:
        return 622
    else:
        return 1245