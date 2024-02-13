from data import load
from control import create

def draw_menu():
    option=input("""
    [c]reate
    [u]pdate
    [d]isplay
    [r]emove 
    [q]uit 
    """
    )
    if option=="c":
       create()
    if option=="d":
        print(load())
    if option=="q":
        print("sorry to see you go...")
        exit()


