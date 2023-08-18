import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()
#print(fonts)

#print(len(sys.argv))
#print(sys.argv)

if len(sys.argv) == 1:
    f = random.choice(fonts)
    figlet.setFont(font=f)
    text = input("Input: ")
    print(figlet.renderText(text))
elif len(sys.argv) == 2 or len(sys.argv) > 3:
    sys.exit("Invalid usage")
elif (sys.argv[1] == "-f" or sys.argv[2] == "--font") and len(sys.argv) == 3 and sys.argv[2] in fonts:
    f = sys.argv[2]
    figlet.setFont(font=f)
    text = input("Input: ")
    print(figlet.renderText(text))
else:
    sys.exit("Invalid usage")
#print(f)
