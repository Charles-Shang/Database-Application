SELECT year,count(id) AS NumOfMovie
FROM Movie
GROUP BY year
ORDER BY year DESC
LIMIT {n}