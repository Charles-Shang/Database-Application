from CONSTANTS import user, password, host, port, sample_database_name, pwd_valid_chars
from mysqlCtrl import MysqlCtrl
import textFormatter as tf
import util
import numpy as np


class User:
    user_type = "Visitor"  # Basic / Standard / Premium / Employee
    user_id = None
    username = None
    last_log_in_time = None
    activeness = None
    salary = None
    working_hours = None
    ctrl = MysqlCtrl(user, password, host, port, sample_database_name)

    def __init__(self) -> None:
        self.last_log_in_time = util.now()

    def is_logged_in(self) -> bool:
        return self.user_type != "Visitor"

    def log_in(self):
        user_name = input("Enter your username: ").strip()
        pwd = input("Enter your password: ").strip()
        result = self.ctrl.query(
            f"""
        SELECT User.id, User.activeness, User.level
        FROM User
        NATURAL JOIN Person
        WHERE username = '{user_name}' AND pwd = '{pwd}';
        """
        )

        if len(result) != 0:
            self.user_id = int(result.iloc[0][0])
            self.activeness = result.iloc[0][1] + 1
            self.user_type = result.iloc[0][2]
            self.username = user_name
            self.last_log_in_time = util.now()

            update_result = self.ctrl.execute(
                f"""
            UPDATE Person SET last_log_in = '{self.last_log_in_time}' WHERE id = {self.user_id};
            """
            )

            if not update_result:
                print(f"""{tf.red("Warning")}: Update last_log_in Failed.""")
                return False
            return True

        result = self.ctrl.query(
            f"""
        SELECT Employee.id, Employee.salary, Employee.working_hours
        FROM Employee
        NATURAL JOIN Person
        WHERE username = '{user_name}' AND pwd = '{pwd}';
        """
        )

        if len(result) != 0:
            self.user_id = int(result.iloc[0][0])
            self.salary = float(result.iloc[0][1])
            self.working_hours = float(result.iloc[0][2])
            self.user_type = "Employee"
            self.username = user_name
            self.last_log_in_time = util.now()

            update_result = self.ctrl.execute(
                f"""
            UPDATE Person SET last_log_in = '{self.last_log_in_time}' WHERE id = {self.user_id};
            """
            )

            if not update_result:
                print(f"""{tf.red("Warning")}: Update last_log_in Failed.""")
                return False
            return True

        print(f"""{tf.red("Warning")}: Invalid username or password.""")
        return False

    def register(self):
        while True:
            user_name = input("Enter your username: ").strip()
            if (
                len(user_name) < 6
                or len(user_name) > 25
                or not util.isAmadefromB(user_name, pwd_valid_chars)
            ):
                print(
                    f"""{tf.red("Warning")}: Choose a username 6-25 characters long. Your username can be any combination of letters, numbers, or underscore '_'."""
                )
                continue
            if (
                self.ctrl.query(
                    f"""
            SELECT count(*)
            FROM User
            NATURAL JOIN Person
            WHERE username = '{user_name}'
            """
                ).iloc[0][0]
                != 0
            ):
                print(f"""{tf.red("Warning")}: User name {user_name} already exists.""")
                continue

            break

        while True:
            pwd = input("Enter your password: ").strip()
            if (
                len(pwd) < 8
                or len(pwd) > 25
                or not util.isAmadefromB(user_name, pwd_valid_chars)
            ):
                print(
                    f"""{tf.red("Warning")}: Choose a password 8-25 characters long. Your password can be any combination of letters, numbers, or underscore '_'."""
                )
                continue
            break

        user_id = util.getUniqueID("Person")
        log_in_time = util.now()

        result = self.ctrl.execute(
            f"""
        INSERT INTO Person (id, username, pwd, last_log_in)
        VALUES ({user_id}, '{user_name}', '{pwd}', '{log_in_time}');
        """
        )

        if not result:
            print(f"""{tf.red("ERROR")}: Registration Failed.""")
            return False

        result = self.ctrl.execute(
            f"""
        INSERT INTO User (id, activeness, level)
        VALUES ({user_id}, 1, 'Basic');
        """
        )

        if not result:
            print(f"""{tf.red("ERROR")}: Registration Failed.""")
            return False

        self.user_type = "Basic"
        self.user_id = user_id
        self.username = user_name
        self.last_log_in_time = log_in_time
        self.activeness = 1

        print(
            f"""{tf.green("Registration Success!")} Current loged in user: {user_name}."""
        )
        return True

    def register_employee(self):
        while True:
            user_name = input("Enter a username: ").strip()
            if (
                len(user_name) < 6
                or len(user_name) > 25
                or not util.isAmadefromB(user_name, pwd_valid_chars)
            ):
                print(
                    f"""{tf.red("Warning")}: Choose a username 6-25 characters long. Your username can be any combination of letters, numbers, or underscore '_'."""
                )
                continue
            if (
                self.ctrl.query(
                    f"""
            SELECT count(*)
            FROM Employee
            NATURAL JOIN Person
            WHERE username = '{user_name}'
            """
                ).iloc[0][0]
                != 0
            ):
                print(f"""{tf.red("Warning")}: User name {user_name} already exists.""")
                continue

            break

        while True:
            pwd = input("Enter the password: ").strip()
            if (
                len(pwd) < 8
                or len(pwd) > 25
                or not util.isAmadefromB(user_name, pwd_valid_chars)
            ):
                print(
                    f"""{tf.red("Warning")}: Choose a password 8-25 characters long. Your password can be any combination of letters, numbers, or underscore '_'."""
                )
                continue
            break

        while True:
            salary = input("Enter the salary: ").strip()
            try:
                salary = float(salary)
                break
            except:
                print(f"""{tf.red("Warning")}: Invalid Salary.""")
                continue
        
        while True:
            working_hours = input("Enter the working hours: ").strip()
            try:
                working_hours = float(working_hours)
                break
            except:
                print(f"""{tf.red("Warning")}: Invalid working hours.""")
                continue

        user_id = util.getUniqueID("Person")
        log_in_time = util.now()

        result = self.ctrl.execute(
            f"""
        INSERT INTO Person (id, username, pwd, last_log_in)
        VALUES ({user_id}, '{user_name}', '{pwd}', '{log_in_time}');
        """
        )

        if not result:
            print(f"""{tf.red("ERROR")}: Registration Failed.""")
            return False

        result = self.ctrl.execute(
            f"""
        INSERT INTO Employee (id, salary, working_hours)
        VALUES ({user_id}, {round(salary, 2)}, {round(working_hours,1)});
        """
        )

        if not result:
            print(f"""{tf.red("ERROR")}: Registration Failed.""")
            return False

        print(
            f"""{tf.green("Registration Success!")}"""
        )
        return True

    def log_out(self):
        self.user_type = "Visitor"  # Basic / Standard / Premium
        self.user_id = None
        self.username = None
        self.last_log_in_time = None
        self.activeness = None

    def get_my_ratings(self):
        result = self.ctrl.query(
            f"""
        SELECT Movie.id, Movie.name, Rating.id, Rating.value, Rating.Comment, Rating.time
        FROM Rating
        JOIN Movie ON Movie.id = Rating.movie_id
        WHERE Rating.user_id = {self.user_id}
        ORDER BY Rating.time DESC;
        """
        )
        if len(result) != 0:
            result.index = np.arange(1, len(result) + 1)
            result.set_axis(
                ["Movie ID", "Movie", "Rating ID", "Rates", "Comment", "Time"],
                axis=1,
                inplace=True,
            )
            return result
        else:
            return ""
