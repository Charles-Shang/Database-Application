-- R9 - filter movies by region
SELECT DISTINCT id, name, region, year, GROUP_CONCAT( DISTINCT category ) AS allCategory, avg_rate, introduction
FROM Movie LEFT JOIN Movie_category ON Movie.id=Movie_category.movie_id
WHERE region='region7'
GROUP BY id
LIMIT 10 OFFSET 0;