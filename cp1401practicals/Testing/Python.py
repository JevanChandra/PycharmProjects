# # age = int(input("your age: "))
# # while age < 0 or age > 120:
# #     print("invalid age ")
# #     age = int(input("enter your age properly "))
# # if age < 18:
# #     print("you are a minor")
# # else:
# #     print("you are an adult")
#
#
# # age = int(input("age: "))
# # name = input("Name: ")
# #
# # for i in range(0, age):
# #     print(name)
#
# # total_age = 0
# # number = int(input("number of ppl in the room: "))
# #
# # for i in range(number):
# #     age = int(input("Enter Age " + str(i + 1) + ":"))
# #     total_age += age
# #
# # average = total_age / number
# #
# # print(total_age)
# # print(average)
#
# # for i in range(10, 0, -2):
# #     print(i ** 2, end=' ')
# print()
#
#
# cost = 0
# color = input("White or Black? ").lower()
# size = input("For Black: Small = $3, Medium = $4, Large = $5. White coffee costs $1 more no matter what size is "
#              "chosen ").lower()
# while size != "small":
#     if size == "medium":
#         print()
#     elif size == "large":
#         cost == 5
#     else:
#         size = input(
#             "For Black: Small = $3, Medium = $4, Large = $5. White coffee costs $1 more no matter what size is "
#             "chosen ").lower()
# else:
#     cost == 3
# if color != "black":
#     if color == "white":
#         cost += 1
#     else:
#         cost = 6
# print("Price: $", cost, sep="")
#
#
# cost = 0
# color = input("White or Black? ").lower()
# size = input("For Black: Small = $3, Medium = $4, Large = $5. White coffee costs $1 more no matter what size is "
#              "chosen ").lower()
# if color != "black":
#     if color == "white":
#         if size == "small":
#             print("$4")
#         elif size == "medium":
#             print("$5")
#         elif size == "large":
#             print("$6")
#         else:
#             print("Invalid choice")
#             color = input("White or Black? ").lower()
#             size = input(
#                 "For Black: Small = $3, Medium = $4, Large = $5. White coffee costs $1 more no matter what size is "
#                 "chosen ").lower()
#     else:
#         print("Invalid choice")
# else:
#     if size == "small":
#         print("$3")
#     elif size == "medium":
#         print("$4")
#     elif size == "large":
#         print("$5")
#     else:
#         print("Invalid choice")
#         color = input("White or Black? ").lower()
#         size = input(
#             "For Black: Small = $3, Medium = $4, Large = $5. White coffee costs $1 more no matter what size is "
#             "chosen ").lower()
#
# choices = input(
#     "For Black: Small = $3, Medium = $4, Large = $5. White coffee costs $1 more no matter what size is "
#     "chosen ").lower()
#
# while choices != "small":
#     if choices == "medium":
#         print("medium")
#     elif choices == "large":
#         print("large")
#     else:
#         choices = input(
#             "For Black: Small = $3, Medium = $4, Large = $5. White coffee costs $1 more no matter what size is "
#             "chosen ").lower()
# else:
#     print("small")


# RECOMMENDED_SLEEP = 40
# # 8 HOURS every 5 days.  8 * 5 = 40
# night = 0
# total_sleep = 0
# MAXIMUM_DAYS = 5
# MAXIMUM_HOURS = 24
# MINIMUM_HOURS = 0
# print("Sleep Tracker")
# while night != MAXIMUM_DAYS:
#     night += 1
#     entry = float(input(f"Night {night} hours sleep: "))
#     while MINIMUM_HOURS > entry or entry > MAXIMUM_HOURS:
#         print("Invalid number of hours.")
#         entry = float(input(f"Night {night} hours sleep: "))
#     else:
#         total_sleep += entry
# else:
#     sleep_debt = RECOMMENDED_SLEEP - total_sleep
#     print(" ")
#     print("Recommended total sleep is:", RECOMMENDED_SLEEP, sep=" ")
#     print("Your total hours of sleep :", total_sleep, sep=" ")
#     if total_sleep >= RECOMMENDED_SLEEP:
#         print("You are getting enough sleep. Keep it up!")
#     else:
#         print("Your sleep debt over this time is:", sleep_debt, sep=" ")


# def print_grid(rows, columns):
#     for i in range(rows):
#         for j in range(columns):
#             print("*", end=" ")
#         print()
#
#
# print_grid(3, 7)

"""
function main()
worker_level = get_valid_Input("Worker level: ", 0, 10)
salary = get_salary(worker_level)
display worker_level, salary


function get_valid_input(prompt, low, high)
    display prompt
    while number < low or worker number > high
        display error message
        get number
    return number


function get_salary(worker_level)
    return 5000 * worker_level
"""

# x = float(int(5.7))**2
# print(x)

# scores.txt = []
# score = int(input("Score: "))
# while score >= 0:
#     scores.txt.append(score)
#     print(scores.txt)
#     score = int(input("Scores: "))
#
# print("Your highest score is", max(scores.txt))

#
# places = []
# place = input("Place: ")
# while place != "":
#     places.append(place)
#     place = input("Place: ")
#
# for place in places:
#     print(place)

# def main():
#
#     age = get_age()
#
#     print(f"At {age}, you are half-way to {age * 2}")
#
#
# def get_age():
#     x = int(input("Age: "))
#     return x
#
#
# main()\


# hours = []
# for i in range(1, 8):
#     hour = int(input("Hours of study last week: "))
#     hours.append(hour)
#
# total = sum(hours)
# average = total / len(hours)
# minimum_hours = min(hours)
# maximum_hours = max(hours)
#
# print(total, average, minimum_hours, maximum_hours)
# in_file = open("letter")
# for line in in_file:
#     if line[0].isupper():
#         print(line.strip())
# in_file.close()