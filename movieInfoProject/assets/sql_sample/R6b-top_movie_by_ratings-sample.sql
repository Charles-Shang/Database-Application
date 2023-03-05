-- R6 - Top 5 movies by user ratings
SELECT name as Title, rates as Rate
FROM movie
ORDER BY rates DESC
LIMIT 5;