from CONSTANTS import app_name
from functionalities import Functionalities

def pprint(content, len = 50, char = '='):
    print(f" {content} ".center(len, char))

def printMenu():
    pprint("Menu", 25, '-')
    pprint("Top n movies: tn", 25, ' ')

def start_app():
    funcCtrl = Functionalities()
    pprint(f"Welcome to {app_name}")
    print("Top 5 movies")
    
    
    while(1):
        printMenu()
        cmd = input("Enter an option: ")
        if (cmd[:2] == "tn"):
            print(funcCtrl.top_movie_by_ratings(int(cmd[3:])))
        elif (cmd == "q"):
            print("Bye!")
            break
        else:
            print("Wrong option, retry.")

start_app()