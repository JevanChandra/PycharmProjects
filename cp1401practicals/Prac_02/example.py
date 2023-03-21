"""
get original_price, surcharge_rate
extra_charge = original_price * surcharge_rate
total_price = original_price + extra_charge
display total_price
"""

#Code

original_price= float(input("What is the original price: $"))
surcharge_rate= float(input("What is the surcharge rate(e.g. 15% is 0.15): $"))
extra_charge = original_price * surcharge_rate
total_price = original_price + extra_charge
print("Your total amount is $", total_price, sep="")

