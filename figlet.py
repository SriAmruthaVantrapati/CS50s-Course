import sys
from pyfiglet import Figlet
import random
figlet=Figlet()
figlet.getFonts()
if len(sys.argv)==1:
    rand=random.choice(figlet.getFonts())
    figlet.setFont(font=rand)
    s=input("Input: ")
    print("Output: ")
    print(figlet.renderText(s))
    sys.exit(0)
elif (len(sys.argv)==3 and sys.argv[2] in figlet.getFonts()) and (sys.argv[1]=="-f" or sys.argv[1]=="--font" in figlet.getFonts()):
    figlet.setFont(font=sys.argv[2])
    s=input("Input: ")
    print("Output: ")
    print(figlet.renderText(s))
    sys.exit(0)
else:
    print("Invalid usage")
    sys.exit(1)
