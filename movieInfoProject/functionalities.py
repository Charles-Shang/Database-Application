from CONSTANTS import user, password, host, port, sample_database_name, TABLES
from mysqlCtrl import MysqlCtrl
import pandas as pd
import numpy as np


class Functionalities:

    def __init__(self):
        self.ctrl = MysqlCtrl(user, password, host, port, sample_database_name)

    def top_movie_by_ratings(self, n: int = 5) -> pd.DataFrame:
        """
        top_movie_by_ratings find the top n movies by user ratings.

        Args:
            n: The number displayed result, by default n=5
        
        Returns: A Table of (movie_name, rating)
        """

        result = self.ctrl.query(f"""
        SELECT name as Title, rates as Rate
        FROM MOVIE
        ORDER BY rates DESC
        LIMIT {n};
        """)

        result.index = np.arange(1, len(result) + 1)
        return result

    def top_actors_with_best_movie(self, n: int = 5) -> pd.DataFrame:
        """
        top_actors_with_best_movie find the top n actors with best movie.

        Args:
            n: The number displayed result, by default n=5

        Returns: A Table of (actor, movie_name)
        """

        result = self.ctrl.query(f"""
            SELECT a.name as actor_name,
                AVG(m.rates) as avg_rating,
                MAX(m.rates) as best_movie_rating,
                m.name as best_movie_name
            FROM ACTOR a
            JOIN ACTS ac ON a.actorID = ac.actorID
            JOIN MOVIE m ON ac.movieID = m.movieID
            GROUP BY a.actorID
            ORDER BY avg_rating DESC
            LIMIT {n};
        """)
        
        result.index = np.arange(1, len(result) + 1)
        return result

    def movie_filter_and_sort (self, region, year, category, letter, sortedBy, limit : int = 10, offset : int = 0) -> pd.DataFrame:
        """
        filter movies by region, year, category, letter
        then sort movies by sortedBy, where sortedBy is in {updateTime, popularity, rating}

        Args: [all string type arguments use empty string "" to indicates no input, int type use 0 to indicates no input unless specified]
            region:       string type, indicates the region where the movies are produced
            year:         string type, indicates the year where the movies are produced
            category:     string type, indicates the category that the movies belong
            letter:       string type, indicates the first letter of the movies' names, if letter is "ALL", then ignore
            sortedBy:     string type, indicates the way we want to sort our result by
            limit:        int type, indicates the number of rows we want to get, default value is 10
            offset:       int type, indicates the offset
        """
        queryStatement = """SELECT DISTINCT movieID, name, region, year, GROUP_CONCAT( DISTINCT category ) AS allCategory, avgRate, introduction
        FROM Movie LEFT JOIN Category ON Movie.movieID=Category.movieID"""

        hasWhere = False
        if (region != "" and region != "ALL") or (year != "" and year != "ALL") or (letter != "" and letter != "ALL"):
            queryStatement += " WHERE"
            hasWhere = True
        if region != "" and region != "ALL":
            queryStatement += " region=" + region + " AND"
        if year != "" and year != "ALL":
            queryStatement += " year=" + year + " AND"
        if letter != "" and letter != "ALL":
            queryStatement += " name REGEXP '^" + letter + "' AND"
        
        if hasWhere:
            # remove last AND
            queryStatement = queryStatement[:-4]
        queryStatement += " GROUP BY movieID"
        if category != "" and category != "ALL":
            queryStatement += " HAVING COUNT(case when category=" + category + " then 1 else 0 end) > 0"

        if sortedBy == "rating":
            queryStatement += " ORDER BY avgRate DESC"
        
        queryStatement += " LIMIT " + str(limit) + " OFFSET " + str(offset) + ";"
        result = self.ctrl.query(queryStatement)
        return result

    
    def fuzz_search (self, n:str) -> pd.DataFrame:
        """
       fuzz_search find the movie which contains the keyword in any of
       author name, director name or movie name.

        Args:
            n: The key word being searched and displayed
        
        Returns: A Table of (movie_name, region, year, category, rating,
                             summary, director_name, [actor_name])
        """
        
        result = self.ctrl.query(f"""
        WITH midList(mids) as (
        (SELECT DISTINCT movieID 
        FROM MOVIE
        WHERE name LIKE '%%{n}%%')
        UNION 
        (SELECT DISTINCT movieID
        FROM ACTS natural join ACTOR
        WHERE name LIKE '%%{n}%%')
        UNION 
        (SELECT DISTINCT movieID
        FROM DIRECTOR natural join DIRECTS
        WHERE name LIKE '%%{n}%%')
        )

        SELECT m.name as Title, m.region as Region, m.year as Year,
        m.category as Category, m.rates as Rating, m.summary as Summary,
        d.name as Directors, GROUP_CONCAT(a.name) as Actors
        FROM MOVIE as m, midList,ACTOR a, ACTS ar, DIRECTOR d, DIRECTS dr 
        WHERE ar.actorID  = a.actorID and ar.movieID = m.movieID and 
            dr.directorID  = d.directorID and dr.movieID = m.movieID and
            m.movieID = midList.mids
        GROUP BY(m.name);
        """)
        result.index = np.arange(1, len(result) + 1)
        return result

    def find_top_n_movies_for_m_categories (self, m: int = 3, n : int = 5) -> pd.DataFrame:
        """
        Top n movie category of average ratings and m top movies in each category

        Args:
            n: The number of movie categories that is returned
            m: The number of movies for each of the n categories
        
        Returns: A Table of (category, averageRating, name, rates)
        """
        
        result = self.ctrl.query(f"""
        WITH MOVIE(name, category, rates) as
        (SELECT Movie.name, Movie_category.category, Movie.avg_rate FROM Movie, Movie_category WHERE Movie.id = Movie_category.movie_id),
        temporaryTop3Category(category, averageRating) as
        (SELECT category, AVG(rates) FROM MOVIE GROUP BY category ORDER BY AVG(rates) desc LIMIT {n})
        SELECT category, averageRating, name, rates FROM (
        SELECT category, averageRating, name, rates, ROW_NUMBER() OVER (PARTITION BY MOVIE.category ORDER BY MOVIE.rates DESC) AS num
        FROM temporaryTop3Category NATURAL JOIN MOVIE 
        ORDER BY averageRating DESC, rates DESC
        ) AS withNum
        WHERE withNum.num <= {m};
        """)
        result.index = np.arange(1, len(result) + 1)
        return result