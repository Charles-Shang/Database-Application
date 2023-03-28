from CONSTANTS import app_name, app_title
from functionalities import Functionalities
import cmd
from textFormatter import Formatter

menus = [
    ["Search a key word", ["search", "<movie/celebrity>"]],
    ["Top movies", ["tm", "<n>"]],
    ["Top actors", ["ta", "<n>"]],
    ["Top categories with movies", ["tc", "<n>", "<m>"]],
    ["Functional Filtering", ["fsp", "<region>", "<year>", "<category>", "<letter>", "<sortedBy>", "<n>"]],
    ["Home page", ["home"]],
    ["Command example", ["help", "<option>"]],
    ["Quit", ["q"]]
]

formatTool = Formatter()

class CLI(cmd.Cmd):

    base_location = "Home"
    location = [base_location]
    intro = app_title + f"Hello! Welcome to {app_name}! This is a database of information related to movie information query and organization."
    prompt = formatTool.underline(location[-1], "pink") + formatTool.yellow("> ")
    func_ctrl = Functionalities()

    def postcmd(self, stop: bool, line: str) -> bool:
        if len(self.location) == 1:
            self.prompt = formatTool.underline(self.location[-1], "pink") + formatTool.yellow("> ")
        else:
            self.prompt = formatTool.yellow("/".join(self.location[:-1]) + "/") + formatTool.underline(self.location[-1], "pink") + formatTool.yellow("> ")
        return super().postcmd(stop, line)

    def do_menu(self, args = None):
        """Generate a menu with a list of available options."""
        print(f"[{formatTool.green('?')}] What can I do for you? ({formatTool.underline('Type')} one of the following options)")
        for index, (option_description, syntax) in enumerate(menus):
            print(f"  {'  ' + str(index+1) if index < 9 else index+1}. {option_description}: {formatTool.pink(syntax[0])}", end="")
            if len(syntax) > 1:
                print(" " + formatTool.italic(" ".join(syntax[1:]), "yellow"), end='')
            print()

    def do_home(self, args):
        """Go back to the Home page."""
        print(self.intro)
        self.do_menu()

    def parse_args(self, args: str, num_expected: int):
        args = args.strip().split()
        if len(args) != num_expected:
            print(f"Expected {num_expected} {'argument' + 's' if num_expected > 1 else ''}, "
                  f"provided {len(args)}: {args}")
            print(formatTool.red("Please try again") + " or type \"" + formatTool.pink("menu") + "\" for help.")
            return None
        else:
            return args

    def do_tm(self, args):
        """Display the top n movies."""
        args = self.parse_args(args, 1)
        if args:
            n = int(args[0])
            print(self.func_ctrl.top_movie_by_ratings(n))

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

    def do_search(self, args):
        """Search movie which contains the keyword in any of author name, director name or movie name."""
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
            print(self.func_ctrl.graph_summary(n = a))

    def do_q(self, _):
        """Exit the program."""
        print(f"Thank you for using {app_name}! Bye!")
        return True

    # do_<command-name>(self, ...args)
    def do_plus(self, args):
        args = self.parse_args(args, 2)
        if args:
            a, b = int(args[0]), int(args[1])
            print(a + b)


if __name__ == "__main__":
    CLI().cmdloop()

