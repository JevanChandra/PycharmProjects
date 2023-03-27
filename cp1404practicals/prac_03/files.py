""" 1 """
out_file = open('name.txt', 'w')
name = input("What is your name: ")
print(name, file=out_file)
out_file.close()

""" 2 """
out_file = open('name.txt', 'r')
name = out_file.read()
print(f"Your name is {name}")

""" 3 """
out_file = open('numbers.txt', 'w')
for i in range(0, 3):
    number = input("Get number: ")
    print(number, file=out_file)
out_file.close()

total = 0
out_file = open('numbers.txt', 'r')
for i in range(0, 2):
    number = out_file.readline()
    total += int(number)
print(total)

""" 4 """
total_number = 0
out_file = open('numbers.txt', 'r')
is_finished = False
while not is_finished:
    try:
        number = out_file.readline()
        total_number += int(number)
    except ValueError:
        is_finished = True
print(total_number)