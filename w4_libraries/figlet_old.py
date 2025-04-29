import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    word = input("Input: ")
    f = random.choice(fonts)
    figlet.setFont(font=f)
elif len(sys.argv) == 3 and ((sys.argv[1] == "-f" or sys.argv[1] == "--f")):
    word = input("Input: ")
    f = font=sys.argv[1] + " " + sys.argv[2]
    print(figlet.renderText(word))
    if f in fonts:
        figlet.setFont(f)
        print(figlet.renderText(word))
else:
    sys.exit("Invalid usage")

#print(sys.argv)
#print(f)


