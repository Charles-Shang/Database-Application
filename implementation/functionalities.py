from CONSTANTS import user, password, host, port, sample_database_name
from mysqlCtrl import MysqlCtrl
import pandas as pd
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class Functionalities:
    def __init__(self):
        self.ctrl = MysqlCtrl(user, password, host, port, sample_database_name)

    def get_movie(self, id: int):
        """
        get_movie finds all information about a movie.

        Args:
            id: Movie id.

        Returns: A Table of (movie_id, movie_name, region, year, introduction, rating, category, director, actor)
        """

        return self.ctrl.query(
            f"""
        SELECT id, name, region, `year`, introduction, avg_rate,
        (SELECT GROUP_CONCAT(category)  FROM Movie_category WHERE movie_id = M.id) AS catgeory,
        (SELECT CONCAT(first_name, " ", last_name, " (", director_id, ")")  FROM Celebrity WHERE id = director_id) AS director,
        (SELECT GROUP_CONCAT(CONCAT(first_name, " ", last_name, " (", actor_id, ")"))  FROM Acts JOIN Celebrity ON id = actor_id WHERE movie_id = M.id) AS actor
        FROM Movie AS M
        WHERE id = {id};
        """
        )

    def get_rating(self, id: int, user_id: int, user_type: str = "NOT Employee"):
        """
        get_rating finds all information about a rating.

        Args:
            id: Rating id.

        Returns: A Table of (id, value, comment, time, movie)
        """

        if user_type == "Employee":
            return self.ctrl.query(
                f"""
            SELECT R.id, value, comment, time,
            (SELECT GROUP_CONCAT(M.name, " (", M.id, ")") FROM Movie AS M WHERE M.id = movie_id) AS movie
            FROM Rating AS R
            WHERE R.id = {id};
            """
            )
        else:
            return self.ctrl.query(
                f"""
            SELECT R.id, value, comment, time,
            (SELECT GROUP_CONCAT(M.name, " (", M.id, ")") FROM Movie AS M WHERE M.id = movie_id) AS movie
            FROM Rating AS R
            WHERE R.id = {id} AND R.user_id = {user_id};
            """
            )

    def get_celebrity(self, id: int):
        """
        get_celebrity finds all information about a celebrity.

        Args:
            id: Celebrity id.

        Returns: A Table of one of director_info, actor_info or celebrity_info
        """

        director_count = int(
            self.ctrl.query(f"SELECT count(*) FROM Director WHERE id = {id};").iloc[0][
                0
            ]
        )
        actor_count = int(
            self.ctrl.query(f"SELECT count(*) FROM Actor WHERE id = {id};").iloc[0][0]
        )
        if director_count:
            return self.get_director(id)
        elif actor_count:
            return self.get_actor(id)
        else:
            return self.ctrl.query(
                f"""
            SELECT id, CONCAT(first_name, " ", last_name) AS name, nationality, birth, summary
            FROM Celebrity
            WHERE id = {id};
            """
            )

    def get_director(self, id: int):
        """
        get_director finds all information about a director.

        Args:
            id: Director id.

        Returns: A Table of (id, name, nationality, birth, summary, graduation, movie(s), famous_movie)
        """

        return self.ctrl.query(
            f"""
        SELECT C.id, CONCAT(first_name, " ", last_name) AS name, nationality, birth, summary, graduation,
        (SELECT GROUP_CONCAT(CONCAT(Movie.name, " (", Movie.id, ")"))  FROM Movie WHERE director_id = C.id) AS movie,
        (SELECT GROUP_CONCAT(CONCAT(Movie.name, " (", DFM.movie_id, ")"))  FROM Director_famousMovie AS DFM JOIN Movie ON Movie.id = DFM.movie_id WHERE DFM.director_id = C.id) AS famous_movie
        FROM Celebrity AS C
        JOIN Director
        ON C.id = Director.id
        WHERE C.id = {id};
        """
        )

    def get_actor(self, id: int):
        """
        get_actor finds all information about an actor.

        Args:
            id: Actor id.

        Returns: A Table of (id, name, nationality, birth, summary, organization, movie(s))
        """

        return self.ctrl.query(
            f"""
        SELECT C.id, CONCAT(first_name, " ", last_name) AS name, nationality, birth, summary, organization,
        (SELECT GROUP_CONCAT(CONCAT(Movie.name, " (", Movie.id, ")"))  FROM Acts JOIN Movie ON Movie.id = movie_id WHERE actor_id = C.id) AS movie
        FROM Celebrity AS C
        JOIN Actor
        ON C.id = Actor.id
        WHERE C.id = {id};
        """
        )

    def count_entries(self, table_name: str) -> int:
        return int(self.ctrl.query(f"SELECT count(*) FROM {table_name};").iloc[0][0])

    def top_movie_by_ratings(self, n: int = 5) -> pd.DataFrame:
        """
        top_movie_by_ratings finds the top n movies by user ratings.

        Args:
            n: The number of movies selected, by default n=5

        Returns: A Table of (movie_name, rating)
        """

        queryStatement = f"""
            SELECT name as Title, avg_rate as Rating
            FROM Movie
            ORDER BY avg_rate DESC
            LIMIT {n};
        """

        result = self.ctrl.query(queryStatement)
        result.index = np.arange(1, len(result) + 1)
        result.set_axis(["Title", "Rating"], axis=1, inplace=True)
        return result

    def top_actors_with_best_movie(self, n: int) -> pd.DataFrame:
        """
        top_actors_with_best_movie finds the top n actors and their one best
        movie.

        Args:
            n: The number of actors selected. By default, n=5

        Returns: A Table of (actor, movie_name)
        """

        queryStatement = f"""
        SELECT CONCAT_WS(' ',C.first_name,C.last_name) as actor_name,
            AVG(M.avg_rate) as avg_rating,
            M.name as best_movie_name,
            MAX(M.avg_rate) as best_movie_rating
        FROM Actor A
        JOIN Acts AC ON A.id = AC.actor_id
        JOIN Movie M ON M.id = AC.movie_id
        JOIN Celebrity C on A.id = C.id
        GROUP BY A.id
        ORDER BY avg_rating DESC
        LIMIT {n};
        """
        result = self.ctrl.query(queryStatement)
        result.set_axis(
            ["Actor", "Actor Rating", "Movie", "Movie Rating"], axis=1, inplace=True
        )
        result.index = np.arange(1, len(result) + 1)
        return result

    def movie_filter_and_sort(
        self, region, year, category, letter, sortedBy, limit: int = 10, offset: int = 0
    ):
        """
        movie_filter_and_sort filters movies by region, year, category, letter
        then sort movies by sortedBy, where sortedBy is in {updateTime, popularity, rating}.

        Args: [all string type arguments use empty string "" to indicates no input, int type use 0 to indicates no input unless specified]
            region:       string type, indicates the region where the movies are produced
            year:         int type, indicates the year where the movies are produced
            category:     string type, indicates the category that the movies belong
            letter:       string type, indicates the first letter of the movies' names, if letter is "ALL", then ignore
            sortedBy:     string type, indicates the way we want to sort our result by
            limit:        int type, indicates the number of rows we want to get, default value is 10
            offset:       int type, indicates the offset
        """
        queryStatement = """SELECT DISTINCT ID, name, region, year, GROUP_CONCAT( DISTINCT category ) AS allCategory, avg_rate, introduction
        FROM Movie LEFT JOIN Movie_category ON Movie.ID=Movie_category.movie_id"""

        hasWhere = False
        if (
            (region != "" and region != "ALL")
            or (year != 0 and year != "ALL")
            or (letter != "" and letter != "ALL")
        ):
            queryStatement += " WHERE"
            hasWhere = True
        if region != "" and region != "ALL":
            queryStatement += " region='" + region + "' AND"
        if year != 0 and year != "ALL":
            queryStatement += " year=" + str(year) + " AND"
        if letter != "" and letter != "ALL":
            queryStatement += " name REGEXP '^" + letter + "' AND"

        if hasWhere:
            # remove last AND
            queryStatement = queryStatement[:-4]
        queryStatement += " GROUP BY ID"
        if category != "" and category != "ALL":
            queryStatement += (
                " HAVING SUM(case when category='"
                + category
                + "' then 1 else 0 end) > 0"
            )

        if sortedBy == "descending":
            queryStatement += " ORDER BY avg_rate DESC"
        elif sortedBy == "ascending":
            queryStatement += " ORDER BY avg_rate ASC"


        queryStatement += " LIMIT " + str(limit) + " OFFSET " + str(offset) + ";"
        result = self.ctrl.query(queryStatement)
        if len(result) == 0:
            return result
        else:
            result.index = np.arange(1, len(result) + 1)
            result.set_axis(
                ["ID", "Movie", "Region", "Year", "Category", "Rating", "Introduction"],
                axis=1,
                inplace=True,
            )
            return result

    def get_unique(self, option: str) -> pd.DataFrame:
        if option == "region":
            result = self.ctrl.query("SELECT DISTINCT(region) FROM Movie;").dropna()
            result.index = np.arange(1, len(result) + 1)
            result.set_axis(["Region"], axis=1, inplace=True)
            return result
        elif option == "category":
            result = self.ctrl.query("SELECT DISTINCT(category) FROM Movie_category;").dropna()
            result.index = np.arange(1, len(result) + 1)
            result.set_axis(["Category"], axis=1, inplace=True)
            return result

    def fuzz_search(self, n: str) -> pd.DataFrame:
        """
        fuzz_search finds the movie which contains the keyword in any of
        author name, director name or movie name.

        Args:
            n: The key word being searched and displayed

        Returns: A Table of (movie_name, region, year, category, rating,
                             summary, director_name, [actor_name])
        """

        result = self.ctrl.query(
            f"""
        WITH midList(mids) as (
            (SELECT DISTINCT Movie.id
            FROM Movie
            WHERE Movie.name LIKE '%%{n}%%')
            UNION 
            (SELECT DISTINCT movie_id
            FROM  Celebrity c  join Acts a on c.id = a.actor_id
            WHERE c.name LIKE '%%{n}%%')
            UNION 
            (SELECT DISTINCT Movie.id
            FROM Celebrity c2  JOIN Movie on Movie.director_id = c2.id
            WHERE c2.name LIKE '%%{n}%%')
        )
        SELECT m.id as ID, m.name as Title, m.region, m.year, m.avg_rate , d.name as Director,
        GROUP_CONCAT(DISTINCT CONCAT_WS(' ',a.first_name,a.last_name)) as actor_name, m.introduction
        FROM Movie as m, midList,Actor natural join Celebrity as a, Acts ar, Director natural join Celebrity as d
        WHERE ar.actor_id  = a.id  and ar.movie_id  = m.id  and m.director_id  = d.id  and m.id  = midList.mids
        GROUP BY(m.name);

        """
        )
        result.index = np.arange(1, len(result) + 1)
        result.set_axis(
            [
                "ID",
                "Movie",
                "Region",
                "Year",
                "Rating",
                "Director",
                "Actor(s)",
                "Introduction",
            ],
            axis=1,
            inplace=True,
        )
        return result

    def find_top_m_movies_for_n_categories(
        self, n: int = 5, m: int = 3
    ) -> pd.DataFrame:
        """
        find_top_m_movies_for_n_categories finds the top n movie category of
        the average ratings and m top movies in each category.

        Args:
            n: The number of movie categories that is returned
            m: The number of movies for each of the n categories

        Returns: A Table of (category, averageRating, name, rates)
        """

        result = self.ctrl.query(
            f"""
        WITH MOVIE(name, category, rates) as
            (SELECT Movie.name, Movie_category.category, Movie.avg_rate
            FROM Movie, Movie_category
            WHERE Movie.id = Movie_category.movie_id),
        temporaryTop3Category(category, averageRating) as
            (SELECT category, AVG(rates)
            FROM MOVIE
            GROUP BY category
            ORDER BY AVG(rates) desc
            LIMIT {n})
        SELECT category, averageRating, name, rates
        FROM (
            SELECT category, averageRating, name, rates,
            ROW_NUMBER() OVER (PARTITION BY MOVIE.category ORDER BY MOVIE.rates DESC) AS num
            FROM temporaryTop3Category
            NATURAL JOIN MOVIE 
            ORDER BY averageRating DESC, rates DESC
        ) AS withNum
        WHERE withNum.num <= {m};
        """
        )
        result.index = np.arange(1, len(result) + 1)
        result.set_axis(
            ["Category", "Category Rating", "Movie", "Movie Rating"],
            axis=1,
            inplace=True,
        )
        return result

    def num_movies_per_year(self, n: int = 20) -> pd.DataFrame:
        result = self.ctrl.query(
            f"""
        SELECT *
        FROM (
            SELECT year, count(id) AS NumOfMovie
            FROM Movie
            GROUP BY year
            ORDER BY year DESC
            LIMIT {n}
        ) AS D
        ORDER BY year ASC;
        """
        )
        result.set_axis(
            ["year", "numOfMovies"],
            axis=1,
            inplace=True,
        )
        result.index = np.arange(1, len(result) + 1)
        return result

    def director_relative_rating(self, n) -> pd.DataFrame:
        """
        The relative rating for all directors (based on the average rating of the average rating for all the movies they directed)

        Args:
            none

        Returns: A Table of (director_id, first_name, last_name, relative_rating)
        """

        result = self.ctrl.query(
            f"""
        WITH AverageRating(movie_id, average_rating) AS
        (
        SELECT RateBy.movie_id, AVG(Rating.value)
        FROM RateBy, Rating
        WHERE RateBy.movie_id = Rating.movie_id AND RateBy.user_id = Rating .user_id AND Rating.value IS NOT NULL
        GROUP BY Rating.movie_id
        )
        SELECT C.id AS director_id, CONCAT(C.first_name, " ", C.last_name) AS name, AVG(A.average_rating) AS relative_rating
        FROM Celebrity AS C, Movie as M, AverageRating as A
        WHERE C.id = M.director_id  AND A.movie_id = M.id
        GROUP BY C.id 
        ORDER BY relative_rating DESC
        LIMIT {n}
        """
        )
        result.index = np.arange(1, len(result) + 1)
        result.set_axis(
            ["id", "name", "rate"],
            axis=1,
            inplace=True,
        )
        return result

    def number_of_movies_by_good_directors_per_year(
        self, n: int, r: float = 0.1
    ) -> pd.DataFrame:
        """
        The number of movies released directed by directors with relative rating of top (n*100)% every year

        Args:
            n: Number of displayed years
            r: The percentage of the directors (in decimal) that counts into the number of movies per year

        Returns: A Table of (year, num)
        """

        result = self.ctrl.query(
            f"""
            WITH AverageRating(movie_id, average_rating) AS (
                SELECT RateBy.movie_id, AVG(Rating.value)
                FROM RateBy, Rating
                WHERE RateBy.movie_id = Rating.movie_id AND RateBy.user_id = Rating .user_id AND Rating.value IS NOT NULL
                GROUP BY Rating.movie_id
            ),
            DirectorRating(director_id, director_first_name, director_last_name, relative_rating, relative_rank) AS (
                SELECT C.id, C.first_name, C.last_name, AVG(A.average_rating) as relative_rating, RANK() OVER (ORDER BY (AVG(A.average_rating)) DESC)
                FROM Celebrity AS C, Movie as M, AverageRating as A
                WHERE C.id = M.director_id  AND A.movie_id = M.id
                GROUP BY C.id 
                ORDER BY relative_rating DESC
            ),
            top_rating_num_directors(year, num) AS (
                SELECT year, COUNT(*) AS num
                FROM Movie
                WHERE director_id IN (
                    SELECT director_id
                    FROM DirectorRating
                    WHERE relative_rank <= (SELECT COUNT(*) FROM DirectorRating)*0.1
                )
                GROUP BY year
                ORDER BY year DESC
                LIMIT {n}
            )
            SELECT *
            FROM top_rating_num_directors
            ORDER BY year ASC;
        """
        )
        result.index = np.arange(1, len(result) + 1)
        result.set_axis(
            ["year", "num"],
            axis=1,
            inplace=True,
        )
        return result

    def employee_permission_authentication(self, employee_id, action, tables) -> bool:
        """
        check whether an employee has the permission to do certain action
        Args:
            employee_id: integer, employee's id as name suggested
            action: string, must be one of {"select", "insert", "update", "delete"}
                    as this function doesn't check correctness, case does not matter (can be capital or lower case)
            tables: list of strings, the table/view names, len(list) >= 1
        """
        total_count = len(
            tables
        )  # count the total number of tables that need permission, should match the # of records returned
        if total_count == 0:
            return False

        queryStatement = """SELECT Permits.employee_id, Permission.name
        FROM Permission LEFT JOIN Permits ON Permits.permission_id=Permission.id
        WHERE Permits.employee_id="""
        queryStatement += str(employee_id) + " AND Permission.name IN ("
        permissionNames = ""
        action = action.upper()

        if action == "SELECT":
            permissionNames = "'view_" + tables[0].lower() + "_db'"
            for i in range(1, len(tables)):
                permissionNames += ", 'view_" + tables[i].lower() + "_db'"
            permissionNames += ");"
        else:
            permissionNames = "'update_" + tables[0].lower() + "_db'"
            for i in range(1, len(tables)):
                permissionNames += ", 'update_" + tables[i].lower() + "_db'"
            permissionNames += ");"

        result = self.ctrl.query(queryStatement + permissionNames)
        return len(result) == total_count

    def user_rating_insert(
        self, rating_id, rating_value, comment, movie_id, user_id
    ) -> bool:
        """
        insert a rating record
        Args:
            rating_id: int, rating_id, must be unique (generation must guarantee that it has not occured in the db)
            rating_value: rating value
            comment: string, user's comment
            movie_id: int, movie_id user comments on
            user_id: int, user's id
        Return:
            boolean, true if insertion success, false otherwise
        """
        insertStatement1 = f"""
        INSERT INTO RateBy (movie_id, user_id)
        SELECT {movie_id} AS movie_id, {user_id} AS user_id
        FROM RateBy
        WHERE (movie_id = {movie_id} AND user_id = {user_id})
        HAVING COUNT(*) = 0;
        """
        insertStatement2 = f"""
        INSERT INTO Rating (id, time, value, comment, movie_id, user_id)
        VALUES ({rating_id}, NOW(), {rating_value}, '{comment}', {movie_id}, {user_id});
        """
        status1 = self.ctrl.execute(insertStatement1)
        status = False
        if status1:
            status2 = self.ctrl.execute(insertStatement2)
        return status2

    def user_rating_delete(self, rating_id) -> bool:
        """
        delete a rating record
        Args:
            rating_id: int, the rating_id of the rating to be deleted
        Return:
            true if deletion is successful, false otherwise
        """
        deleteStatement = "DELETE FROM Rating WHERE id=" + str(rating_id) + ";"
        status = self.ctrl.execute(deleteStatement)
        return status

    def user_rating_update(self, rating_id, new_rating_value, new_comment, new_time) -> bool:
        """
        update a rating record
        Args:
            rating_id: int, the rating_id of the rating to be deleted
            new_rating_value: int, the new rating value
            new_comment: string, the new comment
        Return:
            true if update is successful, false otherwise
        """
        updateStatement = f"UPDATE Rating SET value = {new_rating_value}, comment = '{new_comment}', time = '{new_time}' WHERE id = {rating_id};"
        status = self.ctrl.execute(updateStatement)
        return status

    def movie_update(self, movie_id, new_region, new_year, new_introduction) -> bool:
        updateStatement = f"UPDATE Movie SET region = '{new_region}', year = {new_year}, introduction = '{new_introduction}' WHERE id = {movie_id};"
        status = self.ctrl.execute(updateStatement)
        return status

    def movie_delete(self, id) -> bool:
        status = self.ctrl.execute(f"DELETE FROM Acts WHERE Acts.movie_id = {id};")
        if not status:
            return status
        status = self.ctrl.execute(
            f"DELETE FROM Movie_category WHERE Movie_category.movie_id = {id};"
        )
        if not status:
            return status
        status = self.ctrl.execute(f"DELETE FROM Rating WHERE Rating.movie_id = {id};")
        if not status:
            return status
        status = self.ctrl.execute(f"DELETE FROM RateBy WHERE RateBy.movie_id = {id};")
        if not status:
            return status
        status = self.ctrl.execute(f"DELETE FROM Movie WHERE Movie.id = {id};")
        return status

    def user_rating_count_movie_id(self, movie_id):
        queryStatement = f"""
        SELECT count(*)
        FROM Rating
        WHERE movie_id = {movie_id};
        """
        result = self.ctrl.query(queryStatement).iloc[0][0]
        return int(result)

    def category_count_movie_id(self, movie_id):
        queryStatement = f"""
        SELECT count(*)
        FROM Movie_category
        WHERE Movie_category.movie_id = {movie_id};
        """
        result = self.ctrl.query(queryStatement).iloc[0][0]
        return int(result)

    def acts_count_movie_id(self, movie_id):
        queryStatement = f"""
        SELECT count(*)
        FROM Acts
        WHERE Acts.movie_id = {movie_id};
        """
        result = self.ctrl.query(queryStatement).iloc[0][0]
        return int(result)
    
if __name__ == "__main__":
    func = Functionalities()
    print(func.employee_permission_authentication(
                3000, "update", ["rating"]
            ))
    