from CONSTANTS import user, password, host, port, sample_database_name, TABLES
from mysqlCtrl import MysqlCtrl
import pandas as pd
import numpy as np


class Functionalities:

    def __init__(self):
        self.ctrl = MysqlCtrl(user, password, host, port, sample_database_name)

    # Top n movies by user ratings
    # n is 5 by default
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
        result.index = np.arange(1, n + 1)
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
        result.index = np.arange(1, n + 1)
        return result