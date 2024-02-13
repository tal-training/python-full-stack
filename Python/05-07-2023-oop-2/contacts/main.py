from data import setup
from ui import draw_menu
from data import Contact

print(Contact().__dict__)

setup()

while True:
    draw_menu()

