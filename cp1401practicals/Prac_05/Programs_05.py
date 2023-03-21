# 1. Percentage change
"""
get original, change

addition = original * change
result = addition + original

display original
display the_change
display result
"""

# original = float(input("Original: "))
# change = float(input("The Change: "))
#
# addition = original * change
# result = addition + original
#
# print("Original:", original, end=", ")
# print("Change:", change, end=", ")
# print("Result:", result, end=", ")


# 2. Time of day
"""
get time, action
if time < 12
    time_of_day = before_noon
else: 
    time_of_day = after_noon

if action = coming
    display hi
else: 
    display bye
"""
# NOON = 12
# time = int(input("Time: "))
# action = str(input("Are you coming or going? "))
# if time < NOON:
#     print("It is before noon", end=" and ")
# else:
#     print("It is after noon", end=" and ")
#
# if action == "coming":
#     print("you are coming. Hi!")
# else:
#     print("you are going. Bye!")


# 3. Coffee orders
"""
get color, size

if size = small
    display cost
elif size = medium
    display cost
else
    display cost

if color is not black
    if color is white
        cost =+ 1
    else 
        cost = 6
"""

# cost = 0
# color = input("White or Black? ").lower()
# size = input("For Black: Small = $3, Medium = $4, Large = $5. White coffee costs $1 more no matter what size is "
#              "chosen ").lower()
#
# if size == "small":
#     cost = 3
# elif size == "medium":
#     cost = 4
# else:
#     cost = 5
# if color != "black":
#     if color == "white":
#         cost += 1
#     else:
#         cost = 6
#
# print("Price: $", cost, sep="")


# 4. Coffee orders with error-checking
"""
while color is not black
    if color is white
        if size is small
            display price
        elif size is medium
            display price
        elif size is large
            display price
        else 
            display invalid choice
            get choice
else
    if size is small
            display price
        elif size is medium
            display price
        elif size is large
            display price
        else 
            display invalid choice
            get choice

"""

cost = 0
color = input("White or Black? ").lower()
size = input("For Black: Small = $3, Medium = $4, Large = $5. White coffee costs $1 more no matter what size is "
             "chosen ").lower()
while color != "black":
    if color == "white":
        while size != "small":
            if size == "medium":
                print("$5")
                input("Thanks :)")
            if size == "large":
                print("$6")
                input("Thanks :)")
            else:
                print("Invalid choice")
                color = input("White or Black? ").lower()
                size = input(
                    "For Black: Small = $3, Medium = $4, Large = $5. White coffee costs $1 more no matter what size is "
                    "chosen ").lower()
        else:
            print("$4")
            input("Thanks :)")
    else:
        print("Invalid choice")
        color = input("White or Black? ").lower()
        size = input(
            "For Black: Small = $3, Medium = $4, Large = $5. White coffee costs $1 more no matter what size is "
            "chosen ").lower()
else:
    while size != "small":
        if size == "medium":
            print("$4")
            input("Thanks :)")
        elif size == "large":
            print("$5")
            input("Thanks :)")
        else:
            print("Invalid choice")
            color = input("White or Black? ").lower()
            size = input(
                "For Black: Small = $3, Medium = $4, Large = $5. White coffee costs $1 more no matter what size is "
                "chosen ").lower()
    else:
        print("$3")
        input("Thanks :)")

# 5. Accumulation
"""
get low_value, high_value
for i in range low_value, high_value
    display i    
    display totals
"""

# total = 0
# low_value = int(input("Low Value: "))
# high_value = int(input("High Value: "))
# for i in range(low_value, high_value + 1):
#     print(i, end=" ")
#     total += i
#
# print("totals:", total, )
