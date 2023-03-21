"""
4a. Calculate salary for worker level

function main()
    worker_level = check_worker_level()
    salary = find_worker_salary
    display worker_level, salary


function check_worker_level(prompt, low, high)
    print prompt
    get number
    while number < low or number > high
        display error
        get number
    return number


function find_worker_salary(worker_level)
    worker_level * 5000
    return worker_level

"""

# def main():
#     worker_level = check_worker_level("Worker level: ", 1, 10)
#     salary = find_worker_salary(worker_level)
#     print(f"With worker level {worker_level}, your salary is ${salary:,.2f}")
#
#
# def check_worker_level(prompt, low, high):
#     number = int(input(prompt))
#     while number < low or number > high:
#         print("Invalid worker level")
#         number = int(input(prompt))
#     else:
#         return number
#
#
# def find_worker_salary(worker_level):
#     return worker_level * 5000


# main()


"""
4b. Nested Loops


function main()
    get row, column
    create_grid(row, column)

function create_grid(row, column):
    for i in range(row)
        for j in range(column)
            display j
        display 

"""


def main():
    row = int(input("Rows: "))
    column = int(input("Columns: "))
    create_grid(row, column)


def create_grid(row, column):
    for i in range(row):
        for j in range(column):
            print(j, end=" ")
        print()


main()
