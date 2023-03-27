-- R9 - filter by category and sort by rating
SELECT DISTINCT ID, name, region, year, GROUP_CONCAT( DISTINCT category ) AS allCategory, avg_rate, introduction
FROM Movie LEFT JOIN Movie_category ON Movie.ID=Movie_category.movie_id
GROUP BY ID
HAVING SUM(case when category='category10' then 1 else 0 end) > 0
ORDER BY avg_rate DESC
LIMIT 10 OFFSET 0