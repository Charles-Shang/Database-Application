-- R6 - Top n movies by user ratings
SELECT name as Title, rates as Rate
FROM movie
ORDER BY rates DESC
LIMIT {{ n }};