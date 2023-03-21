"""CP1401 - Practical 10 - Debugging.
Explain the problems (not the solution, not the style issues):
Program crashed when the player won money
...
Describe your debugging process:
Played the game a couple of times until a crash occurs.
Then read the reason why it crashed
fix the issue
...
Fix the code in-place below
There was no return in these two if statements so the program was confused.
    if choice == "C" and risk_chance <= CONSERVATIVE_CHANCE:
        result = (amount_to_risk * (CONSERVATIVE_REWARD / 100))
        print(f"Congratulations! You earned ${result:.2f}")
        return result
    elif choice == "A" and risk_chance <= AGGRESSIVE_CHANCE:
        result = (amount_to_risk * (AGGRESSIVE_REWARD / 100))
        print(f"Congratulations! You earned ${result:.2f}")
        return result
"""
import random

VALID_CHOICES = 'AC'
CONSERVATIVE_CHANCE = 40
CONSERVATIVE_REWARD = 50
AGGRESSIVE_CHANCE = 10
AGGRESSIVE_REWARD = 80


def main():
    money = 100
    print("Welcome to the futility of gambling!")
    print("You start with a balance of $100.")
    while money > 0:
        result = play(money)
        money = money + result
        print(f"Your new balance is ${money}")
    print("You lost :)")


def get_valid_amount(balance, amount):
    while amount < 0 or amount > balance:
        print("Invalid amount")
        amount = int(input("Enter amount to play: "))
    return amount


def play(balance):
    """Calculate and display whether win or lose based on chance."""
    amount = int(input("Enter amount to play: "))
    amount_to_risk = get_valid_amount(balance, amount)
    choice = 'x'
    while choice not in VALID_CHOICES:
        choice = input("(C)onservative, (A)ggressive: ").upper()
        if choice not in VALID_CHOICES:
            print("Invalid choice")
    risk_chance = random.randint(0, 101)
    if choice == "C" and risk_chance <= CONSERVATIVE_CHANCE:
        result = (amount_to_risk * (CONSERVATIVE_REWARD / 100))
        print(f"Congratulations! You earned ${result:.2f}")
        return result
    elif choice == "A" and risk_chance <= AGGRESSIVE_CHANCE:
        result = (amount_to_risk * (AGGRESSIVE_REWARD / 100))
        print(f"Congratulations! You earned ${result:.2f}")
        return result
    else:
        result = -amount_to_risk
        print(f"You lost ${amount_to_risk:.2f}")
        return result


main()
