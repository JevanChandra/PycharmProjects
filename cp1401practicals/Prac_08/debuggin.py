"""CP1401 - Practical 8 - Debugging."""

# Debug program 1 - friends' names
# names = ["Abby", "Jerome", "Olivia", "Monique"]
# print("My friends' names: ")
# for i in range(0, len(names)):
#     print(f"{i + 1}. {names[i]}")
# last_number = len(names) - 1
# print(f"The last name (number {last_number + 1}) is {names[last_number]}")

# Problem(s) for program 1:
# changed from 1 to 0 so that it would display abby
# added a + 1 in print statement, so it wouldn't display a 0 at the start
# added a - 1 in last_number because it is 4 in length but has to be 3 to be called out in the print statement
# added a + 1 in the print last_number to show the correct number

# Fixed code for program 1:
# for i in range(0, len(names)):
# print(f"{i + 1}. {names[i]}")
# last_number = len(names) - 1
# print(f"The last name (number {last_number + 1}) is {names[last_number]}")

# Debug program 2 - title-casing country names
countries = ["australia", "new zeaLAND", "India"]
for i in range(len(countries)):
    countries[i] = countries[i].title()
print(countries)  # country names should be in title-case now

# Problem(s) for program 2:
# list did not use []

# Fixed code for program 2:
# countries = ["australia", "new zeaLAND", "India"]