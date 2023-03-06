from CONSTANTS import app_name
from functionalities import Functionalities


def pprint(content, length=50, char='='):
    print(f" {content} ".center(length, char))


def print_menu():
    pprint("Menu", 25, '-')
    pprint("Top n movies: tn", 25, ' ')
    pprint("Fuzzy Search: fs", 25, ' ')


def start_app():
    func_ctrl = Functionalities()
    pprint(f"Welcome to {app_name}")
    print("Top 5 movies")

    while True:
        print_menu()
        cmd = input("Enter an option: ")
        if cmd[:2] == "tn":
            print(func_ctrl.top_movie_by_ratings(int(cmd[3:])))
        elif cmd[:2] == 'fs':
            print(func_ctrl.fuzz_search(str(cmd[3:])))
        elif cmd == "q":
            print("Bye!")
            break
        else:
            print("Wrong option, retry.")


start_app()
