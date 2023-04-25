MENU = "Menu: \nL - List places \nR - Recommend random place \nA - Add new place \nM - Mark a place as visited \nQ - " \
       "Quit "


def main():
    out_file = open('places.csv', 'r')
    total = 0
    name = "Jevan Chandra"
    print(f"Travel Tracker 1.0 - by {name}")
    total = count_amount_of_places(out_file, total)
    print(f"{total} places loaded from places.csv")
    print(f"{MENU}")
    user_menu_choice = input(">>> ").upper()
    while user_menu_choice != "Q" and user_menu_choice != "0":
        if user_menu_choice == "L" or user_menu_choice == "1":
            places = out_file.readline()
            print(places)
            for i in places:
                print(places)
            print("L")
        elif user_menu_choice == "R" or user_menu_choice == "2":
            print("R")
        elif user_menu_choice == "A" or user_menu_choice == "3":
            print("A")
        elif user_menu_choice == "M" or user_menu_choice == "4":
            print("M")
        else:
            print("Invalid menu choice")
        print(MENU)
        user_menu_choice = input(">>> ").upper()
    print("End")


def count_amount_of_places(in_file, total):
    for i in in_file:
        total += 1
    return total


main()