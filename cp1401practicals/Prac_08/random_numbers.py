"""
1. Random numbers
import random
get quantity, maximum
number = empty

for i in range(0, quantity):
    number = random.randint(0, maximum)
    add number to numbers

display numbers, minimum, maximum, random choice, reversed, sorted
"""


import random
quantity = int(input("How many random numbers: "))
maximum = int(input("Maximum number: "))
numbers = []

for i in range(0, quantity):
    number = random.randint(0, maximum)
    numbers.append(number)

print(numbers)
print(f"The minimum number is {min(numbers)}")
print(f"The maximum number is {max(numbers)}")
print(f"A randomly chosen number is {random.choice(numbers)}")
numbers.reverse()
print(f"The numbers reversed are {numbers}")
numbers.sort()
print(f"The numbers sorted are {numbers}")

