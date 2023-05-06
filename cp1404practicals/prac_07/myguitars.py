import csv
from prac_06_guitar import Guitar


def main():
    guitars = []
    in_file = open('guitars.csv', 'r', newline='')
    data = csv.reader(in_file)
    put_data_in_file(data, guitars, in_file)
    guitars.sort()
    print("This is the guitar list:")
    for guitar in guitars:
        print(guitar)


def put_data_in_file(data, guitars, in_file):
    for name, year, cost in data:
        guitars.append(Guitar(name, int(year), float(cost)))
    in_file.close()


main()