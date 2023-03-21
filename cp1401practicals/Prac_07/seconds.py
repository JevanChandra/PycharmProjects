"""
3. Seconds Display


function main()
    for i in range(0, 3175, 635)
        minutes = convert_seconds_to_minutes_m(i)
        seconds = convert_seconds_to_minutes_s(i)
        display minutes, seconds


function convert_seconds_to_minutes(i)
    return i // 60

def convert_seconds_to_minutes_s(i):
    return i % 60
"""


def main():
    for i in range(0, 3175, 635):
        minutes = convert_seconds_to_minutes_m(i)
        seconds = convert_seconds_to_minutes_s(i)
        print(f"{i} seconds is {minutes}m {seconds}s")


def convert_seconds_to_minutes_m(i):
    return i // 60
# to convert the seconds into minutes we need two functions
# on for the minutes and one more for the seconds


def convert_seconds_to_minutes_s(i):
    return i % 60


main()