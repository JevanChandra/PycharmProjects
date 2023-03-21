"""
2. Dog Years

function main
    get human_years
    while human_years > 0
        dog_years = convert_to_dog_years
        display dog_years
        get human_years
    else


function convert_to_dog_years
    if human_years <= 2:
            dog_years = human_years * 10.5
        else:
            dog_years = 21 + 4 * (human_years - 2)
"""


def main():
    human_years = int(input("human years: "))
    while human_years > 0:
        dog_years = convert_to_dog_years(human_years)
        print(dog_years)
        human_years = int(input("human years: "))


def convert_to_dog_years(human_years):
    if human_years <= 2:
        return human_years * 10.5
    else:
        return 21 + 4 * (human_years - 2)


main()