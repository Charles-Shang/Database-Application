from CONSTANTS import user, password, host, port, sample_database_name, TABLES
from mysqlCtrl import MysqlCtrl
import pandas as pd
import numpy as np


class Functionalities:

    def __init__(self):
        self.ctrl = MysqlCtrl(user, password, host, port, sample_database_name)
    
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
            SELECT name as Title, avg_rate as Rate
            FROM Movie
            ORDER BY avg_rate DESC
            LIMIT {n};
        """
        result = self.ctrl.query(queryStatement)
        result.index = np.arange(1, len(result) + 1)
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
            SELECT C.name as actor_name,
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
        result.index = np.arange(1, len(result) + 1)
        return result

    def movie_filter_and_sort (self, region, year, category, letter, sortedBy, limit : int = 10, offset : int = 0) -> pd.DataFrame:
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
        if (region != "" and region != "ALL") or year != 0 or (letter != "" and letter != "ALL"):
            queryStatement += " WHERE"
            hasWhere = True
        if region != "" and region != "ALL":
            queryStatement += " region='" + region + "' AND"
        if year != 0:
            queryStatement += " year=" + str(year) + " AND"
        if letter != "" and letter != "ALL":
            queryStatement += " name REGEXP '^" + letter + "' AND"
        
        if hasWhere:
            # remove last AND
            queryStatement = queryStatement[:-4]
        queryStatement += " GROUP BY ID"
        if category != "" and category != "ALL":
            queryStatement += " HAVING SUM(case when category='" + category + "' then 1 else 0 end) > 0"

        if sortedBy == "rating":
            queryStatement += " ORDER BY avg_rate DESC"
        
        queryStatement += " LIMIT " + str(limit) + " OFFSET " + str(offset) + ";"
        result = self.ctrl.query(queryStatement)
        return result

    
    def fuzz_search (self, n:str) -> pd.DataFrame:
        """
        fuzz_search finds the movie which contains the keyword in any of
        author name, director name or movie name.

        Args:
            n: The key word being searched and displayed
        
        Returns: A Table of (movie_name, region, year, category, rating,
                             summary, director_name, [actor_name])
        """

        result = self.ctrl.query(f"""
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

        SELECT m.name as Title, m.region, m.year, m.avg_rate , m.introduction , d.name as Director,
        GROUP_CONCAT(a.name) as actor_name
        FROM Movie as m, midList,Actor natural join Celebrity as a, Acts ar, Director natural join Celebrity as d
        WHERE ar.actor_id  = a.id  and ar.movie_id  = m.id  and m.director_id  = d.id  and m.id  = midList.mids
        GROUP BY(m.name);

        """)
        result.index = np.arange(1, len(result) + 1)
        return result

    def find_top_m_movies_for_n_categories(self, n: int = 5, m: int = 3) -> pd.DataFrame:
        """
        find_top_m_movies_for_n_categories finds the top n movie category of
        the average ratings and m top movies in each category.

        Args:
            n: The number of movie categories that is returned
            m: The number of movies for each of the n categories
        
        Returns: A Table of (category, averageRating, name, rates)
        """

        result = self.ctrl.query(f"""
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
        """)
        result.index = np.arange(1, len(result) + 1)
        return result
