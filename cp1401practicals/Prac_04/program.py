# 1. Error Checking
"""
get worker_level
while worker_level < 1 or worker_level > 10
    display Invalid worker level
    get worker_level
salary = worker_level * 5000

display worker_level, salary
"""

# START = 1
# END = 10
# MULTIPLIER = 5000
# worker_level = int(input("Worker level: "))
# while worker_level < START or worker_level > END:
#     print("Invalid worker level")
#     worker_level = int(input("Worker level: "))
#
# salary = worker_level * MULTIPLIER
# print(f"With worker level {worker_level}, your salary is ${salary:,.2f}")


# 2. Number Sequences
# 2a.
# for i in range(1, 100, 2):
#     print(i)

# 2b.
# for i in range(1896, 2023, 4):
#     print(i)

# 2c.
# countdown from 60 to 0
# for i in range(60, -1, -1):
#     print(i)


# 3. Menus
"""
display choices
get user_choice
while user_choice != q
    if choice == s
    display :)
        display choices
        get user_choices
    else if choice == f
    display :(
        display choices
        get user_choices
    else display Invalid choice
        display choices
        get user_choices
display Farewell
"""

# print("(S)miley")
# print("(F)rowny")
# print("(Q)uit")
# user_choice = input("Choose an option: ")
#
# while user_choice != 'q':
#     if user_choice == 's':
#         print(":) ")
#         print(" ")
#         print("(S)miley")
#         print("(F)rowny")
#         print("(Q)uit")
#         user_choice = str(input("Choose an option: "))
#     elif user_choice == 'f':
#         print(":(")
#         print(" ")
#         print("(S)miley")
#         print("(F)rowny")
#         print("(Q)uit")
#         user_choice = str(input("Choose an option: "))
#     else:
#         print("Invalid choice")
#         print("(S)miley")
#         print("(F)rowny")
#         print("(Q)uit")
#         user_choice = str(input("Choose an option: "))
# print("Farewell")


# 4a. Accumulation
# Average Age
"""
get count
get age
while age != -1 
    total += age
average_age = total / count
display average age
"""
# SENTINEL = -1
# total = 0
# count = 0
# age = int(input("age : "))
# while age != -1:
#     total += age
#     count += 1
#     age = int(input("age : "))
# average_age = total / count
# print("average age is :", average_age)
# print("the count is :", count)


# 4b. Smileys Count
"""
display choices
get user_choice
while user_choice != q
    if choice == s
    display :)
    count_smiley += 1
        display choices
        get user_choices
        
    else if choice == f
    display :(
    count_frowney += 1
        display choices
        get user_choices
    else display Invalid choice
        display choices
        get user_choices
display Farewell
display forwneys
display smileys
"""
# count_smiley = 0
# count_frowney = 0
# print("(S)miley")
# print("(F)rowny")
# print("(Q)uit")
# user_choice = input("Choose an option: ")
#
# while user_choice != 'q':
#     if user_choice == 's':
#         print(":) ")
#         print(" ")
#         print("(S)miley")
#         print("(F)rowny")
#         print("(Q)uit")
#         count_smiley += 1
#         user_choice = str(input("Choose an option: "))
#     elif user_choice == 'f':
#         print(":(")
#         print(" ")
#         print("(S)miley")
#         print("(F)rowny")
#         print("(Q)uit")
#         count_frowney += 1
#         user_choice = str(input("Choose an option: "))
#     else:
#         print("Invalid choice")
#         print("(S)miley")
#         print("(F)rowny")
#         print("(Q)uit")
#         user_choice = str(input("Choose an option: "))
# print("Farewell")
# print("Smiley", count_smiley)
# print("Frowneys", count_frowney)


# 4c. Total numbers
"""
get amount_of_numbers
get numbers
total += numbers
display total
"""
# total = 0
# amount_of_numbers = int(input("How many numbers do you want to add up? "))
# for i in range(1, amount_of_numbers + 1):
#     number = int(input("Enter number: "))
#     total += number
# print("The total of those", amount_of_numbers, "numbers is", total)


# 5. Guessing Game
"""
get user_guess
if guess < 6 
    display lower
else 
    display higher
while guess is not 6
    display guess again!
    count += 1
    get user_guess
    get user_guess
    if guess < 6 
        display lower
    else 
        display higher
display You got it
display number of tries
"""
# count = 1
# SECRET = 6
# guess = int(input("Guess a number: "))
# if guess < SECRET:
#     print("Higher")
# else:
#     print("Lower")
# while guess != SECRET:
#     print("Guess again!")
#     count += 1
#     guess = int(input("Guess a number: "))
#     if guess < SECRET:
#         print("Higher")
#     else:
#         print("Lower")
# print("You got it in", count, "guesses!")


# 6. Nested Loops
"""
get row
get column
for row in range(column)
    
    
    
"""
row = int(input("Rows: "))
column = int(input("Columns: "))
for i in range(row):
    for j in range(column):
        print(j, end=' ')
    print()