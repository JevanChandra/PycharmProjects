"""
Game, Set, Match

Estimate: 40 minutes
Actual  : 53 minutes
"""
with open('wimbledon.csv', "r", encoding="utf-8-sig") as in_file:
    winners = {}
    country_winners = []
    skip_first_row = in_file.readline()
    text = in_file.readlines()

    for word in text:
        name = word.split(",")[2]
        if name in winners:
            winners[name] += 1
        else:
            winners[name] = 1
        country = word.split(",")[1]
        if country not in country_winners:
            country_winners.append(country)

    print("Wimbledon Champions: ")
    for winner in winners.items():
        print(f"{winner[0]} {winner[1]}")
    print()

    country_winners.sort()
    print(f"These {len(country_winners)} countries have won Wimbledon: ")
    print(", ".join(country_winners))