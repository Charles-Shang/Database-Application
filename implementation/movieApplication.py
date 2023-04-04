from CONSTANTS import (
    app_name,
    app_title,
    celebrity_template,
    actor_template,
    director_template,
    movie_template,
    rating_template,
    menus,
    menus_user,
    menus_employee,
)
from functionalities import Functionalities
import cmd
import textFormatter as tf
from User import User
import util
from accessCtrl import Access
from graphCtrl import Graph


def login_required(cur_user: User):
    def inner(func):
        def wrapper(*args, **kwargs):
            if cur_user.is_logged_in():
                return func(*args, **kwargs)
            else:
                print(f"""[{tf.green("~")}]: User is currently not logged in.""")

        return wrapper

    return inner


def Standard_required(cur_user: User):
    def inner(func):
        def wrapper(*args):
            if cur_user.user_type in ["Standard", "Premium", "Employee"]:
                return func(*args)
            else:
                print(
                    f"""[{tf.pink("!!!")}]: User is not permitted to use this function. Try upgrade to Standard account."""
                )

        return wrapper

    return inner


def Premium_required(cur_user: User):
    def inner(func):
        def wrapper(*args, **kwargs):
            if cur_user.user_type in ["Premium", "Employee"]:
                return func(*args, **kwargs)
            else:
                print(
                    f"""[{tf.pink("!!!")}]: User is not permitted to use this function. Try upgrade to Premium account."""
                )

        return wrapper

    return inner


def Employee_required(cur_user: User):
    def inner(func):
        def wrapper(*args):
            if cur_user.user_type in ["Employee"]:
                return func(*args)
            else:
                print(
                    f"""[{tf.pink("!!!")}]: User is not permitted to use this function."""
                )

        return wrapper

    return inner


def User_required(cur_user: User):
    def inner(func):
        def wrapper(*args):
            if cur_user.user_type not in ["Employee"]:
                return func(*args)
            else:
                print(
                    f"""[{tf.pink("!!!")}]: Employee is not permitted to use this function."""
                )

        return wrapper

    return inner


def Employee_Permission_required(func_ctrl, cur_user: User, action: str, tables: list):
    def inner(func):
        def wrapper(*args):
            if cur_user.user_type in [
                "Standard",
                "Premium",
            ] or func_ctrl.employee_permission_authentication(
                cur_user.user_id, action, tables
            ):
                return func(*args)
            else:
                print(
                    f"""[{tf.red("Warning")}]: Employee is not permitted to use this function."""
                )

        return wrapper

    return inner


