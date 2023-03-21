"""
CP1401 2022-1 Assignment 2
Market Garden Simulator
Student Name: Jevan Chandra
Date started: 18/09/2022

Pseudocode:
import random
plants = empty

function main():
    days = 0
    total_food = 0
    display introduction sentence, plants, days, total_food, choices, amount of plants
    check_file_option("Would you like to load your plants from plants.txt (Y/n)? ")
    get choice
    while choice != q:
        if choice == w:
            rainfall = get_random_rainfall()
            display rainfall
            check_if_list_empty(rainfall)
            total_food += get_food(rainfall)
            days += 1

        else if choice == d:
            display_plants()

        else if choice == a:
            new_plant = check_if_plant_exists("Enter plant name: ")
            food_cost = plant length
            if total_food < food:
                display new_plant, food_cost, total_food
            else:
                plants.append(new_plant)
                total_food -= food
        else:
            display error message
        display days, food_cost, total_food, choices
        get choice
    else:
        if plants != []:
            print("Your finished with these plants: ")
            display_plants()
            display days, total_food, food_cost
        else:
            display "You finished with no plants"
        check_if_user_save("Would you like to save your plants to plants.txt (Y/n)? ")

main()
"""
import random

plants = []
MAXIMUM_RAINFALL = 128


def main():
    days = 0
    total_food = 0
    int(total_food)
    print("Welcome to my garden. "
          "\nPlants cost and generate food according to their name length (e.g., Sage plants cost 4)."
          "\nYou can buy new plants with the food your garden generates. "
          "\nYou get up to 128 mm of rain per day. Not all plants can survive with less than 32. "
          "\nEnjoy :)")

    check_file_option("Would you like to load your plants from plants.txt (Y/n)? ")
    print(f"You start with these plants: ")
    display_plants()
    print(" ")

    print(f"After {days} days, you have {len(plants)} plants and your total food is {total_food}.\n(W)ait\n("
          "D)isplay plants\n(A)dd new plant\n(Q)uit")
    choice = input("Choose: ").lower()
    while choice != "q":
        if choice == "w":
            rainfall = get_random_rainfall()
            print(f"{rainfall}mm")
            check_if_list_empty(rainfall)
            total_food += get_food(rainfall)
            days += 1

        elif choice == "d":
            display_plants()

        elif choice == "a":
            new_plant = check_if_plant_exists("Enter plant name: ")
            food = len(new_plant)
            if total_food < food:
                print(f"{new_plant} would cost {int(food)} food. With only {total_food}, you can't afford it.")
            else:
                plants.append(new_plant)
                total_food -= food
        #     could not make this section into a function because it wouldn't decrease the total_food amount

        else:
            print("Invalid choice")
        print(f"After {days} days, you have {len(plants)} plants and your total food is {int(total_food)}.\n(W)ait\n("
              "D)isplay plants\n(A)dd new plant\n(Q)uit")
        choice = input("Choose: ").lower()

    else:
        if plants != []:
            print("Your finished with these plants: ")
            display_plants()
            print(
                f"After {days} days, you have {len(plants)} plants and your total food is {int(total_food)}.")
        else:
            print("You finished with no plants")
        check_if_user_save("Would you like to save your plants to plants.txt (Y/n)? ")


def check_if_user_save(prompt):
    """will check if the user saves the file or not"""
    option = input(prompt).lower()
    if option != "n":
        save_file()
    print("Thank you for simulating. Now enjoy some real plants.")


def save_file():
    """will save the file"""
    out_file = open("plants.txt", "w")
    for i in plants:
        print(i, file=out_file)
    out_file.close()
    print("Saved")


def check_if_list_empty(rainfall):
    """will check if the plants list is empty for w section"""
#     did this so program wouldn't crash if user chose w and rainfall was under required rainfall
    if plants != []:
        remove_random_plant(rainfall)


def check_if_plant_exists(prompt):
    """Will check if plant entered is already in the list"""
    plant = input(prompt).title()
    while input == "":
        print("Invalid plant name")
        plant = input(prompt).title()
    else:
        for i in plants:
            while i == plant:
                print(f"You already have a {plant} plant ")
                plant = input(prompt).title()
        return plant


def get_random_rainfall():
    """Gets the random amount of rainfall"""
    return random.randint(0, MAXIMUM_RAINFALL)


def remove_random_plant(rainfall):
    """deletes random plant if it is below required rainfall"""
    rainfall_required = 32
    if rainfall < rainfall_required:
        number = random.randint(0, len(plants) - 1)
        print(f"Sadly, your {plants[number]} plant has died")
        del plants[number]


def get_food(rainfall):
    """Uses the formula for plants to produce food"""
    food = 0
    for i in plants:
        one_third_rainfall = rainfall // 3
        percent = random.randint(one_third_rainfall, rainfall) / MAXIMUM_RAINFALL
        food_produced = percent * len(i) // 1
        print(f"{i.strip()} produced {int(food_produced)}", end=", ")
        food += food_produced
    print(" ")
    return food


def check_file_option(prompt):
    """Checks if the user picks Y or n"""
    choice = input(prompt).lower()
    if choice == "n":
        load_standard_file()
    else:
        load_saved_file()


def load_standard_file():
    """Loads the default plants"""
    default_plants = ["Parsley", "Sage", "Rosemary", "Thyme"]
    for i in default_plants:
        plants.append(i)


def load_saved_file():
    """Loads previous saved file"""
    in_file = open("plants.txt", "r")
    print("Loaded.")
    for i in in_file:
        text = i.strip()
        plants.append(text)
    in_file.close()


def display_plants():
    """shows the plants in list"""
    for i in plants:
        print(i, end=", ")
    print(" ")
    # use for loop so it would not print the brackets


main()