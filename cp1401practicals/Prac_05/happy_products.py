"""
display choices
get user_choice, price

while user choice is not quit
    if choice is instructions
        display instructions
        get user_choice
    elif choice is calculate
        while product amount < 0
            display invalid
            get user_choice
        else
            if choice < 6
                display price
                get user_choice
            else
                display price after discount
                get user_choice
    else
        display invalid choice
        get user_choice
else
    display quit
"""
INVALID = 0
NO_DISCOUNT = 6
DISCOUNT = 0.1
print("Menu:")
print("(I)nstructions")
print("(C)alculate")
print("(Q)uit")
choice = input("Choice: ").lower()

while choice != "q":
    if choice == "i":
        print("Enter the number of products you want to buy and your chosen price.")
        print("If you buy 0-5 items, they're full price, over 5 items and each one is 10% off!")
        print("Menu:")
        print("(I)nstructions")
        print("(C)alculate")
        print("(Q)uit")
        choice = input("Choice: ").lower()
    elif choice == "c":
        product_amount = int(input("Number of products: "))
        while product_amount < INVALID:
            print("Invalid input")
            product_amount = int(input("Number of products: "))
        else:
            price = float(input("Price: "))
            total = price * product_amount
            if product_amount < NO_DISCOUNT:
                print(product_amount, "x $", f'{price:,.2f}', "products = $", f'{total_after_discount:,.2f}')
                print("Menu:")
                print("(I)nstructions")
                print("(C)alculate")
                print("(Q)uit")
                choice = input("Choice: ").lower()
            else:
                discount_percentage = product_amount * DISCOUNT
                discount = discount_percentage * price
                total_after_discount = total - discount
                print(product_amount, "x $", f'{price:,.2f}', "products = $", f'{total_after_discount:,.2f}')
                print("Menu:")
                print("(I)nstructions")
                print("(C)alculate")
                print("(Q)uit")
                choice = input("Choice: ").lower()
    else:
        print("Invalid choice")
        print("Menu:")
        print("(I)nstructions")
        print("(C)alculate")
        print("(Q)uit")
        choice = input("Choice: ").lower()
else:
    print("Farewell")