class CLI(cmd.Cmd):

    base_location = "Home"
    location = [base_location]
    intro = (
        app_title
        + f"Hello! Welcome to {app_name}! This is a database of information related to movie information query and organization."
    )
    prompt = tf.underline(location[-1], "pink") + tf.yellow("> ")
    func_ctrl = Functionalities()
    cur_user = User()
    acc_ctrl = Access()
    graph_ctrl = Graph()

    def postcmd(self, stop: bool, line: str) -> bool:
        if len(self.location) == 1:
            self.prompt = tf.underline(self.location[-1], "pink") + tf.yellow("> ")
        else:
            self.prompt = (
                tf.yellow("/".join(self.location[:-1]) + "/")
                + tf.underline(self.location[-1], "pink")
                + tf.yellow("> ")
            )
        return super().postcmd(stop, line)

    def do_menu(self, args=None):
        """Generate a menu with a list of available options."""
        print(
            f"[{tf.green('?')}] What can I do for you? ({tf.underline('Type')} one of the following options)"
        )

        chosen_menu = menus
        if self.cur_user.user_type == "Employee":
            chosen_menu = menus_employee
        elif self.cur_user.user_type != "Visitor":
            chosen_menu = menus_user

        for index, (option_description, syntax) in enumerate(chosen_menu):
            print(
                f"  {(' ' + str(index+1)) if index < 9 else index+1}. {option_description}: {tf.pink(syntax[0])}",
                end="",
            )
            if len(syntax) > 1:
                print(" " + tf.italic(" ".join(syntax[1:]), "yellow"), end="")
            print()

    def do_home(self, args):
        """Go back to the Home page."""
        print(self.intro)
        self.do_menu()

    def parse_args(self, args: str, num_expected: int):
        args = args.strip().split()
        if len(args) != num_expected:
            print(
                f"Expected {num_expected} 'argument' + {'s' if num_expected > 1 else ''}, "
                f"provided {len(args)}: {args}."
            )
            print(
                tf.red("Please try again")
                + ' or type "'
                + tf.pink("menu")
                + '" for help.'
            )
            return None
        else:
            return args

    def do_tm(self, args):
        """Display the top n movies."""
        args = self.parse_args(args, 1)
        if args:
            try:
                n = int(args[0])
                print(self.func_ctrl.top_movie_by_ratings(n))
            except:
                print(f"""{tf.red("Warning")}: Invalid Input.""")

    def do_ta(self, args):
        """Display the top n actors along with their best movies."""
        args = self.parse_args(args, 1)
        if args:
            try:
                n = int(args[0])
                print(self.func_ctrl.top_actors_with_best_movie(n))
            except:
                print(f"""{tf.red("Warning")}: Invalid Input.""")

    def do_tc(self, args):
        """Display the top m movies for n categories."""
        args = self.parse_args(args, 2)
        if args:
            try:
                n, m = int(args[0]), int(args[1])
                print(self.func_ctrl.find_top_m_movies_for_n_categories(n, m))
            except:
                print(f"""{tf.red("Warning")}: Invalid Input.""")

    def do_search(self, args):
        """Search movie which contains the keyword in any of author name, director name or movie name."""
        args = self.parse_args(args, 1)
        if args:
            s = args[0]
            print(self.func_ctrl.fuzz_search(s))

    def do_fsp(self, args):
        """Filters movies by region, year, category, letter then sort movies by sortedBy, where sortedBy"""
        print(
            "For the following opetions, you can leave a blank to indicate default setting."
        )
        print(
            f"You can also use `{tf.pink('list')}` command to see all possible sub-options."
        )
        region = input("Enter a region (default: ALL): ").strip()
        if region == "":
            region = "ALL"
        else:
            region = " ".join(region.split("_"))
        while True:
            year = input("Enter a year (default: ALL): ").strip()
            if year == "":
                year = "ALL"
                break
            else:
                try:
                    year = int(year)
                    break
                except:
                    print(f"""{tf.red("Warning")}: Invalid Input year.""")
                    continue
        category = input("Enter a category (default: ALL): ").strip()
        letter = input("Enter a letter (default: ALL): ").strip()[:1]
        while True:
            sortedBy = input(
                "Enter a sorting options (default: rating ascending): "
            ).strip()
            if sortedBy == "":
                sortedBy = "ascending"
            try:
                if sortedBy not in ["ascending", "descending"]:
                    1 / 0
                break
            except:
                print(f"""{tf.red("Warning")}: Invalid Input SortedBy.""")

        while True:
            n = input("Enter a number of rows displayed (default: 10): ").strip()
            if n == "":
                n = 10
                break
            else:
                try:
                    n = int(n)
                    break
                except:
                    print(f"""{tf.red("Warning")}: Invalid Input n.""")

        result = self.func_ctrl.movie_filter_and_sort(
            region, year, category, letter, sortedBy, n
        )
        if len(result) == 0:
            print("No results have been found!")
        else:
            print(result)

    def do_list(self, args):
        """Display the suboptions for fsp query"""
        args = self.parse_args(args, 1)
        if args:
            option = args[0].lower()
            if option in ["region", "category"]:
                print(self.func_ctrl.get_unique(option))
            elif option == "year":
                print("Movies with producing year from 1950 to 2022.")
            elif option == "letter":
                print("Movies with starting letters from A to Z and a to z.")
            elif option == "sortedby":
                print(
                    f"Movies are sorted by rating in {tf.yellow('ascending')} order by default, type {tf.yellow('descending')} to indicate in descending order."
                )
            elif option == "n":
                print("Display n rows of query result. n is a non-negative number.")
            else:
                print(f"""{tf.red("Warning")}: Invalid listing options.""")

    def do_graph(self, args):
        while True:
            try:
                print("Enter which graph you would like to see:")
                graphs = [
                    "Number of movies per year (most recent 20 years)",
                    "Relative rating for all directors",
                    "Number of movies directed by directors with top 10% relative rating per year (most recent 20 years)",
                ]
                for index, graph in enumerate(graphs):
                    print(f"{index+1}. {graph}")
                option = int(input())
                if 1 <= option <= len(graphs):
                    break
                else:
                    1 / 0
            except:
                print(f"""{tf.red("Warning")}: Invalid Input.""")

        if option in [1, 3]:
            while True:
                try:
                    print("Enter which type of graph you would like to see:")
                    graph_types = ["Histogram", "Line", "Pie"]
                    for index, graph_type in enumerate(graph_types):
                        print(f"{index+1}. {graph_type}")
                    graph = int(input())
                    if 1 <= graph <= len(graph_types):
                        break
                    else:
                        1 / 0
                except:
                    print(f"""{tf.red("Warning")}: Invalid Input.""")

        if option == 1:
            while True:
                try:
                    n = int(input("Enter the number of displayed years: "))
                    break
                except:
                    print(f"""{tf.red("Warning")}: Invalid Input.""")
            data = self.func_ctrl.num_movies_per_year(n)
            if graph == 1:
                self.graph_ctrl.draw_hist(
                    data["year"].apply(str).to_list(),
                    data["numOfMovies"].to_list(),
                    "Year",
                    "Number of Movies",
                    f"Number of Movies per year (most recent {n} years)",
                )
            elif graph == 2:
                self.graph_ctrl.draw_line(
                    data["year"].apply(str).to_list(),
                    data["numOfMovies"].to_list(),
                    "Year",
                    "Number of Movies",
                    f"Number of Movies per year (most recent {n} years)",
                )
            elif graph == 3:
                self.graph_ctrl.draw_pie(
                    data["numOfMovies"].to_list(),
                    data["year"].apply(str).to_list(),
                    f"Number of Movies per year (most recent {n} years)",
                )
            else:
                1 / 0
        elif option == 2:
            while True:
                try:
                    n = int(input("Enter the number of displayed directors: "))
                    break
                except:
                    print(f"""{tf.red("Warning")}: Invalid Input.""")
            data = self.func_ctrl.director_relative_rating(n)
            data["label"] = data.apply(
                lambda row: f"{row['name']} ({row['id']})", axis=1
            )
            data["rate"] = data["rate"].apply(lambda x: round(float(x), 2))
            self.graph_ctrl.draw_hist(
                data["label"].to_list(),
                data["rate"].to_list(),
                "Diretcors",
                "Relative Rating",
                f"Relative rating for top {n} directors",
            )
        elif option == 3:
            while True:
                try:
                    n = int(input("Enter the number of displayed years: "))
                    break
                except:
                    print(f"""{tf.red("Warning")}: Invalid Input.""")
            data = self.func_ctrl.number_of_movies_by_good_directors_per_year(n)
            if graph == 1:
                self.graph_ctrl.draw_hist(
                    data["year"].apply(str).to_list(),
                    data["num"].to_list(),
                    "Year",
                    "Number of Top 10% Directors",
                    f"Number of Top 10% Directors per year (most recent {n} years)",
                )
            elif graph == 2:
                self.graph_ctrl.draw_line(
                    data["year"].apply(str).to_list(),
                    data["num"].to_list(),
                    "Year",
                    "Number of Top 10% Directors",
                    f"Number of Top 10% Directors per year (most recent {n} years)",
                )
            elif graph == 3:
                self.graph_ctrl.draw_pie(
                    data["num"].to_list(),
                    data["year"].apply(str).to_list(),
                    f"Number of Top 10% Directors per year (most recent {n} years)",
                )
            else:
                1 / 0

    def do_q(self, _):
        """Exit the program."""
        print(f"Thank you for using {app_name}! Bye!")
        return True

    @Employee_required(cur_user)
    def register_employee_helper(self):
        if self.func_ctrl.employee_permission_authentication(
            self.cur_user.user_id, "insert", ["employee"]
        ):
            self.cur_user.register_employee()
        else:
            print(
                f"""[{tf.red("Warning")}]: Employee is not permitted to use this function."""
            )

    def do_register(self, args):
        """Register a user account."""
        if "employee" in str(args).lower():
            self.register_employee_helper()
        else:
            self.cur_user.register()

    def do_login(self, args):
        """Login a user account."""
        if self.cur_user.log_in():
            print(
                f"""{tf.green("Login Success!")} Current loged in user: {tf.italic(self.cur_user.username, 'yellow')}."""
            )

    @login_required(cur_user)
    def do_logout(self, args):
        """Logout the current user."""
        temp = self.cur_user.username
        self.cur_user.log_out()
        print(f"User: {tf.italic(temp, 'yellow')} has been logged out.")

    def do_me(self, args):
        """Check user profile and ratings if the user is logged in."""
        if self.cur_user.is_logged_in() and self.cur_user.user_type == "Employee":
            print(
                f"""
            ID : {self.cur_user.user_id}
            Username: {self.cur_user.username}
            User Type: {self.cur_user.user_type}
            Last Login Time: {self.cur_user.last_log_in_time}
            Salary: {self.cur_user.salary}
            Working Hours: {self.cur_user.working_hours}
            """
            )
            print("\n" + "Rating Records".center(30, "="))
            print(self.cur_user.get_my_ratings())
        elif self.cur_user.is_logged_in():
            print(
                f"""
            ID : {self.cur_user.user_id}
            Username: {self.cur_user.username}
            User Type: {self.cur_user.user_type}
            Last Login Time: {self.cur_user.last_log_in_time}
            Activeness: {self.cur_user.activeness}
            """
            )
            print("\n" + "Rating Records".center(30, "="))
            print(self.cur_user.get_my_ratings())
        else:
            print(
                f"""
            User Type: Visitor,
            Login Time: {self.cur_user.last_log_in_time}
            """
            )

    def display_movie(self, id: int):
        result = self.func_ctrl.get_movie(id)
        if result.empty:
            print(f"""[{tf.green("~")}]: No result has been found.""")
            return False
        else:
            result = [
                "" if str(x).lower() in ["nan", "none", "na"] else str(x)
                for x in result.values.tolist()[0]
            ]
            (
                id,
                name,
                region,
                year,
                introduction,
                rating,
                category,
                director,
                actor,
            ) = result
            print(
                movie_template
                % (
                    id,
                    name,
                    year,
                    rating,
                    region,
                    category,
                    director,
                    actor,
                    introduction,
                )
            )
            return True

    @login_required(cur_user)
    def display_rating(self, id: int, user_id: int):
        if self.func_ctrl.employee_permission_authentication(
            self.cur_user.user_id, "select", ["user"]
        ):
            result = self.func_ctrl.get_rating(id, user_id, "Employee")
        else:
            result = self.func_ctrl.get_rating(id, user_id)

        if result.empty:
            print(f"""[{tf.green("~")}]: No result has been found.""")
            return False
        else:
            result = [
                "" if str(x).lower() in ["nan", "none", "na"] else str(x)
                for x in result.values.tolist()[0]
            ]
            id, value, comment, time, movie = result
            print(rating_template % (id, value, movie, time, comment))
            return True

    def do_navigate(self, args):
        """Navigate a certain Movie/Celebrity/Director/Actor/Rating page by id."""
        args = self.parse_args(args, 2)
        if args:
            # try:
            option, id = args[0], args[1]
            if option in ["celebrity", "director", "actor"]:
                result = self.func_ctrl.get_celebrity(id)
                if result.empty:
                    print(f"""[{tf.green("~")}]: No result has been found.""")
                else:
                    result = [
                        "" if str(x).lower() in ["nan", "none", "na"] else str(x)
                        for x in result.values.tolist()[0]
                    ]
                    result_len = len(result)
                    if result_len == 5:
                        id, name, nationality, birth, summary = result
                        print(
                            celebrity_template % (id, name, nationality, birth, summary)
                        )
                    elif result_len == 7:
                        (
                            id,
                            name,
                            nationality,
                            birth,
                            summary,
                            organization,
                            movie,
                        ) = result
                        print(
                            actor_template
                            % (
                                id,
                                name,
                                nationality,
                                birth,
                                organization,
                                movie,
                                summary,
                            )
                        )
                    elif result_len == 8:
                        (
                            id,
                            name,
                            nationality,
                            birth,
                            summary,
                            graduation,
                            movie,
                            famous_movie,
                        ) = result
                        print(
                            director_template
                            % (
                                id,
                                name,
                                nationality,
                                birth,
                                graduation,
                                movie,
                                famous_movie,
                                summary,
                            )
                        )
                    else:
                        print(f"""{tf.red("Warning")}: Invalid Input.""")
            elif option == "movie":
                self.display_movie(id)
            elif option == "rating":
                self.display_rating(id, self.cur_user.user_id)
            else:
                print(f"""{tf.red("Warning")}: Invalid Input.""")

    @User_required(cur_user)
    @login_required(cur_user)
    def do_rate(self, args):
        """Rate a movie by movie_id."""
        args = self.parse_args(args, 1)
        if args:
            try:
                id = int(args[0])
                if self.display_movie(id):
                    while True:
                        value = input("Enter your rating (1-10): ")
                        try:
                            value = int(value)
                            if 1 <= value <= 10:
                                break
                        except:
                            print(f"""{tf.red("Warning")}: Invalid Rating.""")
                            continue
                    comment = input("Enter your comment: ")
                    if self.func_ctrl.user_rating_insert(
                        util.getUniqueID("Rating"),
                        value,
                        comment,
                        id,
                        self.cur_user.user_id,
                    ):
                        print(f"""{tf.green("Rate Success!")}""")
                    else:
                        print(f"""{tf.red("ERROR")}: Insert rating failed.""")
            except:
                print(f"""{tf.red("Warning")}: Invalid Input.""")

    def try_accquire_lock(self, result):
        if not result:
            print(
                f"""{tf.red("Lock Accquired Failed")}: there are other user currently on this table."""
            )
            return False
        return True

    def try_release_lock(self, result):
        if not result:
            print(f"""{tf.red("Lock Released Failed")}: You don't have the lock.""")

    @Standard_required(cur_user)
    @Employee_Permission_required(func_ctrl, cur_user, "update", ["user"])
    def update_rating(self, id: int):
        if self.try_accquire_lock(
            self.acc_ctrl.try_lock_X(self.cur_user.user_id, "Rating")
        ):
            while True:
                value = input("Enter your rating (1-10): ")
                try:
                    value = int(value)
                    if 1 <= value <= 10:
                        break
                except:
                    print(f"""{tf.red("Warning")}: Invalid Rating.""")
                    continue
            comment = input("Enter your comment: ")
            if self.func_ctrl.user_rating_update(id, value, comment, util.now()):
                print(f"""{tf.green("Update Success!")}""")
            else:
                print(f"""{tf.red("ERROR")}: Update rating failed.""")
            self.try_release_lock(
                self.acc_ctrl.try_unlock_X(self.cur_user.user_id, "Rating")
            )

    @Premium_required(cur_user)
    @Employee_Permission_required(func_ctrl, cur_user, "update", ["user"])
    def delete_rating(self, id: int):
        if input("Are you sure to delete? (Y/n)").lower() in [
            "yes",
            "y",
        ]:
            if self.try_accquire_lock(
                self.acc_ctrl.try_lock_X(self.cur_user.user_id, "user")
            ):
                if self.func_ctrl.user_rating_delete(id):
                    print(f"""{tf.green("Delete Success!")}""")
                else:
                    print(f"""{tf.red("ERROR")}: Delete rating failed.""")
                self.try_release_lock(
                    self.acc_ctrl.try_unlock_X(self.cur_user.user_id, "Rating")
                )
        else:
            print("Delete operation cancelled.")

    @Employee_Permission_required(func_ctrl, cur_user, "update", ["movie"])
    @Employee_required(cur_user)
    def update_movie(self, id: int):
        if self.try_accquire_lock(
            self.acc_ctrl.try_lock_X(self.cur_user.user_id, "Movie")
        ):
            region = input("Enter the region: ")
            while True:
                year = input("Enter the year: ")
                try:
                    year = int(year)
                    if 1 <= year <= 10:
                        break
                except:
                    print(f"""{tf.red("Warning")}: Invalid Year.""")
                    continue
            introduction = input("Enter the introduction: ")
            if self.func_ctrl.movie_update(id, region, year, introduction):
                print(f"""{tf.green("Update Success!")}""")
            else:
                print(f"""{tf.red("ERROR")}: Update Movie failed.""")
            self.try_release_lock(
                self.acc_ctrl.try_unlock_X(self.cur_user.user_id, "Movie")
            )

    @Employee_Permission_required(func_ctrl, cur_user, "delete", ["movie"])
    @Employee_required(cur_user)
    def delete_movie(self, id: int):
        if self.try_accquire_lock(
            self.acc_ctrl.try_lock_X(self.cur_user.user_id, "Movie")
        ):
            print(
                f"{tf.yellow(str(self.func_ctrl.user_rating_count_movie_id(id)))} ratings will be deleted."
            )
            print(
                f"{tf.yellow(str(self.func_ctrl.category_count_movie_id(id)))} categories will be deleted."
            )
            print(
                f"{tf.yellow(str(self.func_ctrl.acts_count_movie_id(id)))} acts relations will be deleted."
            )
            if input("Are you sure to delete the movie? ").lower() in ["yes", "y"]:
                if self.func_ctrl.movie_delete(id):
                    print(f"""{tf.green("Delete Success!")}""")
                else:
                    print(f"""{tf.red("ERROR")}: Delete Movie failed.""")
            else:
                print("Delete movie cancelled.")
            self.try_release_lock(
                self.acc_ctrl.try_unlock_X(self.cur_user.user_id, "Movie")
            )

    @login_required(cur_user)
    def do_modify(self, args):
        """Update or delete an existing rating by the rating id"""
        args = self.parse_args(args, 3)
        if args:
            try:
                table, option, id = args[0], args[1], int(args[2])
                if table == "movie":
                    if self.display_movie(id):
                        if option == "update":
                            self.update_movie(id)
                        elif option == "delete":
                            self.delete_movie(id)
                        else:
                            1 / 0
                    else:
                        1 / 0
                elif table == "rating":
                    if self.display_rating(id, self.cur_user.user_id):
                        if option == "update":
                            self.update_rating(id)
                        elif option == "delete":
                            self.delete_rating(id)
                        else:
                            1 / 0
                    else:
                        1 / 0
                else:
                    1 / 0
            except:
                print(f"""{tf.red("Warning")}: Invalid Input.""")


if __name__ == "__main__":
    CLI().cmdloop()
