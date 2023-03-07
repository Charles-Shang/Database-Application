-- R9 - filter movies by region
SELECT DISTINCT ID, name, region, year, GROUP_CONCAT( DISTINCT category ) AS allCategory, avgRate, introduction
FROM Movie LEFT JOIN Movie_category ON Movie.ID=Movie_category.movieID
WHERE region='region7'
GROUP BY ID
LIMIT 10 OFFSET 0