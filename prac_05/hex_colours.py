COLOUR_CODES = {"absolute zero": "#0048ba", "acid green": "#b0bf1a",
                "baker-miller pink": "#ff91af", "baby pink": "#f4c2c2",
                "baby blue": "#89cff0", "bittersweet": "#fe6f5e",
                "black olive": "#3b3c36", "bubble gum": "#ffc1cc",
                "byzantine": "#bd33a4", "cadetBlue1": "#98f5ff",
                "candy apple red": "#ff0800", "carrot orange": "#ed9121", "cerulean frost": "#6d9bc3",
                "daffodil": "#ffff31", "dark lavender": "#734f96"}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ").lower()