def main():
    password = get_password()
    print_password(password)


def print_password(password):
    for i in range(0, len(password)):
        print("*", end='')


def get_password():
    password = input("Enter password: ")
    while len(password) < 5:
        print("Your password does not reach the minimum length. "
              "Please try again")
        password = input("Enter password: ")
    return password


main()

