import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

"""
What did you see on line 1?
5 is the smallest number and 19 is the largest

What did you see on line 2?
3 is the smallest number and 9 is the largest
no, in line 2 a 4 cannot be produced

What did you see on line 3?
2.5 is the smallest number and 5.4999....
"""

print(random.uniform(1, 100))
