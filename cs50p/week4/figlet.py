'''
Figlet text converter

Why:
- pyfiglet converts text into ASCII art using different font styles

How it works:
- Figlet() creates a figlet object with the default font
- setFont(font=f) changes the font to whatever the user passes in
- renderText(text) converts the input text into ASCII art

Command line arguments (sys.argv):
- sys.argv[0] = script name (figlet.py)
- sys.argv[1] = flag, must be -f or --font
- sys.argv[2] = font name e.g. slant, banner, digital
- If wrong flag → sys.exit with error message
- If invalid font → FontNotFound is raised → sys.exit with error message
- If no arguments → renders in default font

Usage:
- python figlet.py              → default font
- python figlet.py -f slant     → slant font
'''

from pyfiglet import Figlet, FontNotFound
import sys

figlet = Figlet()
text = input("Input: ")
if len(sys.argv) == 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        try:
            figlet.setFont(font = sys.argv[2])
            convert = figlet.renderText(text)  
        except FontNotFound:
            sys.exit("Font not found")
    else:
        sys.exit("First argument must be either '-f' or '--font'")
else:
    convert = figlet.renderText(text)
print(convert)
