"""
All Together Now

import random
menu = "(O)rder - (D)rink - (R)andom choice - (Q)uit"
valid_coffee = ["Flat White", "Espresso", "Long Black", "Babyccino"]
user_coffee = empty


function main():
    display intro, menu
    get choice
    while choice != "q":
        if choice == "o":
            display_valid_coffee()
            order = check_if_valid_coffee("? ")
            display order
            grind_beans()
            tamp_grounds()
            insert_protafilter()
            press_shot_button()
            check_order_choice(order)
            user_coffee.append(order)

        elif choice == "d":
            if len(user_coffee) == 0:
                display error message
            else:
                drink_random_coffee()

        elif choice == "r":
            order = get_random_coffee()
            print(f"Here's how to make a/n {valid_coffee[order]}:")
            grind_beans()
            tamp_grounds()
            insert_protafilter()
            press_shot_button()
            check_order_choice(valid_coffee[order])
            user_coffee.append(valid_coffee[order])

        else:
            display error message
        display menu
        get choice

    else:
        display leave message


function get_random_coffee():
    return random.randint(0, len(valid_coffee) - 1)


function drink_random_coffee():
    drink = random.randint(0, len(user_coffee) - 1)
    display drink
    del drink


function display_valid_coffee():
    for i in valid_coffee:
        print(i, end=" - ")


function check_if_valid_coffee(prompt):
    coffee_choice = input(prompt).title()
    if coffee_choice not in valid_coffee:
        print("Invalid order")
        coffee_choice = input(prompt).title()
    else:
        return coffee_choice


function check_order_choice(order):
    if order == valid_coffee[0]:
        display steps
    if order == valid_coffee[1]:
        return order
    if order == valid_coffee[2]:
        display steps
    if order == valid_coffee[3]:
        display steps


function grind_beans():
    display steps


function tamp_grounds():
    display steps


function insert_protafilter():
    display steps


function press_shot_button():
    display steps


main()
"""
import random
menu = "(O)rder - (D)rink - (R)andom choice - (Q)uit"
valid_coffee = ["Flat White", "Espresso", "Long Black", "Babyccino"]
user_coffee = []


def main():
    print("Welcome to the IT@JCU Coffee Shop")
    print(menu)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "o":
            print("Please choose from:")
            display_valid_coffee()
            order = check_if_valid_coffee("? ")
            print(f"Here's how to make a/n {order}:")
            grind_beans()
            tamp_grounds()
            insert_protafilter()
            press_shot_button()
            check_order_choice(order)
            user_coffee.append(order)

        elif choice == "d":
            if len(user_coffee) == 0:
                print("Oh... where's my coffee?")
            else:
                drink_random_coffee()

        elif choice == "r":
            order = get_random_coffee()
            print(f"Here's how to make a/n {valid_coffee[order]}:")
            grind_beans()
            tamp_grounds()
            insert_protafilter()
            press_shot_button()
            check_order_choice(valid_coffee[order])
            user_coffee.append(valid_coffee[order])

        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").lower()

    else:
        print("Thanks for drinking coffee")


def get_random_coffee():
    """Will choose coffee randomly for you"""
    return random.randint(0, len(valid_coffee) - 1)


def drink_random_coffee():
    """Drinks random coffee user has ordered"""
    drink = random.randint(0, len(user_coffee) - 1)
    print(f"Mmmm, nice {user_coffee[drink]}")
    del user_coffee[drink]


def display_valid_coffee():
    for i in valid_coffee:
        print(i, end=" - ")


def check_if_valid_coffee(prompt):
    """Will check if choice is in valid coffee"""
    coffee_choice = input(prompt).title()
    if coffee_choice not in valid_coffee:
        print("Invalid order")
        coffee_choice = input(prompt).title()
    else:
        return coffee_choice


def check_order_choice(order):
    """displays the rest of the steps"""
    if order == valid_coffee[0]:
        print("- Fill jug with milk")
        print("- Steam milk until nice microfoam formed and milk up to temperature")
        print("- Swirl milk gently in jug")
        print("- Pour milk into cup... carefully, artistically :)")
    if order == valid_coffee[1]:
        return order
    if order == valid_coffee[2]:
        print("- Add hot water to cup")
    if order == valid_coffee[3]:
        print("- Add baby")


def grind_beans():
    print("- Insert portafilter into grinder")
    print("- Press grind button to grind beans into portafilter")


def tamp_grounds():
    print("- Distribute grounds\n- Tamp grounds")


def insert_protafilter():
    print("- Insert full portafilter into group head")


def press_shot_button():
    print("- Press shot button to pour espresso into cup")


main()