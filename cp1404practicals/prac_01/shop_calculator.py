total = 0
DISCOUNT_REQUIREMENT = 100
DISCOUNT_PERCENTAGE = 10
ERROR_CHECKING = 0
item_amount = input("Number of items: ")

while int(item_amount) < int(ERROR_CHECKING):
    print("Invalid number of items!")
    item_amount = input("Number of items: ")


for i in range(0, int(item_amount)):
    item_price = input("Price of item: ")
    total += float(item_price)

if total > DISCOUNT_REQUIREMENT:
    discount = total / DISCOUNT_PERCENTAGE
    total_after_discount = total - discount
print(f"Total price for {item_amount} items is ${total_after_discount:.2f}")
