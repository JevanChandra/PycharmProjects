"""
CP1401 2022-2 Assignment 1
Program 1 – Pay Calculator
Student Name: <Jevan Chandra>
Date started: <08/08/2022>

Pseudocode:
get experience_level, hours_worked
money_multiplied_level = experience_level * 45
money_addition = 0.05 * money_multiplied_level
hourly_pay = money_addition + 45
total_pay = hourly_pay * hours_worked
display hourly_pay
display total_pay
"""

BASE_PAY = 45
PAY_PERCENTAGE = 0.05
# 5% = 0.05
# 10% = 0.10
# etc

print("Experience Counts Pay Calculator")
hours_worked = int(input("Number of hours worked: "))
experience_level = int(input("      Experience level: "))

money_multiplied_level = experience_level * BASE_PAY
money_addition = PAY_PERCENTAGE * money_multiplied_level        # get the amount of money added to the salary
hourly_pay = money_addition + BASE_PAY
total_pay = hourly_pay * hours_worked

print("Based on your experience level (", experience_level, "):", sep="")
print(f"Your hourly pay rate is ${hourly_pay:.2f}")
print(f"Your total pay is ${total_pay:.2f}")
# we use f string and .2f so the result has 2 decimal points.
