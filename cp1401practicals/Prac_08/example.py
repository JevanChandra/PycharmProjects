"""
longest_place = empty
places = empty list
get place
if place = empty
    display I went nowhere :(
else:
    get place
while place is not empty
    add place to places
    get place
for place in places
    if length of longest_place < length of place
        longest_place = place
    print place
"""
longest_place = ""
places = []
place = input("Place: ").title()
if place == "":
    print("I went nowhere :(")
else:
    while place != "":
        places.append(place)
        place = input("Place: ").title()
    print("On my holiday, I went to: ")
    for place in places:
        if len(longest_place) < len(place):
            longest_place = place
        print(place)
    print(f"The place with the longest name was {longest_place}")
