from CONSTANTS import user, password, host, port, sample_database_name, TABLES
from mysqlCtrl import MysqlCtrl
import pandas as pd
import numpy as np

class Functionalities:

    def __init__(self):
        self.ctrl = MysqlCtrl(user, password, host, port, sample_database_name)

    # Top n movies by user ratings
    # n is 5 by default
    def top_movie_by_ratings (self, n : int = 5) -> pd.DataFrame:
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

    def movie_filter_and_sort (self, region, year, category, letter, sortedBy, limit : int = 10, offset : int = 0) -> pd.DataFrame:
        """
        filter movies by region, year, category, letter
        then sort movies by sortedBy, where sortedBy is in {updateTime, popularity, rating}

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
            queryStatement += " HAVING COUNT(case when category='" + category + "' then 1 else 0 end) > 0"

        if sortedBy == "rating":
            queryStatement += " ORDER BY avg_rate DESC"
        
        queryStatement += " LIMIT " + str(limit) + " OFFSET " + str(offset) + ";"
        result = self.ctrl.query(queryStatement)
        return result

    
    