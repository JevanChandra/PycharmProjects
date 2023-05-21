from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    chosen_taxi = None
    total_price = 0

    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("Taxi available:")
            for i in range(len(taxis)):
                print(f"{i} - {taxis[i]}")
            current_taxi = int(input("Chosen taxi: "))
            chosen_taxi = get_valid_taxi(current_taxi, chosen_taxi, taxis)

        elif choice == "d":
            if chosen_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                drive_distance = int(input("Drive how far? "))
                taxis[current_taxi].start_fare()  # This is a false alarm
                taxis[current_taxi].drive(drive_distance)
                print(f"Your {taxis[current_taxi].name} trip cost you ${taxis[current_taxi].get_fare():.2f}")
                total_price += taxis[current_taxi].get_fare()

        else:
            print("Invalid option")
        print(f"Bill to date: ${total_price:.2f}")
        print(MENU)
        choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_price}")
    print("Taxis are now:")
    for i in range(len(taxis)):
        print(f"{i} - {taxis[i]}")


def get_valid_taxi(current_taxi, chosen_taxi, taxis):
    if current_taxi < 0 or current_taxi > len(taxis) - 1:
        print("Invalid taxi choice")
        chosen_taxi = None
    else:
        chosen_taxi = current_taxi
    return chosen_taxi


main()
