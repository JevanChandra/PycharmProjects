#
#
# for i in range(1, 21, 2 ):
#     print(i, end=' ')
# print()
#
# for i in range(0, 101, 10):
#     print(i, end=' ')
# print()
#
# for i in range(20, 0, -1):
#     print(i, end=' ')
# print()
#
stars = input("Number of stars: ")
for i in range(0, int(stars)):
    print("*", end='')
print()

for i in range(0, int(stars)):
    for j in range(0, i + 1):
        print("*", end='')
    print()