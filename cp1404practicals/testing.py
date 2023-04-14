import random

# age = int(input("Enter your age: "))
#
# if age < 5:
#     print("Baby")
# elif age < 17:
#     print("Child")
# elif age < 65:
#     print("Adult")
# else:
#     print("Old")


# for i in range(3):
#     for j in range(4):
#         print(f"{i} - {j}")

# a = 2
# b = 1
# c = 3
# if a > b:
#     if b > c:
#         answer = c
#     else:
#         answer = b
# elif a > c:
#     answer = c
# else:
#     answer = a
#
# print(answer)

# names = ["A", "B", "C", "D", "E"]
# user_input = int(input(f"Enter number up to {len(names)}:"))
# try:
#     print(names[user_input - 1])
# except IndexError:
#     print("Invalid number")


# score_pairs = [['Derek', 7], ['Carrie', 8], ['Bob', 6]]
#
# new_name = input("Enter your name and score: ").split(', ')
# score_pairs.append(new_name)
# print(score_pairs)
# score_pairs.sort(reverse=True)
# print(score_pairs)

#
# def fn(x, y):
#     z = x + y
#
#
# print(fn(1, 2))
#
# # x = str(int('1.0'))
# # x[-1] = '2'
#
# previous_number = 0
# number = random.randint(1, 45)
# for i in range(0, 5):
#     while number < previous_number:
#         bigger_number = random.randint(number, 45)
#         previous_number = bigger_number
#         print(number)
#         print(previous_number)

print("*".join([len(word) for word in "one*two*three".split('*')]))