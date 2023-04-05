"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months_of_income."""
    incomes = []
    months_of_income = int(input("How many months_of_income? "))

    print_income(incomes, months_of_income)

    print_income_report(incomes, months_of_income)


def print_income(incomes, months_of_income):
    for month in range(1, months_of_income + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)


def print_income_report(incomes, months_of_income):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months_of_income + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()