#
# age = int(input("Enter your age: "))
#
# if age < 5:
#     print("Baby")
# elif age < 17:
#     print("Child")
# elif age < 65:
#     print("Adult")
# else:
#     print("Old")


# for i in range(3):
#     for j in range(4):
#         print(f"{i} - {j}")

a = 2
b = 1
c = 3
if a > b:
    if b > c:
        answer = c
    else:
        answer = b
elif a > c:
    answer = c
else:
    answer = a

print(answer)