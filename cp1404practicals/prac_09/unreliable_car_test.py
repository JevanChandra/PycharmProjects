from unreliable_car import UnreliableCar


def main():
    my_car = UnreliableCar("Prius 1", 100, 60)
    my_car.drive(40)
    print(my_car)


main()