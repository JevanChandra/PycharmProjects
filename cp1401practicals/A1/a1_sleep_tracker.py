"""
CP1401 2022-2 Assignment 3
Program 3 – Sleep Tracker
Student Name: <Jevan Chandra>
Date started: <19/08/2022>

Pseudocode:
display Sleep Tracker
while night is not 5
    night = night + 1
    get user_input
    while 0 > user_input > 24
        display error
        get user_input
    else
        total_sleep = total_sleep + user_input
else
    sleep_debt = RECOMMENDED_SLEEP - total_sleep
    display recommended sleep
    display total_sleep
    if total_sleep >= recommended sleep
        display You are getting enough sleep. Keep it up!
    else
        display sleep_debt
"""
RECOMMENDED_SLEEP = 40
# 8 HOURS every 5 days.  8 * 5 = 40
night = 0
total_sleep = 0
MAXIMUM_DAYS = 5
MAXIMUM_HOURS = 24
MINIMUM_HOURS = 0
NIGHT_START = 1

print("Sleep Tracker")
while night != MAXIMUM_DAYS:            # stops the program if it reaches the max days
    night += NIGHT_START
    user_input = float(input(f"Night {night} hours sleep: "))
    while MINIMUM_HOURS > user_input or user_input > MAXIMUM_HOURS:      # checks errors in the input.
        print("Invalid number of hours.")
        user_input = float(input(f"Night {night} hours sleep: "))
    else:
        total_sleep += user_input            # adds up the amount of sleep inputted
else:
    sleep_debt = RECOMMENDED_SLEEP - total_sleep
    print(" ")    # to add empty line
    print("Recommended total sleep is:", RECOMMENDED_SLEEP, sep=" ")
    print("Your total hours of sleep :", total_sleep, sep=" ")
    if total_sleep >= RECOMMENDED_SLEEP:
        print("You are getting enough sleep. Keep it up!")
    else:
        print("Your sleep debt over this time is:", sleep_debt, sep=" ")

