-- R9 - filter and sort movies
SELECT DISTINCT movieID, name, region, year, GROUP_CONCAT( DISTINCT category ) AS allCategory, avgRate, introduction
FROM MOVIE LEFT JOIN CATEGORY ON MOVIE.movieID=CATEGORY.movieID
[WHERE] region={region} AND year={year} AND name REGEXP '^{letter}'
GROUP BY movieID
HAVING COUNT(case when category={category} then 1 else 0 end) > 0
[ORDER BY] avgRate [DESC]
LIMIT {limit}, OFFSET {offset}