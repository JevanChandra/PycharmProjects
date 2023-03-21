def main():
    print("C - Convert Celsius to Fahrenheit\n"
          "F - Convert Fahrenheit to Celsius\n"
          "Q - Quit")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} F")


def convert_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def convert_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


main()
