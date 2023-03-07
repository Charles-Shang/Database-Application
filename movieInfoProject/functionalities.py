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

SELECT m.name as title, m.region, m.year, m.avg_rate , m.introduction , d.name as director_name,
GROUP_CONCAT(a.name) as actor_name
FROM Movie as m, midList,Actor natural join Celebrity as a, Acts ar, Director natural join Celebrity as d
WHERE ar.actor_id  = a.id  and ar.movie_id  = m.id  and m.director_id  = d.id  and m.id  = midList.mids
GROUP BY(m.name);


        """)
        result.index = np.arange(1, len(result) + 1)
        return result

    def find_top_m_movies_for_n_categories (self, n: int = 5, m: int = 3) -> pd.DataFrame:
        """
        Top n movie category of average ratings and m top movies in each category

        Args:
            n: The number of movie categories that is returned
            m: The number of movies for each of the n categories
        
        Returns: A Table of (category, averageRating, name, rates)
        """
        
        result = self.ctrl.query(f"""
        WITH temporaryTop3Category(category, averageRating) as
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