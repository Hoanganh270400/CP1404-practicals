COLOUR_DICT = dict(red = "#FF00", blue = "#0000FF", black = "#000000", white = "#FFFFFF")
print(COLOUR_DICT)
color = input("Enter the name of the color: ").lower()
while color != "":
    if color in COLOUR_DICT:
        print(color, "is", COLOUR_DICT[color])
    else:
        print("Invalid color name")
    color = input("Enter the name of the color: ").lower()