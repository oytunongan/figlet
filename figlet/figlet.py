import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

if len(sys.argv) < 1 or len(sys.argv) > 3 or len(sys.argv) == 2 or sys.argv[1] != "-f" or not sys.argv[2] in figlet.getFonts():
    print("Invalid Usage")
    sys.exit(1)
if len(sys.argv) == 1:
    type = random.choice(figlet.getFonts())
    figlet.setFont(font=type)
if len(sys.argv) == 3:
    figlet.setFont(font=sys.argv[2])

text = input("Input: ")
print(figlet.renderText(text))