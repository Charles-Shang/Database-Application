-- R6-a. Top n movies by user ratings & Top 5 movie actors by average user rating on their movies and one best movie
SELECT a.name as actor_name,
	AVG(m.rates) as avg_rating,
	MAX(m.rates) as best_movie_rating,
	m.name as best_movie_name
FROM ACTOR a
JOIN ACTS ac ON a.actorID = ac.actorID
JOIN MOVIE m ON ac.movieID = m.movieID
GROUP BY a.actorID
ORDER BY avg_rating DESC
LIMIT {{ n }};