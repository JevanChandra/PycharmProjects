password = input("Enter password: ")

while len(password) < 5:
    print("Your password does not reach the minimum length. "
          "Please try again")
    password = input("Enter password: ")
else:
    for i in range(0, len(password)):
        print("*", end='')

