"""
Hex Colours

Estimate: 20 minutes
Actual:   10 minutes
"""

COLOUR_TO_CODE = {"ABSOLUTE ZERO": "#0048ba", "ALIZARIN CRIMSON": "#e32636", "AMETHYST": "#9966cc", "AQUA": "#00ffff",
                  "BITTER LIME": "#bfff00", "BLACK": "#000000", "BLUE": "#0000ff", "BLUEVIOLET": "#8a2be2",
                  "CADIUM RED": "#e30022", "CANARY": "#ffff99"}

for colour in COLOUR_TO_CODE:
    print(f"{COLOUR_TO_CODE[colour]} is {colour}")
colour_input = input("What colour: ").upper()

while colour_input != "":
    if colour_input in COLOUR_TO_CODE:
        print(colour_input, "is", COLOUR_TO_CODE[colour_input])
    else:
        print("Invalid colour")
    colour_input = input("What colour: ").upper()

