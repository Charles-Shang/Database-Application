from CONSTANTS import app_name
from functionalities import Functionalities
import cmd

class CLI(cmd.Cmd):
    
    prompt = 'dbApp>'
    func_ctrl = Functionalities()

    def parse_args(self, args: str, num_expected: int):
        args = args.strip().split()
        if len(args) != num_expected:
            print(f"Expected {num_expected} {'argument' + 's' if num_expected > 1 else ''}, "
                  f"provided {len(args)}: {args}")
            return None
        else:
            return args

    def do_tm(self, args):
        """Display the top n movies."""
        args = self.parse_args(args, 1)
        if args:
            a = int(args[0])
            print(self.func_ctrl.top_movie_by_ratings(n = a))

    def do_ta(self, args):
        """Display the top n actors along with their best movies."""
        args = self.parse_args(args, 1)
        if args:
            n = int(args[0])  # TODO: Remember to add default values
            print(self.func_ctrl.top_actors_with_best_movie(n))

    def do_tc(self, args):
        """Display the top m movies for n categories."""
        args = self.parse_args(args, 2)
        if args:
            n, m = int(args[0]), int(args[1])
            print(self.func_ctrl.find_top_m_movies_for_n_categories(n, m))

    def do_fs(self, args):
        """Fuzzy search."""
        args = self.parse_args(args, 1)
        if args:
            s = args[0]
            print(self.func_ctrl.fuzz_search(s))

    def do_fsp(self, args):
        """Filters movies by region, year, category, letter then sort movies by sortedBy, where sortedBy"""
        args = self.parse_args(args, 6)
        if args:
            region, year, category, letter, sortedBy, n = args[0], int(args[1]), args[2], args[3], args[4], int(args[5])
            print(self.func_ctrl.movie_filter_and_sort(region, year, category, letter, sortedBy, n))

    def do_g(self,args):
        args = self.parse_args(args, 1)
        if args:
            a = int(args[0])
            print(self.func_ctrl.graph_summary(a))
        
    
    def do_q(self, _):
        """Exit the program."""
        print("Bye!")
        return True

    # do_<command-name>(self, ...args)
    def do_plus(self, args):
        args = self.parse_args(args, 2)
        if args:
            a, b = int(args[0]), int(args[1])
            print(a + b)


if __name__ == "__main__":
    print(f"Welcome to {app_name}!")
    CLI().cmdloop()

