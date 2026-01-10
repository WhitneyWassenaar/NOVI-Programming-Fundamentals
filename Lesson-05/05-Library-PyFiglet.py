# You must install the library in the terminal: pip install pyfiglet
# You must use a venv (virtual environment)

from pyfiglet import Figlet
f = Figlet(font='slant')
print(f.renderText('This is awesome!'))

import pyfiglet
f = pyfiglet.figlet_format("You are awesome!", font="slant")
print(f)