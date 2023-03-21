# 1. Discount Price

"""
get original_price
discount = original_price * 0.2
new_price = original_price – discount
print new_price
"""

# DISCOUNT_VALUE = 0.2
# original_price = float(input("what is the price: $"))
# discount = original_price * DISCOUNT_VALUE
# new_price = original_price - discount
# print("Your total is: $", new_price, sep="")


# 2. Kilometer to Miles

"""
get distance_in_kilometres
distance_in_miles = distance_in_kilometres * 0.621371
display distance_in_miles
"""

# CONVERSION_RATE = 0.621371
# distance_in_kilometres = float(input("What is the distance in kilometres: "))
# distance_in_miles = distance_in_kilometres * CONVERSION_RATE
# print("The distance in miles is: ",distance_in_miles, sep="")


# 3. Holiday Cost

"""
get daily_food_cost, daily_activities_cost, number_of_days
total_cost = (daily_food_cost + daily_activities_cost + 75) * number_of_days
display total_cost
"""

# HOTEL_COST = 75
# daily_food_cost = float(input("Daily food cost: $"))
# daily_activities_cost = float(input("Daily activities cost: $"))
# number_of_days = int(input("Number of days: "))
# total_cost = (daily_food_cost + daily_activities_cost + HOTEL_COST) * number_of_days
# print("The trip will cost $", total_cost, sep="")


#  4. Deep Sleep Calculation

"""
get total_sleep_in_seconds, deep_sleep_in_seconds
deep_sleep_in_minutes = deep_sleep_in_seconds // 60
deep_sleep_remainder_in_seconds = deep_sleep_in_seconds % 60
total_sleep_in_minutes = total_sleep_in_seconds // 60
total_sleep_remainder_in_seconds = total_sleep_in_seconds % 60
percentage = (deep_sleep_in_seconds / total_sleep_in_seconds) * 100
display deep_sleep_in_minutes, deep_sleep_remainder_in_seconds
display total_sleep_in_minutes, total_sleep_remainder_in_seconds 
display percentage
"""

MINUTE_CONVERSION = 60
PERCENTAGE_CONVERSION = 100
total_sleep_in_seconds = int(input("Total sleep in seconds : "))
deep_sleep_in_seconds = int(input("Deep sleep in seconds : "))

deep_sleep_in_minutes = deep_sleep_in_seconds // MINUTE_CONVERSION
deep_sleep_remainder_in_seconds = deep_sleep_in_seconds % MINUTE_CONVERSION
total_sleep_in_minutes = total_sleep_in_seconds // MINUTE_CONVERSION
total_sleep_remainder_in_seconds = total_sleep_in_seconds % MINUTE_CONVERSION
percentage = (deep_sleep_in_seconds / total_sleep_in_seconds) * PERCENTAGE_CONVERSION
print("")
print("Deep sleep : ", deep_sleep_in_minutes, "m ", deep_sleep_remainder_in_seconds, "s", sep="")
print("Total sleep : ", total_sleep_in_minutes, "m ", total_sleep_remainder_in_seconds, "s", sep="")
print("Percentage : ", percentage, "%", sep="")




