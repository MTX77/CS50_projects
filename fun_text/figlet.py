from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 1:
    f_number = random.randrange(0, len(figlet.getFonts()))
    list = figlet.getFonts()
    figlet.setFont(font=list[f_number])
    name = input("Input: ")
    print(figlet.renderText(name))

elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in figlet.getFonts():
        figlet.setFont(font=sys.argv[2])
        name = input("Input: ")
        print(figlet.renderText(name))
    else:
        print("Invalid usage")
        sys.exit(1)
else:
    print("Invalid usage")
    sys.exit(1)

print("Provide two command-line arguments: the first should be -f or --font and the second should be the name of a font.\nNo arguments = random font.")

