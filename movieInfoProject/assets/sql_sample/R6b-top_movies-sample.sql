-- R6 - Top 5 movies by user ratings
SELECT name as Title, avg_rate as Rate
FROM Movie
ORDER BY avg_rate DESC
LIMIT 5;