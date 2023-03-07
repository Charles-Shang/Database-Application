-- R9 - filter movies by category
SELECT DISTINCT ID, name, region, year, GROUP_CONCAT( DISTINCT category ) AS allCategory, avg_rate, introduction
FROM Movie LEFT JOIN Movie_category ON Movie.ID=Movie_category.movie_id
GROUP BY ID
HAVING COUNT(case when category='category10' then 1 else 0 end) > 0
LIMIT 10 OFFSET 0