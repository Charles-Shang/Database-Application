from CONSTANTS import app_name
from functionalities import Functionalities


def pprint(content, length=50, char='='):
    print(f" {content} ".center(length, char))


def print_menu():
    padding = 40
    pprint("Menu", padding, '-')
    pprint("Top movies: tm", padding, ' ')
    pprint("Top actors with best movie: ta", padding, ' ')
    pprint("Top categories with top movies: tc", padding, ' ')
    pprint("Fuzzy Search: fs", padding, ' ')


def start_app():
    func_ctrl = Functionalities()
    pprint(f"Welcome to {app_name}")
    print("Top 5 movies")
    print(func_ctrl.top_movie_by_ratings(5))
    print("Top 5 categories with best movie")
    print(func_ctrl.find_top_m_movies_for_n_categories(5, 1))

    while True:
        print_menu()
        args = input("Enter an option: ").split()
        cmd = args[0]
        if cmd == 'tm':
            n = int(args[1])
            print(func_ctrl.top_movie_by_ratings(n))
        elif cmd == 'ta':
            n = int(args[1])
            print(func_ctrl.top_actors_with_best_movie(n))
        elif cmd == 'tc':
            n, m = int(args[1]), int(args[2])
            print(func_ctrl.find_top_m_movies_for_n_categories(n, m))
        elif cmd == 'fs':
            key_word = str(args[1])
            print(func_ctrl.fuzz_search(key_word))
        elif cmd == 'g':
            print(func_ctrl.graph_summary())
        elif cmd == "q":
            print("Bye!")
            break
        else:
            print("Wrong option, retry.")


start_app()
