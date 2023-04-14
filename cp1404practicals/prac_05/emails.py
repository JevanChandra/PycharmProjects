"""
Emails

Estimate: 30 minutes
Actual  : 46 minutes
"""

email_dictionary = {}

email = input("Email: ")
while email != "":
    email_name = " ".join(email.split("@")[0].split(".")).title()
    option = input(f"Is your name {email_name}? (Y/n) ").lower()
    if option != "y" and option != "":
        correct_name = input("Name: ")
    else:
        correct_name = email_name
    email_dictionary[correct_name] = email
    email = input("Email: ")

for email in email_dictionary:
    print(f"{email_dictionary[email]} ({email_dictionary[email]})")