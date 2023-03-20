"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

ERROR = 0
LIMIT = 1000
MIN_BONUS = 10
MAX_BONUS = 15/100

sales = float(input("Enter sales: $"))
while sales >= ERROR:
    if sales < LIMIT:
        print(f"Your bonus is {int(sales/MIN_BONUS)}")
    else:
        print(f"Your bonus is {int(sales*MAX_BONUS)}")
    sales = float(input("Enter sales: $"))
else:
    print("Invalid please try again")
    sales = float(input("Enter sales: $"))