-- R9 - filter and sort movies
SELECT DISTINCT id, name, region, year, GROUP_CONCAT( DISTINCT category ) AS allCategory, avg_rate, introduction
FROM Movie LEFT JOIN Movie_category ON Movie.id=Movie_category.movie_id
[WHERE] region={{region}} AND year={year} AND name REGEXP '^{letter}'
GROUP BY id
HAVING SUM(case when category={category} then 1 else 0 end) > 0
[ORDER BY] avg_rate [DESC]
LIMIT {{limit}} OFFSET {{offset}}
