from CONSTANTS import app_name
from functionalities import Functionalities
import cmd


class CLI(cmd.Cmd):

    prompt = 'dbApp> '
    func_ctrl = Functionalities()

    def do_tm(self, n: int):
        """Display the top n movies."""
        print(CLI.func_ctrl.top_movie_by_ratings(n))

    def do_ta(self, n: int):
        """Display the top n actors along with their best movies."""
        n = 5 if not n else int(n)
        print(CLI.func_ctrl.top_actors_with_best_movie(n))

    def do_tc(self, n: int, m: int):
        """Display the top m movies for n categories."""
        print(CLI.func_ctrl.find_top_m_movies_for_n_categories(n, m))

    def do_fs(self, s: str):
        """Fuzzy search."""
        print(CLI.func_ctrl.fuzz_search(s))

    def do_q(self, _):
        """Exit the program."""
        print("Bye!")
        return True


if __name__ == "__main__":
    print(f"Welcome to {app_name}!")
    CLI().cmdloop()

