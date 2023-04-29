"""
Replace the contents of this module docstring with your own details
Name: Jevan Chandra
Date started: 22/4/2023
GitHub URL:
"""
import random

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
    out_file = open('places.csv', 'r')
    places = []
    visited_places = []
    unvisited_places = []

    put_file_in_list(out_file, places)
    # sort_based_on_priority(places)
    separate_the_places(places, unvisited_places, visited_places)

    user_menu_choice = input(">>> ").upper()
    while user_menu_choice != "Q":
        longest_city_letter = get_longest_city_letter(places)
        longest_country_letter = get_longest_country_letter(places)
        unvisited_places_amount = count_amount_of_unvisited_places(unvisited_places)

        if user_menu_choice == "L":
            number_of_places = display_visited_and_unvisited_place(unvisited_places, visited_places,
                                                                   longest_city_letter, longest_country_letter)
            print(f"{number_of_places - 1} places. You still want to visit {unvisited_places_amount} places.")

        elif user_menu_choice == "R":
            check_if_unvisited_list_is_empty(unvisited_places, unvisited_places_amount)

        elif user_menu_choice == "A":
            city, country, priority = error_check_inputs()
            append_new_place(city, country, places, priority, unvisited_places)

        elif user_menu_choice == "M":
            print("M")

        else:
            print("Invalid menu choice")
        print(MENU)
        user_menu_choice = input(">>> ").upper()
    print("End")


def append_new_place(city, country, places, priority, unvisited_places):
    """Adds the new place into unvisited place. """
    new_place = [city, country, priority, "n"]
    places.append(new_place)
    unvisited_places.append(new_place)


def error_check_inputs():
    """This function will check if the input is wrong or not"""
    city = input("Name: ").title()
    while city == "":
        print("Input cannot be blank")
        city = input("Name: ").title()
    country = input("Country: ").title()
    while country == "":
        print("Input cannot be blank")
        country = input("Country: ").title()
    priority = int(input("Priority: "))
    while priority < 1:
        print("Input cannot be lower than 0")
        priority = int(input("Priority: "))
    return city, country, priority


def check_if_unvisited_list_is_empty(unvisited_places, unvisited_places_amount):
    """This function will decide if the unvisited places list is empty. If it is not empty it will recommend a random
    place."""
    if unvisited_places == []:
        print("No places left to visit!")
    else:
        print("Not sure where to visit next?")
        random_number = random.randint(0, unvisited_places_amount - 1)
        print(f"How about... {unvisited_places[random_number][0]} in {unvisited_places[random_number][1]}?")


# def sort_based_on_priority(places):
#     """This function will sort the places list based on its priority"""
#     # TODO
#     for i in range(len(places)):
#         places[i-1][2] = int(places[i-1][2])
#         places.sort(key=sort_key(place), reverse=False)
#     print(places)


def get_longest_country_letter(places):
    """This function will find the longest letter in the countries. We do this to make sure that the list is aligned
    neatly """
    amount_of_places = len(places)
    longest_word = 0
    for i in range(amount_of_places):
        countries_letters = len(places[i][1])
        if longest_word < countries_letters:
            longest_word = countries_letters
    return longest_word


def get_longest_city_letter(places):
    """This function will find the longest letter in the cities. We do this to make sure that the list is aligned
    neatly"""
    amount_of_places = len(places)
    longest_word = 0
    for i in range(amount_of_places):
        cities_letters = len(places[i][0])
        if longest_word < cities_letters:
            longest_word = cities_letters
    return longest_word


def count_amount_of_unvisited_places(unvisited_places):
    """counts the amount of unvisited places"""
    unvisited_places_amount = 0
    for number in unvisited_places:
        unvisited_places_amount += 1
    return unvisited_places_amount


def display_visited_and_unvisited_place(unvisited_places, visited_places, longest_city_letter, longest_country_letter):
    """Will print the visited and unvisited places."""
    num = 1
    for unvisited_place in unvisited_places:
        print(
            f"*{num}. {unvisited_place[0]:{longest_city_letter}} in {unvisited_place[1]:{longest_country_letter}} {unvisited_place[2]:>3}")
        num += 1
    for visited_place in visited_places:
        print(
            f" {num}. {visited_place[0]:{longest_city_letter}} in {visited_place[1]:{longest_country_letter}} {visited_place[2]:>3}")
        num += 1
    return num


def separate_the_places(places, unvisited_places, visited_places):
    """Puts the place into either a visited or unvisited list"""
    for place in places:
        if "n" == place[3]:
            unvisited_places.append(place)
        else:
            visited_places.append(place)


def put_file_in_list(out_file, places):
    """Will transfer the file data into a list"""
    for text in out_file:
        parts = text.strip().split(',')
        places.append(parts)


def count_amount_of_places(in_file, total):
    """Counts the amount of places there are in the file"""
    for i in in_file:
        total += 1
    return total


if __name__ == '__main__':
    main()
