"""
get birth_month
while <input is not valid>
     display error message
     get birth_month

if birth_month < 7
    display first half of year
else
    display second half of year

for count from 1 to birth_month
    display count

"""
START = 1
END = 12
FIRST_HALF = 7
MINIMUM_MONTH = 1
MAXIMUM_MONTH = 12

birth_month = int(input("Enter the month number (" + str(MINIMUM_MONTH) + "-" + str(MAXIMUM_MONTH) + "): "))

while birth_month < START or birth_month > END:
    print("Invalid month")
    birth_month = int(input("Enter your birth month: "))

for count in range(START, birth_month + START):
    print(count, end=" ")

if birth_month < FIRST_HALF:
    print("First half of year")
else:
    print("Second half of year")