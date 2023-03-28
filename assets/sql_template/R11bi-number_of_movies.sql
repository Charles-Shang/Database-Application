-- R11i - number of movies per year for the most recent 20 years
SELECT year, count(id) AS NumOfMovie
FROM Movie
GROUP BY year
ORDER BY year DESC
LIMIT {n}