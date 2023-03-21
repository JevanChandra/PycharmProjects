# 1. Tax
"""
display Python Party Tax Program - Where tax is a Party
get income
If income < 100
    total_tax = income * 0
else if income < 1000
    total_tax = income * 0.05
else
    total_tax = income * 0.1

take_home_pay = income - total_tax

display Income
display total_tax
display take_home_pay
"""

# TAX_RATE_LOW = 0.05  # 5%
# TAX_RATE_HIGH = 0.1  # 10%
# TAX_THRESHOLD_LOW = 100
# TAX_THRESHOLD_HIGH = 1000
#
# print("Python Party Tax Program - Where Tax is a Party")
# income = float(input("Income: $"))
# if income < TAX_THRESHOLD_LOW:
#     total_tax = 0
# elif income < TAX_THRESHOLD_HIGH:
#     total_tax = TAX_RATE_LOW
# else:
#     total_tax = TAX_RATE_HIGH
#
# take_home_pay = income - total_tax
#
# print("Total tax is: $", total_tax, sep="")
# print("Take home pay is: $", take_home_pay, sep="")


# 2. Car Insurance
"""
get age
if age < 18
    display "Hire refused"
else if age < 25 
    display "Insurance required"
else
    display "Insurance not required"
"""

# HIRE_REFUSED = 18
# INSURANCE_REQUIRED = 25
#
# age = input("Age: ")
# if age < HIRE_REFUSED:
#     print("Hire refused")
# elif age < INSURANCE_REQUIRED:
#     print("Insurance required")
# else:
#     print("Insurance not required")


# 3. Simple Password Checker
"""
get password
If password == "PASSWORD"
    display "Access granted"
else
    display "Access denied"
"""

# PASSWORD = "123456"
#
# password = input("Enter password: ")
# if password == PASSWORD:
#     print("Access granted")
# else:
#     print("Access denied")


# 4. Dog Years
"""
get age_in_human_years
If age_in_human_years < 2 
    age_in_dog_years = age_in_human_years * 10.5
else
    age_after_deduction = age_in_human_years - 2
    age_in_dog_years_4 = age_after_deduction * 4
    age_in_dog_years_10.5 = 2 * 10.5
    age_in_dog_years = age_in_dog_years_10.5 + age_in_dog_years_4
display age_in_dog_years
"""

# NUMBER = 2
# AGE_OF_FIRST_TWO_YEARS = 21
# (DOG_AGE_CONVERSION_IN_FIRST_TWO_YEARS) = 10.5
# age_in_human_years = int(input("Age in human years: "))
# if age_in_human_years < NUMBER:
#     age_in_dog_years = age_in_human_years * DOG_AGE_CONVERSION_IN_FIRST_TWO_YEARS
# else:
#     age_after_deduction = age_in_human_years - NUMBER
#     age_in_dog_years_4 = age_after_deduction * 4
#
#     age_in_dog_years = AGE_OF_FIRST_TWO_YEARS + age_in_dog_years_4
#
# print("Age in dog years is ", age_in_dog_years, sep="")


# 5. Rock of Ages
"""
get age
If age < 0 or age > 120
    display "Invalid age"
else if age < 20
    display "Congrats you are young"
else if age < 60
    display " Congrats you are below 60"
else if age < 100
    display "Congrats you are old"
else
    display "Wow you are very old"
"""

# MINIMUM = 0
# MAXIMUM = 120
# YOUNG = 20
# MIDDLE_AGED = 60
# OLD = 100
#
# age = int(input("Your age: "))
# if age < MINIMUM or age > MAXIMUM:
#     print("Invalid age")
# elif age < YOUNG:
#     print("Congrats you are young")
# elif age < MIDDLE_AGED:
#     print(" Congrats you are below 60")
# elif age < OLD:
#     print("Congrats you are old")
# else:
#     print("Wow you are very old")


# 6. Speeding Fines
"""
get speed, speed_limit
result = speed - speed_limit
if result < 0
    display
    Penalty_amount = 0
    Demerit points = 0
    
else if result < 13
    display
    Penalty_amount = $177
    Demerit points = 1
    
else if result < 20
    display
    Penalty_amount = $266
    Demerit points = 3

else if result < 30
    display
    Penalty_amount = $444
    Demerit points = 4
    
else if result < 40
    display
    Penalty_amount = $622
    Demerit points = 6 
    
else
    display 
    Penalty_amount = $1245
    Demerit points = 8 
"""

LIMIT_LOWEST = 0
LIMIT_LOW = 13
LIMIT_MEDIUM = 20
LIMIT_HIGH = 30
LIMIT_HIGHEST = 40

speed = int(input("What is the speed(kilometre/hour): "))
speed_limit = int(input("What is the speed_limit(kilometre/hour): "))
result = speed - speed_limit

if result < LIMIT_LOWEST:
    print("Penalty_amount = $0")
    print("Demerit points = 0")

elif result < LIMIT_LOW:
    print("Penalty_amount = $177")
    print("Demerit points = 1")

elif result < LIMIT_MEDIUM:
    print("Penalty_amount = $226")
    print("Demerit points = 3")

elif result < LIMIT_HIGH:
    print("Penalty_amount = $444")
    print("Demerit points = 4")

elif result < LIMIT_HIGHEST:
    print("Penalty_amount = $622")
    print("Demerit points = 6")

else:
    print("Penalty_amount = $1245")
    print("Demerit points = 8")
